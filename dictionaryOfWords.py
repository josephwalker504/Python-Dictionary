# Create an empty dictionary
animal = dict()
# Add key/value pairs
animal["name"] = "Kevin"
animal["breed"] = "Bulldog"
animal["age"] = 5

# Create the dictionary with key/value pairs and assign to variable
# animal = {
#     "name": "Kevin",
#     "breed": "Bulldog",
#     "age": 5
# }

# for (key, value) in animal.items():
#     print(f"{key}: {value}")

# Output
# name: Kevin
# breed: Bulldog
# age: 5


# You are going to build a Python Dictionary to represent an actual dictionary. Each key/value pair within 
# the Dictionary will contain a single word as the key, and a definition as the value. Below is some starter code. 
# You need to add a few more words and definitions to the dictionary.
# After you have added them, use square bracket notation to output the definition of two of the words to the console.
# Lastly, use the for in loop to iterate over the KeyValuePairs and display the entire dictionary to the console.


"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
# word_definitions = dict()
# word_definitions = {}

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""
word_definitions = {
"stop":  "To cease movement",
"go": "To start movement",
"confused": "Unable to think clearly",
"laughter": "the action or sound of laughing",
"joyful": "feeling,expressing,or causing great pleasure and happiness",
}
print(word_definitions)


"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""
print(word_definitions["stop"])
print(word_definitions["joyful"])


"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""