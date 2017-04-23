#!/usr/bin/python
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim

import praw
import re

tokenizer = RegexpTokenizer(r'[\w\'\/]+')

# create English stop words list
en_stop = get_stop_words('en')

# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()

reddit = praw.Reddit('wholesome_booty')

subreddit = reddit.subreddit('me_irl')


# subreddit.submit(
#     'Colorado has more Subarus',
#     'Title says all')

comments = []

for submission in subreddit.hot(limit=20):
    for top_level_comment in submission.comments:
        # if top_level_comment == '...':
        #     continue
        # else:
        #     print(top_level_comment.body)
        #print top_level_comment
        if re.search("me too thanks", top_level_comment.body, re.IGNORECASE):
            top_level_comment.reply("I <3 U")
            # print top_level_comment.body
            # comments.append(tb(top_level_comment.body))
            print "We replied to: " + top_level_comment.body
            break

# list for tokenized documents in loop
texts = []

# loop through document list
for i in comments:

    print(i)
    # clean and tokenize document string
    raw = i.lower()

    tokens = tokenizer.tokenize(raw)
    #print tokens

    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in en_stop]
    #print stopped_tokens

    # stem tokens
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    #print stemmed_tokens

    # add tokens to list
    texts.append(stemmed_tokens)

# turn our tokenized documents into a id <-> term dictionary
dictionary = corpora.Dictionary(texts)
#print dictionary

# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]
#print corpus

# generate LDA model
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=2, id2word = dictionary, passes=20)
print(ldamodel.print_topics(num_topics=2, num_words=4))
#print(ldamodel.print_topic(2,topn=4))

    # if re.search("me too thanks", submission.title, re.IGNORECASE):
    #     submission.reply("Size doesn't matter. It's about the passion.")
    #     print "Bot replying to: " + submission.title
