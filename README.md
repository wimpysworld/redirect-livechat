# Redirect YouTube Live Chat

A simple Python server that redirects to a YouTube channel's most recent live
chat.

This script is primarily intended to run as a local server that can be embedded
as multiple browser sources or Browser Docks in OBS Studio. The server will
redirect to the most recent live chat URL for the given YouTube channel ID.

## Rationale

I reference YouTube live chat URLs in 3 places in my OBS setup, it was tedious
updating them all prior to going live. Now I reference `http://localhost:8008`
instead and the server takes care of the rest.

## Caveats

The script doesn't use the YouTube APIs, it will blindly derive a live chat URL
from the most recent videoId found in the given channel Id; even if that videoId
wasn't a live stream. The is by design to keep things simple.


# Usage

  * Clone this git repository
  * Run `redirect-livechat.py` with a YouTube channel ID.
  * Update your OBS browser source and Browser Docks to reference `http://localhost:8008`

```
usage: redirect-livechat.py [-h] [--addr ADDR] [--port PORT] channel_id

YouTube live chat re-director

positional arguments:
  channel_id            youtube channel ID

optional arguments:
  -h, --help            show this help message and exit
  --addr ADDR, -a ADDR  ip address
  --port PORT, -p PORT  port to listen on

example:

  redirect-livechat.py UCQvWX73GQygcwXOTSf_VDVg
```

This will start a webserver on localhost:8008, the output looks something like this:

```
Directing to https://www.youtube.com/live_chat?dark_theme=1&is_popout=1&v=D87-XmWigY0 via localhost:8008
127.0.0.1 - - [18/Feb/2021 13:30:15] "GET / HTTP/1.1" 302 -
```

<kbd>Ctrl</kbd> + <kbd>C</kbd> exits.

# TODO

  - [ ] Make a Snap
  - [ ] Make a Docker
