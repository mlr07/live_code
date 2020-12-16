def dot_product(vec1, vec2):

    assert len(vec1) == len(vec2), "vector lengths are not equal"
    
    m = len(vec1)
    alpha = 0

    for i in range(m):
        alpha = vec1[i] * vec2[i] + alpha

    return alpha
