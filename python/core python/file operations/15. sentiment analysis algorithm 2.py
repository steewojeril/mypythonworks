# mine + chatgpt
comments = ['good', 'bad', 'happy', 'nice', 'awesome', 'not good', 'good']
bad_w = ['bad', 'not good']
good_w = ['good', 'happy', 'nice', 'awesome']

b_word = {c: comments.count(c) for c in bad_w}
g_word = {c: comments.count(c) for c in good_w}

b_sum = sum(b_word.values())
g_sum = sum(g_word.values())

t = b_sum + g_sum

if t <= 0:
    print('negative')
else:
    print('positive')

    










