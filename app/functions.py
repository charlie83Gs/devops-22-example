
import re


def es_par(value):
    return value % 2 == 0


def es_impar(value):
    return value % 2 == 1


def es_alfanumerico(value):
    match = re.findall(re.compile(r"[a-z0-9]", re.IGNORECASE), value)
    return len(value) == len(match)
