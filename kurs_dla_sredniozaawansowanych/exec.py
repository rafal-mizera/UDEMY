import os

files_to_process = [
    r"C:/Users/RMZ/PycharmProjects/UDEMY/kurs_dla_sredniozaawansowanych/exec_1.py",
    r"C:/Users/RMZ/PycharmProjects/UDEMY/kurs_dla_sredniozaawansowanych/exec_2.py"
]


for file in files_to_process:
    filename = print(f"Processing in progress... {os.path.basename(file)}")
    with open(file,"r") as f:
        source = f.read()
        exec(source)


