# Master File 
#
# A simulation of Warbling Babbler movement with different phenotypes between several populations
# in different landscapes aver the course of several weeks. This uses a randomized dispersal matrix
# to determine a rate of migration between populations. 

import random
#import matplotlib.pyplot as plt


class individual:
    """Class of Individual Warbling Babblers which will be moving around different populations"""

    def __init__(self,id = 1, phen = "Fluffy"):
        """Constructor for the individual class that sets and ID and phenotype for each individual
        where the default phenotype is Fluffy"""

        self.id = id
        self.phen = phen



class population:

    def __init__(self,popSize = 0,phenotype = "Fluffy",weights = [0.9,0.1]):
        """Population constructor that initializes the contents of each population and its size, while making sure that
        there are no duplicate individuals. The defaults are that the population is empty and the phenotype is Fluffy"""

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

       

    def phen_prob(self): #######
        """Defines the probability of a phenotype in a specific population"""



class landscape:
    """Defines the landscape class that defines a list of populations and executes the migration between populations 
    and their initial phenotype"""


    def __init__(self,popSize1 = 0,popSize2 = 0):
        """Constructor for Landscape that defines a population size that is passed to the populations inside of it"""

        self.popSize1 = popSize1 # PopSize of Pop1
        self.popSize2 = popSize2 # PopSize of Pop2

        self.weights = [[0.9,0.1],[0.8,0.2]]

        # Landscapes - Only 2 Allowed
        self.lands = [population(popSize1,phenotype="Fluffy",weights=[0.9,0.1]),population(popSize2,phenotype="Fuzzy",weights=[0.8,0.2])]



    def move(self):
        """Executes all movement between populations"""

#        weight1 = [0.9,0.1]
#        weight2 = [0.8,0.2]
         

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



Pop1Size = 5    # Fluffy Population
Pop2Size = 10   # Fuzzy Population

popl = population(Pop1Size,phenotype="Fluffy")

landscape = landscape(Pop1Size,Pop2Size)

#for i in range(1): # how to call population
#    print(popl.indv[i].phen)



#for i in range(Pop1Size): # how to call landscape
#    print(landscape.lands[0].indv[i].phen)

for i in range(10):
    landscape.move()

print("~~~~~~~~~~~~~")
for i in landscape.lands[0].indv: # how to call landscape
    print(i.phen)
print("----")
for i in landscape.lands[1].indv: # how to call landscape
    print(i.phen)