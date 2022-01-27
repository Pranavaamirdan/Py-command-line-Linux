from fileinput import filename
import os
from require.Text import color, style
import require.svgToPDF as svg
from require.usePath import folder_array
import requests
from PyPDF2 import PdfFileMerger

writer = PdfFileMerger()

subject = input("Subject: ")
pptName = input("PPT Name: ")
path_name = input("Path: ")


folder = folder_array[f'{path_name}']

def command():
    """Requesting files from website"""

    folderName = subject + "-" + pptName

    try:
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

        pdfFileName = folderName + "/" + str(pg) + ".pdf"

        filePath = folderName + "/" + fileName

        url = baseUrl + str(pg)

        page = requests.get(url)
        

        if "404 Not Found" in page.text:
            break

        def svg_save():
            with open(filePath, "w+") as file:
                file.write(page.text)

        svg_save()

        os.chdir(folder)

        svg.convert(filePath, fileName, pdfFileName)


    def PDF_merge():
        fileList = os.listdir(folderName)
        fileList.sort(key=lambda f: int("".join(filter(str.isdigit, f))))

        folder = folder_array[f'{path_name}']
        saved_folder = folder + folderName
        os.chdir(saved_folder)    
        for file in fileList:
            if file.endswith('pdf'):
                writer.append(file)
                

        folder = folder_array[f'{path_name}']

        writer.write(folder + folderName + '/' + "file.pdf")
        writer.close()

        pdf = 0
        for file in fileList:
            pdf += 1
            os.chdir(saved_folder)
            os.remove(str(pdf) + ".pdf")

    PDF_merge()

    print(color['green'] + "PPT Successfully Downloaded as SVG Files; Can Be Found In The Folder " + color['end'] + style['bold'] + folderName + style['end'])

    os.system('cat file.pdf')

command()   