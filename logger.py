'''
logging events
'''
import logging

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.DEBUG,
                    filename='./logi-mycrm.log',
                    format='%(asctime)s %(relativeCreated)s %(name)s %(levelname)s >>> %(message)s'
                    )


# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s %(relativeCreated)s %(name)s %(levelname)s >>> %(message)s'
#                     )

