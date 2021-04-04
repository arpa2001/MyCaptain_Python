def most_frequent(txt):
    #converting in lowercase
    txt_l = ""
    for i in txt:
        if (ord(i) >= 65 and ord(i) <= 90):
            txt_l = txt_l + chr(ord(i) + 32)
        else:
            txt_l = txt_l + i

    #making list of letters
    letters = []
    for l in txt_l:
        letters.append(l)
    letters = list(set(letters))

    #creating dictionary
    freq_r = {}
    n = 0
    for k in letters:
        for i in txt_l:
            if k == i:
                n = n + 1
        dbuff = {k: n}
        freq_r.update(dbuff)
        n = 0

    freq_d = sorted(freq_r.items(), key=lambda x: x[1], reverse=True)

    #arranging output
    print("Output:\n")
    for outs in freq_d:
        print(outs[0], " = ", "{:0>2d}".format(outs[1]))


inpt = input("Input: Please enter a string\n\t")
most_frequent(inpt)