aliens=[]
for alien_number in range(30):
	alien={'color':'green','points':5,'speed':'slow'}
	aliens.append(alien)

for alien in aliens[:5]:
	print(alien)
	if alien['color'] == 'green':
		alien ['color'] ='blue'
		alien['speed']='medium'
		alien['points']=20
	print(alien)