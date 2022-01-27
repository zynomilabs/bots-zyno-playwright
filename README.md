# bots-zyno-playwright
software bots developed in playwright python stack

## Installation and setup for command line execution

For these examples to work, ensure that:

- you are running Linux or macOS
- Python 3.7, 3.8, or 3.9 has been installed

```
python3 --version
```

> Clone the repository and `cd` into the root folder

> Create and activate virtual environment, and update pip

```
python3 -m venv .venv
source .venv/bin/activate
pip3 install pip --upgrade
```

> Install playwright

```
pip3 install playwright
```

> Install playwright CLI

```
playwright install
```

> Run the `zoom.py` robot

```bash
python3 zoom.py
```

## Allow port for inbound access

```
#Allow
firewall-cmd --zone=public --permanent --add-port=3000/tcp
sudo firewall-cmd --zone=public --permanent --add-port=8080/tcp

# Refresh
firewall-cmd --reload
```
http://129.158.63.35:3000/export/doc

# Installation and setup as API

## Prerequisite

- Python3
- Pip
- Virtualenvironment

## Installation

1. Clone the repository
   `git clone https://github.com/senthilsweb/playwright-bots.git`

1. Change directory to `zybots\docx`
   `cd playwright-bots`

1. Create virtual environment inside the project root
   `virtualenv venv -p python3.7`

1. Activate the virtual environment from the bin folder inside the **venv**

`source ./venv/bin/activate`

1 Go to project root folder and then Install dependencies

`cd to root folder`

`pip install -r requirements.txt`

1 Start the sever

`gunicorn resources.api:app -b 127.0.0.1:3000`

## API available in this sample code

### Schedule zoom meeting

> POST http://localhost:3000/schedule/zoom

```
{
    "username": "yourname@email.com",
    "password": "your_password",
    "loginurl": "https://zoom.us/signin"
}
```

### Generate word file from docx template

> POST http://127.0.0.1:3000/export/word

```
{
    "user": {
        "firstname": "John",
        "project": {
            "name": "Robot framework development"
        }
    },
    "template": {
        "file": "exp-template.docx"
    }
}
```

