import sys,random
import time
import itertools
def main():
    words = "1234567890"
    temp = itertools.permutations(words,2) #穷举的是words里的所有资源，2是复杂度，例如13，14，15；如果复杂度为3，那么穷举出的就是123，145，141
    password = open("dic.txt","a")
    for i in temp:
        password.write(" ".join(i))
        password.write(" ".join("\n"))
    passwords.close()
    pass
if __name__ == '__main__':
    main()