from tkinter import *
import random
import turtle 

def main():
        a = "h"
        print(a)
        
        #piss
        loopnumber= int(input("please enter a number"))
        
        

        def windowmakerdev(funvalue, cumvalue):
                numbershit=1
                numberpiss =1
                funtotal=0
                loopnumber = 2
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
                if funvalue == 4:
                        if cumvalue == 69:
                                window = Tk()
                                window.title("cum")
                                window.configure(bg="floralwhite", width=500, height= 500)
                window.mainloop()

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
                if funvalue == 4:
                        cumvalue = random.randint(1,100)
                        if cumvalue == 69:
                                window = Tk()
                                window.title("cum")
                                window.configure(bg="ghostwhite", width=500, height= 500)
                window.mainloop()
                
                print("funvalue was", funvalue)
                print("funtotal was", funtotal)
                retry = input("do you want to try again? Y/N?")
                if retry.startswith('y'):
                        loopnumber= int(input("please enter a number"))
                        windowmaker(loopnumber)
                elif retry.startswith('ø'):
                        funvalue= 4
                        cumvalue = 69
                        windowmakerdev(funvalue, cumvalue)
                else:
                        input("Press Enter to continue...")
                
        windowmaker(loopnumber)        
main()
