import csv

map_dict = dict()
map_corpus = dict()
with open('map.csv',encoding='utf8') as map:
    reader = csv.reader(map)
    for row in reader:
        map_dict[row[-1]] = row[0]


with open('corpus.csv',encoding='utf8') as corpus:
    reader = csv.reader(corpus)
    for row in reader:
        map_corpus[row[0]] = row[-1]
        


def translate(sequence:str):
    translate = []
    tokens = sequence.rsplit()
    for token in tokens:
        word = map_corpus[map_dict[token]]
        translate.append(word)
    print(translate)





    
    

    





    