price={'go':67}

price['book']=0.67
price['milk']=3.2
print(price)
print(price.get('don'))


voted={}
def check_voter(name):
    if voted.get(name):
        print ('go')
    else:
        voted[name]='True'
        