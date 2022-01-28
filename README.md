# bots-zyno-playwright
software bots developed in playwright python stack

## Installation and setup for command line execution

For these examples to work, ensure that:

- you are running Linux or macOS
- Python 3.7, 3.8, or 3.9 has been installed

```
python3 --version
```

* Clone the repository and `cd` into the root folder
* Create and activate virtual environment, and update pip

```
python3 -m venv .venv
source .venv/bin/activate
pip3 install pip --upgrade
```
- Install playwright and playwright CLI

```
pip3 install playwright
playwright install
```

- Run the code 

Note: `zoom.py` has been removed from this repo.

```
python3 zoom.py
```


# Installation and setup as API

- Clone the repository

 ```
 git clone https://github.com/senthilsweb/playwright-bots.git
 ```

- Change directory to `zybots\docx`
  
```
cd playwright-bots
```

- Create virtual environment inside the project root

```
python3 -m venv .venv
source .venv/bin/activate
```


- Go to project root folder and then Install dependencies

cd to root folder

```
pip install -r requirements.txt
```

> Start the sever

```
gunicorn resources.api:app -b 0.0.0.0:3000
```

## RESTful APIs

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



## Miscellaneous

### Allow port for inbound access in Oracle cloud

```
#Allow
firewall-cmd --zone=public --permanent --add-port=3000/tcp
sudo firewall-cmd --zone=public --permanent --add-port=8080/tcp

# Refresh
firewall-cmd --reload
```
