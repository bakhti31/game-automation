import uiautomator2 as u2
d = u2.connect()

# Logs Edit
output = d.shell("dumpsys notification --noredact | grep android.title | cut -d= -f2").output
i=1
for x in output.split("\n"):
	notif = x.replace("String (","").replace(")","")
	if (notif == "Security Alert!"):
		d.app_start("vhack.os.reloaded", ".MainActivity")
		d(description="SECURITY").click()
		d(description="CLOSE CONNECTIONS").click()
		d(description="CLOSE CONNECTIONS").click()
		d.press('home')