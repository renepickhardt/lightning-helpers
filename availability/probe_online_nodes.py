"""
author: Rene Pickhardt (rene.m.pickhardt@ntnu.no)
Date: 15.1.2020
License: MIT

Checks which nodes are currently online by establishing a connection to those nodes. Results can later be studied with `lightning-cli listpeers` or when `jq` is installed with `lcli getinfo | jq ".num_peers"`

This tool is intended to be used to make routing decisions in which we we chose a path to the destination in which all hops are online. This should reduce the failed routing attempts and the latency.

=== Support: 
If you like my work consider a donation at https://patreon.com/renepickhardt or https://tallyco.in/s/lnbook
"""
from lightning import LightningRpc, RpcError
from multiprocessing import Process
from time import sleep

rpc = LightningRpc("/home/rpickhardt/.lightning/bitcoin/lightning-rpc")


def connect(nodeid):
    try:
        res = rpc.connect(nodeid)
        print(nodeid, res)
    except RpcError as e:
        print("could not connect to", nodeid, str(e))


nodes = rpc.listnodes()["nodes"]
potential_nodes = []
for node in nodes:
    if "nodeid" in node:
        nodeid = node["nodeid"]
        if "addresses" not in node:
            continue
        addresses = node["addresses"]
        for addr in addresses:
            if addr["type"] == "ipv4":
                potential_nodes.append(nodeid)


print("known nodes:", len(nodes), "nodes with ipv4 addr:", len(potential_nodes))

for r, nodeid in enumerate(potential_nodes):
    p = Process(target=connect, args=(nodeid,))
    print("go", nodeid)
    p.start()
    sleep(0.2)
    print(r)
