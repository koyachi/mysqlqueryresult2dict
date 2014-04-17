import mysqlquery2dict

DATA = '''mysql> SELECT * FROM foo;
+----+-------+
| id | value |
+----+-------+
|  1 |     A |
|  2 |     b |
|  3 |     C |
+----+-------+
3 rows in set (0.01 sec)
'''

dict = mysqlquery2dict.parse_text(DATA)
print dict
