
<img src="https://www.hackthebox.eu/images/favicon.png" width="50" align="right">

# HTB Cancel Machine Resets Bot

[![built with Selenium](https://img.shields.io/badge/built%20with-Selenium-yellow.svg)](https://github.com/SeleniumHQ/selenium)
[![built with Python3](https://img.shields.io/badge/built%20with-Python3-red.svg)](https://www.python.org/)

Script that automatically detects and cancels machine resets, so that you don't have to. 
Please Star this repo if you enjoy it!
Let the script running and enjoy hacking, distraction free!


Table of Contents
=================

* [Getting Started](#getting-started)
  * [Requirements](#requirements)
  * [Installation](#installation)
* [How to use](#how-to-use)  
* [How to contribute](#how-to-contribute)  

## Getting started

### Requirements:
  - Check your chrome version `google-chrome --version`
  - Download Chromedriver: http://chromedriver.chromium.org/downloads
  - Add it to the same directory with the script
  
  Also make sure you've installed selenium using pip
  ```bash
  sudo apt install python-pip -y
  pip install selenium 
  ```
  
### Installation:

```bash
https://github.com/DimitrisPr/HTB-Machine-Reset-Cancellation-Bot.git
cd HTB-Machine-Reset-Cancellation-Bot
```

then add chromedriver.exe in project directory

## How to use

Change these variables with your credentials and the name of the machine you are trying to root

```
username = 'your_email_here'
password = 'your_password_here'
machine_name = "the_machine_name_here"
```

Execute it:

```bash
$ python monitor_resets.py
```

**Disclaimer**: I am by no means responsible for any usage of this tool. 
