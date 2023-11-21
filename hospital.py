from copy import copy, deepcopy
import random


class special_number:
    def __init__(self) -> None:
        random.seed()
        self.value1 = random.randint(1, 500)
        self.value2 = random.randint(1, 500)

    def __str__(self) -> str:
        st = "Special value 1: %s  Special value 2: %s" % (self.value1, self.value2)
        return st

    def __del__(self):
        print("calling special_number destructor")


class doctor:
    """represents a doctor
    attributes: name, age, gender, id, specialty"""

    def __new__(cls, name, age, gender):
        print("creating new object")
        instance = super().__new__(cls)

        instance.secret = 888

        return instance

    doctor_count = 0

    def __init__(self, name, age, gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender

        doctor.doctor_count += 1
        self.id = doctor.doctor_count
        self.doctor_numbers = special_number()

    def __del__(self):
        print("calling doctor destructor")

    def __str__(self) -> str:
        my_str = "%s - %s - %s -  %s\nSpecial Numbers: %s" % (
            self.name,
            self.age,
            self.gender,
            self.id,
            self.doctor_numbers,
        )

        return my_str

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other) -> bool:
        return self.id != other.id

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __hash__(self) -> int:
        return hash(self.id)

    def __len__(self) -> int:
        return 5

    def __bool__(self) -> bool:
        if self.gender == "F":
            return True
        else:
            return False


class pediatrician(doctor):
    def __init__(self, name, age, gender) -> None:
        super().__init__(name, age, gender)

    def __del__(self):
        super().__del__()
        print("calling pediatrician destructor")


class idk:
    def __init__(self) -> None:
        self.num = 4

    def __str__(self) -> str:
        return "this is from str"
    
    def __repr__(self) -> str:
        return "this is from repr"

    def __bytes__(self) -> bytes:
        return b"This is bytes okay?"

    def __format__(self, __format_spec: str) -> str:
        return __format_spec.format(price=49)
    
   
t = idk()