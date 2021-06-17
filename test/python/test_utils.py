import difflib

def print_diff(expected, actual):
  with open(expected, 'r') as f:
    expected_lines = f.read().splitlines()
  with open(actual, 'r') as f:
    actual_lines = f.read().splitlines()
  for line in difflib.unified_diff(expected_lines, actual_lines, fromfile='expected', tofile='actual', lineterm=''):
    print(line)
