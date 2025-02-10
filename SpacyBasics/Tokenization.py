pip install spacy 
import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
for token in doc:
    print(token.text)

doc2 = nlp("Apple isn't looking at buying U.K. of https://www.ai-research.com startup for $1 billion")
for token in doc2:
    print(token.text)

doc3 = nlp(u"Visit https://openai.com for AI updates! Dr. John’s work—worth $1.2M—was published on Jan. 5, 2024.")
for token in doc3:
    print(token.text)

len1=len(doc3)
print(len1)
len2=len(doc3.vocab)

doc4 = nlp(u"Elon Musk's latest tweet (Jan. 5, 2024) went viral! Visit https://tesla.com for details—$TSLA stock soared 12.5%!")
for token in doc4:
    print(token.text,end='|')

for ent in doc4.ents:
    print(ent)
    print(ent.text, ent.label_)
    print(str(spacy.explain(ent.label_)))
    print('\n')

doc5 = nlp(u"Alice bought a MacBook from Amazon and visited https://apple.com.")
for t in doc5.noun_chunks:
    print(t)

from spacy import displacy

doc6 = nlp(u"Apple is looking at buying U.K. startup for $1 billion")

displacy.render(doc6, style='dep', jupyter=True, options={'distance': 90})

doc7 = nlp(u"Apple is looking at buying U.K. startup for $1 billion")

displacy.render(doc7, style='ent', jupyter=True)

doc7 = nlp(u"Apple is looking at buying U.K. startup for $1 billion")
displacy.serve(doc7, style='dep')
# for visualization, open http://127.0.0.1:THE PORT NUMBER/ in browser  and copy the text from the terminal
