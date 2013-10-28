# Prerequirement

- Ubuntu 12.04
- Python 2.7

# Installation

-   Libraries

    Before installing python packages, we must make sure next libraries are installed: libsssl, python-dev, livevent.

        $ sudo apt-get install libssl-dev python-dev libevent-dev

- Python Packages. It's strongly recommended to install python packages using virtual environment.

        $ pip install -r requirements.txt --use-mirrors

# Run the web server
  
We defines below env variables:

- ZK_URI: url://<ip>:<port>
- WEB_PORT: port of the web server

Start server using below command:

    $ python app.py

It will read configuration from environment, and use default in case of no defination in environment.

Or we can define env in command line:

    $ ZK_URI=192.168.7.212:2181 WEB_PORT=8080 python app.py


