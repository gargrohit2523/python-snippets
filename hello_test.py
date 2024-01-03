from hello import *
import pytest

# Specifies that below function is a fixture
@pytest.fixture
def setup():
    hello = Hello("Rohit", 33, ["python", "golang", "python"])
    return hello

def test_hello():
    assert "Rohit" == setup.SayHello()

def test_list():
    assert setup.ReturnList().lower() == "golang"