import spacy
from nltk import sent_tokenize

nlp = spacy.load("en_core_web_trf")

def analyze_text(text):
    doc = nlp(text)
    return {
        "doc": doc,
        "sentences": list(doc.sents),
        "entities": [(ent.text, ent.label_) for ent in doc.ents],
        "noun_chunks": [chunk.text for chunk in doc.noun_chunks],
        "lemmas": [token.lemma_ for token in doc],
        "pos": [(token.text, token.pos_) for token in doc],
        "deps": [(token.text, token.dep_, token.head.text) for token in doc]
    }