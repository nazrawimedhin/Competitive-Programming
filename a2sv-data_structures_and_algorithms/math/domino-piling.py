#!/usr/bin/python3

def dominoPilling(m, n):
    return int(m * n / 2)

if __name__ =="__main__":
    m = int(input("Enter M:\n"))
    n = int(input("Enter N:\n"))
    print(dominoPilling(m, n))
