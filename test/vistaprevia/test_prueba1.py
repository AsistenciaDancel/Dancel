import pytest 


@pytest.mark.marca1
def test_prueba():
    assert 1==1

@pytest.mark.marca1
def test_prueba2():
    assert 1==1

@pytest.fixture(scope="session") 
def fixture_1():
    print("Desde mi fixture antes")
    yield 1 #al usar yield la salida cambia hace un seguimiento
    print ("desde mi fixture luego") 


@pytest.mark.marca1
def test_prueba3(fixture_1):
    print("desde mi test")
    variable= fixture_1
    assert variable==1


@pytest.mark.marca1
def test_prueba4(fixture_1):
    print("desde mi test")
    variable= fixture_1
    assert variable==1


