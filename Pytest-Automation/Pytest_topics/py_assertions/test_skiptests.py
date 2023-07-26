import sys

import pytest

pytestmarker = pytest.mark.skipif(sys.platform == 'win32', reason='will only run on linux')

const = 9 / 5


def cent_to_fah(cent=0):
    fah = (cent * const) + 32
    return fah


@pytest.mark.skip(reason="Skipping for no reason")
def test_case01():
    assert type(const) == float


# @pytest.mark.skipif(sys.version_info.minor > 4, reason="does not work on py version above 3.6")
def test_case02():
    assert cent_to_fah() == 32


@pytest.mark.skipif(pytest.__version__ == '7.3.1', reason="this test case does not support pytest 7.3.1")
def test_case03():
    assert cent_to_fah(38) == 100.4
