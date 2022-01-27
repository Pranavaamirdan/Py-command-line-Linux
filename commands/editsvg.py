from svgutils.compose import *

os.chdir("./h-h")
print(os.getcwd())

fig = Figure("620px", "877px",# "4960px", "7016px"
            Panel(
                    SVG("slide3.svg"),
                    ).move(0, 0)
            )


os.remove("slide3.svg")
fig.save("slide3.svg")