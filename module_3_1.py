calls = 0

def count_calls():
    global calls
    calls = calls + 1

def string_info(string):
    count_calls()
    return [len(string) , string.upper(), string.lower()]

def is_contains(string, list_to_search):
    count_calls()
    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].lower()
    if string.lower() in list_to_search:
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(string_info('Solntse'))
print(string_info('Zvezda'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(is_contains('banana', ['baNaNa', 'BaNaN', 'sbanans']))
print(is_contains('Kosmos', ['KoSmOs', 'cyclic', 'cocmoc',]))
print(calls)

