# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 11:27:18 2019

@author: svrsunil
"""

import Main as m

def test_create_lot(i):
    assert m.setLot(('create_parking_lot {0}').format(i)) == 'Created a parking lot with {0} slots'.format(i), 'Failed in creating parking lot'

def test_carPark(usrIp,op):
    assert m.carPark(usrIp) == op, 'Failed in Allocating lot'

def test_carLeave(usrIp):
    assert m.carLeave(usrIp) == 'Slot number {0} is free'.format(usrIp.split(' ')[1]), 'Failed in removing parking lot'

def test_carInquiry(usrIp,op):
    assert m.carInquiry(usrIp) == op, 'Failed in car inquiry'

if __name__== "__main__":
    
    test_create_lot(2)
    test_carPark('park KA-01-HH-1234 White','Allocated slot number:1')
    test_carPark('park KA-01-HH-9999 White','Allocated slot number:2')
    test_carLeave('leave 1')
    test_carPark('park KA-01-HH-2701 Blue','Allocated slot number:1')
    test_carPark('park KA-01-HH-2701 Blue','Sorry, parking lot is full')
    test_carInquiry('slot_numbers_for_cars_with_colour White','2')
    test_carInquiry('registration_numbers_for_cars_with_colour White','KA-01-HH-9999')
    test_carInquiry('slot_number_for_registration_number KA-01-HH-1234','Not found')
    