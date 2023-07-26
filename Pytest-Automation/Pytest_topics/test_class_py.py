
class TestMyStuff():
    def test_type(self):
        assert type(1.3) == float

    def test_str(self):
        assert str.upper('python') == 'PYTHON'