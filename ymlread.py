import yaml

with open("/Users/smahalingam/Documents/test.yaml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

for section in cfg:
    print(section)
print(cfg['package'])
print(cfg['about'])
print(cfg['requirements'])
