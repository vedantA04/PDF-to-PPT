import os 
import natsort

def rmfiles():
    imagelist = os.listdir("Images/")
    for image in natsort.natsorted(imagelist):
        os.remove("Images/"+image)

