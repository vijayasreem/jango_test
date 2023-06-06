from django.shortcuts import render
from django.http import HttpResponse
from .forms import PaymentForm
import logging

# Create your views here.
def payment_gateway_integration(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            # Process the payment
            payment_method = form.cleaned_data['payment_method']
            if payment_method == 'debit_card' or payment_method == 'credit_card':
                # Redirect user to secure payment page
                return redirect('payment_page')
            elif payment_method == 'paypal':
                # Process paypal payment
                return redirect('payment_page')
            elif payment_method == 'stripe':
                # Process stripe payment
                return redirect('payment_page')
            else:
                return HttpResponse('Payment method not supported.')
        else:
            return HttpResponse('Form not valid.')
    else:
        form = PaymentForm()
        return render(request, 'payment_form.html', {'form': form})


def payment_page(request):
    if request.method == 'POST':
        # Handle payment here
        payment_status = request.POST['payment_status']
        if payment_status == 'success':
            return HttpResponse('Payment successful.')
        elif payment_status == 'failure':
            return HttpResponse('Payment failed.')
        else:
            logging.error('Payment status not known.')
            return HttpResponse('Something went wrong.')
    else:
        return HttpResponse('Invalid request.')