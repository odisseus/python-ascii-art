import pkg_resources
import src.python.ascii_gen as fixture

if __name__ == "__main__":
  import pytest
  raise SystemExit(pytest.main([__file__]))

def test_smoke():
  assert 1 == 1

def test_gen():
  foo = pkg_resources.resource_filename(__name__, '../resources/dazzle.png')
  print('File path: ' + foo)
  fixture.main(['-i',foo,'-o','foo.txt'])
