# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 22:56:26 2019

@author: svrsunil
"""
import sys

class ParkingLot:
    
    def __init__(self, regNo, color,lot):
        self.regNo = regNo
        self.color = color
        self.lot = lot
        
avalLot = []
totLot = 0
alcoDict = {}

def setLot(usrIp):
    print('s'+usrIp)
    global totLot
    totLot =  int(usrIp.split(' ')[1])
    print(totLot)
    global avalLot
    avalLot = [(i+1) for i in range(totalLot)]
    return 'Created a parking lot with {0} slots'.format(totalLot)

def carPark(usrIp):
    
    msg = 'Sorry, parking lot is full'
    i = 0
    if(len(avalLot) > 0) :
        
        i = sorted(avalLot)[0]
        arr = usrIp.split(' ')
        parkingLot = ParkingLot(arr[1],arr[2],i)
        alcoDict[i] = parkingLot
        avalLot.remove(i)
        print(alcoDict)
        msg = 'Allocated slot number:{0}'.format(i)
    return msg

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