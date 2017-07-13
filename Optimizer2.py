import os, glob
from PIL import Image

basedir = os.getcwd()
extensions = ('.png')
os.system('cls')

print ("List of PNG files located in current directory:")
print ("")
for file in glob.glob("*.png"):
	print (file)
print ("")

#########################################################################################
# Checks to see of the directory "Optimized PNG Files" exists and create it if it doesn't
#########################################################################################
try:
    if not os.path.exists(os.path.join(basedir, "Optimized PNG Files")):
        os.makedirs("Optimized PNG Files")
        basedir = os.path.join(basedir, "Optimized PNG Files")
    else:
        basedir = os.path.join(basedir, "Optimized PNG Files")
except:
    print("Unknown Error")
#########################################################################################


print ("Current directory: " + basedir)
print("")
os.chdir("../")
for file in glob.glob("*.png"):
    for newfile in glob.glob("*.png"):
        if newfile[-14:] == "_Optimized.png":
            print (file + " " + "Already Exists")
            continue
        else:
            os.chdir("../")
            print ("Creating...")
            pass
os.chdir("../")
print ("Current directory3" + os.getcwd())
base, extension = os.path.splitext(file)
basedir = os.path.join(basedir, "Optimized PNG Files")
newans = os.path.join(basedir,  base + "_" + "Optimized" + extension)
foo = Image.open(file)
foo = foo.resize((3840,2160),Image.ANTIALIAS)
foo.save(newans,optimized=True)
print ("You are now in 3" + os.getcwd())

#os.system('cls')
print ("Optimization Complete!")
print ("")
print ("Your new file(s) are located: %s" % basedir)
print ("")
print ("")
print ("")
print ("")

