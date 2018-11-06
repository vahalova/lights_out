import frontend
import backend
import pytest
import subprocess
import sys


#input tests
@pytest.mark.parametrize('size', [-1, 123, 0])
def test_is_unvalid_size(size):
    result = frontend.is_valid_size(size)
    assert result == None

@pytest.mark.parametrize('size', [4, 20, 30])
def test_is_valid_size(size):
    result = frontend.is_valid_size(size)
    assert result == True

@pytest.mark.parametrize('size', ['abc',[],  ' ' ])
def test_is_TypeError_size(size):
    with pytest.raises(TypeError):
        frontend.is_valid_size(size)


#winning test
@pytest.mark.parametrize('dark_coordinates', [[]])
def test_win(dark_coordinates):
    result = frontend.check_win(dark_coordinates)
    assert result == True

@pytest.mark.parametrize('dark_coordinates', [[(2,2)]])
def test_not_win(dark_coordinates):
    result = frontend.check_win(dark_coordinates)
    assert result == False
