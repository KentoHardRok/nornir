#!/usr/bin/python3
# -*- coding: utf-8 -*-

from jinja2 import Template

with open("./scrapli/templates/route.j2") as file_:
    template = Template(file_.read())

jinja_var = {
    'mpls':
    True,
    'scan': [{
        'host': 'R1',
        'ip_net': '192.168.100.0',
        'wildcard_mask': '0.0.0.255',
        'area_id': '0'
    }, {
        'host': 'R2',
        'ip_net': '192.168.50.0',
        'wildcard_mask': '0.0.0.255',
        'area_id': '0'
    }]
}

print(template.render(jinja_var))
