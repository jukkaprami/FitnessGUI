# OHJELMA, JOKA KYSYY BMI-TIETOJA USEASTA KUNTOILIJASTA
#----------------------------------------------------

# KIRJASTOT JA MODUULIT
# ---------------------

# Tuodaan fitness.py:n sisältämät toiminnot tähän ohjelmaan
import fitness

# Kysytään tiedot ja tulostetaan painoindeksi kunnes halutaan lopettaa
bmi_lista = []
nimilista = []
pituus_teksti = '0' # alustetaan muuttujan jonkin arvo
while pituus_teksti != '' :  # silmukka jossa ollaan kunnes annetaan tyhjä pituus
    
    nimi = input('nimi, tyhjä lopettaa: ')
    
    if nimi == '':
        break

    nimilista.append(nimi)
    pituus_teksti = input('Pituus (cm): ')
    paino_teksti = input('paino (kg): ')

    # Yritetään muuttaa syötetyt tekstit luvuiksi ja laskea bmi

    try: 
        pituus = float(pituus_teksti)
        paino = float(paino_teksti)

        # Lasketaan painoindeksi fitness-modulin laske_bmi funktiolla
        bmi = fitness.laske_bmi(paino, pituus)

        # Luodaan monikko (tuple), jossa nimi ja bmi
        monikko = (nimi, bmi)

        # Lisätään BMI listaan
        bmi_lista.append(monikko)

        # Näytetään tulokset ruudulla
        print('painoindeksi on', bmi)

     # Jos tapahtuu virhe, ilmoitetaan käyttäjälle
    except Exception as e:
        print('muunnos luvuksi ei onnistunut', e)

# Tulosta ruudulle lopuksi lista painoindekseistä
print('nimet ja painoindeksit olivat:', bmi_lista)
   
# Puretaan lista ja tulostetaan se rivi riviltä > monikko / rivi
for henkilo in bmi_lista:

    #Monikossa on kaksi tietoa, joiden indeksit ovat 0 (ensimmäinen) ja 1 (toinen)
    print(henkilo[0], ' painoindeksi on', henkilo[1])

# Listassa olevien monikoiden määrä
print('listassa oli', len(bmi_lista), 'merkintää')

# Harjoitus: tee bmi-listan perusteella kuntoilijoiden aakkostettu nimilista
nimilista.sort()
print(nimilista)

    