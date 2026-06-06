#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
random.seed(42)


# In[6]:


def generate_one(token):
    #input sentence or word depending on mode
    #choose random token probabilistically from words generated so far
    random.choices(token)
    


# In[12]:


def demonstrate(model, mode="sentence"):
    #print the model string representation
    print(my_model)
    #generate 5 words using generate_one
    wlist = []
    i = 0
    for i in count:
        if i <5:
            i+=1
            wlist.append(generate_one(token))
    '''
    word mode
    ["swicky", "these", "devils", "foonch", "FAQ", "isn't"]
    '''
    
    ''' sentence mode
    ["\"Don't make too much noise,\" said Father Brown.", "Don't go there!", "Father
Brown laughed.", "make noise too much don't Father said Brown.", "The men left.", "The swicky men left."]'''
    #calc raw perplexity for 6 test words/sents using corpus_perplexity method
    for word in corpus:
        print(f"perplexity: {word} {corpus_perplexity(word)}")
    #calc and print laplace smoothed perplexity


# In[11]:


def script():
    if __name__ == "__main__":


# In[25]:


# demo.py
# tokenizer and tokenizerNLTK

import nltk
from nltk.corpus.reader import PlaintextCorpusReader

def Tokenizer():
    myreader = PlaintextCorpusReader("./train", r".*\.txt")
    
def TokenizerNLTK():
    myreader = PlaintextCorpusReader("./train", r".*\.txt")
   


# In[ ]:


#create 12 ngram models

i = 0
for n in [2,3,4]:
    for mode in ["sentence", "word"]:
        

