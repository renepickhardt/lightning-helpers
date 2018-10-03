Small shell script (together with a Makefile to install it) which processes `lightning-cli listfunds` and outputs the funds in a nicer and cleaner way:

```
git clone https://github.com/renepickhardt/lightning-helpers.git

cd lightning-helpers
sudo make install
listfunds
```

After cloning run `sudo make install` and then `listfunds`. 

The result will look like this: 

```
user@computer: listfunds 
223887 satoshi available to fund channels
64523 satoshi owned in channels
7438925 satoshi total channel capacity
---------------
Total funds: 288410 satoshi
Percentage of total channel capacity owned: 0.86737
---------------
Add command line parameter [B] for BTC, [m] for mBTC, [y] for microBTC, [b] for bits and nothting or anything else for satoshi
by Rene Pickhardt.
Consider a tip: via curl -i -H "Accept: application/json" -d '{"amount":ENTER_AN_INTEGER_AMOUNT_OF_SATOSHIS_INSTEAD_OF_THIS}' http://ln.rene-pickhardt.de/invoice
```

As you can see you can pass several command line options to change the unit of your funds.

Check out my Lightning Network related Youtube Channel: https://www.youtube.com/user/RenePickhardt
