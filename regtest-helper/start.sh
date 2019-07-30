!#/bin/bash

#rm -rf /tmp/regtest-env
mkdir -p /tmp/regtest-env/{btc,ln1,ln2}

bitcoind --regtest --datadir=/tmp/regtest-env/btc --rpcuser=rpcuser --rpcpassword=rpcpassword &
sleep 1

source startln1.sh &
source startln2.sh &

source setalias.sh &

