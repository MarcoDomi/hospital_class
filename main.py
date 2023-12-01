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


def create_obj(file_names):
    for f in file_names:
        content_list = get_file_content(f)
        doctor_list = []
        nurse_list = []
        patient_list = []

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


files = ("doctors.txt", "nurses.txt", "patients.txt")
doctor_list, nurse_list, patient_list = create_obj(files)
print(doctor_list, nurse_list, patient_list)
