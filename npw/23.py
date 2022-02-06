def build_profile(first,last,**info):
	info['first']=first
	info['last']=last 
	for key,value in info.items():
		info[key]=value
	return info 
information=build_profile('quan','zhou',field='computer science',age=19,gender='male',two_package=True)
print(information)
