This project is a collection of `lightning-helpers` which are small files (usually) written as shell scripts or in python which are supposed to ease the work with c-lightning.

currently there are two tools:

* listfunds is a small tool that gives you a nicer overview of your funds than the native `lighting-cli listfunds` API call
* pay_anyone_without_invoice is a tool that allows you to pay any lightning node by making a routed payment to yourself and drop a high routing fee for the node which you actually want to pay.

If you want to learn more about these tools visit my youtube channel at: https://www.youtube.com/user/RenePickhardt or send me message at https://twitter.com/renepickhardt

If those tools are usefull for you consider a donation:
* BTC-address: 1KwjU4UknzbXh1rnP1jAKz9wwjcuYwe9AC
* segwit: 38fWwbsxvVeBsJpH4bbHTBai8jT8RUa7DE
* Leave an anonymous tip via the ⚡ Lightning ⚡ network (: Get the invoice with this curl statement `curl -i -H "Accept: application/json" -d '{"amount":ENTER_AN_INTEGER_AMOUNT_OF_SATOSHIS_INSTEAD_OF_THIS}' http://ln.rene-pickhardt.de/invoice` or use the pay_anyone_without_invoice tool which I provide in this repository.

Feel free to issue a pull request if you find a mistake or if you think that you have a tool that should be listed here!