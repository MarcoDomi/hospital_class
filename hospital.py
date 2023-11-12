from copy import copy, deepcopy


class doctor:
    """represents a doctor
    attributes: name, age, gender, id, specialty"""

    doctor_count = 0

    def __init__(self, name, age, gender, sp) -> None:
        self.name = name
        self.age = age
        self.gender = gender
        self.specialty = sp

        doctor.doctor_count += 1
        self.id = doctor.doctor_count


    def __str__(self) -> str:
        my_str = "%s - %s - %s - %s - %s" % (
            self.name,
            self.age,
            self.gender,
            self.specialty,
            self.id
        )

        return my_str

    def __eq__(self, other):
        return self.specialty == other.specialty

    def __ne__(self, other) -> bool:
        return self.specialty != other.specialty

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age
    
    def __hash__(self) -> int:
        return hash(self.id)


d = doctor("max", 32, "M", "gastro")
d2 = doctor("sam", 35, "F", "urol")
d3 = doctor("sam", 35, "F", "urol")

print(hash(d3))