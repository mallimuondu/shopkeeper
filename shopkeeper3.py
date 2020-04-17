class shop:
    def __init__(self,listofgoods):
        self.listofgoods = listofgoods
        
    def showavalablegoods(self):
        print("the goods we have are as follows")
        for goods in self.listofgoods:
            print(goods)
    def buygoods(self,requestedgood):
        if requestedgood in self.listofgoods:
            print("The good that you have requested has been bought")
        else:
            print("sorry! the good that  you have requested is not avalable")
    def  addgoods(self,newgoods):
        self.avalablegoods.append(newgoods)
        print("Thankyou for adding new goods")
#        print('''
#        1. Milk @ 43
#        2. Bread @ 50
#        3. Honey @ 200
#        4. Popcorn @ 20
#        5. Soda @ 50
#        6. Chips @ 80
#        7. Sausage @ 10
#        8. Burger @ 250
#        9. Nyama choma @ 360
#        10. Kuku choma @ 320
#        11. Njugu @ 10
#        12. Water @ 50
#        13. Swimming costume @ 300
#        14. Googles @ 200
#        15. snorkelling gear @ 1000
#        ''')