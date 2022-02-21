x=0
y=5
if x<y:
    print('yes')
if y<x:
    print('yes')
if x:
    print('yes')
if y:
    print('yes')
if 'aul' in 'grault':
    print('yes')
if 'quux' in ['foo','bar','baz']:
    print('yes')

if 'foo' in ['bar','baz','qux']:
    print('Expresion was true')
    print('Executing statement in suite')
    print('...')
    print('Done')
print('After conditional')

if 'foo' in ['foo','bar','baz']:
    print('Outer condition is true')
    if 10>20:
        print('Inner condition 1')
    print('Between inner condition')
    if 10<20:
        print('Inner condition 2')
    print('End of outer confition')
print('After outer condition')

x=120
if x<50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')

hargabuku=20000
hargamajalah=5000
uang=2000
if uang>hargabuku:
    print('Beli Buku')
elif uang>hargamajalah:
    print('Beli Majalah')
else:
    print('Uang tidak cukup')

name='Hacktiv8'
if name == 'Fred':
    print('Hello Fred')
if name == 'Xander':
    print('Hello Xander')
if name == 'Hacktiv8':
    print('Hello Hacktiv8')
if name == 'Arnold':
    print('Hello Arnold')

if 'f' in 'foo': print('1'); print('2'); print('3')

x=2
if x==1: print('foo'); print('bar'); print('baz')
if x==2: print('qux'); print('quux')
else: print('corge'); print('grault')

x=3
if x==1:
    print('foo')
    print('bar')
    print('baz')
if x==2:
    print('qux')
    print('quux')
else:
    print('corge')
    print('grault')

raining=False
print("Let's go to the", 'beach' if not raining else 'library')

raining=True
print("Let's go to the", 'beach' if not raining else 'library')

if True:
    pass
print('foo')

n=5
while n>0:
    n-=1
    print(n)

i=1
while i<6:
    print(i)
    i+=1

n=5
while n>0:
    n-=1
    if n==2:
        break
    print(n)
print('Loop ended.')

n=5
while n>0:
    n-=1
    if n==2:
        continue
    print(n)
print('Loop ended.')

n=5
while n>0:
    n-=1
    print(n)
else:
    print('Loop ended.')

n=5
while n>0:
    n-=1
    print(n)
    if n==2:
        break
else:
    print('Loop ended.')

if age<18:
    if gender == 'M':
        print('son')
    else:
        print('daughter')
elif age>=18 and age<65:
    if gender == 'M':
        print('father')
    else:
        print('mother')
else:
    if gender == 'M':
        print('grandfather')
    else:
        print('grandmother')

a=['foo','bar','baz']
for i in a:
    print(i)
