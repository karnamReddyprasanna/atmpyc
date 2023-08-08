from atmmenu import atmoperations

from atm3 import *
from atm4 import deposite,withdraw,balenq


while(True):
    try:
        atmoperations()
        ch=int(input('enter our choice'))
        match(ch):
            case 1:
                try:
                    deposite()
                except DepositeError:
                    print('dont try to -ve values and zero and values')


            case 2:
                try:
                    withdraw()
                except withdrawError:
                    print('dont try to give -ve and zero values')
                except InsufError:
                    print('u dont have stuff funds')
                except ValueError:
                    print('dont try to deposite space and number')
            case 3:
                balenq()
            case 4:
                print('tnx for our program')
            case _:
                print('ur selection process is wrong try again')

    except ValueError:
        print('dont enter alwayd strs')