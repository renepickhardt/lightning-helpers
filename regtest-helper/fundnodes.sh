#!/bin/bash
source setalias.sh &

addr=$(ln1 newaddr | jq -r .address)
echo $addr
btc generatetoaddress 101 $addr

echo "wait until bitcoind was polled for funds"
sleep 1


#ln1 connect $(ln2 getinfo | jq -r .id) 127.0.0.1 2337 && \
#  ln1 fundchannel $(ln2 getinfo | jq -r .id) 100000 1100perkb && btc generate 1


btc generatetoaddress 16 2N7D9htmJZZaHNoiqF152UuNB5iubJ4dwKuo
ln1 withdraw 2N7D9htmJZZaHNoiqF152UuNB5iuJ4dwKuo all 1200perkb
btc generatetoaddress 6 2N7D9htmJZZaHNoiqF152UuNB5iuJ4dwKuo

ln1 listfunds

echo "wait for gossip"

sleep 1



echo "move some channel balance"
label=$(btc getnewaddress)
ln1 pay $(ln2 invoice 3300000 $label Test_funds | jq -r .bolt11)
