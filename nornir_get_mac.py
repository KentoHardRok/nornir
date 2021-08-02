"""
Gather Specific Facts about the Network
"""

from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir.core.filter import F
import pandas as pd

nr = InitNornir(config_file="config.junos.yaml")
leaf = nr.filter(F(groups__contains="evpn_leaf"))

mac_address = leaf.run(
    task=napalm_get, getters="mac_address_table"
    )

dev_num = len(mac_address.keys())
dev, value = zip(*mac_address.items())
mac_df = []

for i in range(0, dev_num):
    print("*******************  " + dev[i] + "  ************************")
    mac_df.append(pd.DataFrame(mac_address[dev[i]][0].result['mac_address_table']))
    print(pd.concat(mac_df))
    
# total_mac_list = pd.concat(mac_df)
# print(total_mac_list)
# print(total_mac_list.drop_duplicates(subset=['mac']))

