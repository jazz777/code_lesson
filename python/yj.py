import yaml
import json

with open('/home/taiichi930/code_lesson/python/test.json') as file:
    # JSONから辞書
    obj = json.load(file)
    # 辞書からYAML
    ym = yaml.dump(obj)
    print(ym)