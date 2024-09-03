import random
from collections import defaultdict

# Example corpus (can be replaced with any text)
text = """Your text corpus goes here."""

# Tokenize the text into words
def tokenize_words(text):
    return text.split()

# Tokenize the text into characters
def tokenize_chars(text):
    return list(text)

# Build the Markov chain for words or characters
def build_markov_chain(tokens, order=1):
    markov_chain = defaultdict(list)

    for i in range(len(tokens) - order):
        state = tuple(tokens[i:i + order])
        next_token = tokens[i + order]
        markov_chain[state].append(next_token)

    return markov_chain

# Generate text
def generate_text(chain, length=100, seed=None, order=1):
    if seed is None:
        seed = random.choice(list(chain.keys()))

    generated_tokens = list(seed)
    current_state = seed

    for _ in range(length - len(seed)):
        next_token = random.choice(chain.get(current_state, ['']))
        generated_tokens.append(next_token)
        current_state = tuple(generated_tokens[-order:])

    return ' '.join(generated_tokens) if type(seed[0]) == str else ''.join(generated_tokens)

# Choose whether to use words or characters
use_words = True  # Set to False for character-based model

if use_words:
    tokens = tokenize_words(text)
else:
    tokens = tokenize_chars(text)

order = 1  # Order of the Markov chain
markov_chain = build_markov_chain(tokens, order=order)

# Generate text
seed = random.choice(list(markov_chain.keys()))
generated_text = generate_text(markov_chain, length=100, seed=seed, order=order)
print(generated_text)
