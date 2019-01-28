# Filter out duplicate items

items = ['apple', 'orange','pear','apple', 'orange','pear','apple', 'orange','pear','apple', 'orange','pear','apple', 'orange','pear','apple', 'orange','pear']

filter = dict()

for key in items:
    filter[key] = 0

result = set(filter.keys())
print(result)