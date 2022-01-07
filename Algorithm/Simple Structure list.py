# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 11:38:25 2022

@author: gi930
"""

def add_data(friend):
    katok.append(None)
    katok[len(katok)-1] =friend

def insert_dat(position,friend):
    katok.append(None)
    for i in range(len(katok)-1,position,-1):
        katok[i] = katok[i-1]
        katok[i-1] = None
    katok[position] = friend

def delete_data(position):
    katok[position] = None
    for i in range(position,len(katok)-1):
        katok[i] = katok[i+1]
        katok[i+1] = None
    del(katok[len(katok)-1])
    
    
    
    
    
    
    
    
katok = ['다현','정연','쯔위','사나','지효']

katok
add_data('모모')
katok
insert_dat(3,'미나')
katok
delete_data(4)
katok


