# Master File 
#
# A simulation of Warbling Babbler movement with different phenotypes between several populations
# in different landscapes aver the course of several weeks. This uses a randomized dispersal matrix
# to determine a rate of migration between populations. 

import random
import matplotlib.pyplot as plt


class individual:
    """Class of Individual Warbling Babblers which will be moving around different populations"""

    def __init__(self,id = 1, phen = "Fluffy"):
        """Constructor for the individual class that sets and ID and phenotype for each individual
        where the default phenotype is Fluffy"""

        self.id = id
        self.phen = phen



class population:

    def __init__(self,popSize = 0,phenotype = "Fluffy",weights = [0.9,0.1]):
        """Population constructor that initializes the contents of each population, its size, and the probabiity of it staying or
        leaving. The defaults are that the population is empty and the phenotype is Fluffy"""

        self.popSize = popSize
        self.phenotype = phenotype
        self.inQ = []
        self.outQ = []
        self.weights = weights

        # Test populations
        # Checks which phenotype each population is initially classified as and then creates corresponding individuals
        self.indv = []

        if phenotype == "Fluffy": 
            for i in range(popSize):
                self.indv.append( individual(id=i+1,phen = "Fluffy") )
        elif phenotype == "Fuzzy":
            for i in range(popSize):
                self.indv.append( individual(id=i+1,phen = "Fuzzy") )

       

    def prob(self,popnum): #######
        """Defines the probability of a phenotype in a specific population"""

        fluffles = 0
        fuzzles = 0

        for i in self.indv:
            if i.phen == "Fluffy":
                fluffles += 1
            else:
                fuzzles += 1 

        fluffPercent = round(fluffles/(fluffles+fuzzles),4)*100
        fuzzPercent = round(fuzzles/(fluffles+fuzzles),4)*100

        print("Population",popnum,"is",fluffPercent, "% Fluffy")
        print("Population",popnum,"is",fuzzPercent, "% Fuzzy\n")


class landscape:
    """Defines the landscape class that defines a list of populations and executes the migration between populations 
    and their initial phenotype"""


    def __init__(self,popSize1 = 0,popSize2 = 0):
        """Constructor for Landscape that defines a population size that is passed to the populations inside of it"""

        self.popSize1 = popSize1 # PopSize of Pop1
        self.popSize2 = popSize2 # PopSize of Pop2

        # Landscapes - Only 2 Allowed
        self.lands = [population(popSize1,phenotype="Fluffy",weights=[0.9,0.1]),population(popSize2,phenotype="Fuzzy",weights=[0.8,0.2])]

    def move(self):
        """Executes all movement between populations"""
        for popl in self.lands: # Iterates over each population in the landscape
            for indv in popl.indv: # Iterates over each member in a population
                    
                move = random.choices(self.lands, popl.weights) # Weighted Random movement from pop 1 to pop 2

                if move[0] != popl:
                    popl.outQ.append(indv)
                    move[0].inQ.append(indv)

        for popl in self.lands:
            for i in popl.inQ:
                popl.indv.append(i)
            popl.inQ = []

            for i in popl.outQ:
                popl.indv.remove(i)
            popl.outQ = []



Pop1Size = 10   # Fluffy Population
Pop2Size = 15   # Fuzzy Population
Weeks = 10     # Number of Weeks


landscape = landscape(Pop1Size,Pop2Size)


#for i in range(Pop1Size): # how to call landscape
#    print(landscape.lands[0].indv[i].phen)

for i in range(Weeks):
    landscape.move()

    fluff = 0
    fuzz = 0
    fluff2 = 0
    fuzz2 = 0

    if i == (Weeks-1): # Prints the Final Population count
        print("~~~~~~~~~~~~~")
        for i in landscape.lands[0].indv: # how to call landscape
            print(i.phen)

            if i.phen == "Fluffy": # Counts fluff and fuzz
                fluff+=1
            else:
                fuzz+=1

        print(fluff)
        print(fuzz)

        print("----")
        for i in landscape.lands[1].indv: # how to call landscape
            print(i.phen)

            if i.phen == "Fluffy": # Count fluss and fuzz
                fluff2+=1
            else:
                fuzz2+=1
            
        print(fluff2)
        print(fuzz2)
        print("~~~~~~~~~~~~~")

popnum=0
for i in landscape.lands:
    popnum += 1

    i.prob(popnum)




