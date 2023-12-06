from people import doctor, patient, nurse


class team:
    """creates a medical team
    consists of 1 doctor and n nurses"""

    def __init__(self, __doctor: doctor, __my_nurses: nurse = None) -> None:
        self.my_doctor = __doctor
        self.nurse_team = __my_nurses
        if self.nurse_team == None:
            self.nurse_team = {}
        else:
            self.nurse_team = {}
            for n in __my_nurses:
                self.nurse_team[n.id] = n

    def __str__(self) -> str:
        s = []
        border = "{:->20}".format("")
        s += [f"DOCTOR: {self.my_doctor.full_name}", "NURSES:"]
        for n in self.nurse_team.values():
            s += [f"{n.full_name} ID: {n.id}"]

        s += [border]

        return "\n".join(s)

    def __getitem__(self, __key):
        try:
            return self.nurse_team[__key]
        except KeyError:
            return KeyError("Invalid key: nurse not found")
    
    def __len__(self):
        return len(self.nurse_team)
    
    def __iter__(self):
        #experiment with this method
        return iter(self.nurse_team.keys())

    def add_nurse(self, new_nurse):
        self.nurse_team[new_nurse.id] = new_nurse

    def pop_nurse(self, __nurse_id):
        try:
            return self.nurse_team.pop(__nurse_id)
        except KeyError:
            return "Nurse not found."

    def get_team_specialty(self):
        return self.my_doctor.specialty

    def get_nurse(self, __nurse_id):
        try:
            return self.nurse_team[__nurse_id]
        except KeyError:
            return "Nurse not found."

    def get_detailed_info(self):
        s = []
        border = "{:->20}".format("")
        s += ["DOCTOR:", str(self.my_doctor), border, "NURSE(s):"]
        for n in self.nurse_team:
            s += [str(self.nurse_team[n])]
        
        return "\n".join(s)
    
    class hospital:
        """represents a hospital"""

        pass
