from people import doctor, patient, nurse


class team:
    """creates a medical team
    consists of 1 doctor and n nurses"""

    def __init__(self, __doctor: doctor, __my_nurses: nurse = None) -> None:
        self.my_doctor = __doctor
        self.nurse_group = __my_nurses
        if self.nurse_group == None:
            self.nurse_group = []

    def __str__(self) -> str:
        s = []
        border = "{:->20}".format("")
        s += [border, f"Doctor: {self.my_doctor.full_name}", "Nurses"]
        for n in self.nurse_group:
            s += [self.nurse_group.full_name]

        s += [border]

        return "\n".join(s)


doc_file = open("txt_files/doctors.txt", "rt")

line = doc_file.readline()
line_list = line.split(" ")

print(line_list[:2])
print(" ".join(line_list[:2]))
print(line_list[2:])
# for line in doc_file:
#   print(line)
