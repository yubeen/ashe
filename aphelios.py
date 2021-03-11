import pyautogui
import time

#pyautogui.screenshot('white.png',region =(1200, 800, 50,30)) #1200,800위치에 50*30크기로 캡쳐

a1= pyautogui.locateCenterOnScreen('white.PNG') 
pyautogui.moveTo(a1) #화면 캡쳐한 곳 가운데로 이동

pyautogui.click() #한번 클릭
time.sleep(1) #1초 대기

for i in range(2) :
    pyautogui.write('Hello!')
    pyautogui.write(['enter'])

    