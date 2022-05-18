import uiautomator2 as u2
from time import sleep
d = u2.connect()

# output, exit_code = d.shell("dumpsys notification --noredact | grep android.title | cut -d= -f2", timeout=60)
# notifikasi = output.replace("String (","")
# notif = notifikasi.split(")\n")
# for x in notif:
#     print(x)
#     if (x == "Security Alert!"):
#         d.app_start("vhack.os.reloaded", ".MainActivity")
#         d(description="SECURITY").click()
#         d(description="CLOSE CONNECTIONS").double_click()



# d.swipe()

while True:
    if (d(description="FREE \n250").exists):
        d(description="FREE \n250").click()
        sleep(.5)

        d.press("home")
        sleep(1)
        d.app_stop("vhack.os.reloaded")
        sleep(1)

        d.app_start("vhack.os.reloaded", ".MainActivity")
