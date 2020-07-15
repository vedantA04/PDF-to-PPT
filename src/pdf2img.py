from pdf2image import convert_from_path
import os

n = input("What is the name of the file?")
def pdf2imgs(n):
    pages = convert_from_path("C:/Users/ANUP/Desktop/PDF-to-PPT/"+n+".pdf" , 500)
    outdir = 'Images'
    x = 1
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    for page in pages:
        page.save('{}/Picture{}.png'.format(outdir,x), 'PNG')
        x += 1


