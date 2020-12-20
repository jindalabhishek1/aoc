import re

def inp():
    fname = input ("Enter input file name: ")
    try :
        fhand = open (fname)
    except:
        print ("You have provided wrong name, choosing sample input file!!!")
        fname = "../sample_input.txt"
        fhand = open (fname)
    
    for line in fhand:
        line = line.rstrip()
        regString = "([a-z ]+)(?= bags)"
        temp = tuple()
        re.match(line, regString)

bagsList = list()
bagsList = inp()
print (bagsList)