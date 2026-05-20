import probar
import time





def mainloop(selfs):
    counter=0
    filescopy=["app.py","mylib.py","thelib.py","samelib.py"]
    selfs.inserts(filescopy[counter],0)
    #counter=counter+1
    while 1:
        time.sleep(3)
        selfs.inserts(filescopy[counter],20)
        if counter>=len(filescopy)-1:
            #selfs.root.quit()
            selfs.inserts("ends",20)
            break
        counter=counter+1

theapps= probar.inits(mainloop,"my instaler","black","white","file intaler myinstaler")
