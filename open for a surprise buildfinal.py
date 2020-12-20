from tkinter import *
import random
import turtle 

def main():
        a = "h"
        print(a)
        
        #piss
        loopnumber= int(input("please enter a number"))
        
        
        def windowmaker(loopnumber):
                numberpiss = 0
                numbershit = 0
                funtotal = 0
                funvalue = random.randint(1, 4)
                loopnumber = loopnumber ** funvalue
                loophalf = loopnumber / 2
                while numberpiss < loophalf:
                    window = Tk()
                    window.title("piss")
                    window.configure(bg= 'yellow', width=500, height= 500)
                    numberpiss += 1
                    funtotal +=1
                while numbershit < loophalf:
                        window = Tk()
                        window.title("shid")
                        window.configure(bg='saddlebrown', width=500, height= 500)
                        numbershit +=1
                        funtotal +=1
                window.mainloop()
                print("funvalue was", funvalue)
                print("funtotal was", funtotal)
                input("Press Enter to continue...")
        windowmaker(loopnumber)        
main()
