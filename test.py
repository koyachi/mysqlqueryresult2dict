import mysqlqueryresult2dict
import unittest

class TestParseText(unittest.TestCase):

  def setUp(self):
    self.data = '''mysql> SELECT * FROM foo;
+----+-------+
| id | value |
+----+-------+
|  1 |     A |
|  2 |     b |
|  3 |     C |
+----+-------+
3 rows in set (0.01 sec)
'''

  def test_parse_text(self):
    result = mysqlqueryresult2dict.parse_text(self.data)
    #print result
    self.assertEqual(result['header'], ['mysql> SELECT * FROM foo;'], 'result["header"]')
    self.assertEqual(result['fields'], ['id', 'value'], 'result["fields"]')
    self.assertEqual(result['records'],
                     [{'id': '1', 'value': 'A'},
                      {'id': '2', 'value': 'b'},
                      {'id': '3', 'value': 'C'}],
                     'result["records"]')
    self.assertEqual(result['footer'], ['3 rows in set (0.01 sec)', ''], 'result["footer"]')

if __name__ == '__main__':
  unittest.main()
