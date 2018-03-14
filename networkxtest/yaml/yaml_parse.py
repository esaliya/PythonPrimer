import yaml

with open("data/simple_yaml.yaml", 'r') as stream:
    try:
        obj = yaml.load(stream)
        print(obj['a'])
    except yaml.YAMLError as exc:
        print(exc)