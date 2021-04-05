import csv


def lwrcase(txt):
    # converting in lowercase
    txt_l = ""
    for i in txt:
        if (ord(i) >= 65 and ord(i) <= 90):
            txt_l = txt_l + chr(ord(i) + 32)
        else:
            txt_l = txt_l + i
    return txt_l

def numsuffix(num):
    # adding suffix to number
    ns = ""
    n_l = num % 10
    if num % 100 >= 11 and num % 100 <= 19:
        nS = str(num)+"th"
    elif n_l == 1:
        nS = str(num)+"st"
    elif n_l == 2:
        nS = str(num)+"nd"
    elif n_l == 3:
        nS = str(num)+"rd"
    else:
        nS = str(num)+"th"
    return nS

# Taking entries
entr = True
n = 1
while(entr):
    # filling info
    print(f"\nEnter {numsuffix(n)} student's following information:")
    s_name = input("\tName:\t\t")
    s_age = input("\tAge:\t\t")
    s_ph = input("\tPhone number:\t")
    s_email = input("\tEmail ID:\t")

    info_list = [s_name, s_age, s_ph, s_email]  # listing info

    # condition to check entry
    print("\nPlease verify the info:")
    print(f"\tName:\t\t{info_list[0]}\n\tAge:\t\t{info_list[1]}\n\tPhone Number:\t{info_list[2]}\n\tEmail ID:\t{info_list[3]}")
    try_chk = False
    while(not try_chk):
        chk = input("\nIs the entered info correct? (y/n): ")
        chk = lwrcase(chk)
        if chk == "y":
            # condition to ask next entry
            try_info = False
            while(not try_info):
                nN = n + 1
                rep = input(f"\nWish to enter {numsuffix(nN)} student info? (y/n): ")
                rep = lwrcase(rep)
                if rep == "y":
                    n += 1
                    try_info = True
                elif rep == "n":
                    entr = False
                    try_info = True
                else:
                    print("Wrong Input!")
                    try_info = False
            try_chk = True
        elif chk == "n":            
            try_chk = True
        else:
            print("Wrong Input!")
            try_chk = False