def get_formatted_name(first,last,middle=''):
	if middle:
		return (first+ ' ' +middle+' '+last).title()
	else:
		return (first+' '+last).title()

