from django.db import models

class PaymentGateway(models.Model):
    '''
    Payment Gateway model
    '''
    name = models.CharField(max_length=200, unique=True)
    supported_payment_methods = models.CharField(max_length=200)

class CheckoutProcess(models.Model):
    '''
    Checkout process model
    '''
    payment_gateway = models.OneToOneField(PaymentGateway, on_delete=models.CASCADE)
    redirect_url = models.URLField()

class PaymentTransaction(models.Model):
    '''
    Payment transaction model
    '''
    checkout_process = models.ForeignKey(CheckoutProcess, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=200, unique=True)
    payment_details = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    message = models.CharField(max_length=200, blank=True, null=True)

class Log(models.Model):
    '''
    Log model
    '''
    payment_transaction = models.ForeignKey(PaymentTransaction, on_delete=models.CASCADE)
    log_data = models.TextField()