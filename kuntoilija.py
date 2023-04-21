# KUNTOILIJAN TIEDOT JA OLIO-OHJELMOINTINA
# ----------------------------------------

# Kirjastot ja modulit (libraries and modules)
# -------------------

import fitness
import math

# Luokkamääritykset (class of definitons)
# -----------------

# Kuntoilija luokka yliluokka JunioriKuntoilijalle (super fitness)
class Kuntoilija:
    """Luokka kuntoilijan tietoja varten"""

    #Olionmuodostin elin konstruktio
    def __init__(self, nimi, pituus, paino, ika, sukupuoli, kaula, vyotaro, lantio, paiva):

        # Määritellään tulevan olion ominaisuudet (property), luokan kentät (field) 
        self.nimi = nimi
        self.pituus = pituus
        self.paino = paino
        self.ika = ika
        self.sukupuoli = sukupuoli
        self.kaula = kaula
        self.vyotaro = vyotaro
        self.lantio = lantio
        self.bmi = fitness.laske_bmi(self.paino, self.pituus)
        self.fi_rasva = self.rasvaprosentti()

        if self.sukupuoli == 1:
            self.usa_rasvaprosentti = self.usarasvaprosentti_mies(self.pituus, self.vyotaro, self.punnitus_paiva)
        else:
            self.usa_rasvaprosentti = self.usarasvaprosentti_nainen(self.pituus, self.vyotaro, self.lantio, self.kaula)
        self.punnitus_paiva = paiva


    # Metodi rasvaprosentin laskemiseen (Yleinen / Aikuinen)
    def rasvaprosentti(self):
        if self.ika >= 18:

            self.rasvaprosentti = fitness.usarasvaprosentti_nainen(pituus=, lantion_ymparys=, vyotaron_ymparys=):


    
def usa_rasvaprosentti_mies(self, pituus, vyotaron_ymparys, kaulan_ymparys):
    """laske miehen rasvaprosentin USA:n armeijan kaavalla

    Args:
    pituus (float): pituus (cm)
    vyotaron_ymparys (float): vyotaron ympärysmitta (cm)
    kaulan_ymparys (float): kaulan ympärysmitta (cm)

    Returns:
    float: rasvaprosentti
    """

    fitness.usarasvaprosentti_mies(pituus,vyotaron_ymparys,kaulan_ymparys)

    # Muutetaan mitat tuumiksi
    tuumaa_pituus = pituus / 2.5
    tuumaa_vyotaron_ymparys = vyotaron_ymparys / 2.5
    tuumaa_kaulan_ymparys = kaulan_ymparys / 2.5

    # Laskentaan rasvaprosentti

    usarprosentti = 86.010 * math.log10(tuumaa_vyotaron_ymparys - tuumaa_kaulan_ymparys) - 70.041 * math.log10(tuumaa_pituus) + 36.76
    return usarprosentti

def usa_rasvaprosentti_nanen(self, pituus,vyotaron_ymparys,kaulan_ymparys,lantion_ymparys):
    """Laske naisen rasvaprosentti USA:n armeijan kaavalla

    Args:
        pituus (float): pituus (cm)
        vyotaron_ymparys (float): vyotaron ympärysmitta (cm)
        kaulan_ymparys (float): kaulan ympärysmitta (cm)
        lantion_ymparys (float)): lantion ymprärysmitta (cm)

    Returns:
        float : rasvaprosentti
    """
    
    fitness.usarasvaprosentti_nainen(pituus, lantion_ymparys, vyotaron_ymparys, kaulan_ymparys)

    # Muutetaan mitat tuumiksi
    tuumaa_pituus = pituus / 2.5
    tuumaa_vyotaron_ymparys = vyotaron_ymparys / 2.5
    tuumaa_kaulan_ymparys = kaulan_ymparys / 2.5
    tuumaa_lantion_ymparys = lantion_ymparys / 2.5

    # Lasketaan rasvaprosentti

    usarprosentti = 163.205 * math.log10(tuumaa_vyotaron_ymparys + tuumaa_kaulan_ymparys - tuumaa_lantion_ymparys) - 97.684 * math.log10(tuumaa_pituus) + 78.387
    return usarprosentti

# JunioriKuntoilija luokka Kuntoilija luokan yliluokka (subclass)
class JunioriKuntoilija(Kuntoilija):
    ###Luokka nuoren kuntoilijan tiedoille###
    def __init__(self, nimi, pituus, paino, ika, sukupuoli):

        # Määritellään, periytyminen, mitä ominaisuuksia perii
        super().__init__(nimi, pituus, paino, ika, sukupuoli)
    

     # Metodi rasvaprosentin laskemiseen (Ylikirjoitettu )
    def rasvaprosentti(self):
        self.rasvaprosentti = fitness.lapsen_rasvaprosentti(self.bmi, self.ika, self.sukupuoli)
        return self.rasvaprosentti



if __name__ == "__main__":

    kuntoilija = Kuntoilija('mika', 171, 75, 60, 1 30, 90, 0, '2023-04-21')
    print('bmi on', kuntoilija.bmi)
    print('Suomalainen rasvaprosentti on', kuntoilija.rasvaprosentti)
    print('')

    
    # Luodaan olio luokasta Kuntolija
    kuntoilija = Kuntoilija('Kalle kuntoilija', 171, 65, 40, 1)
    print(kuntoilija.nimi, 'painaa', kuntoilija.paino, 'kg' )
    # print('painoindeksi on ', kuntoilija.painoindeksi())
    print('rasvaprosentti on', kuntoilija.rasvaprosentti())

    juniorikuntoilija = JunioriKuntoilija(' aku', 171, 65, 16, 1)
    print(juniorikuntoilija.nimi, 'painaa', juniorikuntoilija.paino, 'kg' )
    # print('painoindeksi on ', kuntoilija.painoindeksi())
    rasvaprosentti = juniorikuntoilija.rasvaprosentti()
    print('rasvaprosentti on', rasvaprosentti)
