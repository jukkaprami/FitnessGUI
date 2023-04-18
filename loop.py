import unittest
runtest=0

def parillisuus():     
    for counter in range (10):
        if (counter % 2) == 0:
            print (counter)
            print ('on parillinen')
        else:
            print (counter)
            print ('on pariton')

if runtest==0:
    parillisuus()