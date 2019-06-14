# anime_downloader

## Requirements

You need to have already installed Python3, [Chrome browser](https://www.google.com/chrome/) and [qbittorrent](https://www.qbittorrent.org).

Make sure you also have installed [pip](https://pip.pypa.io/en/stable/installing/) and run `pip install -r requirements.txt` from project root directory.


## Getting Started

First, you have to change the preferences / settings in qbittorrent. In the WebUI section:
1. check Web User Interface (remote control)
2. fill `127.0.0.1` in the IP address field and `8081` in the port field
3. in the authentification part, check `Bypass authentification for clients on localhost`

Keep in mind that qbittorrent application needs to be running in order to have the application running.

You can now go to the project root directory and launch the following commands:

```
export FLASK_APP=app
flask run
```
