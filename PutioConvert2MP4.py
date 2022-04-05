#   Libraries

import putiopy

############################# User Specific ###########################

# Root Folder
root = 999999999 # INSERT YOUR ROOT FOLDER

# Token
PutioToken = ' ' # INSERT YOUR TOKEN

############################# User Specific ###########################


# Convert Video Video Files to MP4

def PutioConvert2MP4():
    files = client.File.list(root) 
    for file in files:
        if file.file_type == "VIDEO":
            try:
                client.File.convert_to_mp4(file)
                print file.name + " conversion started." 
            except:
                print file.name + " conversion not needed."

client = putiopy.Client(PutioToken) # Instanciate Client Object

PutioConvert2MP4()



