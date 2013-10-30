from boto.sqs import regioninfo
import logging
from boto.sqs.jsonmessage import JSONMessage

# useful for debugging boto connect
#logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)

logger = logging.getLogger(__name__)


def cmb_cxn(key_id, secret_key, name='cmb',
            endpoint='localhost', port='6059', is_secure=False):
    """
    A convenience function for creating a connection to CMB via boto
    """
    fake_region = regioninfo.SQSRegionInfo(name=name, endpoint=endpoint)
    logger.info("Create connection to cmb:%s at: %s:%s", name, endpoint, port)
    cxn = fake_region.connect(aws_access_key_id=key_id,
                              aws_secret_access_key=secret_key,
                              port=port, is_secure=is_secure)
    return cxn
