# anime_downloader

## Disclaimer
**ATTENTION: This is only a example of to use a python bind of torrent library in Python for educational purposes.            I am not responsible for your download of illegal content or without permission. Please respect the laws license permits of your country.**

## Requirements

You need to have already installed [Python3](https://www.python.org/downloads/), [Chrome browser v75+](https://www.google.com/chrome/) and [qbittorrent](https://www.qbittorrent.org).

Make sure you also have installed [pip](https://pip.pypa.io/en/stable/installing/). Run the following commands at the project root:
1. `python3 -m venv venv` if you're on macOS / linux or `py -m venv venv` on windows to create a virtual environment
2. `source venv/bin/activate` if you're on macOS / linux or `.\venv\Scripts\activate` on windows to activate the venv 
3. `pip install -r requirements.txt` to install the dependencies


## Getting Started

First, you have to change the preferences / settings in qbittorrent. In the WebUI section:
1. check Web User Interface (remote control)
2. fill `127.0.0.1` in the IP address field and `8081` in the port field
3. in the authentification part, check `Bypass authentification for clients on localhost`

Keep in mind that qbittorrent application **needs to be launched before the python application**.

You can now go to the project root directory and launch the following commands:

1. `export FLASK_APP=app` if you're on macOS / linux or `SET FLASK_APP=app` on windows 
2. `flask run`

The application will then be accessible from [127.0.0.1:5000](http://127.0.0.1:5000/), just choose your anime in the dropdown list, the resolution and the desired output directory and click on download.
