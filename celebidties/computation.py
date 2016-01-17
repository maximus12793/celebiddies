import json
import datetime
import requests

class Game(object):
    def __init__(self):
        self.date = datetime.datetime(2003,8,1,12,4,5) #do we need the hour?

    def turn(self):
        self.date += datetime.timedelta(days=1)
        print(self.date)  #reveal the new date


class Celebrity(object):
    # this is a celeb character (which exist in game)
    def __init__(self, name="Unknown", worth=100000, team=None):
        self.worth = worth
        self.name = name
        self.volt = 1.0
        self.team = team

    def calcDamage(self, triag): #assign some number value
        pass

    def event(self, positive=False, seti=False, twtVal=0):
        '''det outcome result, we assume bad bc celebs'''
        if not positive:
            pass
            #calcDamage(1)

        if seti: #we will scale tweets by 1000
            self.worth += (self.worth * twtVal)/1000


    def speak(self):
        print "hello this is %s, my net worth is %d\n", self.name, self.worth

    def updateTeam(self, team=None):
        self.team = team #assign celeb to player team

''' triag
1. death
2. drugs (quanitified) -> crime classification?
3. sex
4. crime (quantified) assault > dwi?
5. family conflict
6. debt(crime)
7. child(good or bad?)
8. extension family(complicated)
9. health
10. vacation(s)
11. significant other(s)
12. controversial news



ex1. the game punches officer -> 100000


100 celebs
bet on events

- a team is made of many celebs (5)
- a game is made of 2+ teams
'''

##################### Demo shit
kanye = Celebrity("Kanye", 1000000)

# k1= json.dumps(kanye) # raises TypeError with "is not JSON serializable"

k1 = json.dumps(kanye.__dict__) # s set to: {"x":1, "y":2}
print k1



payload = {'json_playload': k1}
r = requests.get('http://myserver/emoncms2/api/post', data=payload)