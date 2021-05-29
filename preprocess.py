

##  "chkone" ==>[py]==> "شكون" 
## "chkone" == "chkon". "ch" = "ش"
## "walo" ==  ""
### make a function search() that calculates the percentage of likelihood between darija words.

import csv
##conctenate most of the csv files into one big csv file###
files = ['adjectives','adverbs','animals',
'art','clothes','colors','plants','possessives',
'prepositions','pronouns','professions','religion',
'weird','economy','education','technology','family',
'time','food','politics','weird','places']

def concatenate():
    with open("corpus.csv",'a') as corpus:
        for filename in files:
            with open("./files/"+filename+".csv") as file:
                data = file.read()
                corpus.write(data+","+filename)



base = dict()
double_letters ={"gh":"غ","kh":"خ","ou":"و","ch":"ش"}
reverse = dict()

with open('letters.csv',encoding ='utf8') as f:
        reader0 = csv.reader(f,delimiter=',')
        for row in reader0:
            base[row[-1]] = row[0]
            reverse[row[0]] = row[-1]



def transliterate_letter(letter):
    if letter in double_letters:
        return double_letters[letter]
    else:
        return reverse[letter]


def  transliterate_word(word):
    result, word_iterator = [], iter(range(len(word)))
    for i in word_iterator:
        if i < len(word) - 1:
            if word[i:i+2] in double_letters:
                result.append(transliterate_letter(word[i:i+2]))
                next(word_iterator)
            elif word[i] == word[i+1]:
                result.append(transliterate_letter(word[i]))
                next(word_iterator)
            else:
                result.append(transliterate_letter(word[i]))
        else:
            result.append(transliterate_letter(word[i]))
    #result.reverse()
    final = ""
    for letter in result:
        final = final + letter
    return final


#print(transliterate_word("salam a Sahbi"))

## use HIDDEN MARKOV instead of IBM MODEL  maybe sometime. deffo not now###



def generate_map():
    with open('map.csv','a',encoding='utf-8') as MAP:
        WRITER = csv.writer(MAP,lineterminator='\n')
        with open('corpus.csv',encoding='utf-8') as CORPUS:
            READER = csv.reader(CORPUS)
            for row in READER:
                try:
                    WRITER.writerow([row[0],transliterate_word(row[0])])
                except:
                    pass

#generate_data()
#concatenate()

def generate_map_conjug():
    with open('map_conjug_past.csv','a',encoding='utf-8') as MAP, open('./files/conjug_past.csv',encoding='utf-8') as PAST:
        WRITER = csv.writer(MAP,lineterminator='\n')
        READER = csv.reader(PAST)
        for row in READER:
            temp =[]
            for word in row:
                try:
                    temp.append(transliterate_word(word))
                except:
                    print("exception")
            WRITER.writerow(temp)

