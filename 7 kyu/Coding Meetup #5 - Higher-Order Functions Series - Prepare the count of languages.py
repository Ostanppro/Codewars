def count_languages(lst): 
    language_count = {}
    for dict in lst:
        language = dict.get('language')
        try:
            language_count[language] += 1
        except KeyError:
            language_count[language] = 1
    return language_count