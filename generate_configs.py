#!/usr/bin/python3

from jinja2 import Environment, FileSystemLoader, Template

import yaml
from pprint import pprint as p

with open("systems.yaml") as file:
  systems = yaml.safe_load(file)

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
template = env.get_template('example_bigip_jinja.txt')

for system in systems["systems"]:
  print('System: %s' % (system['name']))
  p(system)
  render_config = template.render(data=system)
  #print('Render: %s' % (render_config))
  with open("output/%s_render.txt" % (system['name']), "w") as filehandle:
    filehandle.write(render_config)
