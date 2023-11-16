import pytest
from sparse_recommender import SparseMatrix

def test_get_noValue():     #testing if no value set at certain row or col return 0
    matrix = SparseMatrix()
    assert matrix.get(1, 1) == 0

def test_negative_index_forset():       #testing error raise if negative index is given
    testMatrix = SparseMatrix()
    with pytest.raises(ValueError):
        testMatrix.set(-1, 1, 2)

def test_set_negative_value():          #testing negative value for set
    matrix = SparseMatrix()
    with pytest.raises(ValueError):
        matrix.set(0, 0, -5)

def test_negative_index_forget():       #testing error raise if negative index is given
    testMatrix = SparseMatrix()
    with pytest.raises(ValueError):
        testMatrix.get(0, -1)

def test_get():                   # testing get
    testMatrix = SparseMatrix()
    testMatrix.set(0, 1, 5)
    testMatrix.set(0, 2, 0)
    assert testMatrix.get(0, 1) == 5
    assert testMatrix.get(0, 2) == 0


def test_nonExistant_forGet():      #Testing if out of index or non set set value called default 0 value returned
    testMatrix = SparseMatrix()
    assert testMatrix.get(3, 4) == 0

def test_negative_index_forGet():
    matrix = SparseMatrix()
    with pytest.raises(ValueError):
        matrix.get(-1, 0)

def test_recommend():           #testing recomend method functionality matrix and vector dot product
    testMatrix = SparseMatrix()
    testMatrix.set(0, 0, 5)
    testMatrix.set(1, 1, 3)
    vector = [1, 2]
    result = testMatrix.recommend(vector)
    assert result == [5, 6]

def test_recommend_notValidVector():
    matrix = SparseMatrix()
    matrix.set(0, 1, 6)
    vector = [1, 2, 3]  # Vector length doesn't match matrix size
    with pytest.raises(ValueError):
        matrix.recommend(vector)

def test_add_movie():               #Testing adding movie
    testMatrix1 = SparseMatrix()
    testMatrix1.set(0, 0, 5)
    testMatrix2 = SparseMatrix()
    testMatrix2.set(0, 1, 2)
    result = testMatrix1.add_movie(testMatrix2)
    assert result.get(0, 0) == 5
    assert result.get(0, 1) == 2





