from people import doctor, patient, nurse


class team:
    """creates a medical team
    consists of 1 doctor and n nurses"""

    def __init__(self, __doctor: doctor, __my_nurses: nurse = None) -> None:
        self.my_doctor = __doctor
        self.nurse_team = __my_nurses
        if self.nurse_team == None:
            self.nurse_team = []

    def __str__(self) -> str:
        s = []
        border = "{:->20}".format("")
        s += [border, f"Doctor: {self.my_doctor.full_name}", "Nurses"]
        for n in self.nurse_team:
            s += [n.full_name]

        s += [border]

        return "\n".join(s)
    
    def add_nurse(self, new_nurse):
        self.nurse_team += [new_nurse]

    def pop_nurse(self):
        pass
    
    def get_team_specialty(self):
        return self.my_doctor.specialty
    
    
    #add item retrieval method
    class hospital:
        '''represents a hospital'''
        pass