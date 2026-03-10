#1
contains_a = lambda x: x in 'мама'
print(contains_a('а'))
print(contains_a('н'))

#2
long_string = lambda a : len(a) > 12
print(long_string('Hello, world!'))
print(long_string('Hello!'))

#3
end_in_a = lambda s: s[-1] == 'a'
print(end_in_a('Hello, world!'))
print(end_in_a('Whoa'))

#4
even_or_odd = lambda num: 'четное' if num % 2 == 0 else 'нечетное'
print(even_or_odd(23))
print(even_or_odd(78))

#5
multiple_of_th
print(multiple_of_there(12))
print(multiple_of_there(31))

#6
rate_movie = lambda rating: 'Мне понравился этот фильм' if rating > 8.5 else 'Этот фильм был не очень хорошим'
print(rate_movie(2.9))
print(rate_movie(9.1))