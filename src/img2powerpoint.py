from pptx import Presentation
from pptx.util import Inches
import os
import natsort
from pdf2img import n
import image

def imgs2powerpoint():
    prs = Presentation()
    img = image.Image("Images/Picture1.png")
    width = img.getWidth()
    height = img.getHeight()
    prs.slide_width = Inches(width / 500)
    prs.slide_height = Inches(height / 500)
    blank_slide_layout = prs.slide_layouts[6]
    imagelist = os.listdir("Images/")
    for image in natsort.natsorted(imagelist):
        slide = prs.slides.add_slide(blank_slide_layout)
        left = top = 0
        slide.shapes.add_picture("Images/{}".format(image), left, top, height = prs.slide_height, width = prs.slide_width)
    prs.save("C:/Users/Your_User_Name/Desktop/PDF-to-PPT/"+n+".pptx")#Path for Windows 
             #Path for Linux, "/home/your_user_name(in small letters)/Desktop/PDF-to-PPT/"
