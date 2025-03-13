from datetime import datetime
import json
import os


aktiver_nutzer = None
DATABASE_FILENAME = "data/balance.json"

def load_database():
    if os.path.exists(DATABASE_FILENAME):
        with open(DATABASE_FILENAME, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}


def save_database(data):
    with open(DATABASE_FILENAME,"w") as file:
        json.dump(data, file, indent=4)


konten = load_database()


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
    konten[nutzer]["transaktionen"].insert(0,transaktion)


def einzahlen(betrag):
    konten[aktiver_nutzer]["kontostand"] += betrag
    transaktionen(aktiver_nutzer, "Einzahlung", betrag)
    save_database(konten)


def abheben(betrag):
    if konten[aktiver_nutzer]["kontostand"] < betrag:
        return -1  # nicht genügend Guthaben
    konten[aktiver_nutzer]["kontostand"] -=  betrag
    transaktionen(aktiver_nutzer, "Abhebung", betrag)
    save_database(konten)
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


def ueberweisung(ziel_inhaber, betrag, ref):
    if konten[aktiver_nutzer]["kontostand"] < betrag:
        return -1  # nicht genügend Guthaben
    if ziel_inhaber not in konten:
        konten[aktiver_nutzer]["kontostand"] -=  betrag
        transaktionen(aktiver_nutzer, "Abbuchung", betrag)
        return 0
    konten[aktiver_nutzer]["kontostand"] -= betrag
    konten[ziel_inhaber]["kontostand"] += betrag
    transaktionen(aktiver_nutzer, "Überweisung gesendet", betrag, ziel=ziel_inhaber, ref=ref)
    transaktionen(ziel_inhaber, "Überweisung empfangen", betrag, quelle=aktiver_nutzer, ref=ref)
    save_database(konten)
    return 0


def get_kontostand():
    return konten[aktiver_nutzer]["kontostand"]


def get_kontoauszug():
    auszug = ""
    for transaktion in konten[aktiver_nutzer]["transaktionen"]:
        typ = transaktion["typ"]
        datum = transaktion["datum"]
        formatted_betrag = f"{transaktion['betrag']:.2f}".replace('.', ',')
        auszug += f"{datum} | {typ} | {formatted_betrag} €\n"
    return auszug
