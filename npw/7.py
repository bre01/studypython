users={'mike':{'last':'mike','first':'damn','city':'kunming'},'neo':{'last':'neo','first':'zhou','city':'beijing'}}
for user,userinfo in users.items():
	print('name:'+userinfo['last']+' '+userinfo['first'])
	print('city:'+userinfo['city'])