# repeated.py
def main():
    pass
    inp=input()
    n=list(map(int,input().split()))
    list_2=[]

    for num in n:
        k=n.count(num)
        if(k>1):
            if (num not in list_2):
                list_2.append(num)
        else:
            pass
    if (len(list_2)>0):
        print(list_2)
    else:
        print("unique")

if __name__ == '__main__':
    main()
