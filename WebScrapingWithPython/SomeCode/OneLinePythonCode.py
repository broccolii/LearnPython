print('\n'.join([''.join([('ILoveYou'[(x-y)%8]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))

print('\n'.join(['_'.join(['%s*%s=%-2s' % (y,x,x*y) for y in range(1,x+1)]) for x in range(1,10)]))

import socket
sock=socket.create_connection(('ns1.dnspod.net',6666))
print("---------")
print(sock.recv(13))
sock.close()
