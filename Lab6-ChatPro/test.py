import yaml

with open('config.yml', encoding='utf-8') as f:
    config = yaml.safe_load(f)
print(config)
