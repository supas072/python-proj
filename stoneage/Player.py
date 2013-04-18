'''
Created on Nov 22, 2012

@author: finn
'''

class Player():
    '''
    classdocs
    '''

    def __init__(self, color, strategy):
        self.resources = 12 * [2]
        self.huts = []
        self.personCount = 5
        self.score = 0
        self.color = color
        self.playerAbr = color[:1].lower()
        self.strategy = strategy

    def foodMissing(self):
        return max(0, self.personCount - self.resources.count(2))
    
    def feed(self):
        if self.foodMissing() > 0 :
            self.score -= 10
        for person in range(self.personCount - self.foodMissing()): 
            self.resources.remove(2)

    def getNonFood(self):
        return sorted([resource for resource in self.resources if resource != 2])
    
    def addResources(self, additionalResources):
        self.resources.extend(additionalResources)
        
    def removeResources(self, resourcesToRemove):
        for resource in resourcesToRemove:
            self.resources.remove(resource)
        
    def buyHuts(self, huts):
        return self.strategy.buyHuts(self, huts)

    def buyHut(self, hut, payment):
        self.huts.append(hut)
        self.executeHutPayment(payment)

    def isPayable(self, hut):
        return self.strategy.isPayable(hut, self.resources)

    def executeHutPayment(self, payment):
        self.removeResources(payment)
        self.score += sum(payment)

    def personsLeft(self, board):
        return self.personCount - board.personCount(self.playerAbr)

    def isNewRound(self, board):
        return self.personsLeft(board) == self.personCount

    def placePersons(self, board):
        self.strategy.placePersons(self, board)
    
    def finalScore(self):
        return self.score + len(self.resources)
    
    def getColor(self):
        return self.color

    def getAbr(self):
        return self.playerAbr
    
    def toString(self):
        return """Resources: %s
huts: %s    
score: %d\n""" % (str(sorted(self.resources)), ",". join([hut.toString() for hut in self.huts]), self.score)


