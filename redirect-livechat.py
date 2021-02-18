#!/usr/bin/env python3

import argparse
import http.server
import signal
import socketserver
import sys
import urllib.request
import urllib.error


def signal_handler(signal_received, frame):
    """
    Signal handler that exits gracefully
    """
    sys.exit(0)


def redirect_handler_factory(url):
    """
    Returns a request handler class that redirects to supplied `url`
    """
    class RedirectHandler(http.server.SimpleHTTPRequestHandler):
       def do_GET(self):
           self.send_response(302)
           self.send_header('Location', url)
           self.end_headers()

    return RedirectHandler


def main():
    example_usage = """example:

  redirect-livechat.py UCQvWX73GQygcwXOTSf_VDVg"""

    parser = argparse.ArgumentParser(description='YouTube live chat re-director',
                                     epilog=example_usage,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--addr', '-a', action="store", default="localhost", help='ip address', type=str)
    parser.add_argument('--port', '-p', action="store", default=8008, help='port to listen on', type=int)
    parser.add_argument('channel_id', action="store", help='youtube channel ID', type=str)
    args = parser.parse_args()

    channel_url = "https://www.youtube.com/channel/%s" % args.channel_id
    keyword = '"videoId":'

    # Try get the channel data
    try:
        with urllib.request.urlopen(channel_url) as response:
            data = str(response.read())
    except urllib.error.HTTPError as e:
        print("Error %s, %s: %s" % (e.code, e.reason, channel_url))
        sys.exit(1)
    except urllib.error.URLError as e:
        print("Error, %s: %s" % (e.reason, channel_url))
        sys.exit(1)
    else:
        # Find the character offset to the latest videoId
        keyword_offset = 1 + data.find(keyword) + len(keyword)

        # If the offset is the same as keyword length, the keyword was not found.
        if keyword_offset == len(keyword):
            print("Error, the keyword %s was not found in %s" % (keyword, channel_url))
            sys.exit(1)

        # Derive the live chat URL
        chat_url = "https://www.youtube.com/live_chat?dark_theme=1&is_popout=1&v=%s" % data[keyword_offset:keyword_offset+11]

        # Initialise the signal handler to catch Ctrl+C
        signal.signal(signal.SIGINT, signal_handler)

        # Initialise the redirect handler
        handler = socketserver.TCPServer((args.addr, args.port), redirect_handler_factory(chat_url))
        print("Directing to %s via %s:%s" % (chat_url, args.addr, args.port))
        handler.serve_forever()


if __name__ == "__main__":
    main()
