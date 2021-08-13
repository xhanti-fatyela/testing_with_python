import greet
import pytest


def test_greeted():
    assert greet.greet('Xhanti') == 'Hello Xhanti'
