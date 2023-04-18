import unittest
runtest = 1

def parillisuus(luku):     
    for counter in range (1, luku +1):
        if (counter % 2) == 0:
            print (counter)
            palautusarvo = 'on parillinen'
            print ('on parillinen')
        else:
            print (counter)
            palautusarvo = 'on pariton'
            print ('on pariton')
    if runtest == 1:
        return palautusarvo

if runtest == 0:
    parillisuus(2)

# python.exe -m unittest loop.py
class test_loop(unittest.TestCase):
    def test_loop_parillinen(self):
        testiarvo = 1
        actual = str(parillisuus(testiarvo))
        excepted = 'on parillinen'
        try:
            assert actual == excepted
        except:
            print('Virhe parittomuuden tarkastamisessa' + ' Numero = ' + str(testiarvo) + ' ' actual + '!=' + excepted)

        def test_loop_pariton(self):
            testiarvo = 1
            actual = str(parillisuus(testiarvo))
            excepted = 'on pariton'
        try:
            assert actual == excepted
        except:
            print('Virhe parittomuuden tarkastamisessa' + ' Numero = ' + str(testiarvo) + ' ' actual + '!=' + excepted)   
