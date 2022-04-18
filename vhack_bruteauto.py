# python script on auto vhack card generating. the script has not been tested for bugs, not even launched once, caus no time bro ;-)
# importation of library used to generate the table containing all possible caracters
# in the card password (upper and lower letters and numbers)
from string import ascii_letters, digits
# import the progression bar
# from tqdm import tqdm
# import automator and connect to it
# uh there seems to be a problem on my omputer, even if uiautomator2 was installed with pip, it wont load like that, however it imports correclty once on the python console so just run the python console, "import uiautomator2" then "vhack_bruteforceauto.py"
import uiautomator2 as u2
auto = u2.connect()


#function that generates the password
def bruteforce():
    # makes the variable password usable in differents functions acrosss the script
    global password
    global user_card
    global temporary_password_tab
    global user_id
    # password is blank while not found
    password = ""
    # determines if the script is finished
    all_password_tested = 0
    password_length = 6
    temporary_password_tab = [0] * password_length
    lits_of_possible_password_characters = list(ascii_letters+digits)
    length_of_the_list = len(lits_of_possible_password_characters)
    # progression bar
    # bar = tqdm(unit=" passwords")
    #opens the file to save the progression
    # starts the bruteforce
    while all_password_tested != 1:
        # the tested password
        password_test =  ""
        # puts the password from a table into as string by taking each letter and adding them together
        for number in range (password_length):
            password_test = password_test+str(lits_of_possible_password_characters[temporary_password_tab[number]])
        # increases the number of tries
        temporary_password_tab[0] += 1
        if temporary_password_tab[0] == length_of_the_list:
            for number_2 in range (password_length):
                if temporary_password_tab[number_2] == length_of_the_list:
                    if number_2+1 > password_length-1:
                        print("All passwords tested successfully.")
                        # pauses the program until user interaction and ends it after
                        input()
                        all_password_tested = 1
                    else:
                        temporary_password_tab[number_2] = 0
                        temporary_password_tab[number_2+1] += 1
        # increases the progression bar by one
        # bar.update(1)
        # increase the number of tries
        tries +=1
        # replace the banking pass in the model user card by the tested password
        user_card["bakingpass"] = password_test
        # copy the card and paste it
        auto.set_clipboard(user_card, 'label')
        auto.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[14]').click()
        # every thousand tries, save the most recent 
        if tries % 100 == 0:
            # erase previous file
            d = open("progression_of_uid_"+str(user_id)+".txt", "w")
            # erase previous text variable
            text = ""
            # store the progresion in the text variable
            for k in range(6):
                text = str(text) +str(temporary_password_tab[k])
                # write the variable to the file
            d.write(text)


# opens the progression again if it existed previsouly
def checkFileExistance():
    global temporary_password_tab
    global user_id
    # tries to read the file
    try:
        #if it succeeds, open the progression
        with open("progression_of_uid_"+str(user_id)+".txt", 'r') as f:
            for i in range(6):
                f[0] = temporary_password_tab[0]
    # if no file found
    except:
        print("No progression file has been found! "
        "That's ok if you never oppened the software. "
        "Press enter to continue or CTRL + C to stop.")
        input()


# initalises all needed variables
def init(): 
    # makes user_card variable usable in different functions
    global user_card
    global user_id
    # ask for user id
    user_id = str(input("Enter user ID: "))
    # user_card is defined for the rest of the script, we will just modify the bankingpass later on
    user_card = {"user_id":user_id,"username":"Thenamedoesntmatteranyways","bankingpass":""}
    checkFileExistance()
    bruteforce()