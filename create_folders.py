import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory ' + directory)

for i in range(14):
    createFolder('./Iphone/' + '/10' + str(i))
    i+1
#written to write folders for byui semester classes
#works like a charm, just change what you want the titles to be in the for loop
