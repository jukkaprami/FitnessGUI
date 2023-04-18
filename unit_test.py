#***************************************************** 
# T1_2_2.py kaytetaan luvun parillisuuden tarkistamiseen.
# @author tekija: (ensimmaisen version tekija, omat nimikirjaimet) 
# @since pvm: (versio pvm 18.4.2023) 
# @version versio: (versionumero 1.0) 
# muutos: (nimikirjaimet omat nimikirjaimet) 
#*****************************************************/

#KOODAA SEURAAVA OHJELMA, MITA KOODI TULOSTAA?
#Koodaa seuraava Python- ohjelma kayttaen tyoasemalle asennettua Python ohjelmaa.
#Esittele koodaamasi ohjelma opettajalle ja vastaa kysymyksiin. Pida koodaamasi ohjelma tallessa esim. github:ssa myohempaa tarkastelua varten.

#Yksikkotestausvaiheet:
#1.luo kansio koodille tai lataa github:sta opettajan tehtavan repositori ja avaa kansio seka luo python file kansioon
#(kansion polussa ei saa olla skandeja joten ala kayta onedrivea koska kulun nimessa on skandeja)
#2.lisaa koodin header alkuun mallin mukaan ja lisaa pvm seka omat nimikirjaimet
#3. poista koodista kaikki skandit
#4.muokataan koodi funktiomuotoon (nimea fuktio)
#5.importoidaan yksikkotestikirjasto
#6.lisataan runtest- muuttuja.
#7.jos runtest==0 niin ohjelma kutsuu em. luotua funktiota ja ohjelma toimii normaalisti
#  testaa etta koodi toimii normaalisti kun runtest==0
#8.lisataan testauksessa tarvittavat fuktioparametrit ja vertailut
# (kun runtest==1 niin blokataan mahdolliset kayttoliittymainputit yms. pois koodista)
# -> em. blokatut muuttujat syotetaan funktioparametreina testattavaan funktioon#
#9.testaa etta peruskoodi tulostaa testattavaa numeroa vastaavan testiarvon
#kun peruskoodi tulostaaa oikeita arvoja syottoparametreilla niin lisataan testiluokka seka return lauseke 
#peruskoodiin
#10.lisataan testiluokka ja testifuktiot
#11.ajetaan yksikkotestit terminaalista ja dokumentoidaan koodi (github)
#12.palauta yksikkotestattu koodi githubin "fork"- toiminnolla opettajalle opettajan repositoriin 

import unittest
runtest=0

def testattava_funktio(paluuarvo):
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
    paluuarvo='testin tulos jos ok'

    if runtest==1:
        return paluuarvo

if runtest==0:
    testattava_funktio(1)

#aja testi kaskylla:
#python -m unittest unit_test.py
#luokan nimen tulee olla sama kuin tiedostonnimen (ilman .py paatetta)
class test_unit_test(unittest.TestCase):
    def test_unit_test_parillinen(self):
        testiarvo = 1
        actual = str(testattava_funktio(testiarvo))
        excepted = 'on parillinen'
        if runtest == 1:
            assert actual == excepted
        
        print('Virhe testifunktion parillisuuden tarkastamisessa' + ' Numero = ' + str(testiarvo) + excepted)

        def unit_test_pariton(self):
            testiarvo = 2
            actual = str(testattava_funktio(testiarvo))
            excepted = 'on pariton'
        try:
            assert actual == excepted
        except:
            print('Virhe testifunktion parittomuuden tarkastamisessa' + ' Numero = ' + str(testiarvo) + excepted)
        
        return runtest == 1
    