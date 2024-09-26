import logging

class LogGen:
    @staticmethod
    def loggen():
        #logging.getLogger() returns the root logger, which is the main entry point for logging events.
        logger = logging.getLogger()

        #FileHandler is responsible for writing log messages to a file
        #mode='a' means that the log messages will be appended to the log file if it already exists
        fhandler = logging.FileHandler(filename='../logs/automation.log', mode='a')

        #logging.Formatter defines the layout of the log messages.
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        #This line attaches the previously created formatter to the FileHandler
        fhandler.setFormatter(formatter)
        #The FileHandler is added to the logger

        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger