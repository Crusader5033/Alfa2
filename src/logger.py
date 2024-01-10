import logging
import configparser

class Logger:
    def __init__(self, config_path):
        # Load configuration from config.ini
        self.config = configparser.ConfigParser()
        self.config.read(config_path)

        # Set up logging
        logging_config = self.config['LOGGING']
        logging.basicConfig(
            filename=logging_config.get('filename', 'program.log'),
            level=logging_config.get('level', 'INFO'),
            format=logging_config.get('format', '%(asctime)s - %(levelname)s - %(message)s')
        )
        self.logger = logging.getLogger(__name__)

    def log(self, level, message):
        getattr(self.logger, level.lower())(message)

    def log_info(self, message):
        self.log('INFO', message)

    def log_error(self, message):
        self.log('ERROR', message)

    def log_exception(self, exception):
        self.logger.exception(exception)

    def display_logs(self, filter_string=None):
        with open(self.config.get('LOGGING', 'filename'), 'r') as log_file:
            logs = log_file.readlines()

        filtered_logs = self.filter_logs(logs, filter_string)

        print("Filtered Logs:")
        for log in filtered_logs:
            print(log.strip())

    def filter_logs(self, logs, filter_string):
        if filter_string:
            filtered_logs = [log for log in logs if filter_string.lower() in log.lower()]
        else:
            filtered_logs = logs

        return filtered_logs
