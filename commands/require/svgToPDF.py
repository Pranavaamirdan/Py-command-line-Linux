from svglib.svglib import svg2rlg
from reportlab.platypus import SimpleDocTemplate, Frame, PageTemplate
from reportlab.lib.pagesizes import letter, A3
from svgutils.compose import *
import os

fig = Figure("1120px", "630px",
       Panel(
              SVG("slide1.svg").scale(0.875),
             ).move(0, 0)
       )

os.remove("slide1.svg")
fig.save("slide1.svg")


def convert(path, svgname, name):
    drawing = svg2rlg(path)
    
    width = drawing.width
    height = drawing.height

    def landscape():
        fig = Figure("1120px", "630px",
            Panel(
                    SVG(svgname).scale(0.875),
                    ).move(0, 0)
            )
        os.remove(svgname)
        fig.save(svgname)
    
    def portrait():
        fig = Figure("620px", "877px",
            Panel(
                    SVG(svgname),
                    ).move(0, 0)
            )
        os.remove(svgname)
        fig.save(svgname)

    if width > height:
        size = (1280,720)
        landscape()
    elif width < height:
        size = (620,877)
        portrait()
        
    doc = SimpleDocTemplate(name,
        pagesize= size,
        rightMargin=0,leftMargin=0,
        topMargin=0,bottomMargin=0, showBoundary=True)

    story = []
    story.append(drawing)

    doc.build(story)

    os.remove(path)
