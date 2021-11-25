ichiban_price=100
superdry_price=120

list_c=[('ichiban',135),('ichiban',350),
   ('ichiban',1000),('ichiban',2500),
   ('superdry',135),('superdry',350),
   ('superdry',1000),('superdry',2500),
]
prices=[]
d={}
for i in range(len(list_c)):
   if i<4:
      prices.append(ichiban_price*(2**i))
   else:
      i-=4
      prices.append(superdry_price*(2**i))

for k in range(len(list_c)):
   d[list_c[k]]=prices[k]

for k in d:
    print(d[k])