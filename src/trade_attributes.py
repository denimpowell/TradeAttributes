
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s')
logger = logging.getLogger()



def process_file():

    logger.info("process_file initiated")


    logger.info("process_file completed")
    pass



if __name__ == '__main__':

    logger.info("Application logging is configured")