print([[sum([b.count(x) * int(x) for x in [int(x.split('   ')[0]) for x in data] for b in [[int(x.split('   ')[1]) for x in data]]])][0] for data in [input().split('\n')]][0])
