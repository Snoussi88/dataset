import csv 


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
    return final





result = translate("mchaw lbareh l dzair")
print(result)











