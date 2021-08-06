#!/usr/bin/python3
# -*- coding: utf-8 -*-

from nornir_netmiko.tasks import netmiko_send_command, netmiko_send_config
from nornir_utils.plugins.functions import print_result
from nornir import InitNornir
from nornir.core.filter import F


def get_int_status(devs):
    """
    Runs a list of commands and stores the results
    as class attributes named after the command
    """
    commands = ["sho ip int br"]
    for cmd in commands:
        get = devs.run(task=netmiko_send_command,
                       command_string=cmd,
                       use_textfsm=True)
        devs.host[cmd] = get.result


def run_on_ports(info):
    """
    Send ractive commands to devices
    """
    commands = ["description Unused Ports", "do wr"]
    for key, devs in info.inventory.hosts.items():
        for interf in devs['sho ip int br']:
            if "administratively down" in interf['status']:
                for cmd in commands:
                    info.run(
                        task=netmiko_send_config,
                        config_commands=['interface ' + interf['intf'], cmd])


def main() -> None:
    """
    main body
    """
    nr = InitNornir(config_file="config.yaml")
    pe = nr.filter(F(router_type="pe"))
    result = pe.run(task=get_int_status)
    print_result(result)
    run_on_ports(pe)


if __name__ == '__main__':
    main()
