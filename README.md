## Install on a system with Python, Pip and Pyenv
pip install -r requirements.txt

## Install Somehwere Else
### Debian/ubuntu
#### Install Python
```bash
sudo apt-update
sudo apt install python3
nano ~/.bash_profile
alias python='usr/bin/python3.8'
source ~/.bash_profile
python --version
```
#### Install Pip
```bash
sudo apt-update && \
sudo apt install python3-pip -y
```
`alias pip=pip3`
#### Install `pyenv`
```bash
sudo apt-get update; sudo apt-get install make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

