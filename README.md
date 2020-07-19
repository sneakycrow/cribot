# cribot

### Installation

#### Prerequisites

+ [python3](https://www.python.org/downloads/) 
+ [pip](https://pip.pypa.io/en/stable/installing/)

#### Clone

```sh
git clone https://github.com/sneakycrow/cribot.git
```

#### Setup

```sh
cd cribot
```
Create a bot account ([guide](https://discordpy.readthedocs.io/en/latest/discord.html)) to get a bot **token**. Create an environment variable as below. (If you do not want to do this everytime, add this line to *.bascrc* file)
```sh
export DISCORD_TOKEN=token
```
Virtual environment (optional)
```sh
python -m pip install venv
python -m venv bot-env
source bot-env/bin/activate
```
Install dependencies
```sh
python -m pip install -r requirements.txt
```

### Usage
Run *main.py*
```sh
python3 main.py
```
