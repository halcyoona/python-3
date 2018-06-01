try:
    from a06 import cumulative_marks
except ImportError:
    pass


def test_cumulative_marks_s_1():
    results = [
	('p176118', 'Nauman Ali', 6, 10, 5),
	('p176089', 'Muhammad', 4, 6.7, 4),
	('p176093', 'Qasim Ahmad', 6, 10, 5)
    ]
    results_out = [('17P-6118', 'Nauman Ali', 21),('17P-6089', 'Muhammad', 14.7), ('17P-6093', 'Qasim Ahmad', 21)]

    assert cumulative_marks(results) == results_out

def test_cumulative_marks_s_2():
    results = [
	('p176154', 'Muhammad Shahid Farooq', 2, 3.3, 6),
	('p176173', 'Muhammad Shehroz Khan', None, None, None),
	('p176174', 'Muhammad Sabeeh Hanif', None, None, None)
    ]
    results_out = [('17P-6154', 'Muhammad Shahid Farooq', 11.3), ('17P-6173', 'Muhammad Shehroz Khan', 0),('17P-6174', 'Muhammad Sabeeh Hanif', 0)]

    assert cumulative_marks(results) == results_out


def test_cumulative_marks_s_3():
    results = [
	('p176069', 'Usama Bin', 5),
	('p176072', 'AyeshaAziz', 14.7),
	('p176083', 'Nazakat Ejaz', 21),
	('p176084', 'Khadija Hayat', 21),
	('p176087', 'Sikander Ali', 21),
	('p176094', 'Rida Fatima', 6),
	('p176102', 'Basharat Hussain', 6),
	('p176103', 'Lal Ahsan', 6),
	('p176106', 'Umar Nawaz', 22),
	('p176110', 'Mutahir Hussain', 21),
	('p176113', 'Ahmad Tariq', 6),
	('p176115', 'AbbasIshfaqBabar', 11.3),
	('p176117', 'Muhammad Sarmad', 0),
	('p176119', 'Ammad Amir', 22)
    ]
    results_out = [('17P-6069', 'Usama Bin', 5),('17P-6072', 'AyeshaAziz', 14.7),('17P-6083', 'Nazakat Ejaz', 21),('17P-6084', 'Khadija Hayat', 21),('17P-6087', 'Sikander Ali', 21),('17P-6094', 'Rida Fatima', 6),('17P-6102', 'Basharat Hussain', 6),('17P-6103', 'Lal Ahsan', 6),('17P-6106', 'Umar Nawaz', 22),('17P-6110', 'Mutahir Hussain', 21),('17P-6113', 'Ahmad Tariq', 6),('17P-6115', 'AbbasIshfaqBabar', 11.3),('17P-6117', 'Muhammad Sarmad', 0),('17P-6119', 'Ammad Amir', 22)]

    assert cumulative_marks(results) == results_out


def test_cumulative_marks_s_4():
    results = [
        ('p101111', 'Ali Khayam', None, 78.5, 89, 25, 99),
        ('p101112', 'Mudasser Farooq', 14, 18.5, None, 76),
        ('p101113', 'Tamleek Ali', 87, None, 19.6),
        ('p101114', 'Jawad Mansoor', None, None, None, None)
    ]
    results_out = [('10P-1111', 'Ali Khayam',  291.5), ('10P-1112', 'Mudasser Farooq', 108.5), ('10P-1113', 'Tamleek Ali', 106.6), ('10P-1114', 'Jawad Mansoor', 0)]
    assert cumulative_marks(results) == results_out


def test_cumulative_marks_s_5():
    results = [
        ('p101111', 'Muhammad Amin', None),
        ('p101112', 'Mudasser Farooq', None),
        ('p101113', 'Tamleek Ali'),
        ('p101114', 'Jawad Mansoor', None, None, None, None)
    ]
    results_out = [('10P-1111', 'Muhammad Amin',  0), ('10P-1112', 'Mudasser Farooq', 0), ('10P-1113', 'Tamleek Ali', 0), ('10P-1114', 'Jawad Mansoor', 0)]
    assert cumulative_marks(results) == results_out


def test_cumulative_marks_s_6():
    results = [
        ('p101111', 'Muhammad Amin'),
	('p101112', 'Muhammad Amin'),   
    ]
    results_out = [('10P-1111', 'Muhammad Amin',  0),('10P-1112', 'Muhammad Amin',  0)]
    assert cumulative_marks(results) == results_out




def test_cumulative_marks_i_7():
    results = None
    results_out = None
    assert cumulative_marks(results) == results_out



# output capturing decorator
def capture_output(fn):
    def wrapper(*args, **kwargs):
        import StringIO
        import sys
        orig_stdout = sys.stdout
        capturedOutput = StringIO.StringIO()
        sys.stdout = capturedOutput

        v = fn(*args, **kwargs)

        sys.stdout = orig_stdout # don't rely on __stdout__

        # print 'Captured', capturedOutput.getvalue()
        output_val = capturedOutput.getvalue()
        return v, output_val

    return wrapper
