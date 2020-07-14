from pptx import Presentation
from pptx.util import Inches
import os
import natsort
from pdf2img import n

def imgs2powerpoint():
    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(8.5)
    blank_slide_layout = prs.slide_layouts[6]
    imagelist = os.listdir("Images/")
    for image in natsort.natsorted(imagelist):
        slide = prs.slides.add_slide(blank_slide_layout)
        left = top = 0
        slide.shapes.add_picture("Images/{}".format(image), left, top, height = prs.slide_height, width = prs.slide_width)
    prs.save("C:/Users/ANUP/Desktop/Maa_Sanskrit/Stories/"+n+"/Main Story.pptx")

