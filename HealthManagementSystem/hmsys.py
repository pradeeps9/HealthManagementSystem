def getdate():
    import datetime
    return datetime.datetime.now()


#  take input for what user want to do
act = input("What do you want to do Lock/Retrieve data?\n 1 to Lock &\n 2 to Retrieve")
client = input("Choose whose client:\n 1 for Pradeep\n 2 for Sumeet\n 3 for Kishan")
scdl = input("Choose from:\n 1 for Diet\n 2 for Exercise")

def hms(filename, act1):
    """This function retrieve or lock data depends on the value of act"""
    if act1 == "1":
        with open(filename, "a") as etf:
            cmnt = "[" + str(getdate()) + "]" + input("Write here") + "\n"
            etf.write(cmnt)
            print(cmnt)
    elif act1 == "2":
        with open(filename, "r") as otf:
            print(otf.read())

if client == "1" and scdl == "1":
    hms("Harry_Diet", act)
elif client == "1" and scdl == "2":
    hms("Harry_Ex", act)
elif client == "2" and scdl == "1":
    hms("Rohan_Diet", act)
elif client == "2" and scdl == "2":
    hms("Rohan_Ex", act)
elif client == "3" and scdl == "1":
    hms("Hammad_Diet", act)
elif client == "3" and scdl == "2":
    hms("Hammad_Ex", act)

