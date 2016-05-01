from mock import MagicMock
import py.path

from pytest_datadir_ng import _Datadir


def test_datadir():
    request = MagicMock()
    basedir = py.path.local('tests')
    datadir = basedir.join('data')
    request.fspath.dirpath = MagicMock(return_value=basedir)

    # tests.test_module.TestClass.test_method
    request.module.__name__ = 'test_module'
    request.cls.__name__ = 'TestClass'
    request.function.__name__ = 'test_method'
    d = _Datadir(request)
    assert d._datadirs == [
        basedir.join('test_module', 'TestClass', 'test_method'),
        basedir.join('test_module', 'TestClass'),
        basedir.join('test_module'),
        datadir.join('test_module', 'TestClass', 'test_method'),
        datadir.join('test_module', 'TestClass'),
        datadir.join('test_module'),
        datadir,
    ]

    # tests.test_module.test_function
    request.module.__name__ = 'test_module'
    request.cls = None
    request.function.__name__ = 'test_function'
    d = _Datadir(request)
    assert d._datadirs == [
        basedir.join('test_module', 'test_function'),
        basedir.join('test_module'),
        datadir.join('test_module', 'test_function'),
        datadir.join('test_module'),
        datadir,
    ]
