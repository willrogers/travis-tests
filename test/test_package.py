import package
import package.np

def test_import_package():
    print('Version is {}'.format(package.version()))


def test_import_numpy():
    print('Numpy version is {}'.format(package.np.version()))

