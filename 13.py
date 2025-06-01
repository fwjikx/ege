# Адрес сети = IP-адрес узла & Маска сети
# IP состоит из 4 чисел на каждое из которых выделено по 1 байту (то есть по 8 бит).
# Таким образом числа лежат в диапазоне от 0 до 255 (11111111).
# Маска имеет длину 32 бита и вид: 111111..00 (сначала единицы, затем нули).

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


#❗️Шаблон для первого типа:
#Написать программу, которая определяет адрес сети.
from ipaddress import *
net = ip_network('IP адрес узла/Маска сети', 0)
print(net)

#❗️Шаблон для второго типа:
#наибольшее/наименьшее количество нулей/единиц в двоичной записи маски подсети.
from ipaddress import *
for mask in range(32+1):
    net = ip_network(f'IP адрес узла/{mask}', 0)
    print(net, net.netmask)


#❗️Шаблон для второго типа (решением кодом):

from ipaddress import *
maxi = 0
for mask in range(32+1):
    net = ip_network(f'IP адрес узла/{mask}', 0)
    if str(net) == f'Адрес сети/{mask}':
        maxi = max(maxi, mask)
print(maxi)

#❗️Шаблон для третьего типа:
#Написать программу, которая определяет сколько в сети IP-адресов.
from ipaddress import *
net = ip_network('IP адрес узла/Маска сети', 0)
cnt = 0
for ip in net:
       b = f'{ip:b}'
    if  # тут прописываем условие:
        cnt += 1
print(cnt)

#❗️Шаблон для четвертого типа:
#Написать программу, которая определяет максимальное/минимальное число А - некоторое допустимое для записи IP-адреса число.
from ipaddress import *
maxi = 0
for A in range(0, 255+1):
    net = ip_network(f'IP адрес узла.{A}/Маска сети', 0)
    if all( тут прописываем условие for ip in net):
        maxi = A
print(maxi)

#❗️Шаблон для пятого типа:
#В условии сказано что есть два узла, находящиеся в одной сети.
from ipaddress import *
for mask in range(32+1):
    net1 = ip_network(f'IP узел сети №1/{mask}', 0)
    net2 = ip_network(f'IP узел сети №2/{mask}', 0)
    if net1 == net2:  # меняем условие, относительно одна сеть или несколько
        print(net1.netmask)
