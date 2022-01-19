import os
import time
from require.Text import color

message = input("whats the commit message: ")

def save():
    # print(color["green"] + "✔️ Adding remote origin" + color["end"])
    # time.sleep(0.5)
    # os.system('git remote add origin git@github.com:Pranavaamirdan/Py-command-line.git')
    # time.sleep(3)
    

    text = "│ " + color["green"] + "✔️ Adding files to GitHub" + color["end"]
    length = 80 - len(text)
    rtext = text +  " "*length + "│"
    print("╭" + "—"*70 + "╮")
    print(rtext)
    print("╰" + "—"*70 + "╯")
    time.sleep(0.5)
    os.system('git add *')
    time.sleep(3)

    text = "│ " + color["green"] + "✔️ Committing files to GitHub" + color["end"]
    length = 80 - len(text)
    rtext = text +  " "*length + "│"
    print("╭" + "—"*70 + "╮")
    print(rtext)
    print("╰" + "—"*70 + "╯")
    time.sleep(0.5)
    os.system(f"git commit -m '{message}'")
    time.sleep(3)


    text = "│ " + color["green"] + "✔️ Pushing files to GitHub" + color["end"]
    length = 80 - len(text)
    rtext = text +  " "*length + "│"
    print("╭" + "—"*70 + "╮")
    print(rtext)
    print("╰" + "—"*70 + "╯")
    time.sleep(0.5)
    os.system('git push -u origin master')


save()