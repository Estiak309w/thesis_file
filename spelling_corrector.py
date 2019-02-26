
string = 'মওলানা'
string1 = 'সংশেধন'
word_book =['ভূমিকা','অকারণ','আমরা','মাওলানা','সংশোধন']
word_only = ['অ','আ','ই','ঈ','উ','ঊ','ঋ','এ','ঐ','ও','ঔ','ক','খ','গ','ঘ','ঙ','চ','ছ','জ','ঝ','ঞ','ট','ঠ','ড','ঢ','ণ','ত','থ','দ','ধ','ন','প','ফ','ব','ভ','ম','য','র','ল','শ','ষ','স','হ','ক্ষ','ড়','ঢ়','য়']
wrong_word_1 = []
word_dict = {}


def make_only_word(sent):
    wrong_word_1.clear()
    for i in sent:
        if i in word_only:
            wrong_word_1.append(i)
    wrong_word = "".join(wrong_word_1)
    return wrong_word

def make_dict(word):
    word_without_kar = make_only_word(word)
    return word_without_kar

length = len(word_book)
for i in range(length):
    word_dict[word_book[i]] = make_dict(word_book[i])

for key,value in word_dict.items():
    if make_only_word(string) == value:
        print(key)

for key,value in word_dict.items():
    if make_only_word(string1) == value:
        print(key)
# # spelling correction using modified LONGEST COMMON SUBSEQUENCE

def lcs(x,y,l,m):
    if l == 0 or m == 0:
        return 0
    elif x[l-1] == y[m-1]:
        a = 1 + lcs(x,y,l-1,m-1)
        return a
    else :
        return lcs(x,y,l-1,m-1)

x = 'অবশ্যই'
x_1 = 'শয়তান'
y = 'অবস্যই'
y_1 = 'সয়তান'
def longest_common_sub(x,y):
    a = lcs(x,y,len(x),len(y))
    if(a== (max(len(x),len(y))-1)):
        return x
print(longest_common_sub(x,y))
print(longest_common_sub(x_1,y_1))
