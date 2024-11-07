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
# Функція для додавання тексту в файл
def append_to_file(filename, text):
    try:
        file = open(filename, "a")
        file.write(text)
        file.close()
        print("Text successfully appended.")
    except:
        print("Failed to append text to file")

# Функція для читання файлу
def read_file(filename):
    try:
        file = open(filename, "r")
        content = file.read()
        file.close()
        print(f"{filename}: \n{content}")
    except:
        print("Failed to read the file")

# Відповідь на питання про реверс рядка
answer_3 = """
To reverse a string in Python, you can use slicing. 
For example, if you have a string `s`, you can reverse it using `s[::-1]`.
This slices the string from the end to the beginning, effectively reversing it.
Here is an example:

s = "hello"
reversed_s = s[::-1]
print(reversed_s)  # Output: "olleh"
"""

# Питання для наступного студента
question_4 = "How do you find the maximum value in a list in Python?"

# Текст, який буде додано до файлу
text_to_append = f"\n\nKostyk\n{answer_3}\n{question_4}"

# Додаємо текст у файл
append_to_file("Text.txt", text_to_append)

# Читаємо вміст файлу
read_file("Text.txt")
