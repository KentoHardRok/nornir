"""
Gather Specific Facts about the Network
"""

from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir.core.filter import F
import pandas as pd

# initialize inventory
nr = InitNornir(config_file="config.junos.yaml")
leaf = nr.filter(F(groups__contains="evpn_leaf"))

# pulls mac-address-table via napalm
mac_address = leaf.run(
    task=napalm_get, getters="mac_address_table"
    )

# This finds the num of devices on the net and get's their names
dev_num = len(mac_address.keys())
dev, value = zip(*mac_address.items())

# This loop just displays the mac-address-table per device (and makes an aggr list)
for i in range(0, dev_num):
    mac_df = []
    print("*******************  " + dev[i] + "  ************************")
    mac_df.append(pd.DataFrame(mac_address[dev[i]][0].result['mac_address_table']))
    total_mac_list.append(mac_df)
    print(pd.concat(mac_df))
    
# Below just prints the aggregated list of all of the unique mac-addresses
total_mac_list = pd.concat(total_mac_list)
print(total_mac_list.drop_duplicates(subset=['mac']))

