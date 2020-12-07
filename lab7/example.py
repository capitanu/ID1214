import nltk

sentence = "The crackers run."
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)



from nltk.parse.generate import generate, demo_grammar
from nltk import CFG
grammar = CFG.fromstring("""
S -> NP VBZ | NB JJ | PDet NNP VBP RB
NP -> DetCap N 
PP -> P NP
VBP -> 'run' | 'is' ADJ
VBZ -> 'likes' Det N | 'runs' RB | 'runs' | 'eats' | 'likes' Det NNB
VPP -> 'are'
Det -> 'the' | 'a' | 'that'
DetCap -> 'The' | 'A'
PDet -> 'Those' | 'The'
N -> 'girl' | 'boy' | 'dog'
NNP -> 'boys'
NNB -> 'crackers' | 'house'
NB -> PDet 'crackers' VPP | DetCap 'house is'
RB -> 'fast'
JJ -> 'good' | 'big'
ADJ -> 'happy'
""")

# The girl likes the dog. 
# A boy likes that house. 
# The crackers are good. 
# The girl eats. 
# The dog runs.
# Those boys run fast.
# The house is big.
# The dog is happy.

for sentence in generate(grammar, n=1000):
    print(' '.join(sentence))
