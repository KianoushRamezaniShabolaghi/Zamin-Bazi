import sentencepiece as spm

# Train a SentencePiece model (this is only needed once)
# Normally, you'd use a pre-trained model, but here's an example of training one for demonstration.
with open("sample.txt", "w") as f:
    f.write("Hello, world! How's everything going?\n")

spm.SentencePieceTrainer.train(input='sample.txt', model_prefix='example', vocab_size=24)

# Load the trained SentencePiece model
sp = spm.SentencePieceProcessor()
sp.load("example.model")

# A short sentence
sentence = "Hello, world! How's everything going?"

# Tokenize the sentence
tokens = sp.encode(sentence, out_type=str)

# Print the tokens
print("Tokens:", tokens)

# Convert tokens back to the original text
detokenized_sentence = sp.decode(sp.encode(sentence))
print("Detokenized:", detokenized_sentence)
