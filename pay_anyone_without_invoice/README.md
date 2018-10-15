This programs help you to send a few satohis to another lightning node without the necessity to
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


```
standard route to node:  0307243743f60637f090347f9f2c1c98017071fd8f6afd8d6f6f6a64c7393a858a
[
  {
    "channel": "537914:2372:0",
    "delay": 167,
    "id": "024a8228d764091fce2ed67e1a7404f83e38ea3c7cb42030a2789e73cf3b341365",
    "msatoshi": 100802
  },
  {
    "channel": "541417:2070:0",
    "delay": 153,
    "id": "02ad6fb8d693dc1e4569bcedefadf5f72a931ae027dc0f0c544b34c1c6f3b9a02b",
    "msatoshi": 100001
  },
  {
    "channel": "535682:1650:1",
    "delay": 9,
    "id": "0307243743f60637f090347f9f2c1c98017071fd8f6afd8d6f6f6a64c7393a858a",
    "msatoshi": 100000
  }
]
motified route over node 0307243743f60637f090347f9f2c1c98017071fd8f6afd8d6f6f6a64c7393a858a back to myself
[
  {
    "channel": "537914:2372:0",
    "delay": 864,
    "id": "024a8228d764091fce2ed67e1a7404f83e38ea3c7cb42030a2789e73cf3b341365",
    "msatoshi": 100802
  },
  {
    "channel": "541417:2070:0",
    "delay": 720,
    "id": "02ad6fb8d693dc1e4569bcedefadf5f72a931ae027dc0f0c544b34c1c6f3b9a02b",
    "msatoshi": 100001
  },
  {
    "channel": "535682:1650:1",
    "delay": 576,
    "id": "0307243743f60637f090347f9f2c1c98017071fd8f6afd8d6f6f6a64c7393a858a",
    "msatoshi": 100000
  },
  {
    "channel": "535682:1650:1",
    "delay": 432,
    "id": "02ad6fb8d693dc1e4569bcedefadf5f72a931ae027dc0f0c544b34c1c6f3b9a02b",
    "msatoshi": 2403
  },
  {
    "channel": "541417:2070:0",
    "delay": 288,
    "id": "024a8228d764091fce2ed67e1a7404f83e38ea3c7cb42030a2789e73cf3b341365",
    "msatoshi": 1602
  },
  {
    "channel": "537914:2372:0",
    "delay": 144,
    "id": "03efccf2c383d7bf340da9a3f02e2c23104a0e4fe8ac1a880c8e2dc92fbdacd9df",
    "msatoshi": 801
  }
]
```
