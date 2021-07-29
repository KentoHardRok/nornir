#!/usr/bin/python3
# -*- coding: utf-8 -*-


from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko.tasks import netmiko_send_command, netmiko_send_config
from nornir.core.filter import F

nr = InitNornir(config_file="config.yaml")
#provider = nr.filter(F(groups__contains="blue"))
#provider = nr.filter(F(groups__contains="green"))
#provider = nr.filter(F(groups__contains="red"))
#provider = nr.filter(F(groups__contains="area2"))
#provider = nr.filter(F(groups__contains="area2") | F(groups__contains="area1"))
#provider_ce_only = provider.filter(router_type="pe")
#ce_not_R1 = provider_ce_only.filter(~F(hostname="192.168.100.101"))

provider = nr.filter(F(router_type="ce"))
commands=["wr"]

for cmd in commands:
    results = provider.run(
        task=netmiko_send_command,
        command_string=cmd
        )
    print_result(results)
