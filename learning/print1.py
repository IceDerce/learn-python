import decimal

print(decimal.Decimal(9.58))

t = 'i am a very genius,but your are a fool'

print(t.capitalize()) # Cap first letter
print(t.split()) # split by words
print(t.find('i')) # return index of 'i'
print(t.find('in')) # index of 'i' in 'in'
print(t.find('Python')) # find sth not in
print(t[0:4]) # returu from index 0 to 3
print(t.replace(' ', '|')) # replace by '|'

w = 'http://www.google.com'
print(w.strip('http://')) #delete sth
