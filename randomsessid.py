#!/usr/bin/env python

"""
Coded by: lqm33 github.com/lqm33 telegram:@lqm33
sqlmap random PHPSESSID. PHPSESSID protection bypass
"""

from lib.core.enums import PRIORITY
import random
__priority__ = PRIORITY.NORMAL

def dependencies():
    pass

def randomID():
    
    a=["q","w","e","r","t","y","u","o","p","a","s","d","f","g","h","j","k","l","i","z","x","c","v","b","n","m","0","1","2","3","4","5","6","7","8","9"]
    sessid=random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)
    phpsessid="PHPSESSID:"+sessid
    return phpsessid

def tamper(payload, **kwargs):
    """
    PHPSESSID Protect && block bypass
    """

    headers = kwargs.get("headers", {})
    headers["cookie"]=randomID()
        

    return payload
