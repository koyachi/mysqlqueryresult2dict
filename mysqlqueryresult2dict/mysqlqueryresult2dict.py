import re

class MysqlQueryResult2Dict:
  def __init__(self):
    self.PARSE_STATUS = {
      'header': 1,
      'table_header': 2,
      'table_body': 3,
      'table_footer': 4,
      'footer': 5
      }

    self.TABLE_FRAME_PATTERN = '\+\-+\+'
    self.tableFrameRegex = re.compile(self.TABLE_FRAME_PATTERN)

  def parse_text(self, text):
    result = {
      'header': '',
      'fields': [],
      'records': [],
      'footer': ''
      }
    state = self.PARSE_STATUS['header']
    lines = text.split('\n')
    for index, line in enumerate(lines):
      if self.tableFrameRegex.match(line):
        if state == self.PARSE_STATUS['table_header']:
          result['fields'] = self.process_table_header(lines[index:])
          state = self.PARSE_STATUS['table_body']
        elif state == self.PARSE_STATUS['table_body']:
          records = self.process_table_body(lines[index:])
          tmp_records = []
          for record in records:
            tmp = {}
            for i, key in enumerate(result['fields']):
              tmp[key] = record[i]
            tmp_records.append(tmp)
            result['records'] = tmp_records
          state = self.PARSE_STATUS['table_footer']
        elif state == self.PARSE_STATUS['table_footer']:
          result['footer'] = self.process_table_footer(lines[index:])
          state = self.PARSE_STATUS['footer']
        elif state == self.PARSE_STATUS['footer']:
          self.process_footer(lines[index:])
      else:
        if state == self.PARSE_STATUS['header']:
          result['header'] = self.process_header(lines[index:])
          state = self.PARSE_STATUS['table_header']

    return result

  def process_header(self, lines):
    results = []
    for i, line in enumerate(lines):
      if i != 0 and self.tableFrameRegex.match(line):
        return results

      line = line.rstrip()
      results.append(line)

  def process_table_header(self, lines):
    for i, line in enumerate(lines):
      if i != 0 and self.tableFrameRegex.match(line):
        return
  
      if i == 0 and self.tableFrameRegex.match(line):
        continue
  
      line = line.rstrip()
      p = re.compile('\s')
      headers = p.sub('', line).split('|')[1:-1]
      return headers

  def process_table_body(self, lines):
    results = []
    for i, line in enumerate(lines):
      if i != 0 and self.tableFrameRegex.match(line):
        return results
  
      if i == 0 and self.tableFrameRegex.match(line):
        continue
  
      line = line.rstrip()
      p = re.compile('\s')
      rows = [p.sub('', s) for s in line.split('|')][1:-1]
      results.append(rows)
  
    return result
  
  def process_table_footer(self, lines):
    results = []
    for i, line in enumerate(lines):
      if i != 0 and self.tableFrameRegex.match(line):
        return results
  
      if i == 0 and self.tableFrameRegex.match(line):
        continue
  
      line = line.rstrip()
      results.append(line)
  
    return results
  
  def process_footer(self, lines):
    return

def parse_text(text):
  return MysqlQueryResult2Dict().parse_text(text)

if __name__ == '__main__':
  TEST_DATA = '''mysql> SELECT * FROM foo;
+----+-------+
| id | value |
+----+-------+
|  1 |     A |
|  2 |     b |
|  3 |     C |
+----+-------+
3 rows in set (0.01 sec)
'''
  print parse_text(TEST_DATA)
