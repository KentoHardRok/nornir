#!/usr/bin/python3
# -*- coding: utf-8 -*-

from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('template')
env = Environment(loader=file_loader)

jinja_var = {
    'scan': [{
        'ip_net': '192.168.100.0',
        'wildcard_mask': '0.0.0.255',
        'area_id': '0'
    }]
}

template = env.get_template('/home/tomw/nornir/scrapli/templates/route.j2')
print(template.render(jinja_var))
