calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    list = [len(string), string.upper(), string.lower()]
    my_tuple = tuple(list)
    return my_tuple

def is_contains(string, list_to_search):
    count_calls()
    for word in list_to_search:
        word = word.lower()
        string = string.lower()
        if word == string:
            return True
    return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)

