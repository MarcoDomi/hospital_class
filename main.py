from hospital import team
from people import patient, doctor, nurse


def get_file_content(file_name):
    content_list = []
    file_content = open(f"txt_files/{file_name}","rt")
    for line in file_content:
        line_list = line.split(" ")
        full_name = " ".join(line_list[:2])
        line_list = [full_name] + line_list[2:]
        content_list += [line_list]

    return content_list

    

doc_file = open("txt_files/doctors.txt", "rt")
line = doc_file.readline()
line_list = line.split(" ")

#print(line_list[:2])
#full_name = " ".join(line_list[:2])
#print([full_name] + line_list[2:])
#for line in doc_file:
#  print(line)

files = ("doctors.txt", "nurses.txt", "patients.txt")

line_1 = get_file_content(files[0])[0]
print(line_1)
d = doctor(*line_1)