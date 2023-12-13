from hospital import team, hospital
from people import patient, doctor, nurse


def get_file_content(file_name):
    content_list = []
    file = open(f"txt_files/{file_name}", "rt")
    file_content = file.readlines()
    file.close()
    
    for line in file_content[:-1]:
        line_list = line[:-1].split(" ")
        content_list += [line_list]
   
    last_line = file_content[-1:][0].split(" ")
    content_list += [last_line]

    return content_list


def create_lists(file_names):
    doctor_list = []
    nurse_list = []
    patient_list = []

    for f in file_names:
        content_list = get_file_content(f)
        match f:
            case "doctors.txt":
                for c in content_list:
                    doctor_list += [doctor(*c)]
            case "nurses.txt":
                for c in content_list:
                    nurse_list += [nurse(*c)]
            case "patients.txt":
                for c in content_list:
                    patient_list += [patient(*c)]

    return doctor_list, nurse_list, patient_list


# put nurses in groups of 3 and any remaining nurses in a separate list
def group_nurses(nurse_list):
    GROUP_SIZE = 3

    size = len(nurse_list)

    if size <= GROUP_SIZE:
        return nurse_list

    num_of_groups, rem = divmod(size, GROUP_SIZE)

    new_size = num_of_groups * GROUP_SIZE
    new_list = nurse_list[:new_size]

    grouped_list = []

    for _ in range(num_of_groups):
        grouped_list += [new_list[:GROUP_SIZE]]

    if rem == 0:
        rem_list = []
    else:
        rem_list = nurse_list[-rem:]

    return grouped_list, rem_list


if __name__ == "__main__":
    files = ("doctors.txt", "nurses.txt", "patients.txt")
    doctor_list, nurse_list, patient_list = create_lists(files)

    nurse_group_list, remaining_nurses = group_nurses(nurse_list)

    h1 = hospital()
    h1.create_teams(doctor_list, nurse_group_list, remaining_nurses)
    h1.read_patient_list(patient_list)
    h1.pair()

    
    for i in h1.team_list:
        print(i)
   
# loop thru nurse_obj_list and doctor list
# create a team obj consisting of 1 doctor and 3 nurses
# loop thru remaing_nurses list if length is not 0
# create team obj of 1 doctor and remaining nurses
# WHAT IF THERE ARE NO MORE DOCTORS BUT THERE ARE STILL NURSES?
