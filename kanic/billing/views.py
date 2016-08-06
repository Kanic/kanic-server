from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.response import Response

import braintree

braintree.Configuration.configure(braintree.Environment.Sandbox,
                                  merchant_id="bh39gnhrkjktwdkg",
                                  public_key="gkp752vgb55cw487",
                                  private_key="10354935731a222f961b549ed4032106")



class GetClientTokenView(APIView):
    """
    Method: GET
    Description: generate client token for braintree client side
    """
    def get(self, request, format=None):
        client_token = braintree.ClientToken.generate()
        data = {
            'client_token': client_token
        }
        return Response(data)


class CreatePurchaseView(APIView):
    def post(self, request, format=None):
        payment_method_nonce = request.POST.get('payment_method_nonce', None)
        if payment_method_nonce is not None:
            result = braintree.Transaction.sale({
                "amount": "10.00",
                "payment_method_nonce": payment_method_nonce,
                "options": {
                    "submit_for_settlement": True
                }
            })
            return Response({'status': 'success'})
        else:
            return Response({'status': 'fail'})
