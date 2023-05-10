import funciones
import requests


def test_suma():
    assert 2 == funciones.suma(1, 1)
    assert 4 == funciones.suma(2, 2)


def test_resta():
    assert 2 == funciones.resta(4, 2)
    assert 0 == funciones.resta(2, 2)


def test_suma_resta():
    assert 2 == funciones.suma(1, 1)
    assert 0 == funciones.resta(1, 1)


def test_api():
    url_base = 'https://api-mycloudstorage-gpxkblrpvq-ew.a.run.app'
    names = '/allnames'
    filedata = '/data'

    list_names = requests.get(f'{url_base}{names}')
    last_name = list_names.json()[-1]
    params_c = {'file': last_name}
    data_c = requests.get(f'{url_base}{filedata}', params_c)

    assert 200 == list_names.status_code
    assert 200 == data_c.status_code
