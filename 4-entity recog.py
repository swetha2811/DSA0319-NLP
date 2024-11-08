import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
nltk.download('maxent_ne_chunker')
nltk.download('words')
text = "Harvard University, located in Cambridge, Massachusetts, is a prestigious institution."
tokens = word_tokenize(text)
tagged = pos_tag(tokens)
named_entities = ne_chunk(tagged)
resolved_text = []
for entity in named_entities:
    if isinstance(entity, nltk.tree.Tree):
        entity_type = entity.label()
        if entity_type == 'GPE':
            resolved_text.append('LOCATION')
        else:
            resolved_text.append(entity[0][0])
    else:
        resolved_text.append(entity[0])
print("Resolved Text:", ' '.join(resolved_text))
