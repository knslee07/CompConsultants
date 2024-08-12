

from __future__ import unicode_literals, print_function

import plac
import random
import warnings
from pathlib import Path
import spacy
from spacy.util import minibatch, compounding
from TRAIN_DATA import TRAIN_DATA # train examples are in this py file.

# test the saved model
#print("Loading from", output_dir)
nlp2 = spacy.load('CC_model') # this loads the CC_model in this folder that I trained. 
# Check the classes have loaded back consistently
#assert nlp2.get_pipe("ner").move_names == move_names

test_text='The Committee has engaged Frederic W. Cook & Co., Inc. (“F.W. Cook”) to act as its compensation consultant. F.W. Cook’s sole engagement for the Company is as compensation consultant to the Committee. It did not retain any other compensation consultants like Kwan. Microsoft did not retain any compensation consultants.'
# As of Jan 22, 2021, it currently cannot catch Towers Watson.
doc2 = nlp2(test_text)
for ent in doc2.ents:
    print(ent.label_, ent.text)



## add rule-based method for better results

from spacy.pipeline import EntityRuler
# Initialize
ruler = EntityRuler(nlp2)

CC=[
    'Deloitte','Aon','Aon Hewitt','Compensation Advisory Partners','Mercer HR Consulting',
   'Hewitt','Compensia','Exequity','FPL Advisory Group Co.','Frederic W. Cook & Co., Inc.', 'Frederic W. Cook & Co.','F.W. Cook','F. W. Cook', 'Cook & Co.',
    'FTI Consulting Inc.','Hay Group', 'The Hay Group','Hewitt Associates','Longecker & Associates',
    'Mercer','Mercer Human Resources Consulting','Mercer Human Resource Consulting','Meridian','Meridian Compensation',
    'Pay Governance','Pearl Meyer & Partners','Radford','Semler Brossy Consulting',
    'Semler Brossy','Steven Hall & Partners','Towers Watson','Watson Wyatt','Towers Perrin','Watson Wyatt Worldwide',
    'CCA Strategies','Total Rewards Strategies'
]
patterns=[]
for item in CC:
    pattern={"label": "CC", "pattern": item}
    patterns.append(pattern)

# Add entity ruler to the NLP pipeline. 
ruler.add_patterns(patterns)
nlp2.add_pipe(ruler)

# test again with rule-based addition.
doc2 = nlp2(test_text)
for ent in doc2.ents:
    print(ent.label_, ent.text)
'''

# (Jan22, 2021) this works better.

