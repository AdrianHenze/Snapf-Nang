def test(test_id, result, expected):
    """Testet Funktionen.
    
    Args:
        test_id: Bezeichnung des Tests.
        result: Rückgabewert der zu testenden Funktion.
        expected: Erwarteter Wert der zu testenden Funktion.
    """
    try:
        assert result == expected, f"{result} sollte {expected} sein."
        print(f"• Test {test_id} bestanden.")
    except AssertionError as e:
        print(f"• Test {test_id} fehlgeschlagen: {e}")
