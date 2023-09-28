import pytest  
import subprocess
def test_List_files():
 output = subprocess.check_output([' ./my_program', 'I']) 
assert 'file.txt' in output.decode()
def test_extract_files_with_paths():
 subprocess.call(['./my_program' ,'c','-p','path/to/archive', 'file1.txt','file2.txt'])
output = subprocess.check_output(['./my_program' ,'c','-p','path/to/archive'])
assert os.path.exists('path/to/archive/file1.txt')
assert os.path.exists('path/to/archive/file2.txt')
def test_hash_calculation():
 with open('file.txt', 'w') as f:
     f.write('hello world')
     output = subprocess.check_output([' ./my_program', 'h','file.txt'])
excepted_hash = subprocess.check_output(['crc32', file.txt]).decode().rstrip()
assert output.decode().rstrip() == excepted_hash
if __name__ == '__main__':
    pytest.main()