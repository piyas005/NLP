# pip inssall spacy
import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp(u'Tesla is looking at buying U.S. startup for $6 million')
for token in doc:
    print(token.text, token.pos_, token.dep_)

nlp.pipeline
nlp.pipe_names
doc[0].pos_
type(doc)
sen = nlp.(u"this is the first sentence. this is the second sentence. this is the third sentence.")
for sentence in sen.sents:
    print(sentence)
