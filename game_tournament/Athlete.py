
import random
class Athlete:
    """| Athelte class representing a player int hte tournament. |"""
    def __init__(self, name): 
        """Custom construcotr for Athlete class"""
        self.name = name
        self.number = random.randint(1, 99)
    def __str__(self):
        """String representation of the Athlete object"""
        return f"Athlete: name = {self.name}', number= {self.number}"
    def __repr__(self):
        """ Official string representation"""
        return f"Athlete(name ='{self.name}', number = {self.number})"
    def set_number(self, number):
        """ Set the athlete's number."""
        self.number = number

    def to_json(self):
        """"Generate jspn of athlete"""
        return {
            "name":self.name, 
            "number": self.number}

if __name__ == "__main__":
    #Example usaege
    athlete1 = Athlete("Lionel Messi")
    athlete1.set_number(10)
    #athlete1.number = 10  #mala practica
    print(athlete1) #Output Athlete: name = Lionel Messi', number= 10
    print(repr(athlete1)) #Output: Athlete(name ='Lionel Messi', number = 10)