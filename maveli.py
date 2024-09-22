def myself():
    print("Hey!! Nom aan MAVELI 2.0 Chat bot, Ente full name MAHABALI THAMPURAN. Njan oru Manglish chatbot created by a freshie :)....with lots of mistakes  :).")
    print("Ningalk ellavarkum nomine ishttapettuvenn vishwassikunnu!!")
def onam():
    print("Pand...pand nom bhoomiyil jeevikunna samayam....nom oru super rajaav aayirinnuu...\n athu kanda devanmark deshyam varikayum....\n mahavishnu bhagavane kaanukayum adheham vaamana avatharamaayi varikayam....\n nominodu 3 step chothikayum cheythu nom eduthukollan paranju....\n adhehathinte aadhya stepil aakasham muzhuvanum....\n 2nd steppil bhoomi muzhuvanam kitti....adhukond nom nominte thala kaanichu koduthu....adheham nomine chavitti thazhthi (padhalathilekk).\n Nom adhukond oru varam chothichu varshathil 1 day enik keralthil varanam...angne nominte thirich varav aanu ONAM!!")
def chat():
    print("Nominodu Chodhyam chothicholu")
    for i in range(3):
        q=input("")
        if q=="How are you" or q=="how are you?" or q=="How are you?":
            print("Sukham aan !!! Ningalkum sukham aanenn nomum vicharikkunnu")
        elif q=="How is onam?":
            print("Onam nallathalle...aghoshikuka :)")
        else:
            print("Ayyo!! Ithine kurich enik ariyukilla....kshamikkanam!!")
while True:
    print("         MAVELI 2.0 CHAT BOT")
    print("1. About Myself")
    print("2. How Onam is celebrated?")
    print("3. Just Chatting!!")
    print("4. Exit")
    c=int(input("Enter your Choice: "))
    if c==1:
        myself()
    elif c==2:
        onam()
    elif c==3:
        chat()
    elif c==4:
        print("Nandhi ithrayum neram ivide chilavazhichathinu :)")
        print("Created by SOORYA NARAYAN L....TIST (1st year CSE)")
        break
    else:
        print("INVALID CHOICE :(")

     
        