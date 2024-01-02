from hello import *

def test_hello():
    hello = Hello("Rohit", 33, ["python", "golang", "python"])
    assert "Rohit" == hello.SayHello()

def test_list():
    hello = Hello("Rohit", 33, ["python", "GoLang", "python"])

    assert hello.ReturnList().lower() == "golang"