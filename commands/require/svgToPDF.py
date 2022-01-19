from svglib.svglib import svg2rlg
from reportlab.platypus import SimpleDocTemplate, Frame, PageTemplate
from reportlab.lib.pagesizes import letter, A3
import os

# def scale(drawing, scaling_factor):
#     """
#     scale a reportlab.graphics.shapes.drawing()
#     object while maintaining the aspect ratio
#     """
#     scaling_x = scaling_factor
#     scaling_y = scaling_factor

#     drawing.width = drawing.minWidth() * scaling_x
#     drawing.height = drawing.height * scaling_y
#     drawing.scale(scaling_x, scaling_y)
#     return drawing

def convert(path,name):
    drawing = svg2rlg(path)
    # scaled_drawing = scale(name,scaling_factor = 1)
    

    width = drawing.width
    height = drawing.height
    # print(f'Height = {height}, Width = {width}')

    if width > height:
        size = (1280,720)#(910,700)
    elif width < height:
        size = (800,1056)
        
    doc = SimpleDocTemplate(name,
        pagesize= size,
        rightMargin=0,leftMargin=0,
        topMargin=0,bottomMargin=0, showBoundary=True)

    story = []
    story.append(drawing)

    # frameT = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='normal')

    # doc.addPageTemplates([PageTemplate(id='OneCol',frames=frameT)])

    doc.build(story)

    os.remove(path)