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
            return "Invalid key: nurse not found"

    # this method will not be used but i am implementing it for learning purposes
    def __setitem__(self, __key, __value):
        self.nurse_team[__key] = __value

    # use del to delete a nurse from team
    def __delitem__(self, __key):
        print("calling __delitem__")
        try:
            return self.nurse_team.pop(__key)
        except KeyError:
            raise "Nurse not found."

    def __len__(self):
        return len(self.nurse_team)

    def __iter__(self):
        return iter(self.nurse_team)

    def add_nurse(self, new_nurse):
        self.nurse_team[new_nurse.id] = new_nurse

    # removes a nurse from team
    def pop_nurse(self, __nurse_id):
        try:
            return self.nurse_team.pop(__nurse_id)
        except KeyError:
            return "Nurse not found."

    def get_team_specialty(self):
        return self.my_doctor.specialty

    # uses a nurse id to return a specific nurse
    def get_nurse(self, __key):
        try:
            return self.nurse_team[__key]
        except KeyError:
            return "Nurse not found."

    # prints all nurses from team w/ more detail
    def get_detailed_info(self):
        s = []
        border = "{:->20}".format("")
        s += ["DOCTOR:", str(self.my_doctor), border, "NURSE(s):"]
        for n in self.nurse_team:
            s += [str(self.nurse_team[n])]

        return "\n".join(s)

class hospital:
    """represents a hospital"""
    def __init__(self) -> None:
        self.patient_list = []
        self.patients_unassigned = []
        self.team_list = [] 

    #TODO edit this method
    def create_team(self, __doctor, __nurses):
        self.team_list += [team(__doctor, __nurses)]
        
    # check patient in
    def patient_check_in(self, __new_patient):
        self.patient_list += [__new_patient]

    # check patient out
    def patient_check_out(self, __full_name):
        num_patients = len(self.patient_list)
        for i in num_patients:
            if self.patient_list[i].full_name == __full_name:
                return self.patient_list.pop(i)
        
        return -1

    # swap nurses between teams
    # list of nurses w/o team
    # print patient info
    # print team associated with patient
