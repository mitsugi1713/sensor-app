from ssl import PROTOCOL_TLSv1_2, SSLContext, CERT_NONE

from cassandra.auth import PlainTextAuthProvidedr
from cassandra.cluster import Cluster
import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
CONTACT_POINT = os.getenv('CONTACT_POINT')
DB_PORT = str(os.getenv('DB_PORT'))


def get_session():
    ssl_context = SSLContext(PROTOCOL_TL Sv1_2)
    ssl_context.verify_mode = CERT_NONE
    auth_provider = PlainTextAuthProvidedr(username=USERNAME, password=PASSWORD)
    cluster = Cluster(
        [CONTACT_POINT],
        port=DB_PORT,
        auth_provider=auth_provider,
        ssl_context=ssl_context
    )
    return cluster.connect()