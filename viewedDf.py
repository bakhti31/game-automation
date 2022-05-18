# coding: utf-8
#
import uiautomator2 as u2
import time
d = u2.connect("NZV8TKIBMV5LOBPF")

d.xpath('//*[@content-desc="HOME"]').click()
d.click(0.182, 0.361)
d.xpath('//*[contains(@content-desc,"DEFACES")]').click_exists()

time.sleep(1)

while d.xpath('//*[contains(@content-desc,"VISITED\nNO")]').exists:
    d.xpath('//*[contains(@content-desc,"VISITED\nNO")]').long_click()
    d.xpath('//*[contains(@content-desc,"VISITED\nNO")]').click()
    time.sleep(0.5)
    d(className="android.widget.EditText").click()
    d(className="android.widget.EditText").set_text(d.clipboard)
    time.sleep(0.5)
    d(description="SCAN").click()
    time.sleep(0.5)
    d(description="EXPLOIT").click()
    if d(description="CONNECTION TO THIS TARGET ALREADY OPEN").wait(timeout=1.0) :
        # continue
        d.press('back')
        d.xpath('//*[@content-desc="HOME"]').click_exists()
        
    d(description="TERMINAL").click()
    time.sleep(1)
    d.xpath(f'//*[contains(@content-desc,"{d.clipboard}")]').click_exists()
    print(d.clipboard)
    d.xpath('//*[@content-desc="GET LOG FILE"]').click_exists()
    d.xpath(f'//*[contains(@content-desc,"{d.clipboard}")]').long_click()
    d.xpath('//*[@content-desc="HOME"]').click()
    d.click(0.182, 0.361)
    d.xpath('//*[contains(@content-desc,"DEFACES")]').click()
    time.sleep(0.5)
# d.xpath('//*[@content-desc="HOME"]').click()
# d(description="TERMINAL").click()
# d(descriptionContains="CLOSE ALL").click()