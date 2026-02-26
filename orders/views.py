from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from .models import Order
from .services import create_razorpay_order
from .utils import verify_payment_signature
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import Product

from django.conf import settings
from django.db import transaction
from django.http import HttpResponseBadRequest
import razorpay






def index(request):

    # ✅ Only show paid orders
    orders = Order.objects.filter(
        is_paid=True
    ).order_by('-created_at')

    return render(request, "orders/index.html", {
        "orders": orders,
        "razorpay_key_id": settings.RAZORPAY_KEY_ID
    })

@csrf_exempt
def create_order(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            amount = data.get("amount")
            products = data.get("products", "")  # default empty string

            if not amount:
                return JsonResponse({"error": "Amount missing"}, status=400)

            razorpay_order = create_razorpay_order(amount)

            Order.objects.create(
                razorpay_order_id=razorpay_order["id"],
                amount=amount,
                products=products
            )

            return JsonResponse({
                "id": razorpay_order["id"],
                "amount": razorpay_order["amount"]
            })

        except Exception as e:
            print("CREATE ORDER ERROR:", e)
            return JsonResponse({"error": "Something went wrong"}, status=500)



@csrf_exempt
def verify_payment(request):
    if request.method == "POST":
        try:
            # If using redirect:true → data comes in POST form
            razorpay_payment_id = request.POST.get("razorpay_payment_id")
            razorpay_order_id = request.POST.get("razorpay_order_id")
            razorpay_signature = request.POST.get("razorpay_signature")

            # Initialize Razorpay client
            client = razorpay.Client(
                auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET)
            )

            # 🔐 STEP 1 — Signature Verification
            params_dict = {
                "razorpay_order_id": razorpay_order_id,
                "razorpay_payment_id": razorpay_payment_id,
                "razorpay_signature": razorpay_signature
            }

            client.utility.verify_payment_signature(params_dict)

            # 🔎 STEP 2 — Fetch payment from Razorpay (Server-side validation)
            payment = client.payment.fetch(razorpay_payment_id)

            # 🔎 STEP 3 — Check payment status & amount
            if payment["status"] != "captured":
                return redirect("/")

            order = Order.objects.get(razorpay_order_id=razorpay_order_id)

            if order.is_paid:
               return redirect("/")

            # Razorpay stores amount in paise
            if payment["amount"] != order.amount * 100:
                
                return redirect("/")

            # ✅ STEP 4 — Mark order as paid
            order.razorpay_payment_id = razorpay_payment_id
            order.razorpay_signature = razorpay_signature
            order.is_paid = True
            order.status = "processing"
            order.save()

            return redirect("/")

        except Exception as e:
            print("PAYMENT VERIFICATION ERROR:", e)
            return redirect("/")

        print(payment)
def download_invoice(request, order_id):
    try:
        order = Order.objects.get(id=order_id)

        content = f"""
        SnapMart Invoice

        Order ID: {order.razorpay_order_id}
        Products: {order.products}
        Amount: ₹{order.amount}
        Date: {order.created_at}
        Status: {order.status}

        Thank you for shopping!
        """

        response = HttpResponse(content, content_type='text/plain')
        response['Content-Disposition'] = f'attachment; filename="invoice_{order_id}.txt"'
        return response

    except Order.DoesNotExist:
        return HttpResponse("Order not found")

       


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")   # 🔥 back to index
    return redirect("/")  # no separate page



