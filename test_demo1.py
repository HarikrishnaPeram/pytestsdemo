import pytest
@pytest.mark.usefixtures("setup")
class Testexmple:
    @pytest.mark.smoke
    def test_firstprogram(self):
        print("hello")
    @pytest.mark.skip
    def test_secondprogram(self):
        msg = "Good morning"
        assert  msg == "Good morning"
        print("Test matches")
    @pytest.mark.xfail
    def test_thirdprogram(self):
        print("Iam learning")

    def test_fifthprogram(self):
        print("Hello")

    def test_fourthprogram(self):
        print("Iam still learning")

    def test_fixtures(self):
        print("i will execute steps in fixtures demo method")