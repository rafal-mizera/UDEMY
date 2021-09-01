import os
path = r"C:\\temp\text.txt"


def WordCounter(path):
    with open(path) as file:
        word_counter = []
        for word in file.read().split(" "):
            word_counter.append(word)
    return len(word_counter)



# if os.path.isfile(path):
#     print(WordCounter(path))
# else:
#     print("Creating a file...")
#     with open(path,"w") as file:
#         file.write("Oto nowy napis w pliku text")
#     print(WordCounter(path))

result = os.path.isfile(path) or open(path,"x").close()
print(result)