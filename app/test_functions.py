
from app.functions import *


def test_es_par():

    # Casos positivos
    assert(es_par(2) == True)
    assert(es_par(8) == True)
    assert(es_par(22) == True)
    assert(es_par(46) == True)
    assert(es_par(123456) == True)

    # Casos negativos
    assert(es_par(1) == False)
    assert(es_par(5) == False)
    assert(es_par(7) == False)
    assert(es_par(9) == False)
    assert(es_par(121) == False)


def test_es_inpar():
    # Casos positivos
    assert(es_impar(1) == True)
    assert(es_impar(5) == True)
    assert(es_impar(7) == True)
    assert(es_impar(99) == True)
    assert(es_impar(12324341) == True)

    # Casos negativos
    assert(es_impar(2) == False)
    assert(es_impar(8) == False)
    assert(es_impar(22) == False)
    assert(es_impar(46) == False)
    assert(es_impar(123456) == False)


def test_es_alfanumerico():
    # Casos positivos
    assert(es_alfanumerico("abcde1234") == True)
    assert(es_alfanumerico("asedfoi") == True)
    assert(es_alfanumerico("12334") == True)
    assert(es_alfanumerico("aSRFAEWfadsfsdaf234325445") == True)

    # Casos negativos
    assert(es_alfanumerico("#####") == False)
    assert(es_alfanumerico("dsfdsfdsf$") == False)
    assert(es_alfanumerico("#dsfdsfdsf") == False)
    assert(es_alfanumerico("=dsfdsfdsf") == False)
    assert(es_alfanumerico("123354677|1234") == False)
