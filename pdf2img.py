from pdf2image import convert_from_path

n = input("What is the name of the file?")
def pdf2imgs(n):
    pages = convert_from_path("C:/Users/ANUP/Desktop/Maa_Sanskrit/Stories/"+n+"/"+n+".pdf" , 500)
    outdir = 'Images/'
    x = 1
    for page in pages:
        page.save('{}Picture{}.png'.format(outdir,x), 'PNG')
        x += 1


