from datetime import datetime

konten = {}
aktiver_nutzer = None

def konto_erstellen(inhaber, passwort):
    global aktiver_nutzer
    if inhaber in konten:
        return -1  # Konto existert bereits
    konten[inhaber] = {
        "passwort": passwort,
        "kontostand": 0.0,
        "transaktionen": []
    }
    aktiver_nutzer = inhaber
    return 0


def transaktionen(nutzer, typ, betrag, **zusatzinfos):
    datum = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    transaktion = {
        "typ": typ,
        "betrag": betrag,
        "datum": datum
    }
    transaktion.update(zusatzinfos)
    konten[nutzer]["transaktionen"].append(transaktion)


def einzahlen(betrag):
    konten[aktiver_nutzer]["kontostand"] += betrag
    transaktionen(aktiver_nutzer, "Einzahlung", betrag)


def abheben(betrag):
    if konten[aktiver_nutzer]["kontostand"] < betrag:
        return -1  # nicht genügend Guthaben
    konten[aktiver_nutzer]["kontostand"] -=  betrag
    transaktionen(aktiver_nutzer, "Abhebung", betrag)
    return 0


def login(inhaber, passwort):
    global aktiver_nutzer
    if inhaber not in konten:
        return -1  # Konto existert nicht
    if konten[inhaber]["passwort"] != passwort:
        return -2  # Falsches Passwort
    aktiver_nutzer = inhaber    
    return 0
    

def logout():
    global aktiver_nutzer
    aktiver_nutzer = None


def ueberweisung(ziel_inhaber, betrag):
    if konten[aktiver_nutzer]["kontostand"] < betrag:
        return -1  # nicht genügend Guthaben
    if ziel_inhaber not in konten:
        konten[aktiver_nutzer]["kontostand"] -=  betrag
        transaktionen(aktiver_nutzer, "Abbuchung", betrag)
        return 0
    konten[aktiver_nutzer]["kontostand"] -= betrag
    konten[ziel_inhaber]["kontostand"] += betrag
    transaktionen(aktiver_nutzer, "Überweisung gesendet", betrag, ziel=ziel_inhaber)
    transaktionen(ziel_inhaber, "Überweisung empfangen", betrag, quelle=aktiver_nutzer)
    return 0


def get_kontostand():
    return konten[aktiver_nutzer]["kontostand"]


def get_kontoauszug():
    auszug = ""
    for transaktion in konten[aktiver_nutzer]["transaktionen"]:
        typ = transaktion["typ"]
        betrag = transaktion["betrag"]
        datum = transaktion["datum"]
        auszug += f"{datum} | {typ} | {betrag}\n"
    return auszug
