#!/bin/bash

if [[ $1 == B ]]; then
    #echo "Used unit is  BTC"
    DIV=100000000
    UNIT=BTC
elif  [[ $1 == m ]]; then
    #echo "Used unit is mBTC"
    DIV=100000
    UNIT=mBTC
elif [[ $1 == y ]]; then
    #echo "Used unit is microBTC"
    DIV=100
    UNIT=yBTC
elif [[ $1 == b ]]; then
    #echo "Used unit is bits"
    DIV=100
    UNIT=bis
else
    #echo "Used unit is satoshi"
    DIV=1
    UNIT=satoshi
fi

lightning-cli listfunds | grep "value" | sed 's/      "value": //g' | sed 's/,//g' | awk -v div="$DIV" -v u="$UNIT" '{s+=$1} END {print  s/div " " u " available to fund channels"}'
FREE=$(lightning-cli listfunds | grep "value" | sed 's/      "value": //g' | sed 's/,//g' | awk -v div="$DIV" '{s+=$1} END {print  s/div}')

lightning-cli listfunds | grep "channel_sat" | sed 's/      "channel_sat": //g' | sed 's/,//g' | awk -v div="$DIV" -v u="$UNIT" '{s+=$1} END {print s/div " " u " owned in channels"}'
CHAN=$(lightning-cli listfunds | grep "channel_sat" | sed 's/      "channel_sat": //g' | sed 's/,//g' | awk -v div="$DIV" '{s+=$1} END {print s/div}')

lightning-cli listfunds | grep "channel_total_sat" | sed 's/      "channel_total_sat": //g' | sed 's/,//g' | awk -v div="$DIV" -v u="$UNIT" '{s+=$1} END {print s/div " " u " total channel capacity"}'
CAP=$(lightning-cli listfunds | grep "channel_total_sat" | sed 's/      "channel_total_sat": //g' | sed 's/,//g' | awk '{s+=$1} END {print s}')

echo "---------------"
SUM=$(awk -v f="$FREE" -v c="$CHAN" 'BEGIN {print f+c}')
echo "Total funds: $SUM $UNIT"
if [[ $CAP -gt 0 ]]; then
	CHAN=$(lightning-cli listfunds | grep "channel_sat" | sed 's/      "channel_sat": //g' | sed 's/,//g' | awk '{s+=$1} END {print s}')
	PER=$(awk -v n="$CHAN" -v d="$CAP" 'BEGIN {print n*100/d}')
	echo "Percentage of total channel capacity owned: $PER"
fi
echo "---------------"
echo "Add command line parameter [B] for BTC, [m] for mBTC, [y] for microBTC, [b] for bits and nothting or anything else for satoshi"
echo "by Rene Pickhardt."
echo "Consider a tip: via curl -i -H \"Accept: application/json\" -d '{\"amount\":ENTER_AN_INTEGER_AMOUNT_OF_SATOSHIS_INSTEAD_OF_THIS}' http://ln.rene-pickhardt.de/invoice"
