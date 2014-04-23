=====================
mysqlqueryresult2dict
=====================


Description
===========

Create dict from MySQL query result text.
python port of https://github.com/koyachi/ruby-hash-from_mysql_query_result .

Example
=======

.. code:: python
  import mysqlqueryresult2dict
  
  DATA = '''mysql> SELECT * FROM foo;
  +----+-------+
  | id | value |
  +----+-------+
  |  1 |     A |
  |  2 |     b |
  |  3 |     C |
  +----+-------+
  3 rows in set (0.01 sec)
  
  
  dict = mysqlqueryresult2dict.parse_text(DATA)
  print dict

Author
======

koyachi, rtk2106@gmail.com

License
=======

mysqlquery2dict is avairable under the MIT license. See the LICENSE file for more info.
