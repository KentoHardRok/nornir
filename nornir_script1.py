"""
Gather Specific Facts about the Network
"""

from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get

NR = InitNornir(
        config_file="config.yaml", dry_run=True
)

RESULTS = NR.run(
        task=napalm_get, getters=["facts", "interfaces", "arp_table"]

)

print_result(RESULTS)
