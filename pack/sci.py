import scipy.interpolate


def version():
    print(scipy.__version__)


def interpolate():
    return scipy.interpolate.pchip([1, 2], [1, 2])
