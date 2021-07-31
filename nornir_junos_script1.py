"""
Gather Specific Facts about the Network
"""

from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get
from nornir.core.filter import F

nr = InitNornir(config_file="config.junos.yaml")
spine = nr.filter(F(groups__contains="evpn_spine"))

interfaces = nr.run(
    task=napalm_get, getters="mac_address_table"
    )

print_result(interfaces)

