import logging
import os
LOGS_PATH='Logfolder/'


LOGGING_PATH=os.path.join(LOGS_PATH,'apps_logs.log')


logging.basicConfig(filename= LOGGING_PATH ,level = logging.DEBUG)
#latest