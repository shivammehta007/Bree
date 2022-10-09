import benepar
import spacy

from Bree import Bree, Node


def get_nouns(garbage, constituents):
        roots = []
        for constituent in constituents:
            for i, t in enumerate(constituent):
                if t.pos_ in garbage:
                    continue
                elif t.pos_ == 'NOUN' and len(constituent) == 1:
                    noun = Node(t)
                    roots.append(noun)
        return roots


def build_bree(parsed_sentence, reverse=True, garbage=set(['PUNCT', 'DET', 'CCONJ'])):

    if reverse:
        constituents = list(reversed(list(list(parsed_sentence.sents)[0]._.constituents)))

    roots = get_nouns(garbage, constituents)
    
    brees = [Bree(root) for root in roots]
    
    for bree in brees:
        for constituent in constituents:
            bree.push(constituent)



if __name__ == '__main__':    

    nlp = spacy.load('en_core_web_sm')
    nlp.add_pipe('benepar', config={'model': 'benepar_en3'})
    doc = nlp('A black and grey dog with a hat watching a man by the pool.')
    
    build_bree(doc)
