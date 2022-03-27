def gettxt(filename):
    with open(filename) as file_object:
        text = file_object.read()
    text = text.lower()
    return text



text=gettxt('hamlet.txt')

for word in ",..:-?!'":
    text.replace(word,' ')
for word in ['the','and','is','he','her','they','and','or','so']:
    text.replace(word,' ')
text=text.split()

print(text.count('to'))


counts={}

for word in text:
    counts[word]=counts.get(word, 0)+1

ls=list(counts.items())
ls.sort(key=lambda x:x[1],reverse=True)
for word in ['is','he','her','they','and','or','so']:
    if word in counts.keys():   
        del(counts[word])   
print(ls[:10])

print('you')    
