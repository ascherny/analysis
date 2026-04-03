from math import *


flag = b'\x1c-\x1b#\x1d*2S(\x0c\n\nO\x08J<7\x1bJ\x0c\x1bC=\x1c7/\t\x0f@7\x1b\x0c\x1d\r\x0cJU'
print('[*] Hello this is simple cipher program. Enter the message: ')
message = str(input())
if message == "Give me flag":
    print("[*] where 'please'?")
elif message == "Give me flag please":
    print("[*] None. GLHF")

key = ord(message[len(message)-1])
list_output = []
flag_ouput = []
for i in range(0, len(message)):
    print(chr(ord(message[i])))
    list_output.append(chr(ord(message[i])+key))
for i in range(0, len(flag)):
        flag_ouput.append(chr(flag[i]+key))

str_ouput = ''.join(list_output)
str_flag = ''.join(flag_ouput) 

print('[*] This is your cipher text: ', str_ouput)
print('[*] This is flag output: ', str_flag)

flag = b'\x1c-\x1b#\x1d*2S(\x0c\n\nO\x08J<7\x1bJ\x0c\x1bC=\x1c7/\t\x0f@7\x1b\x0c\x1d\r\x0cJU'

def brute(k: int):
        my_flag = []
        for i in range(len(flag)):
            my_flag.append(chr(flag[i]+k))
        return ''.join(my_flag)
        
def check(candidate: str):
    if candidate:
        ratio = sum(1 for ch in candidate if 32 < ord(ch) < 128)/len(candidate)
        if ratio == 1:
            print(ratio, candidate)
    
for k in range(256):
    check(brute(k))
