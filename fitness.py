# SOVELLUS PAINOINDEKSIN JA KEHON RASVAPROSENTIN LASKEMISEEN
# ==========================================================

# Kirjastot ja moduulit
import math

# Määritellään funktio painoindeksin laskentaan
def laske_bmi(paino, pituus):
    """Laske painoindeksin (BMI)

    Args:
        paino (float): paino (kg)
        pituus (float): pituus (cm)

    Returns:
        _float: painoindeksi desimaalin tarkkuudella_
    """
    pituus = pituus / 100 # muutetaan pituus metreiksi
    bmi = paino / pituus**2
    bmi= round (bmi, 1)
    return bmi

# määritellään funktio aikuisen rasvaprosentin laskemiseen
def aikuisen_rasvaprosentti(bmi,ika,sukupuoli):
    """_summary_

    Args:
        bmi (float): painoindeksi
        ikä (float): henkilon ika
        sukupuoli (float): 1 -> mies, 0 -> nainen

    Returns:
        float: kehon rasvaprosentti (aikuinen)
    """
    rasvaprosentti = 1.20 * bmi + 0.23 * ika - 10.8 * sukupuoli - 5.4
    rasvaprosentti =round(rasvaprosentti, 1)
    return rasvaprosentti
    



# määritellään funktio lapsen rasvaprosentin laskemiseen.
def lapsen_rasvaprosentti(bmi,ika,sukupuoli):
    """_summary_

    Args:
        bmi (float): painoindeksi
        ika (float): ika
        sukupuoli (sukupuoli): 1 > poika, 0 > tyttö

        Returns:
            float: kehon rasvaprosentti (lapsi)
    """
    rasvaprosentti = 1.51 * bmi - 0.70 * ika -  3.6 * sukupuoli + 1.4
    rasvaprosentti = round(rasvaprosentti, 1)
    return rasvaprosentti

def usarasvaprosentti_mies(pituus, vatsan_ymparys, kaulan_ymparys):
    """laske miehen rasvaprosentin USA:n armeijan kaavalla

    Args:
        pituus (float): pituus (cm)
        vyotaron_ymparys (float): vyotaron ympärysmitta (cm)
        kaulan_ymparys (float): kaulan ympärysmitta (cm)

    Returns:
        float: rasvaprosentti
    """

    # Muutetaan mitat tuumiksi
    tuumaa_pituus = pituus / 2.54
    tuumaa_vyotaron_ymparys = vyotaron_ymparys / 2.54
    tuumaa_kaulan_ymparys = kaulan_ymparys / 2.54

    # Laskentaan rasvaprosentti

    usarprosentti = 86.010 * math.log10(tuumaa_vyotaron_ymparys - tuumaa_kaulan_ymparys) - 70.041 * math.log10(tuumaa_pituus) + 36.76
    return usarprosentti

def usarasvaprosentti_nainen(pituus,vyotaron_ymparys,kaulan_ymparys,lantion_ymparys):
    """Laske naisen rasvaprosentti USA:n armeijan kaavalla

    Args:
        pituus (float): pituus (cm)
        vyotaron_ymparys (float): vyotaron ympärysmitta (cm)
        kaulan_ymparys (float): kaulan ympärysmitta (cm)
        lantion_ymparys (float): lantion ymprärysmitta (cm)

    Returns:
        float : rasvaprosentti
    """
    
    # Muutetaan mitat tuumiksi
    tuumaa_pituus = pituus / 2.54
    tuumaa_vyotaron_ymparys = vyotaron_ymparys / 2.54
    tuumaa_kaulan_ymparys = kaulan_ymparys / 2.54
    tuumaa_lantion_ymparys = lantion_ymparys / 2.54

    # Lasketaan rasvaprosentti

    usarprosentti = 163.205 * math.log10(tuumaa_vyotaron_ymparys + tuumaa_kaulan_ymparys - tuumaa_lantion_ymparys) - 97.684 * math.log10(tuumaa_pituus) + 78.387
    return usarprosentti

if __name__ == "__main__":

    #Kysytään käyttäjältä
    pituus_teksti = input('Kuinka pitkä olet (cm): ')
    paino_teksti = input('Kuinka paljon painat (kg): ')
    ika_teksti = input('Kuinka vanha olet: ')
    sukupuoli_teksti = input('Sukupuoli mies, vastaa 1, nainen vastaa 0: ')
    vyotaron_ymparys_teksti = input('Mikä on vyörtärön ympäryseksi (cm): ')
    kaulan_ymparys_teksti = input('Mikä on kaulasi ympäryysmitta (cm): ')

    # Jos vastaus sukupuolikysymykseen on nolla, kysy lantion mitta
    if sukupuoli_teksti == '0':
        lantio_ymparys_teksti = input('Mikä on lantiosi ympärysmitta (cm)')

    #Muutetaan vastaukset liukuluvuiksi
    pituus = float(pituus_teksti) # Muutetaan liukuluvuksi
    paino = float(paino_teksti) # Muutetaan liukuluvuksi
    ika = float(ika_teksti)
    sukupuoli = float(sukupuoli_teksti)
    vyotaron_ymparys = float(vyotaron_ymparys_teksti)
    kaulan_ymparys = float(kaulan_ymparys_teksti)
    lantio_ymparys = float (lantio_ymparys_teksti)


    # Lasketaan painoindeksi funktiolla laske_bmi
    oma_bmi = laske_bmi (paino,pituus)

    # Yli 18 vuotilailla käytetään aikuisen kaavaa
    if ika >= 18:
        oma_rasvaprosentti = aikuisen_rasvaprosentti(oma_bmi, ika, sukupuoli)

    # Muussa tapauksessa käytetään lapsen kaavaa
    else:
        oma_rasvaprosentti = lapsen_rasvaprosentti(oma_bmi, ika, sukupuoli)

    print('painoindeksisi on', oma_bmi,
     'ja kehon rasvaprosentti on', oma_rasvaprosentti)
    
    if sukupuoli_teksti == '1':
        usa_rasvaprosentti = usarasvaprosentti_mies(pituus, vyotaron_ymparys, kaulan_ymparys)
    else:
        usa_rasvaprosentti = usarasvaprosentti_nainen(pituus, vyotaron_ymparys, lantio_ymparys, kaulan_ymparys)
    print('USA:n armeijan kaavalla rasvaprosenttisi on', usa_rasvaprosentti)