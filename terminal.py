# coding: utf-8
#
import uiautomator2 as u2

d = u2.connect()

def swipe():
    d.swipe(0,884,0,699,0.3)
    d.click(0.362, 0.83)

def deface():
	d(description="DEFACE").double_click()
	d(description="GET LOG FILE").click()

def bruteforce():
	d(description="BRUTEFORCE").click()

def swipetarget():
	d.click(0.498, 0.831)
	
while True:# bruteforce all target terminal
    swipe()
    swipetarget()
    bruteforce()


