from basicmath import div
from basicmath import sortlist
import os

def test_div():
	assert div(4, 2) == 2


def test_div_2():
	assert div(15, 3) == 5


def test_div_for_float():
	assert div(2, 2) == 1


def test_srt():
	
	lst = [2,15,16,0,24,3,25,21]

	l = [0,2,3,15,16,21,24,25]

	assert sortlist(lst) == l




from basicmath import openfile

def test_open():
	filename = "missing-file.txt"
	try:
		openfile(filename)
		raise AssertionError("Expected exception is not thrown")

	except FileNotFoundError:
		pass

