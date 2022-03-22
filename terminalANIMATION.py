import time
import os

framerate = float(input("Velocidade: "))

frame1 = 'Loading'
frame2 = 'Loading.'
frame3 = 'Loading..'
frame4 = 'Loading...'
frame5 = 'Loading....'


def animacao(loops):
    for i in range(loops):
        print(frame1)
        time.sleep(framerate)
        os.system("cls")
        print(frame2)
        time.sleep(framerate)
        os.system("cls")
        print(frame3)
        time.sleep(framerate)
        os.system("cls")
        print(frame4)
        time.sleep(framerate)
        os.system("cls")
        print(frame5)
        time.sleep(framerate)
        os.system("cls")
    
    print("---Loading Complete---")
    time.sleep(1)
    os.system("cls")







        
