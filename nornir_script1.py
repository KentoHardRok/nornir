"""
Gather Specific Facts about the Network
"""

from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get
from nornir.core.filter import F

nr = InitNornir(config_file="config.yaml")
provider = nr.filter(F(groups__contains="area1") & ~F(groups__contains="area2"))
customers = nr.filter(F(groups__contains="blue") & ~F(group__contains="red") & ~F(group__contains="green"))

interfaces = nr.run(
    task=napalm_get, getters="mac_address_table"
    )

print_result(interfaces)

