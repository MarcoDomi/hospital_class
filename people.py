class person:
    """represents a human"""

    def __init__(self, first_name, last_name, age) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self) -> str:
        s = f"Name: {self.first_name} {self.last_name}\nAge: {self.age}"
        return s

    def __lt__(self, other: object) -> bool:
        if self.last_name != other.last_name:
            return self.last_name < other.last_name
        else:
            return self.first_name < other.first_name

    def __gt__(self, other: object) -> bool:
        if self.last_name != other.last_name:
            return self.last_name > other.last_name
        else:
            return self.first_name > other.first_name
        
class doctor(person):
    '''represents a doctor'''
    def __init__(self, first_name, last_name, age, specialty) -> None:
        super().__init__(first_name, last_name, age)
        self.specialty = specialty

    def __str__(self) -> str:
        s = super().__str__()
        s += f"\nSpecialty: {self.specialty}"
        return s
    
class nurse(person):
    '''represents a nurse'''
    def __init__(self, first_name, last_name, age, type) -> None:
        super().__init__(first_name, last_name, age)
        self.type = type #registered or advanced

    def __str__(self) -> str:
        s = super().__str__()
        s += f"\nType: {self.type}"
        return s
    
class patient(person):
    '''represents a patient'''
    def __init__(self, first_name, last_name, age, height, weight, ailment) -> None:
        super().__init__(first_name, last_name, age)
        self.height = height
        self.weight = weight
        self.ailment = ailment

    def __str__(self) -> str:
        s = super().__str__()
        s += f"\nHeight: {self.height}\nWeight: {self.weight}\nAilment: {self.ailment}"
        return s
