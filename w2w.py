import csv

map_dict = dict()
map_corpus = dict()
with open('map.csv',encoding='utf8') as map, open('map_conjug_past.csv',encoding='utf8') as map_verbs:
    reader = csv.reader(map)
    reader_verbs = csv.reader(map_verbs)
    for row in reader:
        map_dict[row[-1]] = row[0]
    for row in reader_verbs:
        for column in row[1:]:
            map_dict[column] = row[0] 
        


with open('corpus.csv',encoding='utf8') as corpus, open('./files/verbs.csv',encoding='utf8') as corpus_verbs:
    reader = csv.reader(corpus)
    reader_verbs = csv.reader(corpus_verbs)
    for row in reader:
        map_corpus[row[0]] = row[-1]
    for row in reader_verbs:
        map_corpus[row[0]] = row[-1]

        


def translate(sequence:str):
    translate = []
    tokens = sequence.rsplit()
    for token in tokens:
        word = map_corpus[map_dict[token]]
        translate.append(word)
    print(translate)
    return translate




translate("هوما كلاو")



    