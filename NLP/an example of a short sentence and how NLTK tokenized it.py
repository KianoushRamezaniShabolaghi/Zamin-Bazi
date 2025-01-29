import nltk
from nltk.tokenize import word_tokenize

# Download NLTK data files (only the first time you run it)
nltk.download('punkt')

# A short sentence
sentence = "Hello, world! How's everything going?"

# Tokenize the sentence
tokens = word_tokenize(sentence)

# Print the tokens
print("Tokens:", tokens)
