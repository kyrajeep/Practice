#why would they implement this way? hb list? I guess it was determined by how it was gonna be used?
#usually either something is faster or take up less space
#trie vs. bst!
basic_trie = {
    # a and add word
    'a': {
        'd': {
            'd': {'word_end': True},
            'word_end': False},
        'word_end': True},
    # hi word
    'h': {
        'i': {'word_end': True},
        'word_end': False}}

