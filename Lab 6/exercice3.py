s = ''' En 1815, M. Charles-François-Bienvenu Myriel était évêque de
Digne. C’était un vieillard d’environ soixante-quinze ans ; il occupait le
siège de Digne depuis 1806. … '''
#a
nS = s.replace('.',' ')
nS = s.replace('\n',' ')
nS = s.replace(';',' ')
print(nS)
#b
nS = nS.strip()
print(nS)
#c
nS = nS.lower()
print(nS)
#d
print(nS.count('de'))
#e
nS = nS.replace('était','est')
print(nS)


