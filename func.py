from test import test

# Funktion f soll a und b addieren.
# Bedingung: Wenn Wert negativ, nutze stattdessen seinen positiven Wert.
# Beispiel: -7 + 62 = 69
def f(a, b):
    # TODO: Schreibe hier deinen Code
    pass


# Tests zur Prüfung (NICHT ändern)
test(1, f(27,42), 69)
test(2, f(-69,0), 69)
test(3, f(-4,-65), 69)
test(4, f(68, -1), 69)
test(5, f(-13, -56), 69)
test(6, f(-69, 69), 138)
test(7, f(-7, 62))
