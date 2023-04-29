from fastapi import APIRouter
import numpy

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {'msg': 'Hello, World!'}

@router.get('/matrix')
def matrix() -> dict:
    matrix1 = numpy.random.rand(10, 10)
    matrix2 = numpy.random.rand(10, 10)
    result = numpy.matmul(matrix1, matrix2)
    return {
        'matrix1': matrix1.tolist(),
        'matrix2': matrix2.tolist(),
        'result': result.tolist()
    }