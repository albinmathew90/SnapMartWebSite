from django.conf import settings
import razorpay

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

def verify_payment_signature(data):
    try:
        client.utility.verify_payment_signature(data)
        return True
    except:
        return False