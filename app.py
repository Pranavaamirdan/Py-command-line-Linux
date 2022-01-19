color = {
    "purple" : '\033[95m',
    "cyan" : '\033[96m',
    "darkcyan" : '\033[36m',
    "blue" : '\033[94m',
    "green" : '\033[92m',
    "yellow" : '\033[93m',
    "red" : '\033[91m',
    "end" : '\033[0m',
}

text_style = {
    "bold" : '\033[1m',
    "underline" : '\033[4m' ,
    "end" : '\033[0m'
}   

import os
import sys

print(color["green"] + "[⚹] " + color["end"] + color["purple"] + "Initiating..." + color["end"]) # ⌯ │ ⚹ ▸

line1 =  color['green'] + "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓"
line2 =  f"{color['green']}┃                                                                                            ┃"
line3 =  f"{color['green']}┃{color['purple']}        ╭——————————╮                                                                        {color['end']}{color['green']}┃"
line4 =  f"{color['green']}┃{color['purple']}        ●  ╭————╮  ●                                                                        {color['end']}{color['green']}┃"
line5 =  f"{color['green']}┃{color['purple']}        ●  │    │  ●                                                                        {color['end']}{color['green']}┃"
line6 =  f"{color['green']}┃{color['purple']}        ●  │    │  ●                                                                        {color['end']}{color['green']}┃"
line7 =  f"{color['green']}┃{color['purple']}        ●  ╰————╯  ●                                                                        {color['end']}{color['green']}┃"
line8 =  f"{color['green']}┃{color['purple']}        ●  ╭———————╯ ╭————————╮  ╭————————╮  ╭——╮      ╭——╮  ╭————————╮  ╭——╮   ╭——╮        {color['end']}{color['green']}┃"
line9 =  f"{color['green']}┃{color['purple']}        ●  ●         ╰╮  ╭——╮ │  ●  ╭——╮  ●   ●  ●    ●  ●   ●  ╭——╮  ●  ●  ●   ●  ●        {color['end']}{color['green']}┃"
line10 = f"{color['green']}┃{color['purple']}        ●  ●          ●  ●  ╰—╯  ●  │  │  ●    ●  ●  ●  ●    ●  │  │  ●  ●  ● ╲ ●  ●        {color['end']}{color['green']}┃"
line11 = f"{color['green']}┃{color['purple']}        ●  ●          ●  ●       ●  ╰——╯  ●     ●  ●●  ●     ●  ╰——╯  ●  ●  ●   ●  ●        {color['end']}{color['green']}┃"
line12 = f"{color['green']}┃{color['purple']}        ╰——╯          ╰——╯       ╰————————╯      ●————●      ╰————————╯  ╰——╯   ╰——╯        {color['end']}{color['green']}┃"
line13 = f"{color['green']}┃                                                                                            {color['end']}{color['green']}┃"
line14 = f"{color['green']}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{color['end']}"


def namePrint():
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)
    print(line6)
    print(line7)
    print(line8)
    print(line9)
    print(line10)
    print(line11)
    print(line12)
    print(line13)
    print(line14)

namePrint()

while True:
    command = input(color["green"] + "[>] " + color["end"] + color["purple"]).lower()
    
    if command == "exit": sys.exit()

    def clearConsole():
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)

    if command == 'clear': 
        clearConsole()
        namePrint()
        continue

    file = os.path.isfile(f'./commands/{command}.py')
    if file:
        print(color["green"] + "[⚹] " + color["end"] + color["purple"] + f"Running Command {command}..." + color["end"])
        os.system(f'python ./commands/{command}.py')
    else:
        red = color["red"] + f"There is no command called {command}" + color["end"]
        bold = "\n Use the " + text_style["bold"] + "help " + text_style["end"] + "command to know all the commands."
        print(red + bold)