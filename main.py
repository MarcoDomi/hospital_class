from hospital import team
from people import patient, doctor, nurse


def get_file_content(file_name):
    content_list = []
    file_content = open(f"txt_files/{file_name}","rt")
    for line in file_content:
        line_list = line[:-1].split(" ")
        content_list += [line_list]
        
    return content_list


files = ("doctors.txt", "nurses.txt", "patients.txt")

line_1 = get_file_content(files[0])[0]
d = doctor(*line_1)
print(d)