import os
import argparse

HOST = os.environ.get('N3FJP_HOST', '127.0.0.1')
PORT = int(os.environ.get('N3FJP_PORT', '1100'))

def parse_clargs():
    parser = argparse.ArgumentParser(description='N3FJP Log Sender')
    parser.add_argument('--host', required=False, metavar='HOST', type=str, default=HOST, help='N3FJP host or IP')
    parser.add_argument('--port', required=False, metavar='PORT', type=int, default=PORT, help='N3FJP port')
    parser.add_argument('--pota', required=False, help='Turns on POTA mode (detects parks)', action="store_true")
    parser.add_argument('--verbose', required=False, help='Enables verbose logging', action='store_true')
    parser.add_argument('--dry', required=False, help='Does everything but the log write.', action='store_true')
    parser.add_argument('logline', help="Formatted as: day,time,freq,call,recv,sent,mode,their_park,my_park,comment. \
        day and time are optional. omit their_park and my_park if you're not doing pota. \
        everything else needs to be there.")
    return parser.parse_args()
