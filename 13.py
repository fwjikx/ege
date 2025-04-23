from ipaddress import *

# если IP-адрес: 1.2.3.4, а маска: 255.255.255.192, тогда
net = ip_network(f'1.2.3.4/255.255.255.192', 0) # сеть создается так

# или так:
net = ip_network(f'1.2.3.4/26', 0) # потому что в такой маске 26 единиц

print(net) # сеть в виде: адрес сети / количество единиц в маске
print(net[0]) # адрес сети
print(net[-1]) # адрес широкого вещания сети
print(net.netmask) # маска сети
print(net.num_addresses) # количество IP-адресов в сети
print(net.num_addresses - 2) # количество узлов в сети

# получить все IP-адреса сети
for ip in net:
    print(ip)
    b = f'{int(ip):032b}' # или в двоичном представлении
    print(b)

# получить все узлы сети
for ip in net.hosts():
    print(ip)

# или
for ip in net:
    if net[0] < ip < net[-1]:
         print(ip)

# если IP-адрес: 1.2.3.4
ip = ip_address('1.2.3.4') # его объект создается так

# проверка, что адрес - это адрес сети net
if ip == net[0]:
    print('YES')

# проверка, что адрес - это адрес широкого вещания сети net:
if ip == net[-1]:
    print('YES')

# проверка, что адрес - это узел сети net:
if net[0] < ip < net[-1]:
    print('YES')