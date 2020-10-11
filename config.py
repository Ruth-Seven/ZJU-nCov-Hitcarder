import os, sys

import json

from sender import EmailSender

class Config(object):
    
    def __init__(self, config=None):
        if config == None:
            return
        
        self.username = config["username"]
        self.password = config["password"]
        self.hour = config["schedule"]["hour"]
        self.minute = config["schedule"]["minute"]

        self.set_sender = config["set_sender"]
        self.set_host = config["set_host"]
  
        if(self.set_sender):
            self.mail_user = config["mail_user"]
            self.mail_pass = config["mail_pass"]
            self.mail_receivers = config["mail_receiver"]
            self.sender = EmailSender(self.mail_user, self.mail_pass, self.mail_receivers)

            if(self.set_host):
                self.mail_host = config["mail_host"]            


    def changeItem(self, username, password, hour, minute, set_sender=False, set_host=False, sender=None, mail_host=None ):
        self.username = username
        self.password = password
        self.hour = hour
        self.minute = minute

        self.set_sender = set_sender
        self.set_host = set_host
        self.mail_host = mail_host

class configCollection(object):

    def __init__(self, configfilename):
        if os.path.exists('./config.json'):
            configItmes = json.loads(open('./config.json', 'r').read())
            self.configs = []
            idx = 0
            for item in configItmes.values():
                self.configs.append(Config(item))        
    
    def getconfigs(self):
        return self.configs


    def example(self):
        pass