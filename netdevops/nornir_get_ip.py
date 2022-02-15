"""
Gather Specific Facts about the Network
"""

from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir.core.filter import F
import pandas as pd

# initialize inventory
nr = InitNornir(config_file="config.yaml")
#provider = nr.filter(F(groups__contains="area1") & ~F(groups__contains="area2"))
#customers = nr.filter(F(groups__contains="blue") & ~F(group__contains="red") & ~F(group__contains="green"))

# pulls ip-address-table via napalm
ip_address = nr.run(
    task=napalm_get, getters="ip_address_table"
    )

# This finds the num of devices on the net and get's their names
#dev_num = len(ip_address.keys())
#dev, value = zip(*ip_address.items())
#
## This loop just displays the ip-address-table per device (and makes an aggr list)
#for i in range(0, dev_num):
#    ip_df = []
#    print("*******************  " + dev[i] + "  ************************")
#    ip_df.append(pd.DataFrame(ip_address[dev[i]][0].result['interfaces_ip']))
#    total_ip_list.append(ip_df)
#    print(pd.concat(ip_df))
    
# Below just prints the aggregated list of all of the unique ip-addresses
# total_ip_list = pd.concat(total_ip_list)
print(ip_address)

