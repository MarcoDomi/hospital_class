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
        
    def __getattr__(self, __name):
        if __name == "full_name":
            return f"{self.first_name} {self.last_name}"
        else:
            return AttributeError(f"'{__name}' is not an attribute")


class doctor(person):
    """represents a doctor"""

    def __init__(self, first_name, last_name, age, specialty) -> None:
        super().__init__(first_name, last_name, age)
        self.specialty = specialty

    def __str__(self) -> str:
        s = super().__str__()
        s += f"\nSpecialty: {self.specialty}"
        return s

    def __lt__(self, other: object) -> bool:
        return super().__lt__(other)

    def __gt__(self, other: object) -> bool:
        return super().__gt__(other)
    
    def __getattr__(self, __name):
        return super().__getattr__(__name)


class nurse(person):
    """represents a nurse"""
    nurse_num = 0
    def __init__(self, first_name, last_name, age, type) -> None:
        super().__init__(first_name, last_name, age)
        self.type = type  # registered or advanced

        nurse.nurse_num += 1
        self.id = nurse.nurse_num

    def __str__(self) -> str:
        s = super().__str__()
        s += f"\nType: {self.type}"
        return s

    def __lt__(self, other: object) -> bool:
        return super().__lt__(other)

    def __gt__(self, other: object) -> bool:
        return super().__gt__(other)
    
    def __getattr__(self, __name):
        return super().__getattr__(__name)
    
    def get_id(self):
        return self.id


class patient(person):
    """represents a patient"""

    def __init__(self, first_name, last_name, age, height, weight, ailment) -> None:
        super().__init__(first_name, last_name, age)
        self.height = height
        self.weight = weight
        self.ailment = ailment

    def __str__(self) -> str:
        s = super().__str__()
        s += f"\nHeight: {self.height}\nWeight: {self.weight}\nAilment: {self.ailment}"
        return s

    def __lt__(self, other: object) -> bool:
        return super().__lt__(other)

    def __gt__(self, other: object) -> bool:
        return super().__gt__(other)
    
    def __getattr__(self, __name):
        return super().__getattr__(__name)