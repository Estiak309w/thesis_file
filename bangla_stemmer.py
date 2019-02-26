

word = 'দেখবেন'
dic ={"": ['দের','ের','েন','বেন'],"ই": ['চ্ছি','চ্ছিল'],"য়": ['য়েছিল','েয়েছিল ','েছিল']} 
print(dic)

sentence = "যুদ্ধ যেন ধর্মরক্ষার অন্যতম শ্রেষ্ঠ হাতিয়ার হচ্ছিল"
a = stem('হচ্ছিল')
print(a)

new_sentence = []
words = sentence.split()
for word in words:
    #print(word)
    a = stem(word)
    #print(a)
    new_sentence.append(a)
print(new_sentence)

print(" ".join(new_sentence))
sent = " ".join(new_sentence)
with open("test.txt", "a",encoding="utf-8") as myfile:
    myfile.write((sent+ '\n'))
    myfile.close()


def find_prefix(prefix,word):
    a = word[len(word)-len(prefix):]
    if(a==prefix):
        is_prefix =  True
    else:
        is_prefix = False
    return is_prefix

def stem(word):
    dic ={"": ['দের','ের','েন','বেন'],"ই": ['চ্ছি','চ্ছিল'],"য়": ['য়েছিল','েয়েছিল ','েছিল']} 
    new_word=word
    for key,value in dic.items():
        for i in range(len(value)):
            prefix = dic[key][i]
            if (find_prefix(prefix,word)==True):
                #print(find_prefix(prefix))
                #print(key)
                new_word = word.replace(prefix, key)
                return(new_word)
    if(new_word==word):
        return(word)

