import csv
from difflib import SequenceMatcher
from arabletters import transliterate_word
#from pegasus import get_response


##conctenate most of the csv files into one big csv file###
allforone = ['adjectives','adverbs','animals',
'art','clothes','colors','plants','possessives',
'prepositions','pronouns','professions','religion',
'weird','economy','education','technology','family',
'places','time','verbs','food']
###


conjug = ['conjug_past','conjug_present']
pronouns = ["ana","nta","nti","howa","hia","7na","ntoma","homa"]
def concatenate(files):
    with open("corpus.csv",'a') as corpus:
        for filename in files:  
            with open(filename+".csv") as file:
                data = file.read()
                corpus.write(data)




def translate(sentence):
    tokens = sentence.rsplit(" ")
    eng = dict()
    verbs = dict()
    for item in allforone: 
        with open("./files/"+item+".csv") as corpus:
            reader = csv.reader(corpus,delimiter=',')
            for row in reader:
                for word in row:
                    for token in tokens:
                        if word == token:
                            eng[token] = [tokens.index(token),row[-1],item]
                        
    for item in conjug:
        with open("./files/"+item+".csv") as tense:
            reader = csv.reader(tense,delimiter=',')
            for row in reader:
                for word in row:
                    for token in tokens:
                        if word == token:
                            verbs[token] = [tokens.index(token),row[3],item,pronouns[row.index(token)]]


    #dict ==> key:value

    for item in verbs:
        eng[item] = verbs[item]
    ###sorting dict###
    result = []
    i=0
    while(i<len(eng)):
        for item in eng:
            if eng[item][0] == i and eng[item][2] != 'conjug_past':
                result.append(eng[item][1])
            if eng[item][0] == i and eng[item][2] == 'conjug_past':
                pronoun = eng[item][-1]
                
                verb = eng[item][1]
                with open("./files/"+'pronouns.csv') as eng_pronouns:
                    reader4 = csv.reader(eng_pronouns,delimiter=',')
                    for row4 in reader4:
                        for word4 in row4:
                            if word4 == pronoun:
                                result.append(row4[-1])
                with open("./files/"+'verbs.csv') as verbs_list:
                    reader3 = csv.reader(verbs_list,delimiter=',')
                    for row3 in reader3:
                        for word3 in row3:
                            if word3 == verb:
                                result.append(row3[-1])
                
        i = i + 1
    final = ""
    for item in result:
        final = final+" "+item
    print(result)
    return final





#sequence =transliterate_word("mchina lbareh")

#result = translate(sequence)
#print(result)

'''print(get_response(result,10,10))'''


def map_word(word):
    ## word is in arabic letters ## ==> ##return the word in latin letters.
    with open('map.csv',encoding='utf-8') as MAP:
        MAP_reader = csv.reader(MAP)
        for row in MAP_reader:
            if len(row)<1:
                pass
            else:
                if word in row[-1]:
                    print("word found")
                    return row[0] ##change this line later for more precision.
                else:
                    pass

def search_word(word):
    ratios = dict()
    with open('map.csv',encoding='utf-8') as MAP:
        MAP_reader = csv.reader(MAP)
        for row in MAP_reader:
            if len(row)<1:
                pass
            else:
                s = SequenceMatcher(None,row[-1],word)
                ratio = s.ratio()
                if ratio >= 0.6:
                    ratios[row[-1]]=ratio
    
    a = {k: v for k, v in sorted(ratios.items(), key=lambda item: item[1])}

    b = list(a)
    return(b[-1])


#word = search_word("مطيشة")
#trans_word = map_word(word)
#print(trans_word)

def search_verb(verb):
    ratios = dict()
    with open('map_conjug_past.csv',encoding='utf-8') as MAP_PAST:
        past_reader = csv.reader(MAP_PAST)
        for row in past_reader:
            if len(row)<1:
                pass
            else:
                for word in row:

                    s = SequenceMatcher(None,verb,word)
                    ratio = s.ratio()
                    if ratio >= 0.7:
                        ratios[word] = ratio
    a = {k: v for k, v in sorted(ratios.items(), key=lambda item: item[1])}

    b = list(a)
    return (ratios)






def search_line(word):
    line = None
    pos = None
    trans = None
    with open('map_conjug_past.csv',encoding='utf-8') as MAP_PAST, open('./files/conjug_past.csv',encoding='utf-8') as PAST:
        past_reader = csv.reader(MAP_PAST)
        past = csv.reader(PAST)
        for row in past_reader:
            if len(row)<1:
                pass
            else:
                for column in row:
                    if column == word:
                        line = past_reader.line_num
                        pos = row.index(word)
        for row in past:
            if past.line_num == line:
                trans = row[pos]
                break
    return trans


row = search_line("كلينا")
print(row)
    


        

                         















