import gensim.downloader as api
from gensim.models.word2vec import Word2Vec


model = api.load('glove-wiki-gigaword-50')
#model = Word2Vec(corpus)

sim1 = model.similarity('home','house')

print(sim1)



