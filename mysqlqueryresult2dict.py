import re

PARSE_STATUS = {
  'header': 1,
  'table_header': 2,
  'table_body': 3,
  'table_footer': 4,
  'footer': 5
}

TABLE_FRAME_PATTERN = '\+\-+\+'
tableFrameRegex = re.compile(TABLE_FRAME_PATTERN)

def parse_text(text):
  result = {
    'header': '',
    'fields': [],
    'records': [],
    'footer': ''
    }
  state = PARSE_STATUS['header']
  lines = text.split('\n')
  index = 0;
  for line in lines:
    if tableFrameRegex.match(line):
      if state == PARSE_STATUS['table_header']:
        result['fields'] = process_table_header(lines[index:])
        state = PARSE_STATUS['table_body']
      elif state == PARSE_STATUS['table_body']:
        records = process_table_body(lines[index:])
        tmp_records = []
        for record in records:
          tmp = {}
          i = 0
          for key in result['fields']:
            tmp[key] = record[i]
            i = i + 1
          tmp_records.append(tmp)
        result['records'] = tmp_records
        state = PARSE_STATUS['table_footer']
      elif state == PARSE_STATUS['table_footer']:
        result['footer'] = process_table_footer(lines[index:])
        state = PARSE_STATUS['footer']
      elif state == PARSE_STATUS['footer']:
        process_footer(lines[index:])
    else:
      if state == PARSE_STATUS['header']:
        result['header'] = process_header(lines[index:])
        state = PARSE_STATUS['table_header']
    index = index + 1

  return result

def process_header(lines):
  results = []
  i = 0
  for line in lines:
    if i != 0 and tableFrameRegex.match(line):
      return results

    i = i + 1

    line = line.rstrip()
    results.append(line)

def process_table_header(lines):
  i = 0
  for line in lines:
    if i != 0 and tableFrameRegex.match(line):
      return

    should_continue = False;
    if i == 0 and tableFrameRegex.match(line):
      should_continue = True
    i = i + 1

    if should_continue:
      continue

    line = line.rstrip()
    p = re.compile('\s')
    headers = p.sub('', line).split('|')[1:-1]
    return headers

def process_table_body(lines):
  results = []
  i = 0;
  for line in lines:
    if i != 0 and tableFrameRegex.match(line):
      return results

    should_continue = False;
    if i == 0 and tableFrameRegex.match(line):
      should_continue = True
    i = i + 1

    if should_continue:
      continue

    line = line.rstrip()
    p = re.compile('\s')
    rows = [p.sub('', s) for s in line.split('|')][1:-1]
    results.append(rows)

  return result

def process_table_footer(lines):
  results = []
  i = 0
  for line in lines:
    if i != 0 and tableFrameRegex.match(line):
      return results

    should_continue = False;
    if i == 0 and tableFrameRegex.match(line):
      should_continue = True
    i = i + 1

    if should_continue:
      continue

    line = line.rstrip()
    results.append(line)

  return results

def process_footer(lines):
  return

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
