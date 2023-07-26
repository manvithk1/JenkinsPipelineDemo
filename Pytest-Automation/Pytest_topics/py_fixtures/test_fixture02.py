import pytest

weekdays1 = ['mon', 'tue', 'wed']
weekdays2 = ['fri', 'sat', 'sun']


@pytest.fixture()
def setup01():
    weekdays1.append('thur')
    yield
    print ("\n after yield in setup01 fixture")
    weekdays1.pop()



