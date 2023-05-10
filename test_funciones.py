import funciones


def test_suma():
    assert 2 == funciones.suma(1, 1)
    assert 4 == funciones.suma(2, 2)


def test_resta():
    assert 2 == funciones.resta(4, 2)
    assert 0 == funciones.resta(2, 2)


def test_suma_resta():
    assert 2 == funciones.suma(1,1)
    assert 0 == funciones.resta(1,1)
