import pickle


shops = {"Zabka": "https://raw.githubusercontent.com/DominikWasiolka/picturesForHackathon/master/zabka/logo.png",
         "Biedronka": "https://raw.githubusercontent.com/DominikWasiolka/picturesForHackathon/master/biedronka/logo.png",
         "Empik": "https://raw.githubusercontent.com/DominikWasiolka/picturesForHackathon/master/empik/logo.png",
         "Obi": "https://raw.githubusercontent.com/DominikWasiolka/picturesForHackathon/master/obi/logo.png",
         "Vistula": "https://github.com/DominikWasiolka/picturesForHackathon/blob/master/vistula/logo.jpg",
         "Lidl":  "https://raw.githubusercontent.com/DominikWasiolka/picturesForHackathon/master/lidl/logo.png",
         "Premium": "url"}

cupons = {'id1': {"url": "https://raw.githubusercontent.com/DominikWasiolka/picturesForHackathon/master/zabka/6.jpg",
                  "validate": "30 Listopada 2019", "conditions": "Musisz wydać 90 zł w tym miesiącu, aby uzyskać kupon \nSpecjalne warunki:\n *Niedostępne w listopadzie #NNN",
                   'shop': 'Premium',
                   'requrement':90},
          'id2': {"url": "https://raw.githubusercontent.com/DominikWasiolka/picturesForHackathon/master/empik/5.jpg",
                  "validate": "24 Grudnia 2019", "conditions": "Nic nie musisz wydawac! \nMagia Świąt!",
                  'shop':'Empik','requrement':0},
          'id3': {"url": "https://raw.githubusercontent.com/DominikWasiolka/picturesForHackathon/master/vistula/7.jpg",
                  "validate": "12 Grudnia 2019",
                  "conditions": "Musisz wydać 10 zł w tym miesiącu, aby uzyskać kupon \nSpecjalne warunki: \n*Proszę przyjść z Tatą! Spędź z nim trochę czasu!", 'shop': 'Vistula', 'requrement':10},
          'id4': {"url": "https://raw.githubusercontent.com/DominikWasiolka/picturesForHackathon/master/obi/8.jpg",
                  "validate": "1 stycznia 2111",
                  "conditions": "Musisz wydać 2500 zł w tym miesiącu, aby uzyskać kupon \nSpecjalne warunki: \n*Pssst ... Nie mamy artykułów turystycznych :)", 'shop': 'Obi','requrement':2500},
          'id5': {"url": "https://raw.githubusercontent.com/DominikWasiolka/picturesForHackathon/master/biedronka/12.jpg",
                  "validate": "26 kwietnia 2020",
                  "conditions": "Musisz wydać 2500 zł w tym miesiącu, aby uzyskać kupon \nSpecjalne warunki: \n*Kup też czekoladki, każdy lubi czekoladki", 'shop': 'Biedronka', 'requrement':900},
          'id6': {"url": "https://raw.githubusercontent.com/DominikWasiolka/picturesForHackathon/master/biedronka/11.jpg",
                  "validate": "23 grudnia 2019",
                  "conditions": "Musisz wydać 2000 zł w tym miesiącu, aby uzyskać kupon \nSpecjalne warunki: \n*Powiedz kasjerce coś miłego, niech każdemu będzie słodko!", 'shop': 'Biedronka','requrement':2000},
          'id7': {"url": "https://raw.githubusercontent.com/DominikWasiolka/picturesForHackathon/master/biedronka/9.jpg",
                  "validate": "Jutro",
                  "conditions": "Musisz wydać 3000 zł w tym miesiącu, aby uzyskać kupon \nSpecjalne warunki: \n*Jedno i drugie! Za tydzień Pięć-Set Plus", 'shop': 'Biedronka','requrement':3000},
          'id8': {"url": "https://raw.githubusercontent.com/DominikWasiolka/picturesForHackathon/master/lidl/13.jpg",
                  "validate": "30 listopada 2019",
                  "conditions": "Musisz wydać 40 zł w tym miesiącu, aby uzyskać kupon \nSpecjalne warunki: \n*Sprzedajemy w tym tygodniu tylko masło.", 'shop': 'Lidl','requrement':40},
          'id9': {"url": "https://raw.githubusercontent.com/DominikWasiolka/picturesForHackathon/master/lidl/10.jpg",
                  "validate": "31 grudnia 2020",
                  "conditions": "Musisz wydać 900 zł w tym miesiącu, aby uzyskać kupon \nSpecjalne warunki: \n*Liczyliście na czarny humor, prawda?", 'shop': 'Lidl','requrement':900},
          'id10': {"url": "https://raw.githubusercontent.com/DominikWasiolka/picturesForHackathon/master/zabka/1.jpg",
                  "validate": "30 listopada 2019",
                  "conditions": "Musisz wydać 390 zł w tym miesiącu, aby uzyskać kupon \nSpecjalne warunki: \n*Przy zakupie conajmniej 5*", 'shop': 'Zabka','requrement':390},
          'id11': {"url": "https://raw.githubusercontent.com/DominikWasiolka/picturesForHackathon/master/zabka/2.jpg",
                   "validate": "15 grudnia 2019",
                   "conditions": "Musisz wydać 290 zł w tym miesiącu, aby uzyskać kupon \nSpecjalne warunki: \n*Promocja ważna z kartą dużej rodziny*", 'shop': 'Zabka','requrement':290},
          'id12': {"url": "https://raw.githubusercontent.com/DominikWasiolka/picturesForHackathon/master/zabka/3.jpg",
                   "validate": "30 listopada 2019",
                   "conditions": "Musisz wydać 9011 zł w tym miesiącu, aby uzyskać kupon \nSpecjalne warunki: \n*Nie dotyczy jogurtów, serków, mleka", 'shop': 'Zabka','requrement':9011},
          'id13': {"url": "https://raw.githubusercontent.com/DominikWasiolka/picturesForHackathon/master/zabka/4.jpg",
                   "validate": "31 grudnia 2019",
                   "conditions": "Musisz wydać 123 zł w tym miesiącu, aby uzyskać kupon \nSpecjalne warunki: \n*Bierzcie, pasibrzuchy!", 'shop': 'Zabka','requrement':123}
          }

users = {"user1":{"cupons":['id1','id4','id10','id11','id12','id13','id9'], 
                     "shops":["Obi",'Zabka','Lidl', 'Premium'],
                     "blacklist":['Vistula'],
                     "expenses":{"Zabka":1400,"Obi":500,'Lidl':20,'Premium':133}},
         "user2":{"cupons":['id3'],
                     "shops":["Empik","Zabka"],
                     "blacklist":['Obi'],
                     "expenses":{"Biedronka":100,"Obi":500}}
        }

class Shops:
    def __init__(self):
        self.shops = pickle.load( open( "raw_data/shops.p", "rb" ) )

    def save(self):
        pickle.dump( self.shops, open("raw_data/shops.p", "wb" ) )

class Cupons:
    def __init__(self):
        self.cupons = pickle.load( open( "raw_data/cupons.p", "rb" ) )

    def save(self):
        pickle.dump( self.cupons,  open("raw_data/cupons.p", "wb" ) )

    def return_urls_of_list(self,list_of_ids):
        urls = []
        for elem in list_of_ids:
            urls.append(self.cupons[elem]['url'])
        return urls

    def retrun_urls_with_validates(self,list_of_ids):
        urls = []
        for elem in list_of_ids:
            urls.append({
                'id':elem,
                'url':self.cupons[elem]['url'],
                'validate':self.cupons[elem]['validate']
            })
        return urls

class Users:
    def __init__(self):
        self.users = pickle.load( open( "raw_data/users.p", "rb" ) )

    def save(self):
        pickle.dump( self.users,  open("raw_data/users.p", "wb" ) )


if __name__=='__main__':
    a="a"
    pickle.dump( shops, open("raw_data/shops.p", "wb") ) 
    pickle.dump( cupons,  open("raw_data/cupons.p", "wb" ) )
    pickle.dump( users,  open("raw_data/users.p", "wb" ) )