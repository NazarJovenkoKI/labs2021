import requests
import re

url = "https://mail.univ.net.ua/readme.txt"

f=open('D:\\Jovenko Nazarij\\Lab 1\\Task 1\\PythonTask1\\readme.txt',"wb")
ufr = requests.get(url)
f.write(ufr.content)
f.close()

with open('D:\\Jovenko Nazarij\\Lab 1\\Task 1\\PythonTask1\\readme.txt') as file_in:
    text = file_in.read()
input_word = str(input("Word: "))

f=open('D:\\Jovenko Nazarij\\Lab 1\\Task 1\\PythonTask1\\ReadMe-LIGHT.txt',"w")
new_text = re.compile(re.escape(input_word), re.IGNORECASE)
f.write(new_text.sub('WORD FOUND!!!', text))
f.close()

print("Complete!")
