import pack
import pack.np
import pack.sci


def test_import_pack():
    print('Version is {}'.format(pack.version()))


def test_import_numpy():
    print('Numpy version is {}'.format(pack.np.version()))


def test_import_scipy():
    print('Scipy version is {}'.format(pack.sci.version()))
