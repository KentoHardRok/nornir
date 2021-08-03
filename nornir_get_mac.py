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
total_mac_list = []
mac_df = []

# This loop just displays the mac-address-table per device (and makes an aggr list)
for i in range(0, dev_num):
    print("*******************  " + dev[i] + "  ************************")
    mac_table = pd.DataFrame(mac_address[dev[i]][0].result['mac_address_table'])
    mac_table.insert(loc=0, column='device', value=dev[i])
    mac_df.append(mac_table)
    total_mac_list = pd.concat(mac_df)
    print(mac_table)
    
# Below just prints the aggregated list of all of the unique mac-addressestotal_mac_list = pd.concat(pd.DAtotal_mac_list)
print("\n\n*******************  All Macs  ************************")
result = total_mac_list.sort_values(by=['device'])
print(result)
result.to_csv(r'/tmp/unique_mac.csv', index = False)

