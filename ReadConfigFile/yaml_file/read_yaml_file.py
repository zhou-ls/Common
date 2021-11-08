# -*- coding: utf-8 -*-
import yaml

with open("enviro.yaml", encoding="utf-8") as yaml_file:
    data = yaml.safe_load(yaml_file)

print(data.get("mysql"))
