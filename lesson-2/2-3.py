d={('ichiban',350):210,('ichiban',500):280,('superdry',350):205,
   ('superdry',500):270,('black_label',350):220,('black_label',500):285}
print(d)
# 各キーに対応する値段を表示

for i in d:
   print(d[i])
# 辞書中のキーの一覧と値の一覧も表示
print(d.keys())
print(d.values())