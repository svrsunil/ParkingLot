# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 16:54:16 2019

@author: svrsunil
"""
import sys

class ParkingLot:
    
    def __init__(self, registration_number, cars_with_colour,slot_number):
        self.registration_number = registration_number
        self.cars_with_colour = cars_with_colour
        self.slot_number = slot_number
        
avalLot = []
totLot = 0
alcoDict = {}

def setLot(usrIp):
    global totLot
    if(totLot > 0) :
        return 'Slot already set'
    totLot =  int(usrIp.split(' ')[1])
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
        msg = 'Allocated slot number:{0}'.format(i)
    return msg

def carLeave(usrIp):
    print(usrIp)
    msg = 'Slot number is Invalid'
    i = 0
    arr = usrIp.split(' ')
    print(arr)
    key = int(arr[1])
    if key in alcoDict:
        del alcoDict[key]
        avalLot.append(key)
        msg = 'Slot number {0} is free'.format(key)
        
    return msg

def carInquiry(usrIp):
    
    qtns,ans = usrIp.split(' ')
    qtn = qtns.split('_for_')
    print(qtn)
    result = ''
    for key in sorted(alcoDict):
        result = result + ', ' + str(getattr(alcoDict[key], qtn[0]))
        
    return result[2:]
    
def status():
    result = 'Slot No.    Registration No    Colour'
     
    for key in sorted(alcoDict):
        parkingLot = alcoDict[key]
        result = result + '\n'+str(key)+'           '+parkingLot.registration_number+'      '+parkingLot.cars_with_colour
    
    return result
 
def interact(usrIp):
    usrIp = input(usrIp)
    
    rsp = ''
    if('create_parking_lot' in usrIp):
        
        rsp= setLot(usrIp)
    elif('park' in usrIp) :
        rsp= carPark(usrIp)
    elif('leave' in usrIp) :
        rsp= carLeave(usrIp)
    elif('status' in usrIp) :
        rsp= status()        
    elif('_for_' in usrIp) :
        rsp= carInquiry(usrIp)        
    elif('exit' == usrIp) :
        sys.exit(0)
    else :
        rsp = 'Invalid Arugment'
    print(rsp)
    interact('')

if __name__== "__main__":
    
    if len(sys.argv) > 1:
        print(sys.argv[1])
    else :
        print("No")
        interact('')
