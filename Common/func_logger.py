import logging
from Common.func_option import conf
from Common.func_address import logger_dir



class PutLogger(logging.Logger):
    def __init__(self, file=None):
        super().__init__(conf.get("logger", "name"), conf.get("logger", "level"))
        self.file = file
        # super().__init__()
        fmt = '%(asctime)s %(name)s %(levelname)s %(filename)s-%(lineno)d line：%(message)s'

        # 设置格式
        formatter = logging.Formatter(fmt)

        # 设置通道
        handle1 = logging.StreamHandler()
        handle1.setFormatter(formatter)
        self.addHandler(handle1)
        if self.file:
            handle2 = logging.FileHandler(self.file, encoding="utf-8")
            handle2.setFormatter(formatter)
            self.addHandler(handle2)


if conf.getboolean("logger","file_ok"):
    file_name = logger_dir
else:
    file_name = None

logger = PutLogger(file_name)