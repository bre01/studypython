def build(first,last,**info):
	profile={}
	profile['first']=first
	profile['last']=last
	for key,value in info.items():  ##!!! very importrant    .items() 
		profile[key]=value
	return profile 
information=build('lily','james',gender='femal',nationnality='england')
print(information)
