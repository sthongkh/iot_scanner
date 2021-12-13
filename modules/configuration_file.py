import configparser
from exception import exception, debug
from logger import logger


class Config:

    def __init__(self, file_path, item_name):
        self.config = configparser.ConfigParser()
        self.file_path = file_path
        self.item_name = item_name
        self.status = False
        self.res = ""

    @exception(logger)
    @debug(logger)
    def read(self):
        data = {}
        self.config.read(self.file_path)
        res = self.config.items(self.item_name)
        for i in res:
            data[i[0]] = i[1]

        return data

if __name__ == "__main__":
    config = Config(file_path="config.ini", item_name="SERVER")
    ret = config.read()
    print(ret["host"])
