import os
from dotenv import load_dotenv
from pyftpdlib.servers import FTPServer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.authorizers import DummyAuthorizer

#load configs 
load_dotenv()

FTP_USER = os.getenv("FTP_USER")
FTP_PASS = os.getenv("FTP_PASS")
FTP_DIR = os.getenv("FTP_DIR")  

if not FTP_DIR:
    raise ValueError("FTP_DIR is not set. Please set it in your .env file or as a default.")

authorizer = DummyAuthorizer()
authorizer.add_user(FTP_USER, FTP_PASS, FTP_DIR, perm="elradfmw")
handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("0.0.0.0", 2121), handler)
print("FTP Server running on port 2121...")
server.serve_forever()
