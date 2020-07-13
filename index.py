#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 10:25:17 2020

@author: Emilio Silva
"""


class content():

              
    def askAndReturnSearchTerm():
        ask = input ( "Type a Wikipedia term: " )
        #print (ask)       
        return ask
               
        
    def askAndReturnPrefix():
        
        prefixes = ['Who is', 'Waht is', 'The history of']
        selectedPrefixIndex =  prefixes [int(input('Choose one Options:'))]
        #print (selectedPrefixIndex)
        return selectedPrefixIndex
        
    ask = askAndReturnSearchTerm();
    selectedPrefixIndex = askAndReturnPrefix();
   
    
    print('Term: ',ask, ' ' ,'Prefix: ', selectedPrefixIndex)

    
def start():
   
    content()   
 
              
    start()
      



  
    