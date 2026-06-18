#!/usr/bin/env python3

from  decrypt import add, multiply

def main():
    x = add(2,3)
    y = multiply(x, 10)
    print(add(x,y))

if __name__ == "__main__":
    main()


