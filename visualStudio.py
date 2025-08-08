print()

print('I once heard that', 1, '+', 2, '=', 3)

print("Max's favorite number is...")
print()
print(3)

# This code prints some letters of the alphabet
print('A')
print('B')
print('D')  # We skip 'C' on purpose

# Welcome message
print('Welcome message:')
#print("Welcome to coding in Python with TripleTen!")

pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067
print(pi + 1)

person = 'Maxwell'
print(person)

person = 'Maxwell'
print(person)

person = 'Max'
print(person)

pets = 2

My_Var = 'oh hi'
my_var = 'heeey'
print(My_Var)
first_movie_title = 'Firelight'
first_movie_year = 1964

print("Steven Spielberg's first movie was", first_movie_title, "in", first_movie_year) # write your code inside this print() function

# addition
print(1.5 + 10)

# subtraction
print(1.5 - 10)

# multiplication
print(1.5 * 10)

# division
print(1.5 / 10)

# exponentiation
print(1.5 ** 10) # 1.5 to the 10th power

french_speakers = 300.0
german_speakers = 136.3

total_speakers = french_speakers + german_speakers

print("Millions of people who speak French or German:", total_speakers)


english_speakers = 1350# look up the value in the table and put it here
spanish_speakers = 595.1# look up the value in the table and put it here

# write your code here
total_speakers = english_speakers + spanish_speakers
print(total_speakers)

total_italian = 64.9# look up value in the table and put it here
native_italian = 61.6# look up value in the table and put it here

# write your code here
share_native = native_italian/total_italian
print(share_native)

native_japanese = 125.1 # look up value in the table and put it here
native_french = 97.7 # look up value in the table and put it here

# finish your code below here
speaker_diff = native_japanese - native_french
print(speaker_diff)

name_1 = 'Joe'
2_name = 'Mary'

print(name_1)
print(2_name)

language = 'Chinese'
website_share = 0.014
native_speakers = 1310
total_speakers = 1400

print(type(language))
print(type(website_share))
print(type(native_speakers))
# print the data type for total_speakers
print(type(total_speakers))

# strings
ch_language = 'Chinese'
en_language = 'English'

# floats
ch_website_share = 0.014
en_website_share = 0.604

# integers
ch_total_speakers = 1400
en_total_speakers = 1350

print(ch_language + en_language) # add strings
print(ch_website_share + en_website_share) # add floats
print(ch_total_speakers + en_total_speakers) # add integers
print(ch_total_speakers + 1000.00) # add a float to an integer

print(' 123ABC ' * 6)

result = "Chinese is spoken by "  + 1400 + " million people worldwide"

ru_website_share = 0.085
total_sites = 10000000

ru_sites = total_sites * ru_website_share

print(ru_sites)
print(type(ru_sites))


ru_website_share = 0.085
sites = 10000000

ru_sites = sites * ru_website_share
ru_sites = int(ru_sites)
print(ru_sites)
print(type(ru_sites))

my_list = []

print(my_list)
print(type(my_list))
print(len(my_list))

favorite_films = ['The Graduate', 'Reservoir Dogs', 'Fear and Loathing in Las Vegas']

print(favorite_films)
print(type(favorite_films))
print(len(favorite_films))

my_list = ['<3', 77, 3.89, True, False, ['sub', 'list', 0.2]]

print(my_list)
print(len(my_list))

title = 'Fight Club'
year = 1999
genre = ['thriller', 'drama', 'crime']
duration = 139
rating = 8.644

# write your code here
movie_info = [title, year, genre, duration, rating]
print(movie_info)


movie_info = ['Fight Club', 1999, ['thriller', 'drama', 'crime'], 139, 8.644]

print(movie_info[0])
print(type(movie_info[0]))

print(movie_info[2][0])

movie_info = ['Fight Club', 1999, ['thriller', 'drama', 'crime'], 139, 8.644]

print(movie_info[2:4])
print(type(movie_info[2:4]))

movie_info = ['Fight Club', 1999, ['thriller', 'drama', 'crime'], 139, 8.644]

# write your code here
print(movie_info[1:4])


movie_info = ['Fight Club', 1999, ['thriller', 'drama', 'crime'], 139, 8.644]

print(movie_info[:3])

movie_info = ['Fight Club', 1999, ['thriller', 'drama', 'crime'], 139, 8.644]

print(movie_info[2:])

movie_info = ['Fight Club', 1999, ['thriller', 'drama', 'crime'], 139, 8.644]

print(movie_info[-1])
print(movie_info[-2])

movie_info = ['Fight Club', 1999, ['thriller', 'drama', 'crime'], 139, 8.644]

# write your code here
print(movie_info[-4])

title = 'Fight Club'
year = 2999
genre = ['thriller', 'drama', 'crime']
duration = 139
rating = 8.644

movie_info = [title, year, genre, duration, rating]
print(movie_info)

title = 'Fight Club'
year = 2999
genre = ['thriller', 'drama', 'crime']
duration = 139
rating = 8.644

movie_info = [title, year, genre, duration, rating]
print(movie_info)

movie_info[1] = 1999
print(movie_info)

shopping_list = ['kiwi', 'banana', 'apple', 'orange', 'watermelon']

# write your code here
shopping_list[2] = 'orange'
print(shopping_list)

title = 'The Dark Knight'
year = 2008
genre = 'fantasy, action, thriller'
duration = 152
rating = 8.917

dk_info = [title, genre, duration]

print(dk_info, len(dk_info))
print()

dk_info.append(rating)

print(dk_info, len(dk_info))

count = [1, 2, 3, 4, 5, 6]

# write your code here
count.append(7)
print(count)

title = 'The Dark Knight'
year = 2008
genre = 'fantasy, action, thriller'
duration = 152
rating = 8.917

dk_info = [title, genre, duration]
dk_info.append(rating)

print(f"The list {dk_info} has {len(dk_info)} items.")
print()

dk_info.insert(1, year)

print(f"The list {dk_info} has {len(dk_info)} items.")

movies = ['Matrix', 'Matrix 2', 'Matrix 3']
movies.pop()
print(movies)

movies = ['Matrix', 'Matrix 2', 'Matrix 3']

deleted_movie =  movies.pop(1)

print(movies)
print(deleted_movie)

movie_info = ['Fight Club', 2999, ['thriller', 'drama', 'crime'], 139, 8.644]

# write your code here
genre = movie_info.pop(2)
print(movie_info)
print(genre)

years = [1994, 1972, 2008, 1993, 2003, 1994, 1966, 1999, 1962, 1997]

years_sorted = sorted(years)

print(years)
print(years_sorted)

years = [1994, 1972, 2008, 1993, 2003, 1994, 1966, 1999, 1962, 1997]

print(sorted(years, reverse=True))

movies_duration = [142, 175, 152, 195, 201, 154, 178, 139]
movies_duration_sorted = sorted(movies_duration, reverse=True)# finish this line of code

# print the sorted list here
print(movies_duration_sorted)

animals = ['Koala', 'antelope', 'Gibbon', 'Alligator', 'manatee', 'Capybara']

print(sorted(animals))

years = [1994, 1972, 2008, 1993, 2003, 1994, 1966, 1999, 1962, 1997]
print(years)

years.sort()
print(years)

years = [1994, 1972, 2008, 1993, 2003, 1994, 1966, 1999, 1962, 1997]

years.sort(reverse=True)
print(years)

movies_duration = [142, 175, 152, 195, 201, 154, 178, 139]

# write your code here
movies_duration.sort()
print(movies_duration)

phrase = 'Cuckoo builds a nest!'
words = phrase.split()
print(words)

phrase = 'The * stars * are * out * tonight'
words = phrase.split(' *')
print(words)

headers = "date||order_id||product_id||customer_id||quantity||price||shipping_notes"

# write your code here
columns = headers.split('||')
print(columns)

words = ['Max\'s', 'favorite', 'film', 'is', 'The', 'Graduate.']
phrase = ' '.join(words) # forms a string from the elements, separated by spaces
print(phrase)

movie_info = ['Fight Club', 1999, ['thriller', 'drama', 'crime'], 139, 8.644]

# write your code here
genre = ', '.join(movie_info[2])
movie_info[2] = genre
print(movie_info)

movie_info = ('Fight Club', 3999, ['thriller', 'drama', 'crime'], 139, 8.644)

print(movie_info)
print(type(movie_info))
print(len(movie_info))

empty_tuple = ()

print(empty_tuple)
print(len(empty_tuple))

movie_info = ('Fight Club', 3999, ['thriller', 'drama', 'crime'], 139, 8.644)

print(movie_info[2])

movie_info = ('Fight Club', 3999, ['thriller', 'drama', 'crime'], 139, 8.644)

print(movie_info[1:4])
print(type(movie_info[1:4]))
print(len(movie_info[1:4]))


product = 'annual subscription'
price = 139.99
account = 'premium'
profiles = ('Me', 'Kids', 'Stacey')

# write your code here
data = (product, price, account, profiles)
print(data[1])

movie_info = ('Fight Club', 3999, ['thriller', 'drama', 'crime'], 139, 8.644)
movie_info[1] = 1999

print(movie_info)

movie_info = ['Fight Club', 1999, ['thriller', 'drama', 'crime'], 139, 8.644]
print(movie_info)
print(type(movie_info))
print()

movie_info = tuple(movie_info) 
print(movie_info)
print(type(movie_info))

movie_info = ('Fight Club', 1999, ['thriller', 'drama', 'crime'], 139, 8.644)
print(movie_info)
print(type(movie_info))
print()

movie_info = list(movie_info) 
print(movie_info)
print(type(movie_info))

for genre in film_genres:
    print(genre)

film_genres = ['SCIFI', 'drama', 'Thriller', 'comedy', 'Action']

# write your code here
for genre in film_genres:
    print(genre.lower())

for i in range(10):
    print(i)

for i in range(5, 10):
    print(i)

film_genres = ['SCIFI', 'drama', 'Thriller', 'comedy', 'Action']

for i in range(len(film_genres)):
    film_genres[i] = film_genres[i].lower()

print(f"Processed data: {film_genres}")

sales = [100, 200, 150, 175, 300]
total_sales = 0  # Initialize the total sales variable

for sale in sales:
    total_sales = total_sales + sale  # Add each sale to the total

print(f"Total sales for the month: {total_sales}")

numbers = [1, 2, 3, 4, 5]
squared_numbers = []  # Initialize an empty list

for num in numbers:
    squared_numbers.append(num ** 2)  # Add the square of each number to the list

print(f"Squared numbers: {squared_numbers}")

wrong_message = "!emocleW"

message = ''
for letter in wrong_message:
    message = letter + message

print(message)

scores = [61, 99, 72, 87, 80, 95] 

# initialize the sum and counter
total = 0
k = 0

for score in scores:
    k = k + 1
    total = total + score

print(f"The loop executed {k} times.")

scores = [61, 99, 72, 87, 80, 95] 

# initialize the sum and counter
total = 0
k = 0

for score in scores:
    k = k + 1
    total = total + score

print(f"The loop executed {k} times.")

print(True)
print(False)
print(5 < 3)
print('TripleTen' == 'tripleten')
print('TripleTen'.islower())
print('tripleten'.islower())

name = 'Steven'
age = 40

if name == 'Steven' or name == 'Carol' and age <= 30:
    print("Retrieving customer data...")
else:
    print("Cannot find customer data")

    name = 'Steven'
age = 40

if (name == 'Steven' or name == 'Carol') and age <= 30:
    print("Retrieving customer data...")
else:
    print("Cannot find customer data")

print('com' in 'www.gmail.com')    # Output: True
print('com' in 'www.usda.gov')     # Output: False
print(3 in [1, 3, 5, 7, 9])        # Output: True
print(3 in [0, 2, 4, 6, 8])        # Output: False

name = 'Steven'

if name == 'Carol':
    print("Hello again, Carol!")

if name == 'Steven':
    print("Welcome, Steven!")

name = 'Steven'

if name == 'Carol':
    print("Hello again, Carol!")
else:
    print(f"Welcome, {name}!")

age = 16
is_member = True

if age < 12 or age >= 65:
    print("You get a free entry!")
elif age >= 12 and age <= 18 and is_member:
    print("You get a discounted entry!")
else:
    print("You pay the regular entry fee.")


sept_sales = 201922.71

# write your code here
if sept_sales < 30000:
    print("low sales")
elif sept_sales >= 30000 and sept_sales < 100000:
    print("okay sales")
else:
    print("good sales")

temperature = 75
weather = 'sunny'

if temperature > 80:
    if weather == 'sunny':
        print("It's hot and sunny! Wear light clothing.")
    else:
        print("It's hot but not sunny. Stay cool!")
else:
    if weather == 'sunny':
        print("It's a pleasant day. Enjoy the sun!")
    else:
        print("It's cool and not sunny. You might need a light jacket!")


numbers = [5, 20, 15, 3, 10]

for num in numbers:
    if num < 10:
        print(f"{num} is small!")
    elif num < 20:
        print(f"{num} is medium!")
    else:
        print(f"{num} is large!")

words = ['cat', 'elephant', 'dog', 'hippo', 'bee', 'antelope']

# Initialize a counter variable to track how many words were changed
k = 0

# Loop through each index in the words list
for i in range(len(words)):
    # Check if the word's length is less than 5 characters
    if len(words[i]) < 5:
        # If it is, convert the word to uppercase and assign it back to its index in the list
        words[i] = words[i].upper()
        # Increment the counter since we made a change
        k = k + 1

# Print the number of words that were changed and the updated list of words
print(f"There were {k} words with less than 5 characters")
print(words)

words = ['cat', 'elephant', 'dog', 'hippo', 'bee', 'antelope']
k = 0
for i in range(len(words)):
    if len(words[i]) < 5:
        words[i] = words[i].upper()
        k = k + 1

print(f"There were {k} words with less than 5 characters")
print(words)

animals = ['Koala', 'antelope', 'Gibbon', 'Alligator', 'manatee', 'Capybara']

k = 0
for i in range(len(animals)):
    if not animals[i].islower():
        animals[i] = animals[i].lower()
        k = k + 1

print(f"There were {k} animals with uppercase letters")
print(animals)

console_data = [['NES', 'Nintendo', 1985, 1995, 179.0, 61910000],
 ['Game Boy', 'Nintendo', 1989, 2003, 89.99, 118690000],
 ['SNES', 'Nintendo', 1990, 2003, 199.0, 49100000],
 ['Virtual Boy', 'Nintendo', 1995, 1996, 179.95, 770000],
 ['Game Boy Advance', 'Nintendo', 2001, 2010, 99.99, 81510000],
 ['Atari 2600', 'Atari', 1977, 1992, 199.0, 30000000],
 ['Sega Genesis', 'Sega', 1988, 1997, 189.0, 30750000],
 ['Game Gear', 'Sega', 1990, 1997, 149.99, 10620000],
 ['Sega CD', 'Sega', 1991, 1996, 299.0, 2240000],
 ['3DO', 'The 3DO Company', 1993, 1996, 699.99, 2000000],
 ['PlayStation', 'Sony Electronics', 1994, 2006, 299.0, 102490000],
 ['PlayStation 2', 'Sony Electronics', 2000, 2013, 299.0, 155000000]]

# write your code here
for i in console_data:
    print(i)

console_data = [['NES', 'Nintendo', 1985, 1995, 179.0, 61910000],
 ['Game Boy', 'Nintendo', 1989, 2003, 89.99, 118690000],
 ['SNES', 'Nintendo', 1990, 2003, 199.0, 49100000],
 ['Virtual Boy', 'Nintendo', 1995, 1996, 179.95, 770000],
 ['Game Boy Advance', 'Nintendo', 2001, 2010, 99.99, 81510000],
 ['Atari 2600', 'Atari', 1977, 1992, 199.0, 30000000],
 ['Sega Genesis', 'Sega', 1988, 1997, 189.0, 30750000],
 ['Game Gear', 'Sega', 1990, 1997, 149.99, 10620000],
 ['Sega CD', 'Sega', 1991, 1996, 299.0, 2240000],
 ['3DO', 'The 3DO Company', 1993, 1996, 699.99, 2000000],
 ['PlayStation', 'Sony Electronics', 1994, 2006, 299.0, 102490000],
 ['PlayStation 2', 'Sony Electronics', 2000, 2013, 299.0, 155000000]]

# write your code here
print(console_data[-4])
print(console_data[1][-1])

total_sold = 0
for row in console_data:
    total_sold = total_sold + row[-1]
print(total_sold)


nintendo_sold = 0
for row in console_data:
    if row[1] == 'Nintendo':
        nintendo_sold = nintendo_sold + row[-1]
print(nintendo_sold)

early_units_sold = 0

for console in console_data:
    if console[0] == 'PlayStation' or console[1] == 'Sega':
        if console[2] < 1995:
            early_units_sold = console[-1] + early_units_sold

print(early_units_sold)

laptops = {'lenovo': 399.99, 'apple': 749.99, 'hp': 349.99, 'dell': 599.99}

print(laptops)
print(type(laptops))
print(len(laptops))

# write your code here
coffee_stocks = {'SBUX': 120.29, 'DNKN': 106.48, 'BROS': 76.25}
print(coffee_stocks)

laptops = {'lenovo': 399.99, 'apple': 749.99, 'hp': 349.99, 'dell': 599.99}

print(laptops['dell'])

coffee_stocks = {'SBUX': 120.29, 'DNKN': 106.48, 'BROS': 76.25}

# write your code here
print(coffee_stocks['BROS'])

laptops = {'lenovo': 399.99, 'apple': 749.99, 'hp': 349.99, 'dell': 599.99}

print(laptops.items())
print(type(laptops.items()))



laptops = {'lenovo': 399.99, 'apple': 749.99, 'hp': 349.99, 'dell': 599.99}

laptop_items = list(laptops.items())  # Convert dict_items to a list of tuples
print(laptop_items)
print(type(laptop_items))

laptops = {'lenovo': 399.99, 'apple': 749.99, 'hp': 349.99, 'dell': 599.99}

print(laptops.keys())  # Get all the keys
print(type(laptops.keys()))  # Check the data type

laptops = {'lenovo': 399.99, 'apple': 749.99, 'hp': 349.99, 'dell': 599.99}

print(laptops.values())  # Get all the values
print(type(laptops.values()))  # Check the data type

coffee_stocks = {'SBUX': 120.29, 'DNKN': 106.48, 'BROS': 76.25}

# write your code here
values = tuple(coffee_stocks.values())
print(values)

laptops = {'lenovo': 399.99, 'apple': 749.99, 'hp': 349.99, 'dell': 599.99}
print(laptops)

laptops['dell'] = 499.99 # Changing the price of dell laptop from 599.99 to 499.99
print(laptops)

laptops = {'lenovo': 399.99, 'apple': 749.99, 'hp': 349.99, 'dell': 599.99}

laptops['acer'] = 472.99
print(laptops)

coffee_stocks = {'SBUX': 1.2029, 'DNKN': 106.48, 'BROS': 76.25}

# write your code here
coffee_stocks['SJM'] = 159.22
coffee_stocks['SBUX'] = 120.29
print(coffee_stocks)

laptops = {'lenovo': 399.99, 'apple': 749.99, 'hp': 349.99, 'dell': 599.99}

del laptops['apple']
print(laptops)

laptops = {'lenovo': 399.99, 'apple': 749.99, 'hp': 349.99, 'dell': 599.99}

removed_value = laptops.pop('apple')
print(laptops)
print(removed_value)

coffee_stocks = {'SBUX': 120.29, 'DKNN': 106.48, 'BROS': 76.25}

# write your code here
dnkn_price = coffee_stocks.pop('DKNN')
coffee_stocks['DNKN'] = dnkn_price
print(coffee_stocks)
brands = ['lenovo', 'apple', 'hp', 'dell']
models = ['ideapad', 'macbook air', 'hd+', 'inspiron']
sizes = [15.6, 13.3, 17.3, 16.0]
prices = [399.99, 749.99, 349.99, 599.99]

laptop_data = {'brand': brands, 'model': models, 'size': sizes, 'price': prices }
print(laptop_data)

brands = ['lenovo', 'apple', 'hp', 'dell']
models = ['ideapad', 'macbook air', 'hd+', 'inspiron']
sizes = [15.6, 13.3, 17.3, 16.0]
prices = [399.99, 749.99, 349.99, 599.99]

laptop_data = {'brand': brands, 'model': models, 'size': sizes, 'price': prices }

print("The size column:", laptop_data['size'])
print("HP size:", laptop_data['size'][2])

ticker = ['SBUX', 'DNKN', 'BROS']
ath_price = [120.29, 106.48, 76.25]
ath_year = [2021, 2020, 2021]

# write your code here
ath_data = {'company': ticker, 'price': ath_price, 'year': ath_year}
print(ath_data['year'][1])

laptop_data =  [
    {'brand': 'lenovo', 'model': 'ideapad', 'size': 15.6, 'price': 399.99},
    {'brand': 'apple', 'model': 'macbook air', 'size': 13.3, 'price': 749.99},
    {'brand': 'hp', 'model': 'hd+', 'size': 17.3, 'price': 349.99},
    {'brand': 'dell', 'model': 'inspiron', 'size': 16.0, 'price': 599.99}
]

print(laptop_data)

laptop_data =  [
    {'brand': 'lenovo', 'model': 'ideapad', 'size': 15.6, 'price': 399.99},
    {'brand': 'apple', 'model': 'macbook air', 'size': 13.3, 'price': 749.99},
    {'brand': 'hp', 'model': 'hd+', 'size': 17.3, 'price': 349.99},
    {'brand': 'dell', 'model': 'inspiron', 'size': 16.0, 'price': 599.99}
]

print("The third row:", laptop_data[2])
print("HP size:", laptop_data[2]['size'])

def square_and_halve(number):
    result = (number ** 2) / 2
    return result

x = square_and_halve(6)
print(x)

def square_and_halve_list(numbers):
    result_list = []
    for number in numbers:
        result = (number ** 2) / 2
        result_list.append(result)
    return result_list

numbers = [2, 4, 6, 8]
x = square_and_halve_list(numbers)
print(x)

animals = ['Koala', 'antelope', 'Gibbon', 'Alligator', 'manatee', 'Capybara']

def sort_alph(strings):
    result_list = []
    for string in strings:
        result = string.lower()
        result_list.append(result)
    result_list_sorted = sorted(result_list)
    return result_list_sorted

print(sort_alph(animals))

def square_and_halve(number):
    result = (number ** 2) / 2
    return result

x = square_and_halve()
print(x)

def square_and_halve(number=10):
    result = (number **2) / 2
    return result

x = square_and_halve()
print(x)


def replicate(text, n=2):
    return text * n * 2

print(replicate('Hey!'))


asc = sorted([10, 3, 4, 7, 9, 2, 1, 6, 5, 8])
desc = sorted([10, 3, 4, 7, 9, 2, 1, 6, 5, 8], reverse=True)

print(f"Sorts in ascending order by default: {asc}")
print(f"Change flag to sort in descending order: {desc}")

# List of animals
animals = ['Koala', 'antelope', 'Gibbon', 'Alligator', 'manatee', 'Capybara']

#Function to sort animals and optionally change their case
def sort_animals(animals_list, lowercase=True):
    sorted_animals = []

    if lowercase:
        for animal in animals_list:
            sorted_animals.append(animal.lower())
    else:
        sorted_animals = animals_list[:]

    sorted_animals = sorted(sorted_animals)

    return sorted_animals

sorted_lowercase = sort_animals(animals)
sorted_original_case = sort_animals(animals, lowercase=False)

print(sorted_lowercase)
print(sorted_original_case)

sorted([3, 9, 6], reverse=False)

def division(numerator, demoninator):
    result = numerator / demoninator
    print(result)

division(10, 2)


def division(numerator, denominator): 
    result = numerator / denominator
    print(result)


division(numerator=10, denominator=2)
division(denominator=2, numerator=10)

def division(numerator, demoninator):
    result = numerator / denominator
    print(result)

division(10, denominator=2)

def square(num):
    return num * num

result = square(4)
print(result)



def square_and_cube(num):
    square = num * num
    cube = num * num * num
    return square, cube

sqr, cub = square_and_cube(3)

print(f"Square: {sqr}, Cube: {cub}")

def check_sign(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Call the function with different values
print(check_sign(10))  # Positive
print(check_sign(-5))  # Negative
print(check_sign(0))   # Zero

def analyze_number(num):
    # Your code here
    if num > 0:
        square = num * num
        cube = num * num * num
        return "positive", square, cube
    elif num < 0:
        square = num * num
        cube = num * num * num
        return "negative", square, cube
    else:
        square = num * num
        cube = num * num * num
        return "zero", square, cube

'a-b-c-d'.split('-')
{'a': 2, 'b': 4, 'c': 8}.keys()
' || '.join(['a', 'b', 'c', 'd'])

import pandas

import pandas as pd

# Create a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
}


df = pd.DataFrame(data)
print(df)

import pandas as pd
df = pd.read_csv('/datasets/music_log.csv')

import pandas as pd
df = pd.read_csv('/datasets/music_log.csv')
print(df.dtypes)
print(df.columns)
print(df.shape)
df.info()

import pandas as pd

df = pd.read_csv('/datasets/music_log.csv')
result = df.loc[4, 'genre']
print(result)

df.loc[7,'genre']
df.loc[:,'genre']
df.loc[:,['Artist','genre']]
df.loc[:,'user_id':'genre']
df.loc[1]
df.loc[1:]
df.loc[:3]
df.loc[2:5]

#Slices don’t include the end of the range
#You can’t address a single cell or row
df['genre']
df[['genre','Artist']]
df[1:]
df[:3]
df[2:5]

import pandas as pd

info = [
    ['Chicago', 'the United States'],
    ['Boston', 'the United States'],
    ['New York City', 'the United States'],
    ['Paris', 'France'],
    ['Rome', 'Italy'],
    ['Venice', 'Italy'],
    ['Milan', 'Italy'],
    ['Madrid', 'Spain'],
    ['Barcelona', 'Spain']
]

titles = ['city', 'country']

cities_df = pd.DataFrame(data=info, columns=titles)
print(cities_df)
cities_df['country'] == 'Italy'
cities_of_italy = cities_df[cities_df['country'] == 'Italy']
print(cities_of_italy)

italy_count = len(cities_df[cities_df['country'] == 'Italy'])
print(f"Number of Italian cities: {italy_count}")

non_italy_cities = cities_df[cities_df['country'] != 'Italy']
print("Non-Italian cities:")
print(non_italy_cities)

import pandas as pd
df = pd.read_csv('/datasets/music_log.csv')
print(df.head())
print(f"\nDataset shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")

import pandas as pd
df = pd.read_csv('/datasets/music_log.csv')
jazz_df = df[df['genre'] == 'jazz']
print(f"Found {len(jazz_df)} jazz tracks")
print(jazz_df.head())

import pandas as pd
df = pd.read_csv('/datasets/music_log.csv')
high_total_play_df = df[df['total play'] > 90]
print(f"Tracks with > 90 total play: {len(high_total_play_df)}")
print(high_total_play_df.head())

import pandas as pd
df = pd.read_csv('/datasets/music_log.csv')
step1 = df[df['total play'] >= 80]
step2 = step1[step1['total play'] <= 130]
jazz_moderate_play = step2[step2['genre'] == 'jazz']

print(f"Jazz tracks with 80-130 total play: {len(jazz_moderate_play)}")
print(jazz_moderate_play.head())

import pandas as pd
df = pd.read_csv('/datasets/music_log.csv')

jazz_moderate_play = df[
    (df['genre'] == 'jazz') &
    (df['total play'] >= 80) &
    (df['total play'] <= 130)
]

print(f"Jazz tracks with 80-130 total play: {len(jazz_moderate_play)}")
print(jazz_moderate_play.head())


import pandas as pd

df = pd.read_csv('/datasets/music_log.csv')
print(type(df))

part_df = df[['genre', 'Artist', 'total play']]
print(type(part_df))
print(part_df.head())



import pandas as pd
df = pd.read_csv('/datasets/music_log.csv')
part_df = df['Artist']
print(type(part_df))

series_x = df['column_x']

import pandas as pd
df = pd.read_csv('/datasets/music_log.csv')
artist = df['Artist']
print(artist[0])

#In a list of dictionaries, you indicate the list index first, then the dictionary key
list_of_dicts[0]["key"]
#The reverse is true for a dictionary of lists: first comes the key, then the index
dict_of_lists["key"][0]

total_play.loc[total_play <= 10]

Rename these three columns in df:

- '  user_id' → 'user_id'
- 'total play' → 'total_play'
- 'Artist' → 'artist'

import pandas as pd
df = pd.DataFrame({"old_name": [1, 2, 3]})
df = df.rename(columns={"old_name": "new_name"})


import pandas as pd

df = pd.read_csv('/datasets/music_log.csv')

# write your code here
df.rename(columns={'  user_id': 'user_id','total play':'total_play', 'Artist':'artist'}, inplace=True)
print(df.columns)

import pandas as pd
df = pd.read_csv('/datasets/movies_and_shows.csv')
df.head()
df.info()

--  ------        --------------  -----  
 0      name       85579 non-null  object 
 1   Character     85579 non-null  object 
 2   r0le          85579 non-null  object 
 3   TITLE         85578 non-null  object 
 4     Type        85579 non-null  object 
 5   release Year  85579 non-null  int64  
 6   genres        85579 non-null  object 
 7   imdb sc0re    80970 non-null  float64
 8   imdb v0tes    80853 non-null  float64
dtypes: float64(2), int64(1), object(6)
memory usage: 5.9+ MB

df.loc[85576, ['name']]

# Correct the name
df.loc[85576, 'name'] = 'Ines Prieto'

# Verify the correction
print(df.loc[85576, ['name']])

#Filter rows where the 'name' column is 'Ines Prieto'
filtered_df = df[df['name'] == 'Ines Prieto']

#Select only the specified columns
result = filtered_df[['title', 'release_year', 'imdb_score', 'genres']]

# Filter for movies with an IMDb score above 9.0
high_score_titles = df[df['imdb_score'] > 9.0]


# Extract the 'title' column from the filtered DataFrame
title_series = high_score_titles['title']

# Get a unique set of titles
unique_titles = set(title_series)

# Print the unique titles
print(unique_titles)

# Define the function
def get_unique_top_movies(min_score):
    # Filter for movies with IMDb score above min_score
    high_score_df = df[df['imdb_score'] >= min_score]

    # Extract the 'title' column
    high_score_titles = high_score_df['title']

    # Remove duplicate titles
    unique_titles = set(high_score_titles)

    # Return unique titles
    return unique_titles

# Define the function
def get_top_movies_from_decade(decade_start, min_score):
    # Filter for movies released within the decade
    decade_df = df[(df['release_year'] >= decade_start) & (df['release_year'] < decade_start + 9)]


    # Further filter by IMDb score
    high_score_df = decade_df[decade_df['imdb_score'] >= min_score]

    # Extract and remove duplicate titles
    unique_titles = set(high_score_df['title'])

    # Return unique titles
    return unique_titles

# Define the function
def get_actors_for_title(title):
    # Filter for rows with the specified title and role as 'ACTOR'
    actors_df = df[(df['title'] == title) & (df['role'] == 'ACTOR')]

    # Extract the 'name' column for actor names
    actor_series = actors_df['name']

    # Combine names into a single string
    actors_string = ', '.join(actor_series)

    # Return the result
    return actors_string


# Define the function
def categorize_imdb_score(title):
    # Filter for the row with the specified title
    title_df = df[df['title'] == title]
    # Check if title exists
    if title_df.empty:
        return "Title not found"

    # Retrieve the IMDb score for the movie
    score = title_df['imdb_score'].iloc[0]

    # Categorize score using if-else and return the ranking accordingly
    if score >= 9.0:
        return "Excellent"
    elif 7.0 <= score <= 8.9:
        return "Good"
    elif 5.0 <= score <= 6.9:
        return "Average"
    else:
        return "Low"

import pandas as pd

df = pd.read_csv('/datasets/movies_and_shows.csv')

df.head()

df.info()

df.rename(columns={'  name': 'name',
                   '  Type': 'type',
                   'TITLE': 'title',
                   'release Year': 'release_year',
                   'imdb sc0re': 'imdb_score',
                   'imdb v0tes': 'imdb_votes',
                   'r0le': 'role'
                   }, inplace=True)
print(df.columns)

print(df.loc[85576, ['name']])

df.loc[85576, 'name'] = 'Ines Prieto'

print(df.loc[85576, ['name']])

filtered_df = df[df['name'] == 'Ines Prieto']
result = filtered_df[['title', 'release_year', 'imdb_score', 'genres']]

high_score_titles = df[df['imdb_score'] > 9.0]
title_series = high_score_titles['title']
unique_titles = set(title_series)
print(unique_titles)

def get_unique_top_movies(min_score):
    high_score_df = df[df['imdb_score'] >= min_score]
    high_score_titles = high_score_df['title']
    unique_titles = set(high_score_titles)
    return unique_titles
print(get_unique_top_movies(9.0))

def get_top_movies_from_decade(decade_start, min_score):
    decade_df = df[(df['release_year'] >= decade_start) & df['release_year' < decade_start + 9]]
    high_score_df = decade_df[decade_df['imdb_score'] >= min_score]
    unique_titles = set(high_score_df['title'])
    return unique_titles

print(get_top_movies_from_decade(1990, 8.5))

def get_actors_for_title(title):
    actors_df = df[(df['title'] == title) & (df['role'] == 'ACTOR')]
    actor_series = actors_df['name']
    actors_string = ', '.join(actor_series)
    return actors_string

print(get_actors_for_title("Taxi Driver"))

def categorize_imdb_score(title):
    title_df = df[df['title'] == title]
    if title_df.empty:
        return "Title not found"
    score = title_df['imdb_score'].iloc[0]

    if score >= 9.0:
        return "Excellent"
    elif 7.0 <= score <= 8.9:
        return "Good"
    elif 5.0 <= score <= 6.9:
        return "Average"
    else:
        return "Low"

print(categorize_imdb_score("Taxi Driver"))

df = pd.read_csv('data.csv', sep="|")

df = pd.read_csv('data.csv', names=['birth_year', 'gender', 'score'])

df = pd.read_csv('data.csv', header=None)
df = df.rename(columns={0: 'birth_year',
                        1: 'gender',
                        2: 'score'
                        })

df = pd.read_csv('data.csv', names=['birth_year', 'gender', 'score', 'average_points'], decimal=',')

import pandas as pd
column_names = [
    'country',
    'name',
    'capacity_mw',
    'latitude',
    'longitude',
    'primary_fuel',
    'owner'
]

data = pd.read_csv(
    '/datasets/gpp_modified.csv',
    sep='|', 
    header=None, 
    names=column_names,
    decimal=',',
)
print(data.head())

The data from the quizzes above has been saved in /datasets/letters_colors_decimals.csv, but the separator has been changed to $.

Read it so that:

The first row becomes the header.
Columns are separated correctly.
Decimals are read correctly.

letters;colors;decimals
a;yellow;1a2
b;red;1a3
c;cyan;1a4

import pandas as pd
df = pd.read_csv('/datasets/letters_colors_decimals.csv',
                 sep='$',
                 decimal='a',
)

print(df)

import pandas as pd
df = pd.read_excel('/datasets/product_reviews.xlsx',
                   sheet_name='reviewers',
)
print(df.head())

import pandas as pd

# write your code here
df_categories = pd.read_excel('/datasets/product_reviews.xlsx',
                              sheet_name='product_categories',
)

print(df_categories)

import pandas as pd
column_names = [
    'country',
    'name',
    'capacity_mw',
    'latitude',
    'longitude',
    'primary_fuel',
    'owner',
]

data = pd.read_csv(
    '/datasets/gpp_modified.csv',
    sep='|',
    header=None,
    names=column_names,
    decimal=',',
)

data.info()
print(data.head())

print(data.head(10))

print(data.sample(5))

print(data.sample(5, random_state=1369))

import pandas as pd

column_names = [
    'country',
    'name',
    'capacity_mw',
    'latitude',
    'longitude',
    'primary_fuel',
    'owner'
]
data = pd.read_csv(
    '/datasets/gpp_modified.csv',
    sep='|',
    header=None,
    names=column_names,
    decimal=',',
)

print(data.head())
print()

# write your code here
print(data.sample(5, random_state=543210))

import pandas as pd
column_names = [
    'country',
    'name',
    'capacity_mw',
    'latitude',
    'longitude',
    'primary_fuel',
    'owner'
]

data = pd.read_csv(
    '/datasets/gpp_modified.csv',
    sep='|',
    header=None,
    names=column_names,
    decimal=',',
)

print(data.describe())
print(data['capacity_mw'].describe())
print(data['country'].describe())
print(data.describe(include='object'))
print(data.describe(include='all'))

import pandas as pd

column_names = [
    'country',
    'name',
    'capacity_mw',
    'latitude',
    'longitude',
    'primary_fuel',
    'owner'
]
data = pd.read_csv(
    '/datasets/gpp_modified.csv',
    sep='|',
    header=None,
    names=column_names,
    decimal=',',
)

# write your code here
print(data['primary_fuel'].describe())

import pandas as pd

df_logs = pd.read_csv('/datasets/visit_log.csv')

# write your code here
df_logs.info()
print(df_logs.isna().sum())

import pandas as pd

df_logs = pd.read_csv('/datasets/visit_log.csv')
print(df_logs['source'].value_counts(dropna=False))

There are many ways to find and count missing values in pandas. You learned three ways in this lesson:

Calling info() on a DataFrame
Calling isna().sum() on a DataFrame or Series
Calling value_counts(dropna=False) on a Series

import pandas as pd
df_logs = pd.read_csv('/datasets/visit_log.csv')
df_emails = df_logs[~df_logs['email'].isna()]
print(df_emails.head(10))

import pandas as pd
df_logs = pd.read_csv('/datasets/visit_log.csv')
df_emails = df_logs[df_logs['email'].isna() & df_logs['source'].isna()]

print(df_emails)

DataFrame['column_name'].fillna(value, inplace=False)

df_logs['email'] = df_logs['email'].fillna(value='')
print(df_logs.head())

DataFrame['column_name'].fillna(value=DataFrame['column_name'].mode()[0], inplace=False)

import pandas as pd

analytics_data = pd.read_csv('/datasets/web_analytics_data.csv')
print(analytics_data.head(10))

import pandas as pd

# Example DataFrame
data = {'Salary': [30000, 30000, 30000, 30000, 90000]}

df = pd.DataFrame(data)

median_salary = df['Salary'].median()
print("Median Salary: ", median_salary)

age_median = analytics_data['age'].median()
analytics_data['age'].fillna(value=age_median, inplace=True)
analytics_data.info()

# write your code here
import pandas as pd
df_students = pd.read_csv('/datasets/student_scores.csv')
print(df_students.head(5))

import pandas as pd
df = pd.DataFrame({'col_1': ['A', 'B', 'A', 'A'], 'col_2': [1, 2, 2, 1]})

print(df)
print(df.duplicated())
print(df.duplicated().sum())

import pandas as pd
df = pd.DataFrame({'col_1': ['A', 'B', 'A', 'A'], 'col_2': [1, 2, 2, 1]})

print(df)
print(df['col_1'].value_counts())

print(df.drop_duplicates())
print(df.drop_duplicates(subset='col_1'))

duplicate_count = df_students.duplicated().sum()
print(f"Number of duplicate rows: {duplicate_count}")

import pandas as pd

# Load the dataset
df_students = pd.read_csv('/datasets/student_scores.csv')

# Remove duplicate rows
df_students = df_students.drop_duplicates()

# Count duplicate rows after removal
remaining_duplicates = df_students.duplicated().sum()

# Print the count of remaining duplicate rows
print(f"Number of duplicate rows after cleaning: {remaining_duplicates}")

import pandas as pd
import numpy as np
import plotly.express as px

cases = [33, 61, 86, 112, 116, 129, 192, 174, 344, 304, 327, 246, 320, 339, 376]

dates = ['March<br>'] * len(cases)
day = 18
for i in range(len(dates)):
    dates[i] = dates[i] + str(day)
    day = day + 1
dates[-1] = 'April<br>1'

labels = dict(date="Date", cases="Number of cases")
markers = dict(size=30, line=dict(width=2, color='black'), color='white')
title = dict(text='New Cases Per Day', font=dict(color='white', size=30))
yaxis = dict(tickmode='linear', tick0=30, dtick=30)

df = pd.DataFrame({'cases': cases, 'date': dates})

fig = px.line(df, y='cases', x='date', text='cases', markers=True, labels=labels, title="New Cases Per Day")

fig.update_xaxes(showgrid=False, color='white', tickangle=0)
fig.update_yaxes(color='white', gridcolor='#5c5a5c', gridwidth=2, range=[15, 400])
fig.update_traces(marker=markers, line_color='white', line_width=6)
fig.update_layout(title=title,
                  title_x=0.5,
                  paper_bgcolor='#070230',
                  plot_bgcolor='#070230',
                  yaxis=yaxis,
                  xaxis_type='category')
fig.add_annotation(text='TOTAL CASES', 
                    align='right',
                    showarrow=False,
                    font=dict(color='white', size=12),
                    xref='paper',
                    yref='paper',
                    x=1.08,
                    y=1.25)
fig.add_annotation(text='3,342', 
                    align='right',
                    showarrow=False,
                    font=dict(color='white', size=23),
                    xref='paper',
                    yref='paper',
                    x=1.071,
                    y=1.2)

fig.show()

Creating Figures in Python with matplotlib
In the precode, we have provided import statements for pandas and Matplotlib’s pyplot, as well as created a DataFrame for you in the variable df. Using the plot() method from pandas, create a plot of column 'a' against column 'c' from df that has the following attributes:

The title “A vs C” (case is important)
A star marker style (you can use '*' to achieve this)
Markers colored hot pink (use the new parameter, color=, for this with argument 'hotpink')
Figure size of 5 inches by 5 inches
X-axis range from 0 to 12
Y-axis range from 1 to 6
X-axis labeled “C”
Y-axis labeled “A”
Don’t forget to include plt.show() after you call plot()!


import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame({'a': [2, 3, 4, 5], 'b': [4, 9, 16, 25], 'c': [1, 3, 6, 10]})

#scatterplot of a vs c
df.plot(x='c', y='a', kind='scatter', marker='*', color='hotpink', title='A vs C', figsize=(5, 5),)
#set axis ranges and labels
plt.xlim(0, 12)
plt.ylim(1, 6)
plt.xlabel('C')
plt.ylabel('A')

plt.show()

import pandas as pd
df = pd.read_csv('/datasets/visit_log.csv')
print(df.head())
print()
df.info()

print(df.describe())
df.plot(x='height', y='weight')
plt.show()

df.sort_values('height').plot(x='height', y='weight')
plt.show()

df.plot(x='height', y='weight', style='o')
plt.show()

df.plot(x='height', y='weight', kind='scatter')

he adult height and weight data has been read into the variable df for you in the precode. Use the kind='scatter' argument to create a scatterplot of 'height' against 'age' with this DataFrame. Give the plot the following attributes:

The title “Adult heights” (case is important)
Alpha value of 0.36
Figure size of 8 inches by 6 inches
X axis labeled “Age / years”
Y axis labeled “Height / inches”
Don’t forget to include plt.show().

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('/datasets/height_weight.csv')

# write your code here
df.plot(x='age', 
        y='height', 
        kind='scatter', 
        title='Adult heights', 
        alpha=0.36,
        figsize=[8,6],
        xlabel='Age / years',
        ylabel='Height / inches')
plt.show()

print(df['height'].corr(df['weight']))


import pandas as pd

df = pd.read_csv('/datasets/height_weight.csv')

# write your code here
ah_corr = df['height'].corr(df['age'])
print(ah_corr)

import pandas as pd

df = pd.read_csv('/datasets/height_weight.csv')

# write your code here
print(df.corr())


pd.plotting.scatter_matrix(df, figsize=(9,9))

import pandas as pd

df = pd.read_csv('/datasets/height_weight.csv')

# write your code here
corr_mat = df.corr()
#Extract correlation coefficients for 'male' with other columns
male_corr = corr_mat.loc['male', corr_mat.columns != 'male']
print(male_corr)

df.sort_values('height').plot(x='height', y='weight')

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('/datasets/sbux.csv')

df.plot(x='date',
        y='open',
        legend=False,
        title='Starbucks market open',
        xlabel='Date',
        ylabel='Share price / USD',
        rot=45)
plt.show()

Titled “Historic SBUX volume” (case is important)
X-axis labeled “Date”
Y-axis labeled “Volume”
X-axis tick labels rotated 50 degrees
Y-axis range from 1 million to 70 million (i.e. 1e6 and 7e7)
No legend

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('/datasets/sbux.csv')

# write your code here
df.plot(x='date',
        y='volume',
        xlabel='Date',
        ylabel='Volume',
        title='Historic SBUX volume',
        rot=50,
        legend=False,
        ylim=[1e6,7e7])
plt.show()

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('/datasets/sbux.csv')
cols = ['open', 'close']

# write your code here
df.plot(x='date',
        y=cols,
        xlabel='Date',
        ylabel='Share price / USD',
        rot=50,
        title='Historic SBUX price',)
plt.show()

df.plot(x='year', kind='bar')
plt.show()

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('/datasets/west_coast_pop.csv')

df.plot(x='year',
        kind='bar',
        title='West Coast Population',
        xlabel='Year',
        ylabel='Population / millions')

plt.legend(['CA', 'OR', 'WA'], loc='upper left')
plt.show()

Includes only data for Oregon and Washington
Titled “Pacific Northwest population growth” (case is important)
X axis labeled “Year”
Y axis labeled “Population (millions)”
Legend with labels “OR” and “WA” for Oregon and Washington populations, respectively

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('/datasets/west_coast_pop.csv')

# write your code here
print(df.describe())
cols = ['or_pop', 'wa_pop']

df.plot(x='year',
        y=cols,
        kind='bar',
        title='Pacific Northwest population growth',
        xlabel='Year',
        ylabel='Population (millions)',)

plt.legend(['OR','WA'], loc='upper left')
plt.show()


df.hist()
plt.show()

df.plot(kind='hist')
plt.show()

df.hist(column='height')
plt.show()

df['height'].hist(bins=30)
plt.show()

df['height'].plot(kind='hist', bins=30)
plt.show()

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('/datasets/height_weight.csv')

df[df['male'] == 1]['height'].plot(kind='hist', bins=30)
df[df['male'] == 0]['height'].plot(kind='hist', bins=30, alpha=0.8)
plt.legend(['Male','Female'])
plt.show()

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('/datasets/height_weight.csv')

# partition df into separate data frames based on age
df_20s = df[df['age'] < 30]
df_30s = df[(df['age'] >= 30) & (df['age'] < 40)]
df_40s = df[df['age'] >= 40]

# print out the results
print("Sum of data frame lengths:", len(df_20s) + len(df_30s) + len(df_40s)) # finish this line of code)
print("Min and max age for df_20s:", df_20s['age'].min(), df_20s['age'].max()) # finish this line of code)
print("Min and max age for df_30s:", df_30s['age'].min(), df_30s['age'].max())# finish this line of code)
print("Min and max age for df_40s:", df_40s['age'].min(), df_40s['age'].max())# finish this line of code)

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('/datasets/height_weight.csv')

df_20s = df[df['age'] < 30]
df_30s = df[(df['age'] >= 30) & (df['age'] < 40)]
df_40s = df[df['age'] >= 40]

# write your code here
df_20s['weight'].plot(kind='hist',
                      bins=20,
                      title="Weight / lbs",
                      ylabel="Frequency")
df_30s['weight'].plot(kind='hist',
                      bins=20, 
                      alpha=0.6)
df_40s['weight'].plot(kind='hist',
                      bins=20, 
                      alpha=0.3)

plt.legend(['20s', '30s', '40s'])
plt.show()

import pandas as pd

oceans = pd.Series(['Pacific', 'Atlantic', 'Indian', 'Arctic', 'Southern'])

print(oceans)

print(oceans.index)
print(type(oceans.index))

import pandas as pd

oceans = pd.Series(['Pacific', 'Atlantic', 'Indian', 'Arctic', 'Southern'])

oceans.index = [1, 2, 3 , 4, 5]

print(oceans.index)
print(type(oceans.index))

import pandas as pd

oceans = pd.Series(['Pacific', 'Atlantic', 'Indian', 'Arctic', 'Southern'], index=[1, 2, 3, 4, 5])

print(oceans.index)
print(type(oceans.index))

import pandas as pd

oceans = pd.Series(['Pacific', 'Atlantic', 'Indian', 'Arctic', 'Southern'], index=['A', 'B', 'C', 'D', 'E'])

print(oceans)
print()
print(oceans.index)
print(type(oceans.index))

import pandas as pd

states  = ['Alabama', 'Alaska', 'Arizona', 'Arkansas']
flowers = ['Camellia', 'Forget-me-not', 'Saguaro cactus blossom', 'Apple blossom']
insects = ['Monarch butterfly', 'Four-spotted skimmer dragonfly', 'Two-tailed swallowtail', 'European honey bee']
index   = ['state 1', 'state 2', 'state 3', 'state 4']

df = pd.DataFrame({'state': states, 
                   'flower': flowers, 
                   'insect': insects}, 
                   index=index)
print(df)

print(df.loc['state 4', 'insect'])

import pandas as pd

states  = ['Alabama', 'Alaska', 'Arizona', 'Arkansas']
flowers = ['Camellia', 'Forget-me-not', 'Saguaro cactus blossom', 'Apple blossom']
insects = ['Monarch butterfly', 'Four-spotted skimmer dragonfly', 'Two-tailed swallowtail', 'European honey bee']
index   = ['state 1', 'state 2', 'state 3', 'state 4']

df = pd.DataFrame({'state': states, 
                   'flower': flowers, 
                   'insect': insects}, 
                   index=index)

# write your code here
result_df = df.loc[df['state'].isin(['Alabama', 'Arizona']), ['flower', 'insect']]

print(result_df)

import pandas as pd

states  = ['Alabama', 'Alaska', 'Arizona', 'Arkansas']
flowers = ['Camellia', 'Forget-me-not', 'Saguaro cactus blossom', 'Apple blossom']
insects = ['Monarch butterfly', 'Four-spotted skimmer dragonfly', 'Two-tailed swallowtail', 'European honey bee']
index   = ['state 1', 'state 2', 'state 3', 'state 4']

df = pd.DataFrame({'state': states, 'flower': flowers, 'insect': insects}, index=index)

# write your code here
result_series = df.loc[df['state'] != 'Alabama', 'insect']

print(result_series)

import pandas as pd

states  = ['Alabama', 'Alaska', 'Arizona', 'Arkansas']
flowers = ['Camellia', 'Forget-me-not', 'Saguaro cactus blossom', 'Apple blossom']
insects = ['Monarch butterfly', 'Four-spotted skimmer dragonfly', 'Two-tailed swallowtail', 'European honey bee']
index   = ['state 1', 'state 2', 'state 3', 'state 4']

df = pd.DataFrame({'state': states, 
                   'flower': flowers, 
                   'insect': insects}, 
                   index=index)

print(df)
print()
print(df.iloc[3,2])  # Accessing the insect of state 4 using iloc
print(df.iloc[2,1])  # Accessing the flower of state 3 using iloc
print(df.iloc[0,0])  # Accessing the state of state 1 using iloc
print(df.iloc[[0,2], 1:])

df = df.set_index('state')
print(df)
print()
print(df.index)

df.index.name = None
print(df)
print()
print(df.index)

import pandas as pd

states  = ['Alabama', 'Alaska', 'Arizona', 'Arkansas']
flowers = ['Camellia', 'Forget-me-not', 'Saguaro cactus blossom', 'Apple blossom']
insects = ['Monarch butterfly', 'Four-spotted skimmer dragonfly', 'Two-tailed swallowtail', 'European honey bee']
index   = ['state 1', 'state 2', 'state 3', 'state 4']

df = pd.DataFrame({'state': states, 'flower': flowers, 'insect': insects}, index=index)
df = df.set_index('state')

# write your code here
flowers_series = df.loc['Alabama': 'Arizona', 'flower']
flowers_series = df.iloc[:3, df.columns.get_loc('flower')]
print(flowers_series)

import pandas as pd

df = pd.read_csv('/datasets/vg_sales.csv')

print(df.head())
print()
df.info()

mask = df['jp_sales'] >= 1
print(df[mask][['name', 'jp_sales']])
print(df.query('jp_sales >= 1')[['name', 'jp_sales']])
print(df.query("publisher == 'Nintendo'")[['name', 'publisher']].head())

import pandas as pd

df = pd.read_csv('/datasets/vg_sales.csv')

cols = ['name', 'publisher', 'developer']

# write your code here
df_filtered = df.query('publisher == developer')[cols]
print(df_filtered.head())

handhelds = ['3DS', 'DS', 'GB', 'GBA', 'PSP']
print(df[df['platform'].isin(handhelds)][['name', 'platform']].head())
print(df.query("platform in @handhelds")[['name', 'platform']])

import pandas as pd

df = pd.read_csv('/datasets/vg_sales.csv')

# write your code here
print(df['genre'].unique())

import pandas as pd

df = pd.read_csv('/datasets/vg_sales.csv')

cols = ['name', 'genre']
s_genres = ['Shooter', 'Simulation', 'Sports', 'Strategy']

# write your code here
df_filtered = df[~df['genre'].isin(s_genres)][cols]
print(df_filtered)

import pandas as pd

df = pd.read_csv('/datasets/vg_sales.csv')

cols = ['name', 'genre']
s_genres = ['Shooter', 'Simulation', 'Sports', 'Strategy']

# write your code here
df_filtered = df.query('genre not in @s_genres')[cols]
print(df_filtered)

import pandas as pd

our_list = [2, 5, 10]
df = pd.DataFrame(
    {
        'a': [2, 3, 10, 11, 12],
        'b': [5, 4, 3, 2, 1],
        'c': ['X', 'Y', 'Y', 'Y', 'Z'],
    }
)
print(df)
print()
print(our_list)
print()
print(df.query("a in @our_list"))

import pandas as pd

our_dict = {0: 10, 3: 11, 12: 12}
df = pd.DataFrame(
    {
        'a': [2, 3, 10, 11, 12],
        'b': [5, 4, 3, 2, 1],
        'c': ['X', 'Y', 'Y', 'Y', 'Z'],
    }
)
print(df)
print()
print(our_dict)
print()
print(df.query("a in @our_dict.values()"))

import pandas as pd

our_dict = {0: 10, 3: 11, 12: 12}
df = pd.DataFrame(
    {
        'a': [2, 3, 10, 11, 12],
        'b': [5, 4, 3, 2, 1],
        'c': ['X', 'Y', 'Y', 'Y', 'Z'],
    }
)
print(df)
print()
print(our_dict)
print()
print(df.query("a in @our_dict"))

import pandas as pd

our_series = pd.Series([10, 11, 12])
df = pd.DataFrame(
    {
        'a': [2, 3, 10, 11, 12],
        'b': [5, 4, 3, 2, 1],
        'c': ['X', 'Y', 'Y', 'Y', 'Z'],
    }
)
print(df)
print()
print(our_series)
print()
print(df.query("a in @our_series"))

import pandas as pd

our_series = pd.Series([10, 11, 12], index=['X', 'Y', 'T'])
df = pd.DataFrame(
    {
        'a': [2, 3, 10, 11, 12],
        'b': [5, 4, 3, 2, 1],
        'c': ['X', 'Y', 'Y', 'Y', 'Z'],
    }
)

# write your code here
print(df.query("c in @our_series.index"))

import pandas as pd

df = pd.DataFrame(
    {
        'a': [2, 3, 10, 11, 12],
        'b': [5, 4, 3, 2, 1],
        'c': ['X', 'Y', 'Y', 'Y', 'Z'],
    }
)
our_df = pd.DataFrame(
    {
        'a1': [2, 4, 6],
        'b1': [3, 2, 2],
        'c1': ['A', 'B', 'C'],
    },
    index=['Z', 'X', 'P']
)

print(df)
print()
print(our_df)
print()
print(df.query("c in @our_df.index"))

import pandas as pd

df = pd.DataFrame(
    {
        'a': [2, 3, 10, 11, 12],
        'b': [5, 4, 3, 2, 1],
        'c': ['X', 'Y', 'Y', 'Y', 'Z'],
    }
)
our_df = pd.DataFrame(
    {
        'a1': [2, 4, 6],
        'b1': [3, 2, 2],
        'c1': ['A', 'B', 'C'],
    },
    index=['Z', 'X', 'P']
)

# write your code here
print(df.query("a in @our_df.b1"))

import pandas as pd

df = pd.read_csv('/datasets/vg_sales.csv')
df['user_score'] = pd.to_numeric(df['user_score'], errors='coerce')
print(df[(df['platform'] == 'Wii') & ~(df['genre'] == 'Sports')].head())

print(df[(df['na_sales'] >= 1) | (df['eu_sales'] >= 1)].head())

import pandas as pd

df = pd.read_csv('/datasets/vg_sales.csv')
df['user_score'] = pd.to_numeric(df['user_score'], errors='coerce')

# write your code here
df_filtered = df[(df['year_of_release'] >= 1980) & (df['year_of_release'] <= 1989)]
print(df_filtered.head())

print(df.query("platform == 'Wii' and genre != 'Sports'").head())

import pandas as pd

df = pd.read_csv('/datasets/vg_sales.csv')
df['user_score'] = pd.to_numeric(df['user_score'], errors='coerce')

# write your code here
q_string = "na_sales >= 1 or eu_sales >= 1 or jp_sales >= 1"
df_filtered = df.query(q_string)
print(df_filtered.head())

import pandas as pd

df = pd.read_csv('/datasets/vg_sales.csv')
df['user_score'] = pd.to_numeric(df['user_score'], errors='coerce')

developers = ['SquareSoft', 'Enix Corporation', 'Square Enix']
cols = ['name', 'developer', 'na_sales', 'eu_sales', 'jp_sales']

# write your code here
df_filtered = df[
    (df['na_sales'] > 0) &
    (df['eu_sales'] > 0) &
    (df['jp_sales'] > 0) &
    (df['developer'].isin(developers)) &
    (df['jp_sales'] > (df['na_sales'] + df['eu_sales']))
][cols]

print(df_filtered)

import pandas as pd

df = pd.read_csv('/datasets/vg_sales.csv')
df['user_score'] = pd.to_numeric(df['user_score'], errors='coerce')

df['platform'] = df['platform'].str.replace('NES', 'Nintendo Entertainment System')
print(df.iloc[:, :2].head())

df['platform'] = df['platform'].where(df['platform'] != 'NES', 'Nintendo Entertainment System')
print(df.iloc[:, :2].head())

df[['na_sales', 'eu_sales']] = df[['na_sales', 'eu_sales']].where((df['na_sales'] > 0) | (df['eu_sales'] > 0), None)
print(df[['name','na_sales', 'eu_sales']])

import pandas as pd

df = pd.read_csv('/datasets/vg_sales.csv')
df['user_score'] = pd.to_numeric(df['user_score'], errors='coerce')

# write your code here
print(df['genre'].value_counts(ascending=True))

import pandas as pd

df = pd.read_csv('/datasets/vg_sales.csv')
df['user_score'] = pd.to_numeric(df['user_score'], errors='coerce')

# write your code here
print(df['genre'].value_counts(ascending=True))
genres = ['Puzzle', 'Strategy']
df['genre'] = df['genre'].where(~df['genre'].isin(genres), 'Misc')

import pandas as pd

df = pd.read_csv('/datasets/OnlineRetail.csv')
print(df.head())

import pandas as pd

df = pd.read_csv('/datasets/OnlineRetail.csv')
print(df['StockCode'].min(), df['StockCode'].max())

import pandas as pd

df = pd.read_csv('/datasets/OnlineRetail.csv')

# write your code here
df.info()

import pandas as pd

d = {'col 1': [1.0, 2.0], 'col 2': [3, 4]}
df = pd.DataFrame(data=d)

print(df)
print()
print('Output of df.info():')
df.info()

df_str_dtype = df.astype('str')
print(df_str_dtype)
df_str_dtype.info()

df['col1'] = df['col1'].astype('int')
print(df)
print(df.dtypes)

np.array_equal(df['col1'], df['col1'].astype('int'))  # This will return True if the conversion was successful

np.array_equal(df['col2'], df['col2'].astype('int'))  # This will return True if the conversion was successful

d = {'col 1': ['1.0', '2.0'], 'col 2': ['3', '4']}
df = pd.DataFrame(data=d)

df['col2'] = df['col2'].astype('int')
print(df.dtypes)
df['col1'] = df['col1'].astype('int')

df['col2'] = df['col2'].astype('int')
df['col1'] = pd.to_numeric(df['col1'], errors='coerce')
print(df.dtypes)

import pandas as pd
import numpy as np

df = pd.read_csv('/datasets/OnlineRetail.csv')

# write your code here
np.array_equal(df['Quantity'], df['Quantity'].astype('int'))

import pandas as pd

df = pd.read_csv('/datasets/OnlineRetail.csv')
print(df.sample(5, random_state=42))

print(df['InvoiceDate'].dtype)

import pandas as pd

string_date = '2010-12-17T12:38:00Z'
datetime_date = pd.to_datetime(string_date, format='%Y-%m-%dT%H:%M:%SZ')
print(type(string_date))
print(type(datetime_date))
print(datetime_date)

string_date = '20-12-2002Z04:31:00'
datetime_date = pd.to_datetime(string_date, format='%d-%m-%YZ%H:%M:%S')

string_date = '5/13/13 12:04:00'
datetime_date = pd.to_datetime(string_date, format='%m/%d/%y %H:%M:%S')

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], format='%m/%d/%Y %H:%M:%S', errors='coerce')

print(df.head())
print()
df.info()

import pandas as pd

position = pd.read_csv('/datasets/position.csv')

# write your code here
position.info()

import pandas as pd

position = pd.read_csv('/datasets/position.csv')

# write your code here
position['timestamp'] = pd.to_datetime(position['timestamp'], format='%Y-%m-%dT%H:%M:%S', errors='coerce')
print(position['timestamp'].head())

print(type(df['InvoiceDate'][0]))
print(df['InvoiceDate'][0].day) #error

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], format='%m/%d/%Y %H:%M:%S', errors='coerce')
df['day'] = df['InvoiceDate'].dt.day
print(df.sample(5, random_state=42))

df['InvoiceDate'] = df['InvoiceDate'].dt.tz_localize('UTC')
df['InvoiceDate'] = df['InvoiceDate'].dt.tz_convert('America/New_York')
print(df['InvoiceDate'].sample(5, random_state=42))

import pandas as pd

position = pd.read_csv('/datasets/position.csv')
position['timestamp'] = pd.to_datetime(position['timestamp'], format='%Y-%m-%dT%H:%M:%S')

# write your code here
position['month'] = position['timestamp'].dt.month
print(position.head())

import pandas as pd

position = pd.read_csv('/datasets/position.csv')
position['timestamp'] = pd.to_datetime(position['timestamp'], format='%Y-%m-%dT%H:%M:%S')

# write your code here
position['ts_toronto'] = position['timestamp'].dt.tz_localize('America/Toronto')
print(position.head())

import pandas as pd
df = pd.read_csv('/datasets/vg_sales.csv')
print(df.head())
df['total_sales'] = df['na_sales'] + df['eu_sales'] + df['jp_sales'] + df['other_sales']
print(df['total_sales'].head())
df['eu_sales_share'] = df['eu_sales'] / df['total_sales']
print(df['eu_sales_share'].head())

df['is_nintendo'] = df['publisher'] == 'Nintendo'
print(df['is_nintendo'].head())

print(df['platform'].str.lower().isin(['wii', 'ds', 'gba', 'psp']).head())
print(df['platform'].unique())
df['platform'] = df['platform'].astype('category')
print(df['platform'].head())

import pandas as pd

df = pd.read_csv('/datasets/vg_sales.csv')

# write your code here
df['user_score'] = pd.to_numeric(df['user_score'], errors='coerce')


import pandas as pd

df = pd.read_csv('/datasets/vg_sales.csv')

# write your code here
# Rescale user_score from 0-10 to 0-100
df['user_score'] = pd.to_numeric(df['user_score'], errors='coerce')
df['user_score_scaled'] = df['user_score'] * 10

# Calculate average_score using critic_score and user_score_scaled
df['average_score'] = (df['critic_score'] + df['user_score_scaled']) / 2

# Print the first five values of average_score
print(df['average_score'].head())

import pandas as pd
import numpy as np

df = pd.read_csv('/datasets/vg_sales.csv')
print(df['year_of_release'].min(), df['year_of_release'].max())
df['year_of_release'].value_counts().sort_index()

def era_group(year):
      """
    The function returns the era group for games according to the year of release, using the following rules:
    —'retro'   for year < 2000
    —'modern'  for 2000 <= year < 2010
    —'recent'  for year >= 2010
    —'unknown' for missing year values (NaN)
    """

    if year < 2000:
        return 'retro'
    elif year < 2010:
        return 'modern'
    elif year >= 2010:
        return 'recent'
    else:
        return 'unknown'
df['era_group'] = df['year_of_release'].apply(era_group)
print(df.head())

print(df['era_group'].value_counts())


import pandas as pd
import numpy as np

df = pd.read_csv('/datasets/vg_sales.csv')

# write your function definition here
def score_group(score):
    """
    The function returns the score group for games according to the average score, using the following rules:
    —'low'     for average_score < 60
    —'medium'  for 60 <= average_score < 79
    —'high'    for average_score >= 80
    —'no score' for missing average_score values (NaN)
    """
    
    if pd.isna(score):
        return 'no score'
    elif score < 60:
        return 'low'
    elif score <= 79:
        return 'medium'
    else:
        return 'high'


# print results of calling the function with these inputs in order: 10, 65, 99, np.nan
print(score_group(10))
print(score_group(65))
print(score_group(99))
print(score_group(np.nan))
df['score_group'] = df['critic_score'].apply(score_group)


df.dropna(inplace=True)
df.info()

def era_sales_group(row):
    """
    The function returns a category for games according to the year of release and total sales, using the following rules:
    —'retro'   for year < 2000 and total sales < $1 million
    —'modern'  for 2000 <= year < 2010 and total sales < $1 million
    —'recent'  for year >= 2010 and total sales < $1 million
    —'classic' for year < 2010 and total sales >= $1 million
    —'big hit' for year >= 2010 and total sales >= $1 million
    """

    year = row['year_of_release']
    na_sales = row['na_sales']
    eu_sales = row['eu_sales']
    jp_sales = row['jp_sales']

    total_sales = na_sales + eu_sales + jp_sales

    if year < 2000:
        if total_sales < 1:
            return 'retro'
        else:
            return 'classic'
    if year < 2010:
        if total_sales < 1:
            return 'modern'
        else:
            return 'classic'
    if year >= 2010:
        if total_sales < 1:
            return 'recent'
        else:
            return 'big hit'

row = df.iloc[0]
print(row)
print()
print(era_sales_group(row))

column_names = ['year_of_release', 'na_sales', 'eu_sales', 'jp_sales']
row_values = [2000, 0.1, 0.25, 0]

row = pd.Series(row_values, index=column_names)
print(row)
print()
print(era_sales_group(row))

cols = ['year_of_release', 'na_sales', 'eu_sales', 'jp_sales']

row_1 = pd.Series([1989, 0, 0, 0.6], index=cols) # expect 'retro'
row_2 = pd.Series([1989, 1, 2, 0], index=cols)   # expect 'classic'
row_3 = pd.Series([2006, 0.3, 0, 0], index=cols) # expect 'modern'
row_4 = pd.Series([2020, 0, 0.4, 0], index=cols) # expect 'recent'
row_5 = pd.Series([2020, 1, 1, 1], index=cols)   # expect 'big hit'

print(row_1, row_2, row_3, row_4, row_5, sep='\n\n')
print()

rows = [row_1, row_2, row_3, row_4, row_5]
for row in rows:
    print(era_sales_group(row))

df['game_category'] = df.apply(era_sales_group, axis=1)
print(df.sample(5, random_state=321))
print(df['game_category'].value_counts())

import pandas as pd

df = pd.read_csv('/datasets/vg_sales.csv')
df.dropna(inplace=True)

# write your function definition here
def avg_score_group(row):
    """
    The function returns a category for games according to the average score, using the following rules:
    —'low'     for average_score < 60
    —'medium'  for 60 <= average_score < 80
    —'high'    for average_score >= 80
    —'no score' for missing average_score values (NaN)
    """
    
    score = (row['critic_score'] + row['user_score'] * 10) / 2

    if pd.isna(score):
        return 'no score'
    elif score < 60:
        return 'low'
    elif score < 80:
        return 'medium'
    else:
        return 'high'

# create the test input rows here
row_1 = pd.Series([66, 3.6], index=['critic_score', 'user_score'])  # expect 'low' 
row_2 = pd.Series([72, 8.1], index=['critic_score', 'user_score'])
row_3 = pd.Series([99, 9.4], index=['critic_score', 'user_score'])
    
# print results of calling the function with the test inputs in order
print(avg_score_group(row_1))  # expect 'low'
print(avg_score_group(row_2))
print(avg_score_group(row_3))

df.count(axis=1)

import pandas as pd
exoplanet = pd.read_csv('/datasets/exoplanet_data.csv')
print(exoplanet.groupby('discovered').count())
exo_number = exoplanet.groupby('discovered')['radius'].count()
print(exo_number)
exo_radius_sum = exoplanet.groupby('discovered')['radius'].sum()
print(exo_radius_sum)
exo_number = exoplanet.groupby('discovered')['radius'].count()
exo_radius_mean = exo_radius_sum / exo_number
print(exo_radius_mean)

import pandas as pd
df = pd.read_csv('/datasets/vg_sales.csv')
print(df.head())

df.dropna(inplace=True)
pivot_data = df.pivot_table(index='genre',
                            columns='platform',
                            values='eu_sales',
                            aggfunc='sum',
                            )
print(pivot_data)
print()
print(type(pivot_data))

import pandas as pd
df = pd.read_csv('/datasets/vg_sales.csv')
df.dropna(inplace=True)
groupby_data = df.groupby(['genre', 'platform'])['eu_sales'].mean()
print(groupby_data)
print()
print(type(groupby_data))

import pandas as pd

df = pd.read_csv('/datasets/vg_sales.csv')
df = df[df['year_of_release'] >= 2000]

df.user_score = pd.to_numeric(df.user_score, errors='coerce')

# write your code here
df_pivot = df.pivot_table(index='genre',
                          columns='release_year',
                          values='user_score',
                          aggfunc='mean'
                          )
print(df_pivot)

exoplanet.sort_values(by='radius', ascending=False, inplace=True)
print(exoplanet.sort_values(by='radius').head())
print(exoplanet['radius'].sort_values().head())
print(exoplanet[exoplanet['radius'] < 1].head())
print(exoplanet[exoplanet['discovered'] == 2014])
exo_small_14 = exoplanet[exoplanet['discovered'] == 2014]
exo_small_14 = exoplanet[exoplanet['radius'] < 1]
print(exo_small_14)
print(exo_small_14.sort_values(by='radius', ascending=False).head())
exo_small_14 = exo_small_14.sort_values(by='radius', ascending=False)

import pandas as pd
df = pd.read_csv('/datasets/vg_sales.csv')
df.dropna(inplace=True)
print(df.head())
mean_score = df.groupby('genre')['critic_score'].mean()
print(mean_score)

import pandas as pd
df = pd.read_csv('/datasets/vg_sales.csv')
df.dropna(inplace=True)
grp = df.groupby(['platform', 'genre'])
print(grp['critic_score'].mean())

import pandas as pd
df = pd.read_csv('/datasets/vg_sales.csv')
df.dropna(inplace=True)
grp = df.groupby(['platform', 'genre'])
print(grp)

import pandas as pd
df = pd.read_csv('/datasets/vg_sales.csv')
df.dropna(inplace=True)
grp = df.groupby(['platform', 'genre'])
print(grp['critic_score'].mean().head())

import pandas as pd
df = pd.read_csv('/datasets/vg_sales.csv')
df.dropna(inplace=True)
print(df.groupby(['genre', 'platform'])['critic_score'].mean().head())

import pandas as pd
df = pd.read_csv('/datasets/vg_sales.csv')
df.dropna(inplace=True)

agg_dict = {
    'critic_score': 'mean',
    'user_score': 'mean',
    'na_sales': 'sum',
    'eu_sales': 'sum',
    'jp_sales': 'sum'
}
grp = df.groupby(['platform', 'genre']).agg(agg_dict)
print(grp.head())

import pandas as pd
df = pd.read_csv('/datasets/vg_sales.csv')
df['total_sales'] = df['na_sales'] + df['eu_sales'] + df['jp_sales'] + df['other_sales']
grp = df.groupby('genre')
agg_dict = {
    'total_sales': 'sum',
    'na_sales': 'mean',
    'eu_sales': 'mean',
    'jp_sales': 'mean'
}
genre = grp.agg(agg_dict)
print(genre)

import pandas as pd
df = pd.read_csv('/datasets/vg_sales.csv')
df.dropna(inplace=True)
print(df.head())
mean_score = df.groupby('publisher')['critic_score'].mean()
print(mean_score)

import pandas as pd
df = pd.read_csv('/datasets/vg_sales.csv')
df['total_sales'] = df['na_sales'] + df['eu_sales'] + df['jp_sales'] + df['other_sales']
num_sales = df.groupby('publisher')['total_sales'].sum()
print(num_sales)

import pandas as pd
df = pd.read_csv('/datasets/vg_sales.csv')
mean_score = df.groupby('publisher')['critic_score'].mean()
df['total_sales'] = df['na_sales'] + df['eu_sales'] + df['jp_sales'] + df['other_sales']
num_sales = df.groupby('publisher')['total_sales'].sum()
df_concat = pd.concat([mean_score, num_sales], axis=1)
print(df_concat.head())

import pandas as pd
df = pd.read_csv('/datasets/vg_sales.csv')
df.dropna(inplace=True)
mean_score = df.groupby('publisher')['critic_score'].mean()
df['total_sales'] = df['na_sales'] + df['eu_sales'] + df['jp_sales'] + df['other_sales']
num_sales = df.groupby('publisher')['total_sales'].sum()
df_concat = pd.concat([mean_score, num_sales], axis=1)
df_concat.columns = ['mean_critic_score', 'total_sales']
print(df_concat.head())

import pandas as pd
df = pd.read_csv('/datasets/vg_sales.csv')
rpgs = df[df['genre'] == 'Role-Playing']
platformers = df[df['genre'] == 'Platform']
df_concat = pd.concat([rpgs, platformers])
print(df_concat['name','genre'])

import pandas as pd
df = pd.read_csv('/datasets/vg_sales.csv')
df['total_sales'] = df['na_sales'] + df['eu_sales'] + df['jp_sales'] + df['other_sales']
total_sales = df.groupby('platform')['total_sales'].sum()
num_pubs = df.groupby('platform')['publisher'].nunique()
df_concat = pd.concat([total_sales, num_pubs], axis=1)
df_concat.columns = ['total_sales', 'num_pubs']

import pandas as pd

first_pupil_df = pd.DataFrame(
    {
        'author': ['Alcott', 'Fitzgerald', 'Steinbeck', 'Twain', 'Hemingway'],
        'title': ['Little Women',
                  'The Great Gatsby',
                  'Of Mice and Men',
                  'The Adventures of Tom Sawyer',
                  'The Old Man and the Sea'
                 ],
    }
)
second_pupil_df = pd.DataFrame(
    {
        'author': ['Steinbeck', 'Twain', 'Hemingway', 'Salinger', 'Hawthorne'],
        'title': ['East of Eden',
                  'The Adventures of Huckleberry Finn',
                  'For Whom the Bell Tolls',
                  'The Catcher in the Rye',
                  'The Scarlett Letter'
                 ],
    }
)

print(first_pupil_df)
print()
print(second_pupil_df)

both_pupils = first_pupil_df.merge(second_pupil_df, on='author')
print(both_pupils)

both_pupils = first_pupil_df.merge(second_pupil_df, on='author', how='inner')
print(both_pupils)

both_pupils = first_pupil_df.merge(second_pupil_df, on='author', how='left')
print(both_pupils)
both_pupils = first_pupil_df.merge(second_pupil_df, 
                                   on='author', 
                                   suffixes=('_first', '_second')
)
print(both_pupils)
both_pupils = first_pupil_df.merge(second_pupil_df,
                                   left_on='author',
                                   right_on='authors'
)
print(both_pupils)
print(both_pupils.drop(columns='authors',
                       axis=1)
)

import pandas as pd

# read data
df_members = pd.read_csv('/datasets/new_members.csv')
df_orders = pd.read_csv('/datasets/recent_orders.csv')

# display data
print(df_members)
print()
print(df_orders)

df_merged = df_members.merge(df_orders, 
                             left_on='id',
                             right_on='user_id',
                             suffixes=('_member', '_order'),
)
print(df_merged)
df_merged = df_merged.drop(columns='user_id')
print(df_merged)

# Import the libraries you'll need for this analysis
import pandas as pd
import matplotlib.pyplot as plt

# Load the datasets
# Note: These files use semicolon (;) as the separator instead of comma
orders         = pd.read_csv('/datasets/instacart_orders.csv', sep=';')
products       = pd.read_csv('/datasets/products.csv', sep=';')
departments    = pd.read_csv('/datasets/departments.csv', sep=';')
aisles         = pd.read_csv('/datasets/aisles.csv', sep=';')
order_products = pd.read_csv('/datasets/order_products.csv', sep=';')

products[products['product_name'].isna()]
print(products[products['product_name'].isna() & (products['aisle_id'] != 100)])
print(products[products['product_name'].isna() & (products['department_id'] != 21)])

#Display department_id 21
print(departments[departments['department_id'] == 21])

#Display aisle_id 100
print(aisles[aisles['aisle_id'] == 100])

#Filter rows with missing product_name
missing_products = products[products['product_name'].isna()]
#Group by department_id and aisle_id, and count the number of missing products in each group
print(missing_products.groupby(['department_id', 'aisle_id']).size())

products['product_name'].fillna('Unknown', inplace=True)

print(orders[orders['days_since_prior_order'].isna()])

# Filter for rows where it's not the customer's first order and check for missing values in days_since_prior_order
missing_not_first_order = orders[(orders['order_number'] > 1) & (orders['days_since_prior_order'].isna())]

missing_add_to_cart_order = order_products[order_products['add_to_cart_order'].isna()]

# Use .min() and .max() to find the minimum and maximum values for this column.
print(order_products['add_to_cart_order'].min())
print(order_products['add_to_cart_order'].max())

# Save all order IDs with at least one missing value in 'add_to_cart_order'
missing_order_ids = order_products[order_products['add_to_cart_order'].isna()]['order_id'].unique()

# Do all orders with missing values have more than 64 products?
orders_with_missing = orders[orders['order_id'].isin(missing_order_ids)]
print(orders_with_missing[orders_with_missing['order_number'] > 64])

# Do all orders with missing values have more than 64 products?
orders_with_missing = order_products[order_products['order_id'].isin(missing_order_ids)]
print(orders_with_missing[orders_with_missing['add_to_cart_order'] > 64])

# Replace missing values with 999 and convert column to integer type
order_products['add_to_cart_order'].fillna(999, inplace=True)
order_products['add_to_cart_order'] = order_products['add_to_cart_order'].astype(int)

# Find the number of duplicate rows in the orders dataframe
duplicate_orders = orders.duplicated().sum()

# Remove duplicate orders
orders = orders.drop_duplicates()

# Check for fully duplicate rows
duplicate_products = products.duplicated().sum()
# Check for just duplicate product IDs using subset='product_id' in duplicated()
duplicate_product_ids = products.duplicated(subset='product_id').sum()

# Check for just duplicate product names (convert names to lowercase to compare better)

# Check for duplicate product_name (case-insensitive)
products['product_name_lower'] = products['product_name'].str.lower()
duplicate_product_names = products.duplicated(subset='product_name_lower').sum()
print('Number of duplicate product names (case-insensitive):', duplicate_product_names)

#Drop temporary column
products.drop(columns='product_name_lower', inplace=True)

# Drop duplicate product names (case insensitive)
products['product_name_lower'] = products['product_name'].str.lower()
products = products.drop_duplicates(subset='product_name_lower')
products.drop(columns='product_name_lower', inplace=True)

# Check for aisles entries in the departments dataframe
# Check for duplicate aisles entries in the aisles dataframe
duplicate_aisles = aisles.duplicated().sum()

# Check for duplicate entries in the order_products dataframe
duplicate_order_products = order_products.duplicated().sum()

"""To verify that the values in the order_hour_of_day and order_dow columns are sensible:

Check unique values: Use .unique() on each column to extract all distinct values present.
Sort the results: Use sorted() to arrange the unique values in ascending order for easier verification.
Validate ranges:
Ensure order_hour_of_day values range from 0 to 23 (representing hours of the day).
Ensure order_dow values range from 0 to 6 (representing days of the week).
This process confirms that the data aligns with expected ranges and there are no out-of-bound or invalid entries."""
# Check unique values in order_hour_of_day and order_dow
print('Unique values in order_hour_of_day:', sorted(orders['order_hour_of_day'].unique()))
print('Unique values in order_dow:', sorted(orders['order_dow'].unique()))

"""
To determine the time of day people shop for groceries, analyze the order_hour_of_day column in the orders dataset. Use .value_counts() to count the number of orders placed at each hour, and then sort the results by the hour for a clear chronological order.

Finally, visualize the data with a bar plot to easily observe the shopping trends across different times of the day.
"""
# Count the number of orders for each hour of the day
hour_counts = orders['order_hour_of_day'].value_counts().sort_index()
# Plot the number of orders by hour of the day
hour_counts.plot(kind='bar',
                figsize=(24, 6),
                title='Number of Orders by Hour of Day',
                xlabel='Hour of Day',
                ylabel='Number of Orders',
                color='skyblue'
                #rename x axis ticks
                hour_labels = [f'{hour}:00' for hour in hour_counts.index]
                plt.xticks(ticks=range(len(hour_labels)), labels=hour_labels)
)
plt.xticks(rotation=0)
plt.show()

"""To figure out what day of the week people shop for groceries, analyze the order_dow column in the orders dataset. Use .value_counts() to count the number of orders for each day of the week, and then sort the results by the day index to maintain the correct order.

Visualize the data with a bar plot to clearly observe shopping patterns across the days of the week.
"""
# Count the number of orders for each day of the week
dow_counts = orders['order_dow'].value_counts().sort_index()
# Plot the number of orders by day of the week
dow_counts.plot(kind='bar',
                figsize=(12, 6),
                title='Number of Orders by Day of Week',
                xlabel='Day of Week',
                ylabel='Number of Orders',
                color='lightgreen'
)

plt.xticks(ticks=range(len(dow_counts.index)), labels=['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'])
plt.xticks(rotation=0)
plt.show()

"""To understand how long people wait before placing another order, analyze the days_since_prior_order column in the orders dataset. Use .value_counts() to count how many orders were placed for each interval of days, then sort the results by the number of days for clarity.

Visualize the data using a bar plot to observe patterns in ordering frequency over time."""
# Count the number of orders for each interval of days since the prior order
days_since_prior_order_counts = orders['days_since_prior_order'].value_counts().sort_index()
# Plot the number of orders by days since prior order
days_since_prior_order_counts.plot(kind='bar',
                                    figsize=(12, 6),
                                    title='Number of Orders by Days Since Prior Order',
                                    xlabel='Days Since Prior Order',
                                    ylabel='Number of Orders',
                                    color='lightcoral'
)
plt.xticks(ticks=range(len(days_since_prior_order_counts.index)), labels=days_since_prior_order_counts.index)
plt.xticks(rotation=0)
plt.show()

"""To determine if there's a difference in the order_hour_of_day distributions on Wednesdays and Saturdays, follow these steps:

Create masks for Wednesday (order_dow == 3) and Saturday (order_dow == 6) to filter the orders data.
Count the order hours for each day using .value_counts() and sort them by hour with .sort_index() for clarity.
Combine the counts for both days into a single DataFrame using pd.concat(), and label the columns for easier interpretation.
After preparing the data, plot bar charts for both days to visually compare the distribution of order times. Look for patterns such as peaks or differences in the busiest times throughout the day.

"""
# Create masks for Wednesday and Saturday
wednesday_mask = orders['order_dow'] == 3
saturday_mask = orders['order_dow'] == 6
# Count the order hours for Wednesday and Saturday
wednesday_counts = orders[wednesday_mask]['order_hour_of_day'].value_counts().sort_index()
saturday_counts = orders[saturday_mask]['order_hour_of_day'].value_counts().sort_index()
# Combine the counts into a single DataFrame
comparison_df = pd.concat([wednesday_counts, saturday_counts], axis=1)
comparison_df.columns = ['Wednesday', 'Saturday']
print(comparison_df)
# Plot the order hour distributions for Wednesday and Saturday
comparison_df.plot(kind='bar',
                   figsize=(12, 6),
                   title='Order Hour Distributions for Wednesday and Saturday',
                   xlabel='Hour of Day',
                   ylabel='Number of Orders',
                   color=['skyblue', 'lightgreen']
)
#rename x axis ticks
plt.xticks(ticks=range(len(comparison_df.index)), labels=[f'{hour}:00' for hour in comparison_df.index])

plt.xticks(rotation=0)
plt.show()

"""To explore the distribution of the number of orders per customer:

Group the data by user_id to calculate the total number of orders for each customer. Use .groupby('user_id') and count the order_id for each group.
Sort the results using .sort_values() for better readability.
Visualize the distribution using a histogram to observe how many orders most customers typically place.
Adjust the number of bins in the histogram to refine the visualization and better capture the pattern.


"""
# Group by user_id to count the number of orders per customer
orders_per_customer = orders.groupby('user_id')['order_id'].count().sort_values()
print(orders_per_customer)
# Plot a histogram of the number of orders per customer
orders_per_customer.plot(kind='hist',
                         bins=30,
                         figsize=(12, 6),
                         title='Distribution of Number of Orders per Customer',
                         xlabel='Number of Orders',
                         ylabel='Number of Customers',
                         color='lightblue'
)
plt.show()

"""To identify the top 20 most popular products:

Merge the datasets: Combine order_products and products on product_id to access both the product IDs and names in a single DataFrame.
Group the data: Group by both product_id and product_name to aggregate the order counts for each product using .size().
Sort the results: Use .sort_values(ascending=False) to rank products by their popularity.
Display the top 20: Use .head(20) to focus on the most frequently ordered products.
Visualize the results: Create a bar chart to highlight the top products and their order counts.
This will give you a clear view of the most popular products and their ranking."""
# Merge order_products with products to get product names
merged_products = order_products.merge(products,
                                        on='product_id',
                                        how='left'
    )
# Group by product_id and product_name to count orders for each product
product_counts = merged_products.groupby(['product_id', 'product_name']).size().reset_index(name='order_count')
# Sort the products by order count in descending order
top_20_products = product_counts.sort_values(by='order_count', ascending=False).head(20)
print(top_20_products)
# Plot a bar chart of the top 20 most popular products
top_20_products.plot(kind='bar',
                     x='product_name',
                     y='order_count',
                     figsize=(14, 7),
                     title='Top 20 Most Popular Products',
                     xlabel='Product Name',
                     ylabel='Number of Orders',
                     legend=False,
                     color='lightcoral'
)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

"""To analyze how many items people typically buy in one order:

Group the data by order_id and count the number of products (product_id) in each order using .count(). This gives the number of items in each order.
Aggregate the counts: Use .value_counts() to determine how frequently different order sizes occur, and then sort the results with .sort_index() to organize by the number of items.
Visualize the distribution: Use a bar plot to show the frequency of orders for each size, with the x-axis representing the number of items and t
he y-axis representing the number of orders.
This will help you understand the typical size of a grocery order and identify any trends in purchasing behavior.


"""
# Group by order_id to count the number of items in each order
items_per_order = order_products.groupby('order_id')['product_id'].count()
# Count how many orders have each number of items
order_size_distribution = items_per_order.value_counts().sort_index()
print(order_size_distribution)
# Plot a bar chart of the distribution of order sizes
order_size_distribution.plot(kind='bar',
                             figsize=(12, 6),
                             title='Distribution of Order Sizes',
                             xlabel='Number of Items',
                             ylabel='Number of Orders',
                             color='lightgreen'
)
plt.show()

"""Most of the order numbers are in the tail of the distribution. To get a better look at the non-tail part, let's choose a value in the tail as a cutoff and just plot order with fewer than that many items. An order size of 35 items is far enough into the tail for this."""
# Filter for orders with fewer than 35 items
filtered_order_sizes = order_size_distribution[order_size_distribution.index < 35]
# Plot a bar chart of the filtered distribution of order sizes
filtered_order_sizes.plot(kind='bar',
                          figsize=(12, 6),
                          title='Distribution of Order Sizes (Filtered)',
                          xlabel='Number of Items',
                          ylabel='Number of Orders',
                          color='lightblue'
)
plt.tight_layout()
plt.show()

"""T

o find the top 20 most frequently reordered items:

Filter the data: Use order_products['reordered'] == 1 to isolate only the products that have been reordered.
Merge the datasets: Combine the filtered order_products with the products dataset on product_id to get both the product names and IDs.
Group the data: Group by
both product_id and product_name to calculate how many times each product was reordered, using .size().
Sort the results: Use .sort_values(ascending=False) to rank the products by reorder frequency.
Display the top 20: Use .head(20) to focus on the most frequently reordered products.
Visualize the data: Create a bar chart to showcase the top reordered items and their frequencies.
This process highlights the products that customers consistently return to and reorder."""
# Filter for reordered items
reordered_items = order_products[order_products['reordered'] == 1]
# Merge with products to get product names
merged_reorders = reordered_items.merge(products,
                                        on='product_id',
                                        how='left'
    )
# Group by product_id and product_name to count reorders for each product
reorder_counts = merged_reorders.groupby(['product_id', 'product_name']).size()
reorder_counts = reorder_counts.reset_index(name='reorder_count')
# Sort the products by reorder count in descending order
reorder_counts = reorder_counts.sort_values(by='reorder_count', ascending=False)
top_20_reorders = reorder_counts.head(20)
print(top_20_reorders)
# Plot a bar chart of the top 20 most frequently reordered items
top_20_reorders.plot(kind='bar',
                      x='product_name',
                      y='reorder_count',
                      figsize=(14, 7),
                      title='Top 20 Most Frequently Reordered Items',
                      xlabel='Product Name',
                      ylabel='Number of Reorders',
                      legend=False,
                      color='lightcoral'
)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

"""Merge the datasets: Combine order_products with the products dataset to access product names and IDs in the same DataFrame.
Group the data: Group by product_id and product_name to isolate each product's order history.
Calculate the mean of reordered: Use .mean() on the reordered column to compute the proportion of orders for each product that were reorders. The value represents the reorder rate.
Sort the results: Use .sort_values(ascending=False) to rank products by their reorder rates.
Convert to a DataFrame: Use .reset_index() to organize the grouped data into a readable DataFrame.
Optional Sorting: Sort the results by product_id or another column for better clarity.
This approach provides insights into how frequently each product is reordered, helping identify customer favorites or staples."""
# Merge order_products with products to get product names
merged_products = order_products.merge(products,
                                        on='product_id',
                                        how='left'
    )
# Group by product_id and product_name to calculate reorder rates
grouped = merged_products.groupby(['product_id', 'product_name'])
reorder_rate = grouped['reordered'].mean().reset_index(name='reorder_rate')
# Sort the products by reorder rate in descending order
reorder_rate = reorder_rate.sort_values(by='reorder_rate', ascending=False)
print(reorder_rate.head(20))
# Plot a bar chart of the reorder rates for the top 20 products
reorder_rate.head(20).plot(kind='bar',
                            x='product_name',
                            y='reorder_rate',
                            figsize=(14, 7),
                            title='Top 20 Products by Reorder Rate',
                            xlabel='Product Name',
                            ylabel='Reorder Rate',
                            legend=False,
                            color='lightblue'
)

"""To calculate the proportion of products reordered by each customer:

Merge the datasets: Combine order_products with orders to link order and customer information.
Group the data: Group by user_id to focus on each customer's ordering behavior.
Calculate the mean of reordered: Use .mean() on the reordered column to determine the proportion of products reordered by each customer.
Sort the results: Use .sort_values(ascending=False) to identify customers with the highest reorder rates.
Convert to a DataFrame: Use .reset_index() to format the grouped data into a structured DataFrame for further analysis.
This analysis reveals the extent to which individual customers reorder products, providing insights into customer loyalty and preferences."""
# Merge order_products with orders to get user_id
merged_orders = order_products.merge(orders,
                                       on='order_id',
                                       how='left'
    )
# Group by user_id to calculate the proportion of products reordered by each customer
grouped = merged_orders.groupby('user_id')
reorder_proportion = grouped['reordered'].mean().reset_index(name='reorder_proportion')
# Sort the customers by reorder proportion in descending order
reorder_proportion = reorder_proportion.sort_values(by='reorder_proportion', ascending=False)
print(reorder_proportion.head(20))
# Plot a bar chart of the top 20 customers by reorder proportion
reorder_proportion.head(20).plot(kind='bar',
                                   x='user_id',
                                   y='reorder_proportion',
                                   figsize=(14, 7),
                                   title='Top 20 Customers by Reorder Proportion',
                                   xlabel='User ID',
                                   ylabel='Reorder Proportion',
                                   legend=False,
                                   color='lightgreen'
)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

"""To identify the top 20 items that people most frequently add to their carts first:

1. **Merge the datasets**: Combine `order_products` with `products` to link product names and IDs.
2. **Filter the data**: Focus on rows where `add_to_cart_order` equals 1, indicating the first item added to the cart.
3. **Group the data**: Group by `product_id` and `product_name` to aggregate the count of how often each product was the first in a cart.
4. **Count occurrences**: Use `.count()` to calculate the total number of times each product was the first added.
5. **Sort the results**: Use `.sort_values(ascending=False)` to rank products by their first-in-cart frequency.
6. **Display the top 20**: Use `.head(20)` to extract the most popular first-in-cart items.

This provides insights into which products customers prioritize in their shopping process.

"""
# Merge order_products with products to get product names
merged_products = order_products.merge(products,
                                        on='product_id',
                                        how='left'
    )
# Filter for items that were added first to the cart
first_added = merged_products[merged_products['add_to_cart_order'] == 1]
# Group by product_id and product_name to count how many times each product was added first
first_added_counts = first_added.groupby(['product_id', 'product_name']).size().reset_index(name='first_added_count')
# Sort the products by first added count in descending order
first_added_counts = first_added_counts.sort_values(by='first_added_count', ascending=False)
top_20_first_added = first_added_counts.head(20)
#plot a bar chart of the top 20 first added products
top_20_first_added.plot(kind='bar',
                         x='product_name',
                         y='first_added_count',
                         figsize=(14, 7),
                         title='Top 20 First Added Products',
                         xlabel='Product Name',
                         ylabel='First Added Count',
                         legend=False,
                         color='lightblue'
)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

import pandas as pd
data = pd.Series([11, 20, 22, 31, 32, 33, 41, 42, 43, 44, 51, 52, 53, 54, 55, 61, 62, 63, 64, 65, 66, 71, 72, 73, 74, 75, 76, 77, 81, 82, 83, 84, 85, 86, 87, 88, 91, 92, 93, 94, 95, 96, 97, 98, 99])

data.hist(bins=4, alpha=0.5, color='blue', edgecolor='black')

data.hist(
    bins=[11, 20, 30, 40, 50, 60, 70, 80, 90, 99]
)

"""1.

You've updated the interface for the shopping cart page on a website and want to know just how complicated users find it. Thus, you decide to study customers' order time - the number of seconds from when a customer starts the checkout process to when they complete it.

Only one day after the new interface was released, you've received enough readings to build a histogram.

You have been supplied with a data set containing order times measured in seconds. Build a histogram with bin boundaries at the points of [15, 30, 45, 60, 75, 90]. Set the transparency to 0.7."""
import pandas as pd
import matplotlib.pyplot as plt
# Load the data
pur_time = pd.Series([36, 44, 73, 32, 44, 29, 63, 60, 55, 74, 61, 26, 76, 40, 39, 28, 69, 61, 54, 58, 47, 41, 70, 51, 58, 36, 71, 47, 74, 59, 50, 78, 59, 48, 67, 53, 67, 52, 38, 55, 53, 53, 43, 77, 44, 63, 63, 54])
# Create the histogram
pur_time.hist(bins=[15, 30, 45, 60, 75, 90], alpha=0.7, color='blue', edgecolor='black')
# Set the title and labels
plt.title('Distribution of Order Times')
plt.xlabel('Order Time (seconds)')
plt.ylabel('Frequency')
plt.show()

"""
Again using the order time data from Task 1, build two histograms with the following interval boundaries:

[15, 35, 55, 75, 90]
[15, 45, 55, 90]
Set the transparency to 0.5 for both of them."""
# Load the data
pur_time = pd.Series([36, 44, 73, 32, 44, 29, 63, 60, 55, 74, 61, 26, 76, 40, 39, 28, 69, 61, 54, 58, 47, 41, 70, 51, 58, 36, 71, 47, 74, 59, 50, 78, 59, 48, 67, 53, 67, 52, 38, 55, 53, 53, 43, 77, 44, 63, 63, 54])
# Create the first histogram
pur_time.hist(bins=[15, 35, 55, 75, 90], alpha=0.5, color='blue', edgecolor='black')
# Set the title and labels for the first histogram
plt.title('Distribution of Order Times (15-35-55-75-90)')
plt.xlabel('Order Time (seconds)')
plt.ylabel('Frequency')
plt.show()

# Create the second histogram
pur_time.hist(bins=[15, 45, 55, 90], alpha=0.5, color='blue', edgecolor='black')

import pandas as pd

data = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
mean_value =  # write your code here: find the mean value in the dataset
spacing_all =  # write your code here: for each element in the dataset, find its distance to the mean
spacing_all_mean = # write your code here: calculate the average distance
mean_value = data.mean()
spacing_all = abs(data - mean_value)
spacing_all_mean = spacing_all.mean()
print(mean_value)
print(spacing_all)
print(spacing_all_mean)

import numpy as np
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
variance = np.var(x)
print(variance)
standard_deviation = np.std(x)
print(standard_deviation)
standard_deviation = np.sqrt(variance)
print(standard_deviation)

import pandas as pd
import numpy as np

data = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
standard_dev = np.std(data)
print(standard_dev)

""".

It takes the average user 3 seconds to read a message on a website. Further, you find that the data (which is normally distributed) has a variance of 0.25 seconds squared. Using the three-sigma rule described above, calculate how long a message needs to be displayed in order to get 99.7% of users to see it.

Print your results as follows: Message display time is ... ."""
import numpy as np

adv_mean = 3
adv_var = 0.25
adv_std = np.sqrt(adv_var) # calculate standard deviation

adv_time = adv_mean + 3 * adv_std # calculate the message display time
print(f'Message display time is {adv_time:.2f} seconds.')

"""A manufacturing company produces bolts with a target diameter of 10.0 mm. Quality control measurements show that the actual diameters are normally distributed with a mean of 10.0 mm and a standard deviation of 0.15 mm.
Calculate the range of diameters that contains 99.7% of the bolts produced (using the three-sigma rule). Any bolt outside this range would be considered defective.
Print your results as follows: Acceptable range: ... to ... mm"""
import numpy as np

bolt_mean = 10.0  # mm
bolt_std = 0.15   # mm

lower_bound = bolt_mean - 3 * bolt_std # calculate the lower boundary
upper_bound = bolt_mean + 3 * bolt_std # calculate the upper boundary

print(f"Acceptable range: {lower_bound:.2f} to {upper_bound:.2f} mm")

print(
    len(music[music['song'] == 'The Sound of Silence']) / len(music) * 100,
)

"""TripleTen monitors the number of successful blog posts for Zen. A post is considered completely successful if the number of shares is comparable with the number of likes. This is considered a 100% success.

Generate sets of 20, 400, and 10,000 random integers from the range of [1, 100]. This is the ratio of reposts to likes in the total population of bloggers. If the percentage for our chosen blogger is always high, the blogger is considered prolific.

For each selection of numbers, calculate the probability of the event “The number generated is in the range [21, 40]” (the most common proportion of shares). Store the results in variables p_20, p_400, and p_10000, accordingly.

To calculate the probability, create the function calculate_p, using the number of random integers generated from the range [1, 100] as a parameter, and the resulting output will be the percentage of integers in the range of 21 to 40, inclusive.

Print the resulting probabilities separated by spaces."""
import random
random.seed(42)  # Set seed for reproducibility

def calculate_p(N):
    cnt_21_40 = 0
    for i in range(N):
        random_integer = random.randint(1, 100)
        if 21 <= random_integer <= 40:
            cnt_21_40 += 1 
    return cnt_21_40 / N * 100

p_20 = calculate_p(20)
p_400 = calculate_p(400)
p_10000 = calculate_p(10000)

# print the probabilities separated by spaces
print(f"{p_20:.2f} {p_400:.2f} {p_10000:.2f}")

import numpy as np

spots = np.array(
    [
        [2, 3, 4, 5, 6, 7],
        [3, 4, 5, 6, 7, 8],
        [4, 5, 6, 7, 8, 9],
        [5, 6, 7, 8, 9, 10],
        [6, 7, 8, 9, 10, 11],
        [7, 8, 9, 10, 11, 12],
    ]
)

spot_counts = {}

for i in range(spots.shape[0]):
    for j in range(spots.shape[1]):
        if spots[i, j] not in spot_counts.keys():
            spot_counts[spots[i, j]] = 1
        else:
            spot_counts[spots[i, j]] += 1
print(spot_counts)

spot_probs = {}
for k in spot_counts:
    spot_probs[k] = spot_counts[k] / spots.size

print(spot_probs)
import pandas as pd
# Create a DataFrame from the spot probabilities
pd.Series(spots.reshape(36)).hist(density=True, bins=12, alpha=0.5, color='blue', edgecolor='black')

""".

The above matrix for the sample space "sum of two pythons' spots" (where each python is equally likely to have 5, 6, 7, 8, 9, or 10 spots) is stored in the spot_matrix variable.

Compile a spot_probs dictionary containing the probability distribution for this random variable. The lines containing the possible experimental outcomes need to be the dictionary keys, and the float outcome probabilities need to be the values. Print the value of the spot_probs variable."""
import numpy as np

spot_matrix = np.array(
    [
        [10, 11, 12, 13, 14, 15],
        [11, 12, 13, 14, 15, 16],
        [12, 13, 14, 15, 16, 17],
        [13, 14, 15, 16, 17, 18],
        [14, 15, 16, 17, 18, 19],
        [15, 16, 17, 18, 19, 20],
    ]
)


spot_counts = {}
for i in range(spot_matrix.shape[0]):
    for j in range(spot_matrix.shape[1]):
        if spot_matrix[i, j] not in spot_counts.keys():
            spot_counts[spot_matrix[i, j]] = 1
        else:
            spot_counts[spot_matrix[i, j]] += 1
#loop code
spot_probs = {}
# dictionary code
for k in spot_counts:
    spot_probs[k] = spot_counts[k] / spot_matrix.size    

for i in range(10, 21):
    print(i, spot_probs[i])

#Check that the probabilities for all possible outcomes add up to 1. Enter the results into the sum_probs_one variable and print them.
sum_probs_one = sum(spot_probs.values())
print(sum_probs_one)

x_probs = {
    '3': 0.1,
    '4': 0.2,
    '5': 0.2,
    '7': 0.3,
    '11': 0.1,
    '16': 0.05,
    '18': 0.05    
}

expectation = 0
for x_i in x_probs:
    expectation += int(x_i) * x_probs[x_i]

print(expectation)

x_probs = {
    '3': 0.1,
    '4': 0.2,
    '5': 0.2,
    '7': 0.3,
    '11': 0.1,
    '16': 0.05,
    '18': 0.05    
}

expected = 0
expected_of_squares = 0
square_of_expected = 0

for x_i in x_probs:
    expected += int(x_i) * x_probs[x_i]
    expected_of_squares += (int(x_i) ** 2) * x_probs[x_i]

square_of_expected = expected ** 2
variance = expected_of_squares - square_of_expected
print(variance)

""".

The probability distribution for the random variable X (the temperature of City N in April) is defined in the variable x_probs as a dictionary. Find its expected value and variance. Store the results in the expectation and variance variables. Print the results on the screen."""
import numpy as np

x_probs = {
    '-4': 0.05,
    '-2': 0.25,
    '0': 0.1,
    '1': 0.1,
    '5': 0.1,
    '7': 0.05,
    '15': 0.35,
}

# code for your calculations
expectation = 0
variance = 0

for x_i in x_probs:
    expectation += int(x_i) * x_probs[x_i]
    variance += (int(x_i) ** 2) * x_probs[x_i]

variance -= expectation ** 2

print('Expected value:', expectation)
print('Variance:', variance)

"""
It’s a known fact that pythons with different zodiac signs will vary in weight as adults. Among the 12 Zodiac signs, there are four elemental sign groups (Air, Fire, Earth, and Water), containing three signs each. Water signs weigh 2 kg, Fire and Earth 3 kg, and Air signs 5 kg. Python birth rates do not vary throughout the year.

Write the probability distribution for the random variable “Python weight” in your weight_probs dictionary. Find the expected value and variance for it and add them to the expectation and variance variables. Then print the results."""
weight_probs = {
    '2': 0.25,
    '3': 0.5,
    '5': 0.25
}

# code for your calculations
expectation = 0
variance = 0

for x_i in weight_probs:
    expectation += int(x_i) * weight_probs[x_i]
    variance += (int(x_i) ** 2) * weight_probs[x_i]

variance -= expectation ** 2

print('Expected value:', expectation)
print('Variance:', variance)

a = .088
b - .12

prob = a * a * a * b * b
print(prob)

from math import factorial
x = factorial(5)
print(x)

from math import factorial
c = factorial(14)/(factorial(5) * factorial(14 - 5))
print(c)

from math import factorial
from matplotlib import pyplot as plt

n = 5
p = .5

distr = []

for k in range(0, n+1):
    choose = factorial(n)/(factorial(k) * factorial(n - k))
    prob = choose * (p ** k) * ((1 - p) ** (n - k))
    distr.append(prob)

plt.bar(range(0, n+1), distr)

"""
On some days, the pythons in the python nursery are fed apples, and on other days they’re given pears.

There’s a three-day supply of pears and a four-day supply of apples for the next week (seven days). On any given day, the pythons can be fed only apples or pears, not a combination.

So an example of their diet would be pears, apples, pears, pears, apples, apples, apples.

How many different combinations of a pears-and-apples diet can there be this week? Save the results to the n_diets variable and print it."""

from math import factorial
n_apples = 4
n_pears = 3
n_diets = factorial(n_apples + n_pears) / (factorial(n_apples) * factorial(n_pears))

"""After graduating from the snake nursery, Peter Python decides to apply to a python academy. To get in, he needs to take six different exams (where the probability of passing each is independent of the probability of passing the others). Peter thinks he’s really well prepared: the probability of failing each of these exams, judging by his practice tests, is 15%.

Create a probability distribution for the random variable “number of exams Peter fails” and a histogram for it."""
from math import factorial

n_exams = 6
failure_rate = 0.15
def binomial_prob(n, k, p):
    """Calculate the binomial probability of k successes in n trials."""
    choose = factorial(n) / (factorial(k) * factorial(n - k))
    return choose * (p ** k) * ((1 - p) ** (n - k))

distr = []

for k in range(0, n_exams + 1):
    prob = binomial_prob(n_exams, k, failure_rate)
    distr.append(prob)

#Create a histogram
from matplotlib import pyplot as plt
plt.bar(range(0, n_exams + 1), distr, color='skyblue', edgecolor='black')
plt.title('Probability Distribution of Exams Failed by Peter Python')
plt.xlabel('Number of Exams Failed')
plt.ylabel('Probability')
plt.xticks(range(0, n_exams + 1))
plt.show()

"""Your company is organizing an important event. The PR team is looking for at least six media partners to provide publicity for it. Going by experience, about one in five media outlets that they negotiate with will say yes. Create a probability distribution and histogram for the random variable “number of media representatives who say yes” if you begin negotiations with 30 outlets."""
from math import factorial
from matplotlib import pyplot as plt

n = 30
p = 0.2

distr = []

for k in range(0, n + 1):
    choose = factorial(n) / (factorial(k) * factorial(n - k))
    prob = choose * (p ** k) * ((1 - p) ** (n - k))
    distr.append(prob)

plt.plot(range(0, n + 1), distr, kind='hist', color='lightgreen', edgecolor='black')
plt.xlabel('Number of Media Representatives Who Say Yes')
plt.ylabel('Probability')
plt.title('Probability Distribution of Media Representatives Saying Yes')


import pandas as pd
import matplotlib.pyplot as plt
# Load the datasets
# Note: These files use semicolon (;) as the separator instead of comma
orders         = pd.read_csv('/datasets/instacart_orders.csv', sep=';')
products       = pd.read_csv('/datasets/products.csv', sep=';')
departments    = pd.read_csv('/datasets/departments.csv', sep=';')
aisles         = pd.read_csv('/datasets/aisles.csv', sep=';')
order_products = pd.read_csv('/datasets/order_products.csv', sep=';')

"""To analyze the distribution of orders by day of the week, focus on the order_dow column in the orders dataframe."""
order_distribution = orders['order_dow'].value_counts().sort_index()
print(order_distribution)
# Plot the distribution of orders by day of the week
import matplotlib.pyplot as plt
# Count the number of orders for each day
plt.bar(order_distribution.index, order_distribution.values)
plt.xlabel('Day of the Week')
plt.ylabel('Number of Orders')
plt.title('Distribution of Orders by Day of the Week')
plt.xticks(rotation=45)
plt.show()

print(dataset.isna().sum())
print(dataset[dataset['column_name'].isna()])
print(dataset.isna().sum())

# Display rows where 'product_name' is missing
print(products[products['product_name'].isna()])
print(products[products['product_name'].isnull() & products['aisle_id'] != 100])
print(products[products['product_name'].isnull() & products['department_id'] != 21])
print(departments[departments['department_id'] == 21])
print(aisles[aisles['aisle_id'] == 100])
#Filter rows with missing product names
missing_product_names = products[products['product_name'].isnull()]
#Group by department_id and aisle_id to see if there are patterns
print(missing_product_names.groupby(['department_id', 'aisle_id']).size())
# Fill missing product names with 'Unknown Product'
products['product_name'].fillna('Unknown Product', inplace=True)
# Verify that there are no more missing product names
print(products[products['product_name'].isnull()])

# Count the number of orders for each day since prior order
days_since_prior_order_counts = orders['days_since_prior_order'].value_counts().sort_index()
print(days_since_prior_order_counts)
# Plot the distribution of days since prior order
import matplotlib.pyplot as plt
plt.bar(days_since_prior_order_counts.index, days_since_prior_order_counts.values)
plt.xlabel('Days Since Prior Order')
plt.ylabel('Number of Orders')
plt.title('Distribution of Days Since Prior Order')
plt.show()

"""To compare the order_hour_of_day distributions on Wednesdays and Saturdays, follow these steps:
1. Filter the orders dataframe for Wednesdays and Saturdays.
2. Count the number of orders for each hour of the day for both days.
3. Plot the distributions on the same graph for comparison.
"""
# Filter for Wednesdays (3) and Saturdays (6)
wednesday_orders = orders[orders['order_dow'] == 3]
saturday_orders = orders[orders['order_dow'] == 6]
# Count the number of orders for each hour of the day
wednesday_hour_counts = wednesday_orders['order_hour_of_day'].value_counts().sort_index()
saturday_hour_counts = saturday_orders['order_hour_of_day'].value_counts().sort_index()
# Combine the counts into a single DataFrame for easier plotting
comparison_df = pd.DataFrame({
    'Wednesday': wednesday_hour_counts,
    'Saturday': saturday_hour_counts
}).fillna(0)

# Plot the order hour distributions for Wednesday and Saturday
comparison_df.plot(kind='bar',
                   figsize=(12, 6),
                   title='Order Hour Distributions for Wednesday and Saturday',
                   xlabel='Hour of Day',
                   ylabel='Number of Orders',
                   color=['skyblue', 'lightgreen']
)
#rename x axis ticks
plt.xticks(ticks=range(len(comparison_df.index)+1), labels=comparison_df.index)
plt.xticks(rotation=0)
plt.show()

#Display rows where 'days_since_prior_order' is missing
print(orders[orders['days_since_prior_order'].isna()])
#Are there any missing values where its not a customers first order?
print(orders[orders['days_since_prior_order'].isna() & orders['order_number'] != 1])

# Display rows where the add_to_cart_order column has missing values
missing_add_to_cart_order = order_products[order_products['add_to_cart_order'].isna()]
print(missing_add_to_cart_order)

# Check if there are any missing values in the reordered column
missing_reordered = order_products[order_products['reordered'].isna()]
print(missing_reordered)
# Check if there are any missing values in the product_id column
missing_product_id = order_products[order_products['product_id'].isna()]
print(missing_product_id)
# Check if there are any missing values in the order_id column
missing_order_id = order_products[order_products['order_id'].isna()]
print(missing_order_id)
print(orders['user_id'].nunique())
print(orders['order_id'].nunique())
# Count the number of orders per customer
orders_per_customer = orders.groupby('user_id').size()
print(orders_per_customer)
#find min and max of add_to_cart_order
print(order_products['add_to_cart_order'].min())
print(order_products['add_to_cart_order'].max())
print(order_products['add_to_cart_order'].value_counts().sort_index())

#Find the number of unique products in the order_products dataset
unique_products = order_products['product_id'].nunique()
print(unique_products)
# Find the number of unique products in the products dataset
unique_products_in_products = products['product_id'].nunique()
print(unique_products_in_products)
# Find the number of unique products in the merged dataset
merged_products = order_products.merge(products, on='product_id', how='left')
print(merged_products['product_id'].nunique())
"""To analyze the most frequently ordered products:
1. Count the number of orders for each product.
2. Identify the top N most frequently ordered products.
3. Visualize the results.
"""
# Count the number of orders for each product
product_order_counts = order_products['product_id'].value_counts()
# Merge with products to get product names
product_order_counts = product_order_counts.reset_index()
product_order_counts.columns = ['product_id', 'order_count']
merged_products = product_order_counts.merge(products,
                                              on='product_id',
                                              how='left'
    )
# Sort the products by order count in descending order
product_counts = merged_products.sort_values(by='order_count', ascending=False)
# Get the top 20 most popular products
top_20_products = product_counts.head(20)
print(top_20_products)
# Plot a bar chart of the top 20 most popular products
top_20_products.plot(kind='bar',
                     x='product_name',
                     y='order_count',
                     title='Top 20 Most Popular Products',
                     xlabel='Product Name',
                     ylabel='Number of Orders',
                     color='skyblue'
)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
"""To analyze the distribution of order sizes:
1. Calculate the size of each order.
2. Visualize the distribution of order sizes.
"""
# Group by order_id to count the number of items in each order
order_sizes = order_products.groupby('order_id').size()
# Count how many orders have each number of items
order_size_counts = order_sizes.value_counts().sort_index()
print(order_size_counts)
# Plot a bar chart of the distribution of order sizes
order_size_counts.plot(kind='bar',
                       title='Distribution of Order Sizes',
                       xlabel='Number of Items in Order',
                       ylabel='Number of Orders',
                       color='lightgreen'
)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

duplicate_orders = orders.duplicated.sum()
print(duplicate_orders)

#Drop duplicates
orders = orders.drop_duplicates()
# Count the number of items in each order
order_items_per_order = order_products.groupby('order_id').size()
# Create a series to hold the distribution of order sizes
order_size_distribution = order_items_per_order.value_counts().sort_index()
# Plot a bar chart of the distribution of order sizes
order_size_distribution.plot(kind='bar',
                             figsize=(12, 6),
                             title='Distribution of Order Sizes',
                             xlabel='Number of Items in Order',
                             ylabel='Number of Orders',
                             color='lightgreen'
)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

"""To focus on the more common order sizes, filter the distribution to include only orders with fewer than 35 items. This helps to avoid clutter in the visualization from very large
orders that are less frequent."""
# Filter the order size distribution to include only orders with fewer than 35 items
filtered_order_sizes = order_size_distribution[order_size_distribution.index < 35]
# Plot a bar chart of the filtered distribution of order sizes
filtered_order_sizes.plot(kind='bar',
                          figsize=(12, 6),
                          title='Distribution of Order Sizes (Fewer than 35 Items)',
                          xlabel='Number of Items in Order',
                          ylabel='Number of Orders',
                          color='lightgreen'
)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
"""Filter for reordered items: Select rows from order_products where the reordered column equals 1.
Merge with products: Combine the filtered reordered items with the products dataset to get product names.
Group by product_id and product_name: Aggregate the data to count how many times each product was reordered.
"""
reordered_items = order_products[order_products['reordered'] == 1]
merged_reordered = reordered_items.merge(products, on='product_id', how='left')
reordered_counts = merged_reordered.groupby(['product_id', 'product_name']).size().reset_index(name='reorder_count')

#Save all order ids with at least one missing value in 'add to cart order'
missing_order_ids = order_products[order_products['add_to_cart_order'].isna()]['order_id'].unique()
#Do all orders with missing values have more than 64 items?
orders_with_missing = order_products[order_products['order_id'].isin(missing_order_ids)]
print(orders_with_missing.groupby('order_id').size().min())
print(orders_with_missing.groupby('order_id').size().max())
#Count the number of times each product was reordered
reorder_counts = reordered_counts.groupby(['product_id', 'product_name']).size()
#replace missing values with 999 and covert column to integer
order_products['add_to_cart_order'].fillna(999, inplace=True)
order_products['add_to_cart_order'] = order_products['add_to_cart_order'].astype(int)

#find the number of duplicated rows in the orders dataframe
duplicate_orders = orders.duplicated().sum()

#View the duplicate rows
print(duplicate_orders)

#Drop duplicates
orders = orders.drop_duplicates()

#Double check for duplicates
duplicate_orders = orders.duplicated().sum()
print(duplicate_orders)
duplicate_products = products.duplicated().sum()

duplicate_product_ids = products.duplicated(subset=['product_id']).sum()
print(duplicate_product_ids)

duplicate_products = products.duplicated().sum()
#check for duplicate lowercase product names
products['product_name_lower'] = products['product_name'].str.lower()
duplicate_product_names = products.duplicated(subset=['product_name_lower']).sum()
print('Duplicate product names:', duplicate_product_names)

is size() ascending by default and value_counts() descending by default? Yes or no
Yes

from scipy import stats as st
mu = 1000
sigma = 100

distr = st.norm(mu, sigma)

x = 1000

result = distr.cdf(x) # calculate the probability of getting the value x
print(result)

result = st.norm(mu, sigma).cdf(1000)

from scipy import stats as st
distr = st.norm(1000, 100)

x1 = 900
x2 = 1100

result = distr.cdf(x2) - distr.cdf(x1)
print(result)

from scipy import stats as st

distr = st.norm(1000, 100)
p1 = 0.841
result = distr.ppf(p1)  # calculate the value corresponding to the probability p1
print(result)

"""The number of monthly visitors to an online store has a normal distribution with a mean of 100,500 and a standard deviation of 3,500.

Find the probability that in the next month the outlet website will have:

Fewer than 92,000 visitors
More than 111,000 visitors
Fill in the code according to the comments, and use the print() statements in the precode to display your results."""

from scipy import stats as st

mu = 100500# what is the mean of the distribution?
sigma = 3500# what is the standard deviation of the distribution?

more_threshold = 111000# what is the lower limit for number of visitors?
fewer_threshold = 92000# what is the upper limit for number of visitors?

p_more_visitors = 1 - st.norm(mu,sigma).cdf(more_threshold) # calculate the probability that there are more visitors than the lower threshold
p_fewer_visitors = st.norm(mu,sigma).cdf(fewer_threshold)# calculate the probability that there are fewer visitors than the upper threshold

print(f'Probability there are more than {more_threshold} visitors: {p_more_visitors}')
print(f'Probability there are fewer than {fewer_threshold} visitors: {p_fewer_visitors}')

"""A different online store, Fancy Pants, sells gift products to a very narrow audience of corporate clients. The store's weekly sales of premium chess sets made from mammoth tusk have a normal distribution with a mean of 420 and a standard deviation of 65.

The inventory team is deciding how many sets to order. They want the chance of selling all of them next week to be 90%. How many should they order?"""
from scipy import stats as st

mu = 420# place your code here: what is the distribution's mean?
sigma = 65# place your code here: what is the distribution's standard deviation?
prob = .9 # place your code here: what is the required probability of selling all the products?

n_shipment = st.norm(mu, sigma).ppf(1 - prob) # place your code here: how many items should be ordered?

print('Need to order items:', int(n_shipment)+1)

"""
Prices of orders placed on an online store follow a normal distribution with a mean of $24 and a standard deviation of $3.20.

Some customers choose fast courier delivery, which has a fixed price regardless of the order value.

To keep customers happy, the courier delivery price should be set so that it is less than or equal to the order price for 75% of all orders.

What delivery price corresponds to the 75th percentile of order prices?"""

from scipy import stats as st

mu = 24# place your code here: what is the distribution's mean?
sigma = 3.20 # place your code here: what is the distribution's standard deviation?
threshold = .75 # place your code here: what percentage of orders should cost more than twice the cost of delivery?

max_delivery_price = st.norm(mu, sigma).ppf(1 - threshold)# place your code here: the max delivery cost

print('Maximum cost for courier delivery:', max_delivery_price)

#Plot a binomial distribution with a normal distribution overlay
from matplotlib import pyplot as plt
from math import factorial
from scipy import stats as st

#binomial distribution parameters
p = .8
n = 50

binom = []
for k in range(0, n + 1):
    choose = float(factorial(n) / (factorial(k) * factorial(n - k)))
    prob = choose * (p ** k) * ((1 - p) ** (n - k))
    binom.append(prob)

# Create a normal distribution with the same mean and standard deviation as the binomial distribution
mu = n * p
var = n * p * (1 - p)
sigma = var ** 0.5

x = range(n+1)
normal = st.norm.pdf(x, mu, sigma)

plt.bar(range(25, n + 1), binom[25:], width=0.8, label='Binomial Distribution', color='lightblue', edgecolor='black', alpha=0.3)
plt.plot(range(25, n + 1), normal[25:], 'g-', label='Normal Distribution', linewidth=2)
plt.xlabel('Number of Successes')
plt.ylabel('Probability')
plt.title('Binomial Distribution with Normal Distribution Overlay')
plt.show()

# Continuous range for normal PDF
x = np.linspace(25, 50, 100)  # Smooth range for normal curve
norm_probs = st.norm.pdf(x, mu, sigma)

from scipy import stats as st
import math as mt

binom_n = 5000
binom_p = .15

clicks = 715

mu = binom_n * binom_p
sigma = mt.sqrt(binom_n * binom_p * (1 - binom_p))

p_clicks = st.norm(mu, sigma).cdf(clicks)
print(f'Probability of getting {clicks} clicks or fewer: {p_clicks:.4f}')

# Calculate the probability of getting more than 715 clicks
p_more_clicks = 1 - p_clicks
print(f'Probability of getting more than {clicks} clicks: {p_more_clicks:.4f}')

"""A company sends its clients a monthly newsletter with news and offers from partners. It knows that 40% of users open the newsletter.

One partner is planning an advertising campaign and is hoping for a reach of about 9,000 users. Calculate the probability that the client’s expectations will be met if the newsletter is sent to 23,000 people.

(In the last example, we created a variable called clicks; here, create one called threshold, and save the value 9,000 to it. Let the population size be binom_n and let the probability that the newsletter gets opened be binom_p.)

Save the probability that the client's expectations will be met as p_threshold and print it."""
from scipy import stats as st
import math as mt

binom_n = 23000
binom_p = 0.4
threshold = 9000
mu = binom_n * binom_p
sigma = mt.sqrt(binom_n * binom_p * (1 - binom_p))
p_threshold = 1 - st.norm(mu, sigma).cdf(threshold)
print(f'Probability of reaching at least {threshold} users: {p_threshold:.4f}')

variance is the average of the squared differences from the mean
variance is the expectation of the squares minus the squared expectation
standard deviation is the square root of the variance

scipy.stats.ttest_1sample(array, popmean)

from scipy import stats as st
import numpy as np
import pandas as pd

time_on_site = pd.read_csv('/datasets/user_time.csv)

interested_value = 120

alpha = 0.05 # significance level

results = st.ttest_1samp(time_on_site, interested_value)

print(f'T-statistic: {results.statistic}, P-value: {results.pvalue}')

if results.pvalue < alpha:
    print('We reject the null hypothesis: the average time on site is significantly different from 120 seconds.')
else:
    print('We fail to reject the null hypothesis: the average time on site is not significantly different from 120 seconds.')
results.plot(kind='hist', bins=30, alpha=0.5, color='blue', edgecolor='black')
plt.title('Distribution of Order Times (15-45-55-90)')
plt.xlabel('Order Time (seconds)')
plt.ylabel('Frequency')
plt.show()

"""You own a chain of scooter rental stations called Scooters Get You There. There are 20 locations in the center of the city and each one has a maximum of 50 electric scooters. You want to test the hypothesis that in the past month there were on average 30 scooters available at any station during the day. An urban group called 'Squirrel' highlighted the importance of this number in their study of resident mobility. (If there are fewer scooters at the station, users will think that they won’t be able to rent one when they need one—but when there are more, people think that they won’t be able to dock their scooter after a trip because there won’t be any free spaces.)

Every hour, each station sends the number of available scooters to the server. You have downloaded the numbers from 1 pm to 4 pm for the past 30 days. Test your hypothesis using this sample."""
from scipy import stats as st
import pandas as pd

scooters = pd.Series([15, 31, 10, 21, 21, 32, 30, 25, 21,
28, 25, 32, 38, 18, 33, 24, 26, 40, 24, 37, 20, 36, 28, 38,
24, 35, 33, 21, 29, 26, 13, 25, 34, 38, 23, 37, 31, 28, 32,
24, 25, 13, 38, 34, 48, 19, 20, 22, 38, 28, 31, 18, 21, 24,
31, 21, 28, 29, 33, 40, 26, 33, 33,  6, 27, 24, 17, 28,  7,
33, 25, 25, 29, 19, 30, 29, 22, 15, 28, 36, 25, 36, 25, 29,
33, 19, 32, 32, 28, 26, 18, 48, 15, 27, 27, 27,  0, 28, 39,
27, 25, 39, 28, 22, 33, 30, 35, 19, 20, 18, 31, 44, 20, 18,
17, 28, 17, 44, 40, 33,])

optimal_value = 30# write your code here

alpha = .05 # write your code here

results = st.ttest_1samp(scooters, optimal_value) # write your code here

print('p-value: ', results.pvalue) # write your code here)

if (results.pvalue < alpha): # write your code here):
    print('We reject the null hypothesis')
else:
    print("We can't reject the null hypothesis")

from scipy import stats as st
import pandas as pd

screens = pd.Series([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9, 5.4, 4.8, 4.8, 4.3, 5.8, 5.7, 5.4])
prev_screens_value = 4.867

alpha = 0.05

results = st.ttest_1samp(screens, prev_screens_value)
#one-sided test p-value will be halved
print(f'T-statistic: {results.statistic}, P-value: {results.pvalue/2}')

if results.pvalue / 2 < alpha and results.statistic < 0:
    print('We reject the null hypothesis: the average screen time is significantly larger than 4.867 frames.')
else:
    print('We fail to reject the null hypothesis: the average screen time is not significantly larger than 4.867 frames.')

"""On June 1, 2019, you took a course with a famous coach and entrepreneur named Robby Tobbinson. If you apply his signature mindful-business techniques, your online project is guaranteed to bring in at least $800 a day. Maybe more. In just one month. He promises.

Promises are good, but statistical tests are better. Let's see what the numbers tell us.

Use a data set with daily revenue for the past month to test your hypothesis. The hypothesis is that your average daily revenue equaled or exceeded $800.

Remember: the hypothesis containing the equal sign is usually the null hypothesis. Therefore, “Everything will work out like the coach predicted” is your null hypothesis, and “Revenue will be less than what was predicted” is the alternative hypothesis. Random deviations are always possible. You can only say “Tobbinson’s methodology didn’t work!” if your revenue is significantly lower than the proposed amount."""
from scipy import stats as st
import numpy as np
import pandas as pd

revenue = pd.Series([727, 678, 685, 669, 661, 705, 701, 717, 
                     655,643, 660, 709, 701, 681, 716, 655, 
                     716, 695, 684, 687, 669,647, 721, 681, 
                     674, 641, 704, 717, 656, 725, 684, 665])

interested_value = 799 # how much did Robby Tobbinson promise?

alpha = .05# indicate the statistical significance level

results =  st.ttest_1samp(revenue, interested_value) # use the method st.ttest_1samp

print('p-value:', results.pvalue/2)# print the p-value for a one-sided test)

if (results.pvalue / 2 < alpha and results.statistic < 0): # compare the value you get and the critical statistical significance level
    # and check to see if the sample mean is on the correct side of interested_value):
    print(
        "We reject the null hypothesis: revenue was significantly lower than 800 dollars"
    )
else:
    print(
        "We can't reject the null hypothesis: revenue wasn't significantly lower"
    )

scipy.stats.ttest_ind(array1, array2, equal_var=False)

from scipy import stats as st
import numpy as np

sample_1 = [3071, 3636, 3454, 3151, 2185, 3259, 1727, 2263, 2015, 
            2582, 4815, 633, 3186, 887, 2028, 3589, 2564, 1422, 1785, 
            3180, 1770, 2716, 2546, 1848, 4644, 3134, 475, 2686, 
            1838, 3352]
sample_2 = [1211, 1228, 2157, 3699, 600, 1898, 1688, 1420, 5048, 3007, 
            509, 3777, 5583, 3949, 121, 1674, 4300, 1338, 3066, 
            3562, 1010, 2311, 462, 863, 2021, 528, 1849, 255, 
            1740, 2596]

alpha = 0.05  # significance level

results = st.ttest_ind(sample_1, sample_2)

print(f'T-statistic: {results.statistic}, P-value: {results.pvalue}')
if results.pvalue < alpha:
    print('We reject the null hypothesis: the average values of the two samples are significantly different.')
else:
    print('We fail to reject the null hypothesis: the average values of the two samples are not significantly different.')
print(f'The average of sample 1 is {np.mean(sample_1)} and the average of sample 2 is {np.mean(sample_2)}.')    

"""
There are two data sets: the average time spent on a website 1) for users who sign in with usernames and passwords, and 2) for users signing in through social media. Test the hypothesis that both user groups spend the same amount of time on the website."""

from scipy import stats as st
import numpy as np

# time spent on the website by users with a username and password
time_on_site_logpass = [368, 113, 328, 447, 1, 156, 335, 233, 
                       308, 181, 271, 239, 411, 293, 303, 
                       206, 196, 203, 311, 205, 297, 529, 
                       373, 217, 416, 206, 1, 128, 16, 214]

# time spent on the website by users signing in through social media
time_on_site_social  = [451, 182, 469, 546, 396, 630, 206, 
                        130, 45, 569, 434, 321, 374, 149, 
                        721, 350, 347, 446, 406, 365, 203, 
                        405, 631, 545, 584, 248, 171, 309, 
                        338, 505]


# your code goes below

alpha = 0.05  # set a critical statistical significance level

results = st.ttest_ind(time_on_site_logpass, time_on_site_social)# your code: test the hypothesis that the means of the two independent populations are equal

print('p-value:', results.pvalue) # your code: print the p-value you get)

if (results.pvalue < alpha):  # your code: compare the p-value you get and the critical statistical significance level
    # if the p-value is less than the significance level, we reject the null hypothesis         
    print("We reject the null hypothesis")
else:
    print("We can't reject the null hypothesis")

"""
We have two data sets: the visit depth for the website from different groups of users for summer and autumn months. Test the hypothesis that the visit depths for the websites are equal. For instance, maybe in the summer visitors don't get as deep into the content, which would be something to consider when planning an ad campaign for the summer months. Let the significance level be 0.05.

We don't expect the variances to be the same, so set the equal_var parameter to False. You can run np.var(pages_per_session_autumn) etc. to check the variance of the set."""

from scipy import stats as st
import numpy as np

pages_per_session_autumn = [7.1, 7.3, 9.8, 7.3, 6.4, 10.5, 8.7, 
                            17.5, 3.3, 15.5, 16.2, 0.4, 8.3, 
                            8.1, 3.0, 6.1, 4.4, 18.8, 14.7, 16.4, 
                            13.6, 4.4, 7.4, 12.4, 3.9, 13.6, 
                            8.8, 8.1, 13.6, 12.2]
pages_per_session_summer = [12.1, 24.3, 6.4, 19.9, 19.7, 12.5, 17.6, 
                            5.0, 22.4, 13.5, 10.8, 23.4, 9.4, 3.7, 
                            2.5, 19.8, 4.8, 29.0, 1.7, 28.6, 16.7, 
                            14.2, 10.6, 18.2, 14.7, 23.8, 15.9, 16.2, 
                            12.1, 14.5]

alpha = 0.05 # your code: set a critical statistical significance level

results = st.ttest_ind(pages_per_session_autumn, pages_per_session_summer, equal_var=False) # your code: test the hypothesis that the means of the two independent populations are equal

print('p-value:', # your code: print the p-value you get)

if (results.pvalue < alpha):# your code: compare the p-value you get with the significance level):
    print("We reject the null hypothesis")
else:
    print("We can't reject the null hypothesis")

scipy.stats.test_rel(array1, array2)
from scipy import stats as st
import numpy as np

before = [157, 114, 152, 355, 155, 513, 299, 268, 164, 320, 
                    192, 262, 506, 240, 364, 179, 246, 427, 187, 431, 
                    320, 193, 313, 347, 312, 92, 177, 225, 242, 312]

after = [282, 220, 162, 226, 296, 479, 248, 322, 298, 418, 
                 552, 246, 251, 404, 368, 484, 358, 264, 359, 410, 
                 382, 350, 406, 416, 438, 364, 283, 314, 420, 218]

alpha = 0.05  # significance level

results = st.ttest_rel(before, after)  # test the hypothesis that the means of the two related populations are equal

print('p-value:', results.pvalue)

if (results.pvalue < alpha):
    print("We reject the null hypothesis")
else:
    print("We can't reject the null hypothesis")

# Calculate the mean and standard deviation of the before and after samples
mean_before = np.mean(before)
std_before = np.std(before)

mean_after = np.mean(after)
std_after = np.std(after)

print("Before - Mean:", mean_before, ", Std Dev:", std_before)
print("After - Mean:", mean_after, ", Std Dev:", std_after)

"""
We have two datasets: the time one set of users spent in their personal account areas on a website, recorded before and after the personal account was redesigned. Test the hypothesis that the time they spend there changed (increased or decreased) after the redesign."""
from scipy import stats as st
import numpy as np

time_before = [1732, 1301, 1540, 2247, 1632, 1550, 754, 1946, 1889, 
          2748, 1349, 1648, 1665, 2416, 1470, 1681, 1868, 1629, 
          1271, 1633, 2131, 942, 1599, 1127, 2200, 661, 1207, 
          1737, 2410, 1486]

time_after = [955, 2577, 360, 139, 1618, 990, 644, 1796, 1487, 949, 472, 
         1906, 1758, 1258, 2554, 612, 309, 1864, 1294, 1487, 1164, 1559, 
         491, 2286, 1270, 2069, 1553, 1629, 1704, 1623]

alpha = 0.05 # your code: set a critical statistical significance level

results = st.ttest_rel(time_before, time_after) # your code: conduct the test and calculate the p-value

print('p-value:', results.pvalue)

if (results.pvalue < alpha):# your code: compare the p-value to the statistical significance level):
    print("We reject the null hypothesis")
else:
    print("We can't reject the null hypothesis")

"""
We have two datasets: the number of bullets purchased by avid players of an online game, before and after introducing a game mechanic that provided incentives for firing in bursts. Test the hypothesis that players started using more bullets after the new feature was introduced."""

from scipy import stats as st
import numpy as np
import pandas as pd

bullets_before = [821, 1164, 598, 854, 455, 1220, 161, 1400, 479, 215, 
          564, 159, 920, 173, 276, 444, 273, 711, 291, 880, 
          892, 712, 16, 476, 498, 9, 1251, 938, 389, 513]

bullets_after = [904, 220, 676, 459, 299, 659, 1698, 1120, 514, 1086, 1499, 
         1262, 829, 476, 1149, 996, 1247, 1117, 1324, 532, 1458, 898, 
         1837, 455, 1667, 898, 474, 558, 639, 1012]

print('mean before:', pd.Series(bullets_before).mean())
print('mean after:', pd.Series(bullets_after).mean())

alpha = # your code: set a critical statistical significance level

results = st.ttest_rel(
    bullets_before, 
    bullets_after)

print('p-value:', results.pvalue) # your code: print the p-value you get)

if (results.pvalue < alpha) & (pd.Series(bullets_after).mean() > pd.Series(bullets_before).mean()):# your code: compare the p-value to the statistical significance):
    print("We reject the null hypothesis")
else:
    print("We can't reject the null hypothesis")


merged_data.groupby(by="user_id").agg(['mean', 'median'])

File path: 

/datasets/megaline_calls.csv Download dataset

/datasets/megaline_internet.csv Download dataset

/datasets/megaline_messages.csv Download dataset

/datasets/megaline_plans.csv Download dataset

/datasets/megaline_users.csv Download dataset

# Loading all the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Load the datasets
calls = pd.read_csv('/datasets/megaline_calls.csv')
internet = pd.read_csv('/datasets/megaline_internet.csv')
messages = pd.read_csv('/datasets/megaline_messages.csv')
plans = pd.read_csv('/datasets/megaline_plans.csv')
users = pd.read_csv('/datasets/megaline_users.csv')
# Display the first few rows of each dataset
print("Calls dataset:")
print(calls.head())
print("\nInternet dataset:")
print(internet.head())
print("\nMessages dataset:")
print(messages.head())
print("\nPlans dataset:")
print(plans.head())
print("\nUsers dataset:")
print(users.head())
# Check for missing values in each dataset
print("\nMissing values in calls dataset:")
print(calls.isnull().sum())
print("\nMissing values in internet dataset:")
print(internet.isnull().sum())
print("\nMissing values in messages dataset:")
print(messages.isnull().sum())
print("\nMissing values in plans dataset:")
print(plans.isnull().sum())
print("\nMissing values in users dataset:")
print(users.isnull().sum())
# Check the data types of each column in the calls dataset
print("\nData types in calls dataset:")
print(calls.dtypes)
# Check the data types of each column in the internet dataset
print("\nData types in internet dataset:")
print(internet.dtypes)
# Check the data types of each column in the messages dataset
print("\nData types in messages dataset:")
print(messages.dtypes)
# Check the data types of each column in the plans dataset
print("\nData types in plans dataset:")
print(plans.dtypes)
# Check the data types of each column in the users dataset
print("\nData types in users dataset:")
print(users.dtypes)
# Check the unique values in the 'call_date' column of the calls dataset
print("\nUnique values in 'call_date' column of calls dataset:")
print(calls['call_date'].unique())
# Check the unique values in the 'session_date' column of the internet dataset
print("\nUnique values in 'session_date' column of internet dataset:")
print(internet['session_date'].unique())
# Check the unique values in the 'message_date' column of the messages dataset
print("\nUnique values in 'message_date' column of messages dataset:")
print(messages['message_date'].unique())
# Check the unique values in the 'start_date' column of the users dataset
print("\nUnique values in 'start_date' column of users dataset:")
print(users['start_date'].unique())
# Check the unique values in the 'end_date' column of the users dataset
print("\nUnique values in 'end_date' column of users dataset:")
print(users['end_date'].unique())
# Check the unique values in the 'plan_name' column of the plans dataset
print("\nUnique values in 'plan_name' column of plans dataset:")
print(plans['plan_name'].unique())
# Check the unique values in the 'user_id' column of each dataset
print("\nUnique values in 'user_id' column of calls dataset:")
print(calls['user_id'].unique())
print("\nUnique values in 'user_id' column of internet dataset:")
print(internet['user_id'].unique())
print("\nUnique values in 'user_id' column of messages dataset:")
print(messages['user_id'].unique())
print("\nUnique values in 'user_id' column of plans dataset:")
print(plans['user_id'].unique())
print("\nUnique values in 'user_id' column of users dataset:")
print(users['user_id'].unique())
# Print a sample of data for plans
print("\nSample data for plans dataset:")
print(plans.sample(5))

for df in [calls, internet, messages, users]:
    df['call_date'] = pd.to_datetime(df['call_date'], errors='coerce')
    df['session_date'] = pd.to_datetime(df['session_date'], errors='coerce')
    df['message_date'] = pd.to_datetime(df['message_date'], errors='coerce')
    df['reg_date'] = pd.to_datetime(df['reg_date'], errors='coerce')
    df['churn_date'] = pd.to_datetime(df['churn_date'], errors='coerce')
plans['plan_name'] = plans['plan_name'].astype('category')
plans['usd_monthly_pay'] = plans['usd_monthly_pay'].astype(float)

# Aggregate calls
monthly_minutes = calls.groupby([calls['user_id'], calls['call_date'].dt.to_period('M')])['duration'].sum().reset_index(name='monthly_minutes')
monthly_minutes['call_date'] = monthly_minutes['call_date'].dt.to_timestamp()

# Aggregate internet
monthly_mb_used = internet.groupby([internet['user_id'], internet['session_date'].dt.to_period('M')])['mb_used'].sum().reset_index(name='monthly_mb_used')
monthly_mb_used['session_date'] = monthly_mb_used['session_date'].dt.to_timestamp()

# Aggregate messages (count per month)
monthly_messages = messages.groupby([messages['user_id'], messages['message_date'].dt.to_period('M')]).size().reset_index(name='monthly_messages')
monthly_messages['message_date'] = monthly_messages['message_date'].dt.to_timestamp()

# Merge into a single usage DataFrame
usage = monthly_minutes.merge(monthly_mb_used, on=['user_id', 'call_date'], how='outer') \
                      .merge(monthly_messages, on=['user_id', 'call_date'], how='outer') \
                      .rename(columns={'call_date': 'month'})
usage = usage.fillna(0)  # Replace NaN with 0 for no usage

# Merge usage with users and plans
user_plans = users.merge(plans, left_on='plan', right_on='plan_name', how='left')
monthly_data = usage.merge(user_plans[['user_id', 'messages_included', 'mb_per_month_included', 'minutes_included', 
                                      'usd_monthly_pay', 'usd_per_gb', 'usd_per_message', 'usd_per_minute', 'plan_name']], 
                          on='user_id', how='left')

# Calculate overages
monthly_data['messages_overage'] = monthly_data['monthly_messages'] - monthly_data['messages_included']
monthly_data['mb_overage'] = monthly_data['monthly_mb_used'] - monthly_data['mb_per_month_included']
monthly_data['minutes_overage'] = monthly_data['monthly_minutes'] - monthly_data['minutes_included']
monthly_data[['messages_overage', 'mb_overage', 'minutes_overage']] = monthly_data[['messages_overage', 'mb_overage', 'minutes_overage']].clip(lower=0)  # No negative overage

monthly_data['total_monthly_cost'] = monthly_data['usd_monthly_pay'] + \
                                     (monthly_data['mb_overage'] / 1024 * monthly_data['usd_per_gb']) + \
                                     (monthly_data['messages_overage'] * monthly_data['usd_per_message']) + \
                                     (monthly_data['minutes_overage'] * monthly_data['usd_per_minute'])

internet['gb_used'] = internet['mb_used'] / 1024

import pandas as pd

# Convert date columns to datetime
for df in [calls, internet, messages, users]:
    df['call_date'] = pd.to_datetime(df['call_date'], errors='coerce')
    df['session_date'] = pd.to_datetime(df['session_date'], errors='coerce')
    df['message_date'] = pd.to_datetime(df['message_date'], errors='coerce')
    df['reg_date'] = pd.to_datetime(df['reg_date'], errors='coerce')
    df['churn_date'] = pd.to_datetime(df['churn_date'], errors='coerce')

plans['plan_name'] = plans['plan_name'].astype('category')
plans['usd_monthly_pay'] = plans['usd_monthly_pay'].astype(float)

# Add gb_used
internet['gb_used'] = internet['mb_used'] / 1024

# Aggregate monthly usage
monthly_minutes = calls.groupby([calls['user_id'], calls['call_date'].dt.to_period('M')])['duration'].sum().reset_index(name='monthly_minutes')
monthly_minutes['call_date'] = monthly_minutes['call_date'].dt.to_timestamp()

monthly_mb_used = internet.groupby([internet['user_id'], internet['session_date'].dt.to_period('M')])['mb_used'].sum().reset_index(name='monthly_mb_used')
monthly_mb_used['session_date'] = monthly_mb_used['session_date'].dt.to_timestamp()

monthly_messages = messages.groupby([messages['user_id'], messages['message_date'].dt.to_period('M')]).size().reset_index(name='monthly_messages')
monthly_messages['message_date'] = monthly_messages['message_date'].dt.to_timestamp()

usage = monthly_minutes.merge(monthly_mb_used, on=['user_id', 'call_date'], how='outer') \
                      .merge(monthly_messages, on=['user_id', 'call_date'], how='outer') \
                      .rename(columns={'call_date': 'month'})
usage = usage.fillna(0)

# Merge with user plans
user_plans = users.merge(plans, left_on='plan', right_on='plan_name', how='left')
monthly_data = usage.merge(user_plans[['user_id', 'messages_included', 'mb_per_month_included', 
                                      'minutes_included', 'usd_monthly_pay', 'usd_per_gb', 
                                      'usd_per_message', 'usd_per_minute']], on='user_id', how='left')

# Add derived features
monthly_data['messages_overage'] = (monthly_data['monthly_messages'] - monthly_data['messages_included']).clip(lower=0)
monthly_data['mb_overage'] = (monthly_data['monthly_mb_used'] - monthly_data['mb_per_month_included']).clip(lower=0)
monthly_data['minutes_overage'] = (monthly_data['monthly_minutes'] - monthly_data['minutes_included']).clip(lower=0)

monthly_data['total_monthly_cost'] = monthly_data['usd_monthly_pay'] + \
                                    (monthly_data['mb_overage'] / 1024 * monthly_data['usd_per_gb']) + \
                                    (monthly_data['messages_overage'] * monthly_data['usd_per_message']) + \
                                    (monthly_data['minutes_overage'] * monthly_data['usd_per_minute'])

users['is_active'] = users['churn_date'].isna()
reference_date = pd.to_datetime('2018-12-31')
users['tenure_months'] = ((reference_date - users['reg_date']) / pd.Timedelta(days=30)).astype(int)

def categorize_age(age):
    if age <= 30: return '18-30'
    elif age <= 50: return '31-50'
    else: return '51+'
users['age_group'] = users['age'].apply(categorize_age)

# Verify
print(monthly_data.head())
print(users.head())

print("NaT counts:")
print(calls['call_date'].isna().sum(), internet['session_date'].isna().sum(), 
      messages['message_date'].isna().sum(), users['reg_date'].isna().sum())

print("Plan mismatches:", set(users['plan']) - set(plans['plan_name']))
# Print the general/summary information about the users' DataFrame
print("\nUsers DataFrame Info:")
print(users.info())
# Print the first few rows of the users DataFrame
print("\nUsers DataFrame Head:")
print(users.head())
# Print the unique values in the 'plan' column of the users DataFrame
print("\nUnique Plans in Users DataFrame:")
print(users['plan'].unique())
# Print the unique values in the 'plan_name' column of the plans DataFrame
print("\nUnique Plans in Plans DataFrame:")
print(plans['plan_name'].unique())

# Print a sample of data for users
print("\nSample data for users DataFrame:")
print(users.sample(5))

# Print the general/summary information about the calls' DataFrame
print("\nCalls DataFrame Info:")
print(calls.info())

# Print a sample of data for calls
print("\nSample data for calls DataFrame:")
print(calls.sample(5))

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy.stats import ttest_ind, levene

# Average call duration per plan per month
monthly_calls = calls.merge(users[['user_id', 'plan']], on='user_id')
monthly_calls['month'] = monthly_calls['call_date'].dt.to_period('M').dt.to_timestamp()
avg_call_duration = monthly_calls.groupby(['plan', 'month'])['duration'].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='month', y='duration', hue='plan', data=avg_call_duration)
plt.title('Average Call Duration per Plan per Month (2018)')
plt.xlabel('Month')
plt.ylabel('Average Call Duration (minutes)')
plt.xticks(rotation=45)
plt.show()

# Monthly minutes histogram
plt.figure(figsize=(10, 6))
sns.histplot(data=monthly_data, x='monthly_minutes', hue='plan_name', bins=30)
plt.title('Distribution of Monthly Call Minutes by Plan (2018)')
plt.xlabel('Monthly Minutes')
plt.ylabel('Frequency')
plt.show()

# Statistics
call_stats = monthly_data.groupby('plan_name')['monthly_minutes'].agg(['mean', 'var']).reset_index()
print("Call Minutes Statistics by Plan:")
print(call_stats)

# Boxplot
plt.figure(figsize=(8, 6))
sns.boxplot(x='plan_name', y='monthly_minutes', data=monthly_data)
plt.title('Monthly Call Minutes Distribution by Plan')
plt.xlabel('Plan')
plt.ylabel('Monthly Minutes')
plt.show()

# Print the general/summary information about the messages' DataFrame
print("\nMessages DataFrame Info:")
print(messages.info())

# Print a sample of data for messages
print("\nSample data for messages DataFrame:")
print(messages.sample(5))

# Print the general/summary information about the internet DataFrame
print("\nInternet DataFrame Info:")
print(internet.info())

# Print a sample of data for internet
print("\nSample data for internet DataFrame:")
print(internet.sample(5))

# Calculate the number of calls made by each user per month. Save the result.
calls_per_user = calls.groupby([calls['user_id'], calls['call_date'].dt.to_period('M')]).size().reset_index(
print(calls_per_user.head())

# Calculate the amount of minutes spent by each user per month. Save the result.
minutes_per_user = calls.groupby([calls['user_id'], calls['call_date'].dt.to_period('M')])['duration'].sum().reset_index(name='monthly_minutes')
print(minutes_per_user.head())

# Calculate the number of messages sent by each user per month. Save the result.
messages_per_user = messages.groupby([messages['user_id'], messages['message_date'].dt.to_period('M')]).size().reset_index(name='monthly_messages')

# Calculate the volume of internet traffic used by each user per month. Save the result.
internet_per_user = internet.groupby([internet['user_id'], internet['session_date'].dt.to_period('M')])['mb_used'].sum().reset_index(name='monthly_mb_used')
print(internet_per_user.head())

# Compare average duration of calls per each plan per each distinct month. Plot a bar plat to visualize it.
avg_duration_per_plan = calls.groupby([calls['call_date'].dt.to_period('M'), 'user_id'])['duration'].mean().reset_index()
avg_duration_per_plan = avg_duration_per_plan.merge(users[['user_id', 'plan']], on='user_id')
plt.figure(figsize=(12, 6))
sns.barplot(x='call_date', y='duration', hue='plan', data=avg_duration_per_plan)
plt.title('Average Call Duration per Plan per Month')
plt.xlabel('Month')
plt.ylabel('Average Duration (minutes)')
plt.xticks(rotation=45)
plt.show()

# Compare the number of minutes users of each plan require each month. Plot a histogram.
plt.figure(figsize=(12, 6))
sns.histplot(data=monthly_data, x='monthly_minutes', hue='plan_name', bins=30)
plt.title('Distribution of Monthly Call Minutes by Plan (2018)')
plt.xlabel('Monthly Minutes')
plt.ylabel('Frequency')
plt.show()

# Calculate the mean and the variance of the monthly call duration
call_stats = monthly_data.groupby('plan_name')['monthly_minutes'].agg(['mean', 'var']).reset_index()
print("Call Minutes Statistics by Plan:")
print(call_stats)
# Plot a boxplot to visualize the distribution of monthly call minutes by plan
plt.figure(figsize=(12, 6))
sns.boxplot(x='plan_name', y='monthly_minutes', data=monthly_data)
plt.title('Distribution of Monthly Call Minutes by Plan (2018)')
plt.xlabel('Plan')
plt.ylabel('Monthly Minutes')
plt.show()

# Compare the number of messages users of each plan tend to send each month
plt.figure(figsize=(12, 6))
sns.histplot(data=monthly_data, x='monthly_messages', hue='plan_name', bins=30)
plt.title('Distribution of Monthly Messages by Plan (2018)')
plt.xlabel('Monthly Messages')
plt.ylabel('Frequency')
plt.show()

# Compare the amount of internet traffic consumed by users per plan
plt.figure(figsize=(12, 6))
sns.histplot(data=monthly_data, x='monthly_gb_used', hue='plan_name', bins=30)
plt.title('Distribution of Monthly Internet Traffic by Plan (2018)')
plt.xlabel('Monthly GB Used')
plt.ylabel('Frequency')
plt.show()

import numpy as np
from matplotlib import pyplot as plt

rad = np.linspace(0, 2 * np.pi, 200)

x = np.sin(rad)**3
y = 20 * np.cos(rad) - 10 * np.cos(2 * rad) - 5 * np.cos(3 * rad) - 2 * np.cos(4 * rad)

plt.plot(x, y)
plt.show()

import pandas as pd
print(pd.__version__)

from matplotlib import pyplot as plt
print(plt.__version__) #error

from matplotlib import pyplot as plt
print(matplotlib.__version__) #error

~$ ls -ra
~$ ls -r work
~$ ls -r work/visualStudio.py
~$ mkdir -p my_parent_dir/my_sub_dir
~$ mkdir -p -v my_parent_dir/my_sub_dir
mkdir --help
~$ rm -d my_new_directory
~$ rm file1 file2 file3
~$ rm -d -i my_new_directory

if x%2 == 0:
    print("x is even")
else:
    print("x is odd")

