import requests
import os

def command():
    """Requesting files from website"""

    subject = input("Subject: ")
    pptName = input("PPT Name: ")
    path_name = input("Path: ")

    folderName = subject + "-" + pptName

    try:
        folder_array = {
            "computer": "C:/Users/prana/OneDrive/Desktop/Pranava Amirdan/Delhi Public School 9th Grade/Subject_Computer/",
            "english": "C:/Users/prana/OneDrive/Desktop/Pranava Amirdan/Delhi Public School 9th Grade/Subject_English/",
            "english-l": "C:/Users/prana/OneDrive/Desktop/Pranava Amirdan/Delhi Public School 9th Grade/Subject_English/Literature/",
            "english-g": "C:/Users/prana/OneDrive/Desktop/Pranava Amirdan/Delhi Public School 9th Grade/Subject_English/Grammar/",
            "math": "C:/Users/prana/OneDrive/Desktop/Pranava Amirdan/Delhi Public School 9th Grade/Subject_Maths/",
            "sanskrit": "C:/Users/prana/OneDrive/Desktop/Pranava Amirdan/Delhi Public School 9th Grade/Subject_Sanskrit/",
            "sanskrit-a": "C:/Users/prana/OneDrive/Desktop/Pranava Amirdan/Delhi Public School 9th Grade/Subject_Sanskrit/Activity/",
            "sanskrit-l": "C:/Users/prana/OneDrive/Desktop/Pranava Amirdan/Delhi Public School 9th Grade/Subject_Sanskrit/Literature/",
            "sanskrit-g": "C:/Users/prana/OneDrive/Desktop/Pranava Amirdan/Delhi Public School 9th Grade/Subject_Sanskrit/Grammar/",
            "science": "C:/Users/prana/OneDrive/Desktop/Pranava Amirdan/Delhi Public School 9th Grade/Subject_Science/",
            "science-b": "C:/Users/prana/OneDrive/Desktop/Pranava Amirdan/Delhi Public School 9th Grade/Subject_Science/Biology/",
            "science-c": "C:/Users/prana/OneDrive/Desktop/Pranava Amirdan/Delhi Public School 9th Grade/Subject_Science/Chemistry/",
            "science-p":"C:/Users/prana/OneDrive/Desktop/Pranava Amirdan/Delhi Public School 9th Grade/Subject_Science/Physics",
            "sst":"C:/Users/prana/OneDrive/Desktop/Pranava Amirdan/Delhi Public School 9th Grade/Subject_SST/",
            "sst-h": "C:/Users/prana/OneDrive/Desktop/Pranava Amirdan/Delhi Public School 9th Grade/Subject_SST/History/",
            "sst-c": "C:/Users/prana/OneDrive/Desktop/Pranava Amirdan/Delhi Public School 9th Grade/Subject_SST/Civics/",
            "sst-e": "C:/Users/prana/OneDrive/Desktop/Pranava Amirdan/Delhi Public School 9th Grade/Subject_SST/Economics/",
            "sst-g": "C:/Users/prana/OneDrive/Desktop/Pranava Amirdan/Delhi Public School 9th Grade/Subject_SST/Geography/",
            "test" : "C:/Users/prana/OneDrive/Desktop/Py-command-line/"
        }

        folder = folder_array[f'{path_name}']
        if folder: 
            os.chdir(folder)
            os.mkdir(folderName)
        else:
            os.mkdir(folderName)
    except Exception as e:
        print(e)

    baseUrl = input("Base URL: ")

    pg = 0

    while True:
        
        pg += 1
        
        fileName = "slide" + str(pg) + ".svg"

        filePath = folderName + "/" + fileName

        url = baseUrl + str(pg)

        page = requests.get(url)

        if "404 Not Found" in page.text:
            break

        with open(filePath, "w+") as file:
            file.write(page.text)

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
    
    print(color["green"] + "PPT Successfully Downloaded as SVG Files; Can Be Found In The Folder " + color["end"] + text_style["bold"] + folderName + text_style["end"])

command()