from ipaddress import ip_network

'''Сеть задана IP-адресом 172.30.0.0 и маской сети 255.254.0.0.
Сколько в этой сети IP-адресов, для которых количество единиц в двоичной записи IP-адреса не  кратно 12?'''

net = ip_network('204.16.168.0/255.255.248.0', 0)

count = 0
for ip in net:
    ipb = bin(int(ip))[2:].zfill(32)
    if ipb.count('1') % 5 != 0:
        count += 1

print(count)

'''Для узла с IP-адресом 115.12.69.38 адрес сети равен 115.12.64.0. 
Найдите наименьшее возможное количество единиц в двоичной записи маски подсети.'''

a = []
for m in range(0, 33):
    net = ip_network(f'115.12.69.38/{m}', 0)
    if str(net.network_address) == '115.12.64.0':
        mb = bin(int(net.netmask))[2:].zfill(32)
        a.append(mb.count('1'))

print(min(a))
