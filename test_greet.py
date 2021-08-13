import greet
import pytest


def test_greeted():
    assert greet.greet('Xhanti') == 'Hello Xhanti'


def test_geet_in_lang():
    assert greet.greet_in_lang('es', 'Andre') == 'Hola Andre'


def test_geet_in_lang():
    assert greet.greet_in_lang('fr', 'Andre') == 'Bonjour Andre'
