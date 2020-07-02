def powerset(s):
    x = len(s)
    masks = [1 << i for i in range(x)]
    for i in range(1 << x):
        yield [ss for mask, ss in zip(masks, s) if i & mask]


ps = powerset([1,2,3,4,6])
for ele in ps:
    print(ele)