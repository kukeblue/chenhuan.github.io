import logging

logging.basicConfig(
    level=logging.INFO,
)
log = logging.getLogger("user_log")


class Logger:
    log_data = ''

    def launch_logger(self, msg=''):
        self.log_data = self.log_data + '#' + msg;
        log.info(msg=msg)


logger = Logger()