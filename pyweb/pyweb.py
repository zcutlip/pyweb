import argparse
# import http.server
from http.server import SimpleHTTPRequestHandler
import socketserver
import os
import logging

PORT = 8080
# ~/.pyweb
DEFAULT_PYWEB_HOME = os.path.join(os.getenv("HOME"), ".pyweb")
# ~/.pyweb/var
DEFAULT_PYWEB_VAR = os.path.join(DEFAULT_PYWEB_HOME, "var")
# ~/.pyweb/var/www
DEFAULT_PYWEB_CONTENT_DIR = os.path.join(DEFAULT_PYWEB_VAR, "www")
# ~/.pyweb/var/log
DEFAULT_PYWEB_LOG_DIR = os.path.join(DEFAULT_PYWEB_VAR, "log")


class LoggingHttpHandler(SimpleHTTPRequestHandler):

    def log_message(self, format, *args):
        logging.info("%s -- [%s] %s" % (self.client_address[0], self.log_date_time_string(), format % args))


def serve(config):
    web_dir = config["path"]
    port = config["port"]
    os.chdir(web_dir)

    Handler = LoggingHttpHandler
    socketserver.TCPServer.allow_reuse_address = True
    httpd = socketserver.TCPServer(("127.0.0.1", port), Handler)
    logging.info("Serving at port: %d" % port)
    logging.info("Serving at path: %s" % web_dir)
    httpd.serve_forever()


def parse_args(argv):
    parser = argparse.ArgumentParser()

    parser.add_argument("--port", help="TCP port to listen on.", type=int)
    parser.add_argument("--www-root", help="WWW root path to serve from.")
    parser.add_argument("--log-path", help="Directory to write logfiles to.")
    args = parser.parse_args(argv)

    return args


def main(argv):
    args = parse_args(argv)

    port = args.port or PORT
    path = args.www_root or DEFAULT_PYWEB_CONTENT_DIR
    logpath = args.log_path or DEFAULT_PYWEB_LOG_DIR

    logging.basicConfig(filename=os.path.join(logpath, "pyweb.log"), level=logging.DEBUG)

    config = {"port": port,
              "path": path}

    serve(config)
