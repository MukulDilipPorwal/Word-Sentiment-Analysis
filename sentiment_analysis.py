#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 14:06:01 2018

@author: muporwal
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 01:13:58 2018

@author: muporwal
"""


#importing required libraries
import RPi.GPIO as GPIO
import time

#setting up the pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)



#Function to check if entered_word is present in file_to_check
def check_word_in_file(word, file_to_check):
    a=0
    text_file = open(file_to_check, "r")
    all_words=text_file.read().split('\n')
    if word in all_words:
            a+=1
    return a


#main body of the program
while(True):
    entered_value = raw_input("Enter 1 to exit and 2 to continue.")
    if (entered_value == '1'):
        print ("Quiting the application. Bye!")
        break
    
    elif (entered_value == '2'):
        #input from user
        entered_word = raw_input("Enter a word to check the associated sentiment.").lower()
        
        #testing if word is negative
        neg= check_word_in_file(entered_word, "/home/pi/Documents/negative_words_only.txt")
        #testing if word is positive
        pos= check_word_in_file(entered_word, "/home/pi/Documents/positive_words_only.txt")
        
        #associated sentiment
        if (pos == 1):
            senti="positive"
            pin=18
        elif (neg==1):
            senti="negative"
            pin=14
        else:
            senti="neutral"
            pin=15
            
            
        print("LED is on based on sentiment" )
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(3)
        print("LED going off")
        GPIO.output(pin,GPIO.LOW)
        
        #Printing Result
        print ("Entered word is:", entered_word )
        print ("Associated sentiment is " + senti)
    
    else:
        continue



