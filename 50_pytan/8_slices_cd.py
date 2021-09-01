
a = "python_moj_kod.py"
b = "python_notatki.txt"

def stringControl(string):
    return string.startswith("python") and string.endswith(".py")
    # return string[0:6] == "python" and string[-3::] == ".py"

print(stringControl(b))
print(stringControl(a))