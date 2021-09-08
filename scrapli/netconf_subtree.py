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
juniper = nr.filter(F(groups__contains="juniper_group"))


def netconf_iosxe(task):
    result = task.run(task=netconf_get,
                      filter_="""
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <GigabitEthernet>
                <name/>
                <ip>
                    <address>
                        <primary>
                        </primary>
                    </address>
                </ip>
            </GigabitEthernet>
        </interface>
    </native>
    """)


def netconf_junos(task):
    result = task.run(task=netconf_get,
                      filter_="""
    <configuration>
        <interfaces>
            <interface>
                <name/>
                <unit>
                    <name/>
                    <family>
                        <inet>
                            <address>
                                <name/>
                            </address>
                        </inet>
                    </family>
                </unit>
            </interface>
        </interfaces>
    </configuration>
    """)


juniper_info = juniper.run(task=netconf_junos)
cisco_info = cisco.run(task=netconf_iosxe)
print_result(juniper_info)
print_result(cisco_info)
