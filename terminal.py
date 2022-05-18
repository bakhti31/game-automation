# coding: utf-8
#
import uiautomator2 as u2

d = u2.connect()

# d.swipe(0,996,0,699)
def next_target():
    d.swipe(0,884,0,699,0.2)
    d.click(0.362, 0.83)

