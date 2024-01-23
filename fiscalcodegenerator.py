# -*- coding: iso-8859-15 -*-

# Implementare un algoritmo che calcoli il codice fiscale
# di una persona.

# Ma come si calcola il codice fiscale ?
# Beh, cerchiamo innanzitutto di capire come è composto,
# da quali elementi e successivamente come calcolarlo.

# E' un codice Alfanumerico (composto da lettere e numeri) di 16 caratteri.
# I primi 15 sono relativi ai dati personali (nome, cognome, sesso, data di nascita
# e luogo di nascita)
# mentre l'ultimo è un carattere di controllo che viene
# calcolato con delle formule applicate ai precedenti 15 caratteri.
#
# Prima indicazione => i dati da gestire sono:
#   nome, cognome, sesso, data di nascita, luogo di nascita

class DatiPersonali:

    def __init__(self, nome, cognome, genere='m', data_di_nascita='1/1/70', luogo_di_nascita=""):
        """
        Contesto di inizializzazione dei dati gestiti dalla classe.
        Si chiama "COSTRUTTORE".
        """
        self.nome = nome
        self.cognome = cognome
        self.sesso = genere
        self.data = data_di_nascita
        self.luogo = luogo_di_nascita

    def stampa(self):
        """
        Stampa le informazioni di una persona.
        """
        print(self.nome, self.cognome, self.sesso, self.data, self.luogo)


persona = DatiPersonali(nome="Paperon", cognome="De' Paperoni")
print(persona.nome)
print(persona.cognome)
print(persona.sesso)
print(persona.luogo)
print(persona.data)
persona = DatiPersonali(nome="giorgia", cognome="meloni", genere="f",
                        data_di_nascita="15/1/1977",
                        luogo_di_nascita="H501")
persona.stampa()

s = str(object="prova")
print(s.upper())
print(s.title())

# scriviamo l'algoritmo
# per calcolare il codice fiscale, in input dovremo avere i dati personali
# l'output sarà la stringa che rappresenta il codice fiscale corrispondente ai dati.


def calcola_cf(dati):
    """
    Calcola il codice fiscale appartenente alla persona i cui dati personali sono passati come input.
    """
    risultato = ""
    # E' un codice Alfanumerico (composto da lettere e numeri) di 16 caratteri.
    # I primi 15 sono relativi ai dati personali (nome, cognome, sesso, data di nascita e
    # luogo di nascita) mentre
    # l'ultimo è un carattere di controllo che viene calcolato con delle formule applicate
    # ai precedenti 15 caratteri.
    # è composto dai seguenti blocchi:
    # - 3 lettere per il cognome
    risultato += gestisci_cognome(dati.cognome)
    # - 3 lettere per il nome
    risultato += gestisci_nome(dati.nome)
    # - l'anno di nascita (numero)
    # - il mese della data di nascita (lettera)
    # - il giorno della data di nascita (numero)
    risultato += gestisci_anno(dati.data, dati.sesso)
    # - il codice del comune di nascita
    risultato += gestisci_comune(dati.luogo)
    # - il carattere di controllo
    risultato += calcola_codice_controllo(risultato)
    return risultato


def separa_consonanti(testo):
    """
    Dato il testo in input separa le consonanti dalle vocali
    """
    # metto il testo in maiuscolo
    testo = testo.upper()
    # mi creo una variabile per contenere tutte le consonanti
    consonanti = ""
    # mi creo una variabile per contenere tutte le vocali
    vocali = ""
    # percorro il testo lettera per lettera
    for lettera in testo:
        # se si tratta di una lettera dell'alfabeto
        # if lettera >= 'A' and lettera <= 'Z':
        if 'Z' >= lettera >= 'A':
            #   la aggiungo alle vocali se è una vocali
            # if lettera == 'A' or lettera == 'O' or lettera == 'I' or lettera == 'U' or lettera == 'E':
            if lettera in 'AOIUE':
                vocali += lettera
    #   altrimenti la aggiungo alle consonanti
            else:
                consonanti += lettera
    # restuisco le due variabili
    return consonanti, vocali


def gestisci_cognome(cognome):
    """
    Sono necessari 3 caratteri per rappresentare il cognome, 
    e sono la prima la seconda e la terza consonante del cognome.
    E' possibile che le consonanti siano meno di tre, 
    in questo caso è possibile aggiungere le vocali nell'ordine in cui compaiono nel cognome.
    Per cognomi più corti di 3 caratteri, 
    è possibile sostituire il carattere mancante con la lettera X.
    Chiaramente se ci sono cognomi con più parti, è necessario rimuovere gli spazi 
    e considerare tutto come un cognome unico.
    """
    # Cosa significa?
    # significa che dal cognome che mi arriva come input devo separare le
    # consonanti dalle vocali
    # ALTRO PROBLEMA => dato un testo separa le consonanti dalle vocali
    c, v = separa_consonanti(cognome)
    # come prendo le informazioni che mi servono?
    # prendo le consonanti ci aggiungo le vocali e ci aggiungo pure 3 X per sicurezza
    info = c + v + "XXX"
    # restituisco i primi 3 caratteri!
    return info[:3]


def gestisci_nome(nome):
    """
    Per il nome il discorso è analogo al cognome con la particolarità che se il nome è composto 
    da 4 o più consonanti vengono prese nell'ordine la prima, la terza e la quarta.
    Anche qui potremmo trovarci nella situazione di un numero di consonanti minore 
    di 3 e allo stesso modo si aggiungo le vocali.
    Ripetiamo anche qui che se il nome è più corto di 3 lettere 
    è possibile sostituire i caratteri mancanti con delle X.
    Se il nome fosse composto da più nomi, bisogna considerarlo tutto assieme.
    """
    c, v = separa_consonanti(nome)
    if len(c) > 3:  # se ci sono più di 3 consonanti
        c = c[0] + c[2:]  # prendo la prima e poi dalla 3^ in poi
    # prendo le consonanti ci aggiungo le vocali e ci aggiungo pure 3 X per sicurezza
    info = c + v + "XXX"
    # restituisco i primi 3 caratteri!
    return info[:3]


def gestisci_anno(datanascita, sesso):
    """
    Per l'anno vengono prese semplicemente le ultime due cifre.
    Per quanto riguarda il mese c'è una tabella di conversione.
    Per il giorno è sufficiente riportare il numero del giorno, 
    con il particolare che per le donne questo numero dev'essere aumentato di 40!
    """
    # supponendo che la data di nascita sia g/m/a
    parti = datanascita.split('/')
    anno = int(parti[2]) % 100  # modulo 100 per avere le ultime 2 cifre
    mese = int(parti[1])
    tabella_mesi = "ABCDEHLMPRST"
    lettera_mese = tabella_mesi[mese - 1]
    giorno = int(parti[0])
    if sesso == 'f':
        giorno += 40
    car_anno = str(anno)  # conversione in stringa dell'anno
    if len(car_anno) < 2:  # se ci sono meno di due caratteri
        car_anno = '0' + car_anno  # aggiungo uno zero all'inizio
    car_giorno = str(giorno)  # caratteri per il giorno
    if len(car_giorno) < 2:  # se ci sono meno di due caratteri
        car_giorno = '0' + car_giorno
    return car_anno + lettera_mese + car_giorno


def gestisci_comune(comune):
    return comune


def calcola_codice_controllo(codice_fiscale):
    return "X"


cf = calcola_cf(persona)
print("Il codice fiscale della persona è:", cf)

print(separa_consonanti("questo testo serve per prova"))