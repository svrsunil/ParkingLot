# -*- coding: utf-8 -*-

import sys,os

class ParkingLot:
    
    def __init__(self, registration_number, cars_with_colour,slot_number):
        self.registration_numbers = registration_number
        self.cars_with_colour = cars_with_colour
        self.slot_numbers = slot_number
        
avalLot = []
totalLot = 0
alcoDict = {}

'''
This method will be called from switch if user request for create slot. 
It will add that slot no in avalLot List
@param : usrIp
@return : response String to display
'''

def setLot(usrIp):
    global totalLot
    if(totalLot > 0) :
        return 'Slot already set'
    totalLot =  int(usrIp.split(' ')[1])
    global avalLot
    avalLot = [(i+1) for i in range(totalLot)]
    return 'Created a parking lot with {0} slots'.format(totalLot)

'''
This method will be called from switch if user request for Parking. 
It will ADD the ParkingLot object from avalLot DICTIONARY and remove that slot no in avalLot List
@param : usrIp
@return : response String to display
'''
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

'''
This method will be called from switch if user request for car leaving. 
It will remove the ParkingLot object from avalLot DICTIONARY and add that slot no in avalLot List
@param : usrIp
@return : response String to display
'''

def carLeave(usrIp):
    msg = 'Slot number is Invalid'
    i = 0
    arr = usrIp.split(' ')
    key = int(arr[1])
    if key in alcoDict:
        del alcoDict[key]
        avalLot.append(key)
        msg = 'Slot number {0} is free'.format(key)
        
    return msg

'''
This method will be called from switch if user request for car Inquires
@param : usrIp
@return : response String to display
'''

def carInquiry(usrIp):
    
    qtns,ans = usrIp.split(' ')
    qtn = qtns.split('_for_')
    
    result = ''
    for key in sorted(alcoDict):
        parkingLot = alcoDict[key]
        
        try:
            getattr(parkingLot, qtn[1])
        except AttributeError:
           qtn[1] = qtn[1]+'s'

        try:
            getattr(parkingLot, qtn[0])
        except AttributeError:
           qtn[0] = qtn[0]+'s'
        
        if(str(getattr(parkingLot, qtn[1])) in ans):
            result = result + ', ' + str(getattr(parkingLot, qtn[0]))
    
    if(len(result) > 0) :
           result = result[2:] 
    else:
        result = 'Not found'
    return result

'''
This method will be called from switch if user request for status
@param : usrIp
@return : response String to display
'''

def status():
    result = 'Slot No.    Registration No    Colour'
    
    if len(alcoDict) == 0:
        return 'No Cars'
    for key in sorted(alcoDict):
        parkingLot = alcoDict[key]
        result += '\n'+str(key)+'           '+parkingLot.registration_numbers+'      '+parkingLot.cars_with_colour
    
    return result

'''
This method will interactive to user and call switch method for repsonse
@param : usrIp
@return : response String to display

'''
def interact(usrIp):
    usrIp = input(usrIp)
    print(switch(usrIp))
    interact('')
    
'''
This method will understand user request and routie to the responding method
@param : usrIp
@return : response String to display

'''

def switch(usrIp):
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
    
    return rsp

'''
This the main program called from script , it take argument as filename optional
If argument is empty it will invoke interactive method
@param : sys.argv[1] as filename
'''
if __name__== "__main__":
    
    if len(sys.argv) > 1:
        #print(sys.argv[1])
        if os.path.exists(sys.argv[1]) :
            f = open(sys.argv[1], "r")
            for x in f:
                print(switch(x).replace('\n\n','\n').strip())
        else:
            print('Invalid File')
    else :
        interact('')
