#!/usr/bin/env python

import os
import logging
import stripe
import paypal

from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/checkout', methods=['POST'])
def checkout():
    # read payment details from request
    payment_details = request.form

    # check if payment details are valid
    if not payment_details:
        return redirect(url_for('error'))

    # set up payment processor
    if payment_details['payment_method'] == 'credit_card':
        payment_processor = stripe
    elif payment_details['payment_method'] == 'paypal':
        payment_processor = paypal
    else:
        return redirect(url_for('error'))

    # call payment processor's API
    payment_result = payment_processor.process_payment(payment_details)

    # handle payment result
    if payment_result == 'success':
        return redirect(url_for('success'))
    else:
        return redirect(url_for('error'))

@app.route('/success')
def success():
    return 'Payment Successful.'

@app.route('/error')
def error():
    return 'Payment Failed.'

if __name__ == '__main__':
    # set logging level
    logging.basicConfig(level=logging.INFO)

    # set Stripe/PayPal API keys
    stripe.api_key = os.environ.get('STRIPE_API_KEY')
    paypal.api_key = os.environ.get('PAYPAL_API_KEY')

    # run Flask app
    app.run()