from pathlib import Path
from shutil import copyfile
lagu = "/media/zani/bakarp/Music/"
liric = "/media/zani/utama/Lyrics/"
musicdirectory = Path(lagu)
liricdirectory = Path(liric)
totalsuccess =0
totalfail = 0
number =0
for amba in musicdirectory.glob('*.*'):
    
    if (amba.suffix == '.flac' or amba.suffix == '.mp3'):
        number += 1
        namalagu = amba.stem
        namaliric = '{}.lrc'.format(namalagu)
        pathliric = musicdirectory / namaliric
        if not (pathliric.exists()):
            counter = False
            for cariliric in liricdirectory.glob('*.lrc'):
                if cariliric.name == namaliric:
                    copyfile(cariliric, pathliric)
                    print("dapat: ", number)
                    totalsuccess +=1
                    counter =True
                    break
                
            if not (counter):
                print(namalagu)
                totalfail += 1   
        else:
            print("ada: ", number)
            totalsuccess += 1

print("success: ", totalsuccess)
print("fail: ", totalfail)
     