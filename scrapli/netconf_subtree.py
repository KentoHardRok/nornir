"""
Gather Specific Facts about the Network
"""

from nornir_utils.plugins.functions import print_result
from nornir_scrapli.tasks import netconf_get, netconf_get_config, netconf_edit_config
from nornir.core.filter import F
from nornir import InitNornir
import xmltodict as x2d

nr = InitNornir(config_file="/home/tomw/nornir/scrapli/config.mv.yaml")
cisco = nr.filter(F(groups__contains="cisco_group"))
juniper = nr.filter(F(groups__contains="juniper_group"))
single_host = nr.filter(F(hostname='192.168.100.131'))


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


def try_get_config(task):
    result = task.run(task=netconf_get_config, source="candidate")


def gorunteldat(task):
    result = task.run(task=netconf_edit_config,
                      target="candidate",
                      config="""
    <config>
        <configuration>
            <interfaces>
                <interface>
                    <name>ge-0/0/0</name>
                    <unit>
                        <name>0</name>
                        <family>
                            <inet>
                                <address>
                                    <name>10.24.31.2/24</name>
                                </address>
                            </inet>
                        </family>
                    </unit>
                </interface>
            </interfaces>
        </configuration>
    </config>
                      """)


# juniper_info = juniper.run(task=netconf_junos)
# cisco_info = cisco.run(task=netconf_iosxe)
edit = single_host.run(task=gorunteldat)
config = single_host.run(task=try_get_config)

print_result(edit)
print_result(config)

# this is how we extract ip information from the juniper devices
# juniper_data = {}
# juniper_data['vMX15'] = x2d.parsejuniper_info['vMX15'][1].result
# just to extract the ip address off of an interface
# juniper_data['vMX15']['nc:rpc-reply']['nc:data']['configuration'][
#     'interfaces']['interface'][0]['unit']['family']['inet']['address']['name']

# import ipdb

# ipdb.set_trace()
