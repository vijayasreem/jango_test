from django.urls import path

urlpatterns = [
    path('payment_gateway_integration/', payment_gateway_integration, name='payment_gateway_integration'),
    path('payment_page/', payment_page, name='payment_page'),
]