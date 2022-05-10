import os_tools.tools as f
import os
import shutil



# тесты для "чистых" функций
def test_about():
    assert f.about() == '(c) Konstantin Voloshenko'


# тесты для "грязных" функций
def test_create_dir():
    dir_name = 'test_dir_1'
    if os.path.exists(dir_name):
        os.rmdir(dir_name)
    f.create_dir(dir_name)
    assert os.path.exists(dir_name)
    os.rmdir(dir_name)


def test_del_dir():
    dir_name = 'test_dir_2'
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    f.del_dir(dir_name)
    assert not os.path.exists(dir_name)


def test_copy_dir():
    dir_name = 'test_copy_dir1'
    dir_new = 'test_copy_dir2'
    os.mkdir(dir_name)
    f.copy_dir(dir_name, dir_new)
    assert os.path.exists(dir_new)
    os.rmdir(dir_name)
    os.rmdir(dir_new)


def test_info_dir():
    cur_dir = os.getcwd()
    dir_name = 'test_info_dir'
    os.mkdir(dir_name)
    os.chdir(dir_name)
    os.mkdir('test_dir_1')
    os.mkdir('test_dir_2')
    open('test_file_1', mode='a').close()
    open('test_file_2', mode='a').close()
    assert f.info_dir('dirs') == ['test_dir_1', 'test_dir_2']
    assert f.info_dir('files') == ['test_file_1', 'test_file_2']
    assert f.info_dir('all') == ['test_dir_1', 'test_dir_2', 'test_file_1', 'test_file_2']
    os.chdir(cur_dir)
    # os.rmdir(dir_name)
    shutil.rmtree(dir_name, ignore_errors=True)


def test_info_os():
    assert len(f.info_os()) > 1

def test_save_info_dir():
    cur_dir = os.getcwd()
    dir_name = 'test_save_dir'
    os.mkdir(dir_name)
    os.chdir(dir_name)
    os.mkdir('test_dir_1')
    os.mkdir('test_dir_2')
    open('test_file_1', mode='a').close()
    open('test_file_2', mode='a').close()
    f.save_info_dir()
    with open('listdir.txt', 'r') as file:
        #  Прочитать сразу все данные
        result = file.read()
    #print(result)
    assert result == 'files: test_file_1, test_file_2\ndirs: test_dir_1, test_dir_2\n'
    os.chdir(cur_dir)
    shutil.rmtree(dir_name, ignore_errors=True)




