from string import ascii_letters, digits
from time import sleep

import uiautomator2 as u2
d = u2.connect()

uid = "382702" #User ID Card
uname = "Test" #Username For Card
to = "vHack System" #Friends that we send the card

def bf(uid,p,uname):
    txt = '{"user_id":uid,"username":"uname","bankingpass":"passw"}' #json for bankcard
    # Replacing Field 
    a = txt.replace("uid", uid)
    b = a.replace("uname", uname)
    done = b.replace("passw", p)
    # Set into clipboard
    d.set_clipboard(done, 'label')
    # Clicking send Bankcard button
    d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[14]').click()

    # Testing Part
    # Search last Bankcard
    d(longClickable='true')[-1].click()
    # Wait Until its show fail or into bankcard
    sleep(0.4)
    if d(description="ACCOUNT BALANCE").exists:
        print("Its Pass")
    else:
        d(description="HOME").click() #Get back to home
        d(description="MESSENGER").click() #Get back to messager
        d.xpath(f'//*[contains(@content-desc,"{to}")]').click() #Click user that we sending test bankcard
    sleep(0.2)

c = list(ascii_letters+digits)
pwt = ['0'] * 6 #we tried to bf 6 digit pw

for dig1 in c:
    for dig2 in c:
        for dig3 in c:
            for dig4 in c:
                for dig5 in c:
                    for dig6 in c:
                        pwt[0]=dig1;
                        pwt[1]=dig2;
                        pwt[2]=dig3;
                        pwt[3]=dig4;
                        pwt[4]=dig5;
                        pwt[5]=dig6;
                        pwds = ''.join(pwt)
                        bf(uid,pwds,uname)