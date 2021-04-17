import csv 


##conctenate most of the csv files into one big csv file###
allforone = ['adjectives','adverbs','animals',
'art','clothes','colors','plants','possessives',
'prepositions','pronouns','professions','religion',
'weird','economy','education','technology','family',
'places','time','verbs','food']
###

def concatenate(files):
    with open("corpus.csv",'a') as corpus:
        for filename in files:
            with open(filename+".csv") as file:
                data = file.read()
                corpus.write(data)




def tokenize(sentence):
    tokens = sentence.rsplit(" ")
    print(tokens)
    with open("corpus.csv") as corpus:
        reader = csv.reader(corpus,delimiter=',')
       
        for row in reader:
            for word in row:
                for token in tokens:
                    if word == token:
                        print(row[-1])


tokenize("ana kla formaj")



