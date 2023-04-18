import unittest
runtest=0

def parillisuus(luku):     
    for counter in range (1, luku +1):
        if (counter % 2) == 0:
            print (counter)
            print ('on parillinen')
        else:
            print (counter)
            print ('on pariton')

if runtest==0:
    parillisuus(2)

class test_loop(unittest.TestCase):
    def test_loop(self):
        testiarvo = 1
        actual = str(parillisuus(testiarvo))
        excepted = 'pariton'
    
