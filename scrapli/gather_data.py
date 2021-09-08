"""
Gather Specific Facts about the Network
"""

from nornir_scrapli.tasks import netconf_get
from nornir_utils.plugins.functions import print_result

from nornir import InitNornir
from nornir.core.filter import F

nr = InitNornir(config_file="/home/tomw/nornir/scrapli/config.mv.yaml")
cisco = nr.filter(F(groups__contains="cisco_group"))
juniper = nr.filter(F(platform__eq="junos"))


def netconf_iosxe(task):
    result = task.run(
        task=netconf_get,
        filter_="/native/interface/GigabitEthernet/ip/address/primary",
        filter_type="xpath")


def netconf_junos(task):
    result = task.run(task=netconf_get,
                      filter_="/get-config",
                      filter_type="xpath")


info = juniper.run(task=netconf_junos)
print_result(info)
