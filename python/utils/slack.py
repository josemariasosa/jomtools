#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils.config import SLACK
import requests

class Slack():
    def send_notification(self, message, channel=None):
        self.url = SLACK["URL"]
        payload = {"text": message}
        if bool(channel):
        	payload["channel"] = "#" + channel
        requests.post(self.url, json=payload)

