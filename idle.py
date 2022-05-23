# coding: utf-8
#
import uiautomator2 as u2
import time
d = u2.connect()
while True:
	d.click(0.861, 0.964)
	time.sleep(1)
	now = datetime.now()

    sleep(1)    
    if (d.app_wait("vhack.os.reloaded", front=True)):
        if (d(description="RECONNECT").exists):
            d(description="RECONNECT").click() 