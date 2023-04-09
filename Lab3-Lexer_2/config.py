import yaml
def Read(fileDir):
    with open('config.yml',encoding = 'utf-8') as f:
        data = yaml.safe_load(f)
    return data

if __name__ == '__main__':
    print(Read('config.yml'))
