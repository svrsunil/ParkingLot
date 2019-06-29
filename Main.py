# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 22:56:26 2019

@author: svrsunil
"""
import sys

def interact(usrIp):
    usrIp = input(usrIp)
    
    rsp = ''
    if('create_parking_lot' in usrIp):
        rsp= setLot(usrIp)
    elif('park' in usrIp) :
        rsp= carPark(usrIp)
    elif('park' in usrIp) :
        rsp= carPark(usrIp)
    elif('exit' == usrIp) :
        sys.exit(0)
    else :
        rsp = 'Invalid Arugment'
    
    interact('')

if __name__== "__main__":
    
    if len(sys.argv) > 1:
        print(sys.argv[1])
    else :
        print("No")
        interact('')