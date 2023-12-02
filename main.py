from hospital import team
from people import patient, doctor, nurse


def get_file_content(file_name):
    content_list = []
    file_content = open(f"txt_files/{file_name}", "rt")
    for line in file_content:
        line_list = line[:-1].split(" ")
        content_list += [line_list]

    file_content.close()
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


def group_nurses(nurse_list):
    group_size = 3
    size = len(nurse_list)

    if size <= group_size:
        return nurse_list

    quot, rem = divmod(size, 3)

    new_size = quot * group_size
    new_list = nurse_list[:new_size]

    if rem == 0:
        rem_list = []
    else:
        rem_list = nurse_list[-rem:]

    return new_list, rem_list


files = ("doctors.txt", "nurses.txt", "patients.txt")
doctor_list, nurse_list, patient_list = create_lists(files)

nurse_obj_list, remaining_nurses = group_nurses(nurse_list)
# loop thru nurse_obj_list and doctor list
# create a team obj consisting of 1 doctor and 3 nurses
# looper thru remaing_nurses list if length is not 0
# create team obj of 1 doctor and remaining nurses
# WHAT IF THERE ARE NO MORE DOCTORS BUT THERE ARE STILL NURSES?
