# Snapfs Realm

# TODO: Datenstruktur für Konten

# TODO: Funktion zum Einzahlen

# TODO: Funktion zum Abheben

# TODO: Getter-Funktion für Kontostand


import sqlite3

class Konto:
    def __init__(self, konto_nummer, konto_halter, guthaben=0.0, passwort="", ober_konto=None):
        """
        Erstellung eines Kontos mit Kontonummer, Inhaber und Guthaben
        wenn benötigt kann auch ein Unterkonto erstellt werden.
        """
        self.Konto_nummer = konto_nummer
        self.Konto_halter = konto_halter
        self.Guthaben = guthaben
        self.Passwort = passwort
        self.Ober_konto = ober_konto

class BankDatenbank:
    def __init__(self, db_name="bank.db"):
        """
        Baut eine Verbindung zur Datenbank auf.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON")
        self.create.tables()
        self.logged_in_account = None # Speichert das aktuelle eingeloggte Konto

        def create_tables(self):
            """
            Erstellt Tabellen für Konten, falls diese noch nicht existieren.
            Ober_konto erlaubt es, eine Beziehung zwischen Ober- und Unterkonto herzustellen
            """
            self.cursor.execute(
                CREATE TABLE IF NOT EXISTS konto (
                    konto_nummer TEXT PRIMARY KEY,
                    konto_halter TEXT NOT NULL,
                    guthaben REAL NOT NULL,
                    ober_konto TEXT,
                    FOREIGN KEY (ober_konto) REFERENCES konto (konto_nummer)
                )
            )
            self.conn.commit()

            def add_konto(self, konto):
                """
                Fügt ein neues Konto in die Datenbank hinzu.
                Wenn angeben wird das ein Oberkonto existiert, wird dies überprüft (dessen Existens)
                """
                if konto.ober_konto is not None:
                    #Überprüft ob das Oberkonto existiert
                    try:
                        self.get_konto(konto.ober_konto)
                    except ValueError:
                        raise ValueError("Das angegebene Oberkonto existiert nicht.")
                    
                try:
                    self.cursor.execute(
                        "INSERT INTO Kontos (konto_nummer, konto_halter, guthaben, ober_konto) VALUE(?, ?, ?, ?)"
                        (konto.konto_nummer, konto.konto_halter, konto.guthaben, konto.ober_konto)
                    )
                    self.conn.commit()
                    print(f"Konto {konto.konto_nummer} erfolgreich hinzugefügt.")
                except sqlite3.IntgerityError:
                    raise ValueError("Ein Konto mit dieser Nummer existiert bereits.")
                
            def get_konto(self, konto_nummer):
                """
                Das Konto wird anhang der Nummer ausgelesen.
                """
                self.cursor.execute(
                    "SELECT konto_nummer, konto_halter, guthaben, ober_konto FROM kontos WHERE konto_nummer = ?"
                    (konto_nummer,)
                )
                result = self.cursor.fetchone()
                if result:
                    return Konto(*result)
                else:
                    raise ValueError("Das Konto existiert nicht.")
                
            def update_konto(self, konto):
                """
                Aktualisiert die Daten eines Kontos in der Datenbank.
                """
                self.cursor.execute(
                    "UPDATE kontos SET konto_halter = ?, guthaben = ?, ober_konto = ? WHERE konto_nummer = ?",
                    (konto.konto_nummer, konto.konto_halter, konto.guthaben, konto.ober_konto)
                )
                self.conn.commit()

            def get_subkontos(self, ober_konto_nummer):
                """
                Gibt an welche Unterkontos zu diesem Oberkonto gehören.
                """
                self.cursor.execute(
                    "SELECT konto_nummer, konto_halter, ober_konto, FROM kontos WHERE ober_konto = ?"
                    (ober_konto_nummer,)
                )
                rows = self.cursor.fetchall()
                return [Konto(*row) for row in rows]
            
            def deposit(self, konto_nummer, betrag):
                """
                Führt eine Einzahlung auf das angegebene Konto durch.
                """
                konto = self.get_konto(konto_nummer)
                if betrag <= 0:
                    raise ValueError("Der Einzahlungsbetrag muss ein positiver Wert sein.")
                konto.guthaben += betrag
                self.update_konto(konto)
                print(f"{betrag} wurden eingezahlt. Neuer Kontostand: {konto.guthaben}")

            def abheben(self, konto_nummer, betrag):
                """
                Führt eine Abbuchung vom angegebenen Konto durch.
                """
                konto = self.get_konto(konto_nummer)
                if betrag <= 0:
                    raise ValueError("Der abzubuchender Betrag muss ein positiver Wert sein.")
                if betrag > konto.guthaben:
                    raise ValueError("Der abzubuchende Betrag ist höher als der Kontostand")
                konto.guthaben -= betrag
                self.update_konto(konto)
                print(f"{betrag} wurden abgehoben. Neuer Kontostand: {konto.guthaben}")

            def transfer(self, von_konto_nummer, zu_konto_nummer, betrag):
                """
                Führt eine Überweisung durch vom Quellenkonto zum Zielkonto.
                """
                if betrag = <= 0:
                    raise ValueError("Der Überweisungsbetrag muss positiv sein.")
                von_konto = self.get_konto(von_konto_nummer)
                zu_konto = self.get_konto(zu_konto_nummer)
                if betrag > von_konto.guthaben:
                    raise ValueError("Kontostand ist zu gering für die ausstehende Überweisung.")
                
                try:
                    self.conn.execute("BEGIN")
                    von_konto.betrag -= betrag
                    zu_konto.betrag += betrag
                    self.cursor.execute(
                        "UPDATE kontos SET guthaben = ? WHERE konto_nummer = ?",
                        (von_konto.guthaben , zu_konto_nummer)
                    )
                    self.cursor.execute(
                        "UPDATE kontos SET guthaben = ? WHERE konto_nummer = ?",
                        (zu_konto.guthaben, von_konto_nummer)
                    )
                    self.conn.commit()
                    print(f"Überweisung über {betrag} von Konto {von_konto_nummer} zu Konto {zu_konto_nummer} war erfolgreich.")
                except sqlite3.Error as e:
                    self.conn.rollback()
                    raise e
                
            def login(self, konto_halter, passwort):
                """
                Benutzer wird angemeldet, indem das Konto anhand des Kontoinhabers und Passworts gesucht wird.
                Bei erfolgreichem Login wird das Konto als {logged_in_konto} gespreichert.
                """
                self.cursor.execute(
                    "SELECT konto_nummer, konto_halter, guthaben, passwort, ober_konto, FROM kontos WHERE konto_halter = ? AND passwort = ?"
                    (konto_halter, passwort)
                )
                result = self.cursor.fetchone()
                if result:
                    self.logged_in_konto = Konto(*result)
                    print(f"Login erfolgreich für {konto_halter}.")
                    return self.logged_in_konto
                else:
                    raise ValueError("Login fehlgeschlagen: Kontohalter oder Passwort falsch.")
                
            def logout(self):
                """
                Meldet den angemeldeten Benutzer ab.
                """
                if self.logged_in_konto:
                    print("Sie sind abgemeldet. Auf wiedersehen.")
                    self.logged_in_konto = None
                else:
                    print("Kein Benutzer angemeldet.")
