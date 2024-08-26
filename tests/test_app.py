import pytest
from src import app

def test_main():
    assert app.main() is None
