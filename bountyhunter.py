import uiautomator2 as u2
import xml.etree.ElementTree as ET
from uiautomator2 import UiObject
import time

d = u2.connect()

lol = []
left, top, right, bottom = 485, 1740, 595, 1850
havewinner = True

center_x = (left + right) // 2
center_y = (top + bottom) // 2
hierarchy = d.dump_hierarchy()
# analizar la cadena XML
root = ET.fromstring(hierarchy)

# encontrar la vista con los bounds y el índice específico
view_index = 11  # índice de la vista
view_bounds = "[806,144][842,177]"  # bounds de la vista como una cadena
view = None
for node in root.iter():
    if node.attrib.get('index') == str(view_index) and node.attrib.get('bounds') == view_bounds:
        view = node
        break
ui_object = d.xpath('//*[@index="{}"]'.format(view_index))



# obtener el texto de la vista
level = ui_object.info['contentDescription']
if ":" in level:
    print("There's no bounty running")
else:
	while havewinner:
		for x in d.xpath('//*[contains(@content-desc, "LEVEL ")]').all():
			info = x.info["contentDescription"].split("\n")
			ip = info[0]
			level1 = info[2]
			if level1 == level:
				print(f"found level {level}")
				x.click()
				time.sleep(0.25)
				continue
			else:
				
				continue
		
		# check if there are any items in the list
		time.sleep(.3)
		d.click(center_x, center_y)
		time.sleep(.2)



