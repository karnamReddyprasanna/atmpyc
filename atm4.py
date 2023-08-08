from atmmenu import atmoperations



from atm3 import DepositeError,withdrawError,InsufError
bal=500.00
def deposite():
    global bal
    damt=float(input('enter the deposited bal: '))
    if damt<0:
        raise DepositeError
    else:
        global bal
        bal+=damt
        print('ur account xxxxxxx123 created with INR:{}'.format(damt))
        print('now ur account xxxxx123 after deposite INR:{}".format(bal)')
def withdraw():
    global bal
    wamt=float(input('enter the deposited bal: '))
    if bal<=wamt:
        raise withdrawError
    elif (wamt+500)>bal:
        raise InsufError
    else:
        bal-=wamt
        print('ur account number xxxxxxx123 withdraw with INR:{}'.format(wamt))
        print('now ur account xxxx123 after deposit INR:{}'.format(bal))
def balenq():
    print('now ur account xxx123 after deposite INR:{}'.format(bal))
