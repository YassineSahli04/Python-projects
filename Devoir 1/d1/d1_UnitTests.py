# test automatique pour D1
# metez-le dans le meme repertoire que votre fichier solution et excutez le fichier test avec Run
# put it in the same directory as your solution file and press Run to excute the test file

import unittest
from d1 import *

class d1_Tests(unittest.TestCase):

    def test_q1(self):
        print("Test de la  question 1")
        print("Q1_1")
        n=tempsVoyage(400,100)
        self.assertEqual(n,240.0)
        print("Q1_2")
        n=tempsVoyage(20.6,60)
        self.assertEqual(n, 20.6)
      

    def test_q2(self):
        print("\nTest de la  question 2")
        print("Q2_1")
        n=noteFinale(100,100,100,100,100)
        self.assertEqual(n,100.0)
        print("Q2_2")
        n=noteFinale(50,90.5,60,80,70)
        self.assertEqual(n, 74.625)
      

    def test_q3(self):
        print("\nTest de la  question 3")
        print("Q3_1")
        n = bibformat("Antoine de Saint Exupery", "Le petit prince", "Paris", "Jeunesse", 1943)
        self.assertEqual(n, 'Antoine de Saint Exupery (1943). Le petit prince. Paris: Jeunesse')

    # pas de unit test pour Q4 parce qu'elle ne retourne rien

    def test_q5(self):
        print("\nTest de la  question 5")
        print("Q5_1")
        n=logFun(7)
        self.assertEqual(n,0.25)
        print("Q5_2")
        n=logFun(20)
        self.assertTrue(proche(n,0.3404))
        print("Q5_3")
        n=logFun(999999997)
        self.assertTrue(proche(n,2.25))
        print("Q5_4")
        n=logFun(0.1)
        self.assertTrue(proche(n,0.12284))
        print("Q5_5")
        n=logFun(9997)
        self.assertTrue(proche(n,1.0)) 

    def test_q6(self):
        print("\nTest de la  question 6")
        print("Q6_1")
        n=anneeBis(1904)
        self.assertEqual(n,True)
        print("Q6_2")
        n=anneeBis(1928)
        self.assertEqual(n,True)
        print("Q6_3")
        n=anneeBis(1950)
        self.assertEqual(n,False)
        print("Q6_4")
        n=anneeBis(1990)
        self.assertEqual(n,False)
        print("Q6_5")
        n=anneeBis(1932)
        self.assertEqual(n,True)

 
def proche(a,b, margeDErreur=0.0001):
	if a*b <= 0:
		resultat = abs(a-b) < margeDErreur
	else: 
		resultat = 1-abs(b/(abs(a)+0.00000001)) < margeDErreur
	if resultat:
		return resultat
	print("\n\tERREUR:",a,"et",b,"ne sont pas assez proche!")
	return resultat  

if __name__ == '__main__':
    unittest.main()

