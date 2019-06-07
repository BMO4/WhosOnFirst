##################################################################################################
##
##  name:           whos_on_first.py
##  author:         Matt Crane
##  date:           1/4/2018
##  description:    a simple humorous interactive program based on the classic(genius)comic sketch
##                  "Who's On First" by Abbott and Costello circa 1937 (see on YouTube)
##                  Also an exercise in regular expressions and linguistic heuristics.
##                  (Declaratives mixed up with interogatives)
##                  Stick to lowercase with no punctuation for best results!
##  license:        GNU GPLv3.0
##  modifications:  originally written as Linux case switches, converted to python 7/6/2019
##
##################################################################################################

import re                                                                  
response = input("Abbott: whos on first"+'\n'+"Costello: ")
shortstop="i dont give a darn"
while response != shortstop:
    if re.search(r'(.*what.*name.*first.*)', response):
        response = input("Abbott: who"+'\n'+"Costello: ")
    elif re.search(r'(.*what.*name.*third)',response):
        response = input("Abbott: i dont know"+'\n'+"Costello: ")
    elif re.search(r'(^who.*second.*)',response):
        response = input("Abbott: who is on first, what is on second"+'\n'+"Costello: ")
    elif "asking" in response:
        response = input("Abbott: im telling you, whos on first, whats on second, i dont knows on third"+ '\n'+ "Costello: ")
    elif response  == "what":
        response = input("Abbott: whats on second, whos on first"+ '\n'+ "Costello: ")
    elif re.search(r'(^what.*second)', response):
        response = input("Abbott: thats right"+'\n'+"Costello: ")
    elif re.search(r'(.*who.*first)',response):
        response = input("Abbott: yes"+'\n'+"Costello: ") 
    elif re.search(r'(.*who.*second)',response):
        response = ("Abbott: who's on first, what is on second"+'\n'+"Costello: ")
    elif re.search(r'(.*who.*third)',response):
        response = ("Abbott: i dont know"+'\n'+"Costello: ")
    elif re.search(r'(.*i.*dont.*know)',response):               
        response = input("Abbott: you do know these guys names, hes on third"+'\n'+"Costello: ")
    elif  "who" in response:
        response = input("Abbott: whos on first" + '\n' + "Costello: ")
    elif  "what" in response:
        response = input("Abbott: hes on second" + '\n' + "Costello: ")
    elif response == shortstop:
        print("Abbott: ohh he's our shortstop")

