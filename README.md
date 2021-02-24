# Redirect YouTube Live Chat [![Discord](https://img.shields.io/discord/712850672223125565?color=0C306A&label=WimpysWorld%20Discord&logo=Discord&logoColor=ffffff&style=flat-square)](https://discord.gg/KcEGTDEhZK)

A simple Python 🐍 server that redirects to a YouTube 📺 channel's most recent
live chat 💬 URL.

This script is primarily intended to run as a local server that can be embedded
as multiple browser sources or Browser Docks in [OBS Studio](https://obsproject.com/).
The server will redirect 👉 to the most recent live chat URL for the given
YouTube channel ID.

## Rationale

My OBS setup references YouTube live chat URLs in three different places; it was
tedious updating them all prior to going live 📡 Now I reference `http://localhost:8008`
instead and the server takes care of the rest.

## Caveats

The script does not use YouTube APIs, it will blindly 🙈 derive a live chat URL
from the most recent `videoId` found for the given channel; even if that `videoId`
wasn't a live stream. This is by design to keep things simple.

# Usage

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

## From Docker

Run the following commands to build and run the Docker container:

```console
$ docker build -t redirect-livechat .
$ docker run -p 8008:8008 -it redirect-livechat -a 0.0.0.0 UCQvWX73GQygcwXOTSf_VDVg
```

## From Source

  * Clone this git repository
  * Run `redirect-livechat.py` with a YouTube channel ID.
  * Update your OBS browser source(s) and Browser Dock(s) to reference `http://localhost:8008`

# TODO

  - [ ] Make a Snap
  - [x] Make a Docker
