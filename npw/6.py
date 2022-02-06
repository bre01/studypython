favorite_languages = {
      'jen': ['python', 'ruby'],
      'sarah': ['c'],
      'edward': ['ruby', 'go'],
      'phil': ['python', 'haskell'],
      }
for name, languages in favorite_languages.items():
      print(name+"'s favorite language is ")
      if len(languages)==1:
            for language in languages:
                  print('only    '+language)
      else:
            for language in languages:
                  print('\t'+ language)

