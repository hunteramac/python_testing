from asyncio.windows_events import NULL
import pytest


from functions import substringsBetween
# test

def test_simpleCase():
    assert substringsBetween("abcd", "a", "d") == ["bc"]

def test_manyStrings():
    assert substringsBetween("abcdabcdab", "a", "d") == ["bc", "bc"]