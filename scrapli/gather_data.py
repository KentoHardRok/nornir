"""
Gather Specific Facts about the Network
"""

from nornir_utils.plugins.functions import print_result
from nornir_scrapli.tasks import netconf_get
from nornir.core.filter import F
from nornir import InitNornir

nr = InitNornir(config_file="/home/tomw/nornir/scrapli/config.mv.yaml")
cisco = nr.filter(F(groups__contains="cisco_group"))


def netconf_iosxe(task):
    result = task.run(
        task=netconf_get,
        filter_="/native/interface/GigabitEthernet/ip/address/primary",
        filter_type="xpath")


info = cumulus.run(task=netconf_cumulus)
print_result(info)
