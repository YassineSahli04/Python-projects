class Temps:
  '''classe temporelle'''

  def __init__(self, h=12, m=0, s=0):
    '''(Temps)-> None'''
    self.heure = h
    self.minute = m
    self.seconde = s
    self.setTemps(h,m,s)

  def setTemps(self, h, m=0, s=0):
    '''(Temps)-> None'''
    if ( s > 59) :
      m = m + s // 60
      s = s % 60
    if ( m > 59 ) :
      h = h + m // 60
      m = m % 60
      
    self.heure = h % 24
    self.minute = m
    self.seconde = s

  def affiche_heure(self):
    '''(Temps)-> None'''
    print("{0}:{1}:{2}".format(self.heure, self.minute, self.seconde)) 

  def __repr__(self):
    '''(Temps)-> str'''
    return (str(self.heure) +":" +str(self.minute) +":" +str(self.seconde))

  def __eq__(self, autre):
    '''(Temps)-> bool'''
    return self.heure == autre.heure and self.minute == autre.minute and self.seconde == autre.seconde

  def estAvant(self,t2) :
    '''Retourne True si le temps est représenté par self est avant le temps de t2, et Flase sinon.'''''
    avant = self.heure < t2.heure or (self.heure == t2.heure and self.minute < t2.minute) or (self.heure == t2.heure and self.minute == t2.minute and self.seconde < t2.seconde)
    return avant

  def durée(self,t2) :
    ''' Retourne un nouvel objet temps abve le nombre d'heures, de minutes et de secondes entre self et t2. '''
    if self.estAvant(t2) :
      diffS = 60*60*(t2.heure - self.heure) + 60*(t2.minute - self.minute) + (t2.seconde - self.seconde)
    else :
      diffS = 60*60*(self.heure - t2.heure) + 60*(self.minute - t2.minute) + (self.seconde - t2.seconde)
    résultat = Temps()
    résultat.setTemps(0,0,diffS)
    return résultat


t1 = Temps(12,4,0)
t2 = Temps(10,2,1)
print(t1.estAvant(t2))
print(t2.estAvant(t1))
t2.setTemps(12,45,2)
print(t1.estAvant(t2))
print(t1.durée(t2))

