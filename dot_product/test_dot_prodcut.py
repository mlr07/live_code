import pytest
import numpy as np

from dot_product import dot_product


def test_unequal_lengths():
    x = [1,1,1,1]
    y = [1,1]

    with pytest.raises(AssertionError):
        dot_product(x,y)


def test_scaler_output():
    x = [1,2,3,4,5]
    y = [1,1,1,1,1]

    output = type(dot_product(x,y))

    assert output == int or output == float


def test_result():
    x = [1,2,3,4,5]
    y = [1,1,1,1,1]

    np_x = np.array(x)
    np_y = np.array(y)
    
    assert dot_product(x,y) == np_x.dot(np_y)
