import logging
import logging.config
from pathlib import Path
import os
import sys
sys.path.append(os.path.split(os.path.abspath(os.path.dirname(__file__)))[0])
from logExe.common.filetool import FileTool
file = FileTool()

def initialize_logini(path, simple_logger_on_fail=False):
    """
    读logini配置文件，实现全局log打印 - 供Android使用
    :param path:
    :return:
    """
    logfile1 = f"{Path(__file__).parent.parent}/log/uilog/uicaseLog.txt"
    file.create_file(logfile1)
    logfile2 = f"{Path(__file__).parent.parent}/log/overlog/overLog.txt"
    file.create_file(logfile2)
    logging.config.fileConfig(path, defaults={"logfullfile": logfile1, "logoverfile": logfile2})

def overinitialize_logini(path, simple_logger_on_fail=False):
    """
    读logini配置文件，实现全局log打印 - 供Android使用
    :param path:
    :return:
    """
    overlogfilepath = f"{Path(__file__).parent.parent}/log/overlog/overlog.txt"
    file.create_file(overlogfilepath)
    logging.config.fileConfig(path, defaults={'logfile': overlogfilepath})
