# coding: utf-8
#
import uiautomator2 as u2
import time
d = u2.connect()
def openNetwork():
    d.xpath('//*[@content-desc="HOME"]').click()
    d.click(0.182, 0.361)
    d.xpath('//*[contains(@content-desc,"DEFACES")]').click_exists()

def exploit(ip):
	d(className="android.widget.EditText").click()
    d(className="android.widget.EditText").set_text(d.clipboard)
    time.sleep(0.5)
    d(description="SCAN").click()
    time.sleep(0.5)
    if d(description="EXPLOIT").wait(timeout=1.0):
    	d(description="EXPLOIT").click()
    	return False;
    else:
    	return True;
    

def visit(el):
	el.long_click()
	el.click()
	
    if exploit(d.clipboard):
        # continue
        d.press('back')
        d.xpath('//*[@content-desc="HOME"]').click_exists()
        
    d(description="TERMINAL").click()
    time.sleep(1)
    d.xpath(f'//*[contains(@content-desc,"{d.clipboard}")]').click_exists()
    print(d.clipboard)
    d.xpath('//*[@content-desc="GET LOG FILE"]').click_exists()
    d.xpath('//*[@content-desc="HOME"]').click()
    d.click(0.182, 0.361)
    d.xpath('//*[contains(@content-desc,"DEFACES")]').click()
    time.sleep(0.5)


while d.xpath('//*[contains(@content-desc,"VISITED\nNO")]').exists:
    visit(d.xpath('//*[contains(@content-desc,"VISITED\nNO")]'))
# d.set_fastinput_ime(False)