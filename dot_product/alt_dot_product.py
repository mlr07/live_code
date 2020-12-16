# TODO: implement tests and fixtures for different vec types/lenghts
# TODO: figure out module import for pytest


def ver1(vec1, vec2):
    """
    compute dot product of two vectors with LAFF inspired routine. 
    """
    
    assert len(vec1) == len(vec2), "vector dimensions are not aligned."

    assert all(isinstance(i, (int, float)) for i in vec1), "vec1 contains non-numeric."

    assert all(isinstance(i, (int, float)) for i in vec2), "vec2 contains non-numeric."

    m = len(vec1)
    alpha = 0

    for i in range(m):
        alpha = vec1[i] * vec2[i] + alpha

    return alpha


def ver2(x,y):
    """
    compute dot prodcut of two vectors with built-ins and comprehension.
    """
    
    # statement to find errors early in execution
    assert len(x) == len(y), "vector dimensions are not equal."

    # comprehension, built-ins
    alpha = sum(x*y for x,y in zip(x,y))

    return alpha


if __name__ == "__main__":
    x = [10, 20, 30, 40, 50]
    y = [1, 2, 3, 4, 5]

    alpha = ver1(x,y)
    print(f"x dot y = {alpha}")
