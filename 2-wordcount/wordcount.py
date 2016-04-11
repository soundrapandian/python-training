excerpt = """
is small, yellow, and leech-like, and probably the oddest thing in
the Universe. It feeds on brainwave energy received not from its own
carrier but from those around it. It absorbs all unconscious mental
frequencies from this brainwave energy to nourish itself with. It then
excretes into the mind of its carrier a telepathic matrix formed by
combining the conscious thought frequencies with nerve signals picked
up from the speech centres of the brain which has supplied them. The
practical upshot of all this is that if you stick a Babel fish in your
ear you can instantly understand anything said to you in any form of
language. The speech patterns you actually hear decode the brainwave
matrix which has been fed into your mind by your Babel fish.
"""

# Write a python program to print the three most common words from the
# text above
def count_value(dict_item):
    return dict_item[1]
    
count = {}
excerpt.lower().replace(',','').replace('.','')
for word in excerpt.split():
    if word in count.keys():
        count[word] += 1
    else:
        count[word] = 1

l = list(count.items())
l.sort(key=count_value, reverse=True)
print (l[0])
print (l[1])
print (l[2])
print ('-'*40)
for li in l:
    print (li)
    
