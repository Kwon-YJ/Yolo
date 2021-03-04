# -*- coding: utf-8 -*- 
import pyautogui
import time


def screen_shot_1():
    pyautogui.click(x = 2195, y = 863, clicks=1)
    time.sleep(2)

def screen_shot_2():
    pyautogui.click(x = 2195, y = 770, clicks=1)
    time.sleep(2)

def press_key(key):
    pyautogui.write(key)
    time.sleep(2)

def savefile():
    pyautogui.click(x = 105, y = 276, clicks=1)
    pyautogui.click(x = 870, y = 705, clicks=1)

if __name__ == '__main__':
    for i in range(10):
        time.sleep(2)

        press_key('w') # 로드뷰 화면 전진

        if i == 0:
            screen_shot_1() # 스크린샷 버튼 클릭
        else:
            screen_shot_2() 
            
        press_key(str(i)) # 파일명 작성

        savefile() # 저장 경로 설정 및 저장


