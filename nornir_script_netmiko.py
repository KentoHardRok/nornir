#!/usr/bin/python3
# -*- coding: utf-8 -*-


from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko.tasks import netmiko_send_command, netmiko_send_config
from nornir.core.filter import F

NR = InitNornir(config_file="config.yaml")

provider = NR.filter(F(has_parent_group="area1", "area2"))

RESULTS = provider.run(
    task=netmiko_send_config, config_commands = ["do wr"]

)

print_result(RESULTS)
