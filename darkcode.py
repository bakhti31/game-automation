# coding: utf-8
#
import uiautomator2 as u2
from string import ascii_uppercase, digits
d = u2.connect()	

c = list(ascii_uppercase+digits)
pwt = ['A'] * 12

for dig1 in c:
    for dig2 in c:
        for dig3 in c:
            for dig4 in c:
                for dig5 in c:
                    for dig6 in c:
                        for dig7 in c:
                            for dig8 in c:
                                for dig9 in c:
                                    for dig10 in c:
                                        for dig11 in c:
                                            for dig11 in c:
                                                for dig12 in c:
                                                    pwt[0]=dig1
                                                    pwt[1]=dig2
                                                    pwt[2]=dig3
                                                    pwt[3]=dig4
                                                    pwt[4]=dig5
                                                    pwt[5]=dig6
                                                    pwt[6]=dig7
                                                    pwt[7]=dig8
                                                    pwt[8]=dig9
                                                    pwt[9]=dig10
                                                    pwt[10]=dig11
                                                    pwt[11]=dig12
                                                    code = "".join(pwt)
                                                    d(className="android.widget.EditText").set_text(code);
                                                    d.click(0.887, 0.183)
                                                    # d(description="SEND").click()
                                                    # sleep(.5)