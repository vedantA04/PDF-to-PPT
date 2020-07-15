from pdf2image import convert_from_path
import os

n = input("What is the name of the file?")
def pdf2imgs(n):
    pages = convert_from_path("C:/Users/Your_User_name/Desktop/PDF-to-PPT/"+n+".pdf" , 500) # This path is for Windows, 
    outdir = 'Images'                                                                       # assuming that the codes and the pdf file 
    x = 1                                                                                   # are located in /Desktop/PDF-to-PPT/
    if not os.path.exists(outdir):                                                          # Path for Linux, 
        os.makedirs(outdir)                                                                 # "/home/your_user_name(in small letters)/Desktop/PDF-to-PPT/"
    for page in pages:
        page.save('{}/Picture{}.png'.format(outdir,x), 'PNG')
        x += 1


