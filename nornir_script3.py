"""
Gather Specific Facts about the Network
"""

from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get

NR = InitNornir(
        config_file="config.yaml", dry_run=True
)

get_interfaces_ip_result = NR.run(napalm_get, getters=['get_interfaces_ip'])
print_result(get_interfaces_ip_result)

"""
RESULTS = NR.run(
        task=napalm_get, getters=["facts", "interfaces", "arp_table"]

)


print_result(RESULTS)
"""
