import pack
import pack.np


def test_import_pack():
    print('Version is {}'.format(pack.version()))


def test_import_numpy():
    print('Numpy version is {}'.format(pack.np.version()))

