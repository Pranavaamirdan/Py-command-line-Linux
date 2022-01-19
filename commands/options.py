from msvcrt import getch
import os

option_text =["hello","peace","nice"] 

key_options = [72,80,13]# 77,75
recorded = [1]

def clearConsole():
        command = 'clear'
        if os.name in ('nt', 'dos'):
            command = 'cls'
        os.system(command)
clearConsole()

option = f"""
> {option_text[0]}
  {option_text[1]}
  {option_text[2]}
"""
print (option)

while True:
    char = ord(getch())
    size = len(recorded)
    last_record = recorded[size - 1]

    if char:
        clearConsole()
        if char == 27:
            break

        if char == key_options[0]:
            if last_record == 1:
                pass
            else:
                last_record = last_record - 1
            recorded.append(last_record)

        elif char == key_options[1]:
            if last_record == 3:
                pass
            else:
                last_record = last_record + 1
            recorded.append(last_record)
        
        elif char == key_options[2]:
            text = option_text[last_record - 1 ]
            print (f"you chose {text}")
            break

        if last_record == 1:
            option = f"""
> {option_text[0]}
  {option_text[1]}
  {option_text[2]}"""
            print(option)
            
        if last_record == 2:
            option = f"""
  {option_text[0]}
> {option_text[1]}
  {option_text[2]}"""
            print(option)

        if last_record == 3:
            option = f"""
  {option_text[0]}
  {option_text[1]}
> {option_text[2]}"""
            print(option)