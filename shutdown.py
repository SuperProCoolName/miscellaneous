import os
import time

def main():
    counter = int(input('Input time in seconds: '))
    while counter > 0:
        print(counter)
        counter = counter - 1
        time.sleep(1)
    os.system("shutdown /s /t 1")

if __name__ == '__main__':
    main()