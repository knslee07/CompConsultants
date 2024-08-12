# (Jan 16, 2021)
"""
emulates train_new_entity_type.py from Spacy
to train CC
"""

# to-do
# read spacy
# compare the ways to train in the book and the website.
# find out ways to load the "CC_model" so that you do not need to retrain the model unless you add more examples
# looks like I can just load the model and do it easily. READ the book


from __future__ import unicode_literals, print_function
#from spacy.train_new_entity_type import TRAIN_DATA

import plac
import random
import warnings
from pathlib import Path
import spacy
from spacy.util import minibatch, compounding
from TRAIN_DATA import TRAIN_DATA  # train examples are in this py file.

# new entity label
LABEL = "CC"

try:
    if spacy.require_gpu():
        print('GPU used')
except:
    print('GPU not used')

@plac.annotations(
    model=("Model name. Defaults to blank 'en' model.", "option", "m", str),
    new_model_name=("New model name for model meta.", "option", "nm", str),
    output_dir=("Optional output directory", "option", "o", Path),
    n_iter=("Number of training iterations", "option", "n", int),
)
def main(model=None, new_model_name="CC", output_dir="CC", n_iter=5000):
    # change output_dir to "CC" after training is finished to save it to
    """Set up the pipeline and entity recognizer, and train the new entity."""
    random.seed(0)

    # if using an existing model
    # use a pre-loaded model lead to a better result than creating a blank model.
    model = 'en_core_web_lg'

    if model is not None:
        nlp = spacy.load(model)  # load existing spaCy model
        print("Loaded model '%s'" % model)
    else:
        # let's use built-in model, not a blank one.
        # nlp=spacy.load("en_core_web_lg")
        #print ('loaded lg model')
        nlp = spacy.blank("en")  # create blank Language class
        print("Created blank 'en' model")

    # Add entity recognizer to model if it's not in the pipeline
    # nlp.create_pipe works for built-ins that are registered with spaCy
    if "ner" not in nlp.pipe_names:
        ner = nlp.create_pipe("ner")
        nlp.add_pipe(ner)
    # otherwise, get it, so we can add labels to it
    else:
        ner = nlp.get_pipe("ner")

    ner.add_label(LABEL)  # add new entity label to entity recognizer
    # Adding extraneous labels shouldn't mess anything up
    ner.add_label("VEGETABLE")

    if model is None:
        optimizer = nlp.begin_training()
    else:
        # optimizer = nlp.resume_training() # This line is from Spacy
        # This line is from NLP with Spacy, Ch. 10. It says this builds on the existing model.
        optimizer = nlp.entity.create_optimizer()

    move_names = list(ner.move_names)
    # get names of other pipes to disable them during training
    pipe_exceptions = ["ner", "trf_wordpiecer", "trf_tok2vec"]
    other_pipes = [
        pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]

    # only train NER
    with nlp.disable_pipes(*other_pipes), warnings.catch_warnings():
        # show warnings for misaligned entity spans once
        warnings.filterwarnings("once", category=UserWarning, module='spacy')

        sizes = compounding(1.0, 4.0, 1.001)
        # batch up the examples using spaCy's minibatch
        for itn in range(n_iter):
            random.shuffle(TRAIN_DATA)
            batches = minibatch(TRAIN_DATA, size=sizes)
            losses = {}
            for batch in batches:
                texts, annotations = zip(*batch)
                nlp.update(texts, annotations, sgd=optimizer,
                           drop=0.25, losses=losses)
            print("Losses", losses)

    # test the trained model
    test_text = 'Determining Non-Employee Director Compensation.  The Compensation Committee annually reviews our non-employee directors’ compensation. Based on this review, the Compensation Committee recommends any changes to our non-employee directors’ compensation to the Board for approval. In addition, the Board and Compensation Committee periodically evaluate how our director pay levels and pay policies compare to the competitive market. In fiscal 2014, the Board and Compensation Committee reviewed competitive market data compiled by Compensia, Inc., the Compensation Committee’s independent compensation consultant (“Compensia”). While competitive market data is important to the evaluation of the directors’ compensation, it is just one of several factors considered by the Board in approving director compensation, and the Board has '
    #test_text='The Compensation Committee retained Semler Brossy Consulting Group, LLC (“Semler Brossy”) in November 2008 to replace Mercer as its consultant. Semler Brossy was selected as the consultant to the Compensation Committee after an interview process with several compensation consulting firms. The Compensation Committee has requested Semler Brossy to advise it on substantially similar compensation-related issues for 2009 as the Compensation Committee requested from Mercer in 2008. '
    #test_text = "The Compensation Committee has the sole authority to retain an independent consultant. The Committee annually reviews the independence of Kwan & Co., LLC (Kwan) to meet the SEC requirements and decide on whether Kwan is eligible to provide services to Citigroup. The Committe replaced Kwan in 2021 and engaged the services of Heejeong, LLC as its compensation consultant. Deloitte also assisted the Committee for drafting employment agreements, but did not engage in compensation services. Jiyou is CEO."
    # in one sentence, it catches but in two sentences, it fails?
    # CC Kwan & Co., LLC
    # CC Kwan
    # CC Kwan
    # CC Kwan
    # CC Heejeong, LLC
    # CC Deloitte

    doc = nlp(test_text)
    print("Entities in '%s'" % test_text)
    if doc.ents == None:
        print("There is no CC. Am I wrong?")
    for ent in doc.ents:
        print(ent.label_, ent.text)

    # save model to output directory
    if output_dir is not None:
        output_dir = Path(output_dir)
        if not output_dir.exists():
            output_dir.mkdir()
        nlp.meta["name"] = new_model_name  # rename model
        nlp.to_disk(output_dir)
        print("Saved model to", output_dir)

        """
        # test the saved model
        print("Loading from", output_dir)
        nlp2 = spacy.load(output_dir)
        # Check the classes have loaded back consistently
        assert nlp2.get_pipe("ner").move_names == move_names
        doc2 = nlp2(test_text)
        for ent in doc2.ents:
            print(ent.label_, ent.text)
        """


# main(model=None, new_model_name="CC", output_dir=None, n_iter=30)
if __name__ == "__main__":
    # plac.call(main())
    main()
