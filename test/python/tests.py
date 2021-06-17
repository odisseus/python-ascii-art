import pkg_resources
import filecmp
import test_utils
import src.python.ascii_gen as fixture

if __name__ == "__main__":
  import pytest
  raise SystemExit(pytest.main([__file__]))

def test_smoke():
  assert 1 == 1

def test_gen():
  input = pkg_resources.resource_filename(__name__, '../resources/star.png')
  output = 'star.txt'
  fixture.main(['-i', input, '-o', output, '-c', '4'])
  expected = pkg_resources.resource_filename(__name__, '../resources/star.txt')
  ok = filecmp.cmp(expected, output)
  if not ok:
    test_utils.print_diff(expected, output)
  assert ok
