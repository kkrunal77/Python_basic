import nltk
#nltk.download()
sentence = """Nov 20 (Reuters) - The RSM Classic was headed to a five-man playoff at the Seaside Resort in St Simons, Georgia on Sunday in the last regular PGA tournament of 2016.     Billy Horschel (68) and fellow American Blayne Barber (66), Camilo Villegas of Colombia (68), Canadian rookie Mackenzie Hughes (69) and Sweden&apos;s Henrik Norlander (65) were all tied on 17-under-par after the regulation 72 holes.   (Reporting by Larry Fine in New York; Editing by Ken Ferris)  ((; +1 646-729-6291; Reuters Messaging: Reuters Messaging: ))  Keywords: GOLF PGA/PLAYOFF
"""
tokens = nltk.word_tokenize(sentence)
#print(tokens)
tagged = nltk.pos_tag(tokens)
print(tagged)
length = len(tagged)
list1=[]
for i in range(length):
    if(tagged[i][1]=="NN" or tagged[i][1]=="NNP"):
        list=tagged[i][0]
        list1.append(list)
print(list1)




