import logging

logging.basicConfig(
    level=logging.INFO,
)
log = logging.getLogger("USER-LOG")


class Logger:
    log_data = ''

    def launch_logger(self, msg=''):
        self.log_data = self.log_data + '\r\n' + msg;
        log.info(msg=msg)


logger = Logger()