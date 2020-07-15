from pdf2image import convert_from_path
import os

path = input("What is the path of the file?")
def pdf2imgs(path):
    pages = convert_from_path(path , 500) 
    outdir = 'Images'                                                                     
    x = 1                                                                                   
    if not os.path.exists(outdir):                                                         
        os.makedirs(outdir)                                                                 
    for page in pages:
        page.save('{}/Picture{}.png'.format(outdir,x), 'PNG')
        x += 1


