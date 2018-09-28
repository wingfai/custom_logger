import logging.handlers


class CustomLogging:

    def __init__(
            self,
            path: str,
            filename: str,
            formatter: str = '%(asctime)s: %(levelname)s: %(name)s: %(message)s',
            level=logging.DEBUG
            ):
        
        self.__logger = logging.getLogger()
        self.path = path
        self.filename = filename
        self.__logger.setLevel(level)

        time_rotating_file_handler = logging.handlers.TimedRotatingFileHandler(
            self.path + self.filename, when='D', interval=1, backupCount=0)
        stream_handler = logging.StreamHandler()

        formatter = logging.Formatter(formatter)
        time_rotating_file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)

        self.__logger.addHandler(time_rotating_file_handler)
        self.__logger.addHandler(stream_handler)

    def get_logger(self):
        return self.__logger


if __name__ == '__main__':
    def add(x, y):
        return x + y

    num1 = 10
    num2 = 5
    logger = CustomLogging(path='D:/bkcheck/', filename='test111.log').get_logger()
    print('{} + {} = {}'.format(num1, num2, add(num1, num2)))
    logger.info('{} + {} = {}'.format(num1, num2, add(num1, num2)))

    while num1 < 15:
        num1 += 1
        print('{} + {} = {}'.format (num1, num2, add(num1, num2)))
        logger.info('{} + {} = {}'.format(num1, num2, add(num1, num2)))
