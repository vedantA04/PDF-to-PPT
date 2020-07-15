from pdf2img import pdf2imgs, path
from img2powerpoint import imgs2powerpoint
from rmfile import rmfiles

outpath = input("What is the path of your presentation?")
pdf2imgs(path)
imgs2powerpoint(outpath)
rmfiles()
