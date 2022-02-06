from collections import OrderedDict
favourite_language=OrderedDict()
favourite_language['lily']='python'
favourite_language['amy']='C'
favourite_language['phil']='fortran'
for name,language in favourite_language.items():
	print(name,"'s",'favourite languae is ',language)
