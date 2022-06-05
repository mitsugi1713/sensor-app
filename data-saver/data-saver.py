import datetime
import os
import urllib.parse
from http.server import BaseHTTPRequestHandler, HTTPServer

from dotenv import load_dotenv

import helper

session = helper.get_session()

hostName = "0.0.0.0"

load_dotenv()
SERVER_PORT = int(os.getenv('SERVER_PORT'))


def save_data(data):
    datetime_now = datetime.datetime.now()
    session.execute(
        "INSERT INTO sensors.temperature (id, record_date, record_time, sensor, temperature) VALUES (now(), %s, %s, %s, %s)",
        [datetime_now.strftime('%Y-%m-%d'), datetime_now.strftime('%H:%M:%S'), data['device'][0],
         float(data['temperature'][0])]
    )
    return True

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        query = urllib.parse.urlparse(self.path)

        result = 'not-processed'
        if query.path == '/save':
            if save_data(urllib.parse.parse_qs(query.query)):
                self.wfile.write(bytes('{"result": true}', "utf-8"))
                result = 'data-processed'
            else:
                self.wfile.write(bytes('{"result": false}', "utf-8"))
                result = 'data-processed-with-error-result'
        
        print("%s request: %s result: %s" % (str(datetime.datetime.now()), self.path, result))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, SERVER_PORT), MyServer)
    print("Server start http://%s:%s" % (hostName, SERVER_PORT))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")