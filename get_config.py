#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Gather Specific Facts about the Network
"""

from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir.core.filter import F
from nornir_utils.plugins.functions import print_result
import ipdb
import os.path

# initialize inventory
nr = InitNornir(config_file="config.junos.yaml")

# pulls configs via napalm
config = nr.run(task=napalm_get, getters="config")

print_result(config)
ipdb.set_trace()
