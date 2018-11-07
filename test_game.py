import frontend
import backend
import pytest



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


#winning tests
@pytest.mark.parametrize('dark_coordinates', [[]])
def test_win(dark_coordinates):
    result = frontend.check_win(dark_coordinates)
    assert result == True

@pytest.mark.parametrize('dark_coordinates', [[(2,2)]])
def test_not_win(dark_coordinates):
    result = frontend.check_win(dark_coordinates)
    assert result == False


#switch tests
def test_cross_switch():
    click_coordinate = (1,1)
    light_coordinates = [(1,1), (1,2), (1,0), (0,1), (2,1)]
    dark_coordinates = []
    SIZE = 4
    backend.cross_switch(click_coordinate, light_coordinates, dark_coordinates, SIZE)
    assert light_coordinates == []
    for a in light_coordinates:
        assert a in dark_coordinates

def test_corner_switch():
    click_coordinate = (0,0)
    light_coordinates = [(0,0), (0,1), (1,0)]
    dark_coordinates = []
    SIZE = 4
    backend.cross_switch(click_coordinate, light_coordinates, dark_coordinates, SIZE)
    assert light_coordinates == []
    for a in light_coordinates:
        assert a in dark_coordinates
