# coding: utf-8
#
import uiautomator2 as u2
import time
d = u2.connect()


d(description="50\nBooyah").click()
a = 0
while True:
    text = "progress: " + str(a) + "X" 
    print ("\r" + text + "        ", end='')
    a = a + 1
    d(description="ATTACK\n9").click()   
    time.sleep(7)
    d(description="BACK").click()