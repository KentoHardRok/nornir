"""
Gather Specific Facts about the Network
"""

from nornir_utils.plugins.functions import print_result
from nornir_scrapli.tasks import netconf_get
from nornir.core.filter import F
from nornir import InitNornir
# from xml.dom import minidom

nr = InitNornir(config_file="/home/tomw/nornir/scrapli/config.mv.yaml")
cisco = nr.filter(F(groups__contains="cisco_group"))
junos = nr.filter(F(groups__contains="junos_group"))


def netconf_test(task):
    result = task.run(task=netconf_get,
                      filter_="/native/router",
                      filter_type="xpath")


info = junos.run(task=netconf_test)
print_result(info)