import time

class auto:
    speed = 0
    besitzer = "-"
    marke = "-"
    color = "-"

    def __init__(self, besitzer, marke, color):
        """Auto Konstruktor
        
        Args:
            marke (str): Automarke.
            color (str): Autofarbe.
        """
        self.besitzer = besitzer
        self.marke = marke
        self.color = color
    
    def __str__(self):
        """Ausgabe des Objekts.

        Returns:
            [str]: Verständlicher Satz.
        """
        return f"{self.besitzer}s {self.marke} hat die Farbe {self.color}."

    def accelerate(self, new_speed):
        speed_steps = new_speed/10
        print(f"{self.besitzer}s {self.marke} startet mit {self.speed} km/h.")
        for i in range(10):
            self.speed += speed_steps
            time.sleep(0.5)
            print(f"\n{self.besitzer} beschleunigt auf {int(self.speed)} km/h.")
        print(f"\n{self.besitzer}s {self.marke} fährt nun konstant {int(self.speed)} km/h.")


# Aufrufe
snapf_wagen = auto("Snäpf", "Honda", "Pink")
print(snapf_wagen)
snapf_wagen.accelerate(70)
