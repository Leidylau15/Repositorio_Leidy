import random as rd 
def main():
    a=''
    pal='leidy'
    while a!= 'exit':
        print(rd.choice(pal))
        a=input("oprime enter :")

if __name__=="__main__":
    main()