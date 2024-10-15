def createfile(filename):
  try:
    file = open(filename, "w")
    print("File successfully created")
  except:
    print("Failed to create file")
      
def writefile(filename, words):
  try:
    file = open(filename, "w")
    file.write(text)
    print("File successfully written.")
  except:
    print("Failed to write to file")

text = "Sevati \nHow`s your day going?"
try:
  createfile("Text.txt")
  print("File Text.txt successfully created.")
  writefile("Text.txt", text)
  try:
    file = open("Text.txt", "r")
    print("Text.txt: ")
    print(file.read())
  except:
     print("Failed to open file")
except:
  print("Failed to create file")
