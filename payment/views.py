from decimal import Decimal
from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from paypal.standard.forms import PayPalPaymentsForm
from orders.models import Order
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage



@csrf_exempt
def payment_done(request):
    email_id = Order.objects.filter(email)
    email = EmailMessage('Payment Confirmed', "This is to confirm you that, your payment has been succesfully completed and your tests are booked now! ", to=['mokshnarang22@gmail.com','sanchit_1996@ymail.com','ms135165@gmail.com','kanwal.badshah@gmail.com','guptas0797@gmail.com','ahujadisha24@gmail.com'])
    email.send()
    return render(request, 'payment/done.html')


@csrf_exempt
def payment_canceled(request):
    email = EmailMessage('Payment Cancelled', "Sorry, your payment for Tests is Cancelled. Please try again later!  ", to=['mokshnarang22@gmail.com','sanchit_1996@ymail.com','ms135165@gmail.com','kanwal.badshah@gmail.com','guptas0797@gmail.com','ahujadisha24@gmail.com'])
    email.send()
    return render(request, 'payment/canceled.html')


def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    host = request.get_host()

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '%.2f' % order.get_total_cost().quantize(Decimal('.01')),
        'item_name': 'Order {}'.format(order.id),
        'invoice': str(order.id),
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('payment:done')),
        'cancel_return': 'http://{}{}'.format(host, reverse('payment:canceled')),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'payment/process.html', {'order': order,
                                                    'form':form})
