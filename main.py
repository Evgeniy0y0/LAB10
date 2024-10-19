def createfile(filename):
    try:
        file = open(filename, "w")
        file.close()  
        print("File successfully created")
    except:
        print("Failed to create file")

def writefile(filename, text):
    try:
        file = open(filename, "w")
        file.write(text)
        file.close()
        print("File successfully written.")
    except:
        print("Failed to write to file")

# Прізвище та питання першого студента
text = "Sevati \nHow's your day going?"

try:
    createfile("Text.txt")
    writefile("Text.txt", text)

    try:
        file = open("Text.txt", "r")
        print("Text.txt: ")
        print(file.read())
        file.close()
    except:
        print("Failed to open file")
except:
    print("Failed to create file")


def append_to_file(filename, text):
    try:
        file = open(filename, "a")
        file.write(text)
        file.close()
        print("Text successfully appended.")
    except:
        print("Failed to append text to file")

def read_file(filename):
    try:
        file = open(filename, "r")
        content = file.read()
        file.close()
        print(f"{filename}: \n{content}")
    except:
        print("Failed to read the file")

surname_2 = "Lobanov"
answer = "My day is going well. How's yours?"

question_3 = "How do you reverse a string in Python?"
text_to_append = f"\n\n{surname_2}\n{answer}\n{question_3}"

append_to_file("Text.txt", text_to_append)

read_file("Text.txt")
