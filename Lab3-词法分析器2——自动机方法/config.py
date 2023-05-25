import yaml
class Config:
    def __init__(self, fileDir='config.yml'):
        with open(fileDir,encoding = 'utf-8') as f:
            data = yaml.safe_load(f)
        for key, val in data.items():
            setattr(self, key, val)

    def Print(self):
        for attr, val in self.__dict__.items():
            print(attr, val)

if __name__ == '__main__':
    config = Config()
    config.Print()
