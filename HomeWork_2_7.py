import json
import os
import yaml


json_file = os.path.join(os.getcwd(), "file.json")
# json in text
with open(json_file, "r") as js_file:
    # data = json.load(js_file)
    text = open("json_tex_file.txt", "w")
    # text.write(str(data))
    for i in js_file:
        text.write(i)
    text.close()


# json in yaml
with open(json_file, "r") as js_file:
    data = json.load(js_file)
with open("json_yaml_file.yml", "w") as yaml_:
    yaml.dump(data, yaml_)


# yaml in json
with open("json_yaml_file.yml", "r") as ym_file:
    data = yaml.safe_load(ym_file)
with open(json_file, "w") as tx:
    json.dump(data, tx, indent=4)

# yaml in text
with open("json_yaml_file.yml", "r") as yml_file:
    tx = open("json_file.txt", "w")
    for i in yml_file:
        tx.write(i)
    tx.close()

# TEXT in JSON
with open("json_tex_file.txt", "r") as text_js_file:
    data = text_js_file.read()

with open("text_file.json", "w") as text:
    a = json.loads(data)
    json.dump(a, text, indent=4)

