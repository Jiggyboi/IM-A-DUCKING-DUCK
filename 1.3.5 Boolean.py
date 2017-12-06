def how_elegible():
    sentence = raw_input('Insert your essay: ')
    print sentence.count('?')+sentence.count('.')+sentence.count('"')