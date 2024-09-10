import unittest
from d2 import *

class d2_Tests(unittest.TestCase):

    def test_q1(self):
        print("Test de la  question 1")
        print("Q1_1")
        n=patinage(30, -10)
        self.assertEqual(n,True)
        print("Q1_2")
        n=patinage(25.4, -15)
        self.assertEqual(n,False)
        print("Q1_3")
        n=patinage(33, -15)
        self.assertEqual(n,True)
        print("Q1_4")
        n=patinage(33, -5)
        self.assertEqual(n,False)
      

    def test_q2(self):
        print("\nTest de la  question 2")
        print("Q2_1")
        n=alphaNote(100)
        self.assertEqual(n,'A+')
        print("Q2_2")
        n=alphaNote(89)
        self.assertEqual(n,'A')
        print("Q2_3")
        n=alphaNote(56)
        self.assertEqual(n,'D+')
        print("Q2_4")
        n=alphaNote(30)
        self.assertEqual(n,'F')
      

    # pas de unit test pour Q3 parce qu'elle ne retourne rien

    # pas de unit test pour Q4 parce qu'elle ne retourne rien

    def test_q5(self):
        print("\nTest de la  question 5")
        print("Q5_1")
        n =facteursDeN(12)
        self.assertEqual(n,False)
        print("Q5_2")
        n =facteursDeN(9)
        self.assertEqual(n,True)
        print("Q5_3")
        n =facteursDeN(5)
        self.assertEqual(n,True)       
        

    def test_q6(self):
        print("\nTest de la  question 6")
        print("Q6_1")
        n =carreParfait(16)
        self.assertEqual(n,True)
        print("Q6_2")
        n =carreParfait(15)
        self.assertEqual(n,False)

    def test_q7(self):
        print("\nTest de la  question 7")
        print("Q7_1")
        n = maFun(0)
        self.assertEqual(n,1.0)
        print("Q7_2")
        n = maFun(1)
        self.assertTrue(proche(n,-0.3333))
        print("Q7_3")
        n = maFun(10)
        self.assertTrue(proche(n,0.0476))
        print("Q7_4")
        n = maFun(2)
        self.assertTrue(proche(n,0.2))

    def test_q8(self):
        print("\nTest de la  question 8")
        print("Q8_1")
        n = maFun_bis(10)
        self.assertTrue(proche(n,3.2323))
        print("Q8_2")
        n = maFun_bis(100)
        self.assertTrue(proche(n,3.1514))
        print("Q8_3")
        n = maFun_bis(1000)
        self.assertTrue(proche(n,3.1425))   

   
def proche(a,b, margeDErreur=0.001):
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

