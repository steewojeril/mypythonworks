for l in 'john':
    if l=='o':
        pass
    print(l,end=' ')

# ans >>> j o h n

for l in 'john':
    if l=='o':
        continue
    print(l,end=' ')

# ans >>>  j h n

for l in 'john':
    if l=='o':
        break
    print(l,end=' ')

# ans >>> j