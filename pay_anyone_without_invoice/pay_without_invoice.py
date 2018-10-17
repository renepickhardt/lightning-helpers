"""
This software comes at absolutely no warrenty! Use at your own risk!
(c) Rene Pickhardt License Apache 2.0 

This program helps you to send a view satohis to another lightning node without the necessity to
have the other node issuing an invoice first.

It is achieved by an idea explained in this video: https://youtu.be/Dwl-0cY6KkU
The key is that `getroute` finds a route to the designated route which is then appeneded by its
reverse path so that there is a fully circular payment. Finally you issue an invoice of one satoshi
and pay the invoice with the `sendpay` command and the modified route. while paying yourself you
leave a redicoulus high fee at the node which you wanted to pay without invoice.

Obviously you don't have to do this with a circular payment but you could also pay a small invoice
to your friend Alice and find a route over the "real" recipient

These payments are even more anonymous as the reciepient will just believe it routed a payment.

use the tool by `$ python3.6 pay_without_invoice.py node_id amount_in_satoshi`. If this programm is
usefull or enlightning for you please consider to use it while using the node id of my lightning
node which can be found at http://ln.rene-pickhardt.de and by the time of righting is
`03efccf2c383d7bf340da9a3f02e2c23104a0e4fe8ac1a880c8e2dc92fbdacd9df`


"""

from lightning.lightning import LightningRpc
from time import time
import json
import sys

#/home/username/.lightning/lightning-rpc would be the standard value
#path_to_lightning_rpc_interface = "CHANGE ME"

ln1 = LightningRpc(path_to_lightning_rpc_interface)

id1 = ln1.getinfo()["id"]


def send_the_payment(route):
    label = "sendwithout-invoice-{}".format(time())
    invoice = ln1.invoice(1000, label, label)
    print(invoice)
    ph = invoice["payment_hash"]
    res = ln1.sendpay(route, ph)
    print(json.dumps(res,sort_keys=True,indent=2))

def pay_without_invoice(dest_id, amount):
    route = ln1.getroute(dest_id, amount*1000, 1.0)["route"]
    print("standard route to node: ", dest_id)

    first_channel = dict(route[0])
    first_channel["id"] = id1
    print(json.dumps(route,sort_keys=True,indent=2))
    
    max_delay = int(first_channel["delay"])
    max_routing_fee = int(first_channel["msatoshi"]) - (amount+1)*1000
    if len(route) > 1:
        max_delay = 0
        for i in range(1, len(route)):
            delay = int(route[i-1]["delay"]) - int(route[i]["delay"])
            fee = int(route[i-1]["msatoshi"]) - int(route[i]["msatoshi"])
            if delay > max_delay:
                max_delay = delay
            if fee > max_routing_fee:
                max_routing_fee = fee

    delay = first_channel["delay"]
    for x in range(len(route)):
        route[x]["delay"] += delay

    end_short_channel_id = route[-1]["channel"]
    
    reversed_route = [dict(x) for x in reversed(route)]
    reversed_route.append(first_channel)
    reversed_route = reversed_route[1:]

    fee = len(reversed_route) * max_routing_fee
    for i in range(len(reversed_route)):
        reversed_route[i]["msatoshi"] = fee - i * max_routing_fee

    fullroute = route
    fullroute.extend(reversed_route)
    full_delay = max_delay * len(fullroute)
    for i in range(len(fullroute)):
        fullroute[i]["delay"] = full_delay - i * max_delay
    
    for i in range(len(fullroute)-2,0,-1):
        fullroute[i]["channel"] = fullroute[i-1]["channel"]
        if fullroute[i]["channel"] == end_short_channel_id:
            break
    print("modified route over node {} back to myself".format(dest_id))
    print(json.dumps(fullroute,sort_keys=True,indent=2))
    send_the_payment(fullroute)


if len(sys.argv) !=3:
    print("need to be called with node_id as first and amount (in satoshi) as second argument")
    exit()

nodeid = sys.argv[1]
amount = int(sys.argv[2])
flag = pay_without_invoice(nodeid, amount)
print("done check your funds and channels")
