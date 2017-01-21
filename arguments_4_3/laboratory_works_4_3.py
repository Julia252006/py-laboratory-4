
# Create string variable word
# Create dictionary variable ids
# Create function_4_1 that include at least 2 arguments_4_3 word and name from ids dictionary
# Function also should have one default argument age
# If additional arguments will added to function call it should work properly
# During first function calling use unpack arguments from dictionary ids
# During second call use ids key value and some range of values

print('\n\Laboratory Work 4.3')

word = 'Found name:'
ids = {'name':"Alice", 'age':27}

def intersection(word,name,*args,age=None):
    print(word, name)
    print('Age:',age)
    print(args)

intersection(word, **ids)
intersection(word, ids['name'], *list(range(10)))
