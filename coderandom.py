import random
import string
import uiautomator2 as u2
d = u2.connect()

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_uppercase+string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    # print("Random string of length", length, "is:", result_str)
    return result_str

while True:
    code = get_random_string(12)
    d(className="android.widget.EditText").set_text(code);
    d.click(0.887, 0.183)