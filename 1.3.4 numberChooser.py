def number(n):
    if int(n)==n:
        if n%2==0:
            if n%3==0:
                print("N is a multiple of 6")
            else:
                print("N is even")
        else:
            print("N is odd")
    else:
        print("N is not an integer")