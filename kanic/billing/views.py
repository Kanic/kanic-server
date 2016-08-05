from django.http import HttpResponse
from django.shortcuts import render

import braintree

braintree.Configuration.configure(braintree.Environment.Sandbox,
                                  merchant_id="bh39gnhrkjktwdkg",
                                  public_key="gkp752vgb55cw487",
                                  private_key="10354935731a222f961b549ed4032106")


def get_client_token(request):
    print "i, here"
    client_token = braintree.ClientToken.generate()
    data = {
        'client_token': client_token
    }
    return HttpResponse(data)
