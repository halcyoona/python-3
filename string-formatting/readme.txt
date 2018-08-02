
String Formattting is technique which allows you to do variable substitutions and value formatting. This lets you concatenate elements together within a string through positional formatting.


Basic Formatting

Simple positional formatting is probably the most common use-case. Use it if the order of your arguments is not likely to change and you only have very few elements you want to concatenate.

Old technique for string formatting works by putting in one or more replacement field or placeholders — defined by special symbols i.e %s, %d, %r, %f, into a string and using special symbol i.e '%' and variable in paranthesis that have to be replaced in string. %s is used for string , %d is used for digits and %f is used for floats.

New technique for Formatting work by putting in one or more replacement fields or placeholders — defined by a pair of curly braces {} into a string and calling the str.format() method. 


Old: print ('halcyoona loves %s and also %s' % ('linux','mac'))

New: print('halcyoona loves {} and also {}'.format('linux','mac'))

output: halcyoona loves linux and also mac

With new style formatting you can also give explicit positional index inside curly braces {}.

New: print('halcyoona loves {1} and also {0}'.format('linux','mac'))

output: halcyoona loves mac and also linux 

this can not be done in the old technique of formatting.

Padding 

You can add padding on both sides of the string. But in both i.e old and new , method have opposite default padding.let's see this.Padding on left side.

Old: '%15s' % ('halcyoona')

New: '{:>15}'.format('halcyoona')

Output: '      halcyoona'



Padding on right side.

Old: '%-15s' % ('halcyoona')

New: '{:15}'.format('halcyoona')

Output: 'halcyoona      '


In above, we are holding 15 spaces i.e in placeholder, in a string 9 spaces are filled by word "halcyoona" and others are white spaces on either specified side.

This method is not available in old technique of formatting.

New: '{:-<15}'.format('test')

Output: 'halcyoona------'

In this above code space which ever left is filled with dashes "-".

This method is not available in old technique of formatting.

New: '{:^15}'.format('halcyoona')

Output: '   halcyoona   '

In this code, spaces are divided on both side of word.


Truncating long strings
In this long string is cutted to a specified characters. The digit after "."  in placeholder is specifing the character.


Old: '%.5s' % ('halcyoona',)

New: '{:.5}'.format('halcyoona')

Output: 'halcy'


Combining truncating and padding
It is also possible to combine truncating and padding:

Old: '%-10.5s' % ('halcyoona')

New: '{:10.5}'.format('halcyoona')

Output: 'halcy     '



Numbers


x = 12
y = 24

Old: print ("x = %d and y = %d" % (x,y))

New: print('x = {} and y = {}'.format(x,y))

output: x = 12 and y = 24

With new style formatting you can also give explicit positional index inside curly braces {}.

New: print('x = {1} and y = {0}'.format(x,y))

output: x = 24 and y = 12 

this can not be done in the old technique of formatting.

Floats:

Old: '%f' % (3.141592653589793)

New: '{:f}'.format(3.141592653589793)

Output: '3.141593'


In floats, if you give a digit after "." in placeholder that works differently.

Old: '%.10f' % (3.141592653589793)

New: '{:.10f}'.format(3.141592653589793)

Output: '3.1415926536'


Padding Numbers

Similar to strings numbers can also be constrained to a specific width.

Old: '%4d' % (24)

New: '{:4d}'.format(24)

Output: '  24'


Old: '%04d' % (24)

New: '{:04d}' .format(24)

Output: '0024'

Again similar to truncating strings the precision for floating point numbers limits the number of positions after the decimal point.

Old: '%06.2f' % (3.141592653589793)

New: '{:06.2f}'.format(3.141592653589793)

Output: '003.14'

Signed Numbers

By default only negative numbers are prefixed with a sign. This can be changed of course.

Old: '%+d' % (24)

New: '{:+d}'.format(24)

Output: '+24'

This method is not available in old technique of formatting.

New: '{:=5d}'.format((- 24))

Output: '-  24'

New: '{:=+5d}'.format(24)

Output: '+  24'



Named placeholders

Both formatting styles support named placeholders.

data = {'first': 'linux', 'last': 'linux!'}

Old: '%(first)s %(last)s' % data

New: '{first} {last}'.format(**data)

Output: 'linux linux!'


str.format() also accepts keyword arguments.This method is not available in old techhnique of formatting.

New: '{first} {last}'.format(first='linux', last='linux!')

Output: 'linux linux!'


data = [4, 8, 15, 16, 24, 48]

New: '{d[4]} {d[5]}'.format(d=data)

Output: '24 48'


class Plant(object):
    type = 'tree'
    kinds = [{'name': 'good'}, {'name': 'nice'}]

New: '{p.type}: {p.kinds[0][name]}'.format(p=Plant()) 

Output: 'tree: good'


Datetime
This method is not available in old techhnique of formatting.
New style formatting also allows objects to control their own rendering. This for example allows datetime objects to be formatted inline:

from datetime import datetime

New: '{:%Y-%m-%d %H:%M}'.format(datetime(2003, 2, 26, 4, 5))

Output: '2003-02-26 04:05'



Parametrized formats
Additionally, new style formatting allows all of the components of the format to be specified dynamically using parametrization. Parametrized formats are nested expressions in braces that can appear anywhere in the parent format after the colon.
Old style formatting also supports some parametrization but is much more limited. Namely it only allows parametrization of the width and precision of the output.

Old: '%.*s = %.*f' % (3, 'halcyoona', 3, 2.7182)

New: '{:.{prec}} = {:.{prec}f}'.format('halcyoona', 2.7182, prec=3)

Output: 'hal = 2.718'


Old: '%*.*f' % (5, 2, 2.7182)

New: '{:{width}.{prec}f}'.format(2.7182, width=5, prec=2)

Output: ' 2.72'


This method is not available in old techhnique of formatting.

New: '{:{prec}} = {:{prec}}'.format('halcyoona', 2.7182, prec='.3')

Output: 'hal = 2.72'

New: '{:{}{}{}.{}}'.format(2.7182818284, '>', '+', 10, 3)

Output: '     +2.72'

New: '{:{}{sign}{}.{}}'.format(2.7182818284, '>', 10, 3, sign='+')

Output: '     +2.72'

from datetime import datetime
dt = datetime(2003, 2, 26, 4, 5)

New: '{:{dfmt} {tfmt}}'.format(dt, dfmt='%Y-%m-%d', tfmt='%H:%M')

Output: '2003-02-26 04:05'