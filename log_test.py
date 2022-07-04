# -*- coding: UTF-8 -*-
'''
@Time: 2022/7/4 22:53
@author: nicole1010
'''

from logExe.common.log import *
from logExe.common.filetool import FileTool

file = FileTool()
ini_path = file.path("../logfile/log.ini")

initialize_logini(ini_path, simple_logger_on_fail=True)

uilog = logging.getLogger("full")
overlog = logging.getLogger("overall")

uilog.debug("uilog->debug")
uilog.error("uilog->error")

overlog.info("存到overlog下：info")
overlog.warning("存到overlog下：warn")

uilog.warning("uilog->warn")
