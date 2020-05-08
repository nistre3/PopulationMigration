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

    def __init__(self,popSize = 0,phenotype = "Fluffy"):
        """Population constructor that initializes the contents of each population and its size, while making sure that
        there are no duplicate individuals. The defaults are that the population is empty and the phenotype is Fluffy"""

        self.popSize = popSize
        self.phenotype = phenotype

        # Test populations
        # Checks which phenotype each population is initially classified as and then creates corresponding individuals
        self.indv = []

        if phenotype == "Fluffy": 
            for i in range(popSize):
                self.indv.append( individual(id=i+1,phen = "Fluffy") )
        elif phenotype == "Fuzzy":
            for i in range(popSize):
                self.indv.append( individual(id=i+1,phen = "Fuzzy") )

        #include a test to check for duplicates
       

    def phen_prob(self): #######
        """Defines the probability of a phenotype in a specific population"""



class landscape:
    """Defines the landscape class that defines a list of populations and executes the migration between populations 
    and their initial phenotype"""


    def __init__(self,popSize1 = 0,popSize2 = 0):
        """Constructor for Landscape that defines a population size that is passed to the populations inside of it"""

        self.popSize1 = popSize1 # PopSize of Pop1
        self.popSize2 = popSize2 # PopSize of Pop2

        # Landscapes - Only 2 Allowed
        self.lands = [population(popSize1,phenotype="Fluffy"),population(popSize2,phenotype="Fuzzy")]



    def move(self):
        """Executes all movement between populations"""

        migrate = ["stay","leave"]
        weight1 = [0.9,0.1]
#        weight2 = [0.8,0.2]
         
        for i in self.lands: 

            for popl in self.lands: # Iterates over each population in the landscape

                for indv in popl.indv: # Iterates over each member in a population
                    
#                    if self.lands[i] == self.lands[0]:
                        move = random.choices(migrate, weight1) # Weighted Random movement from pop 1 to pop 2

                        if move == "leave":
                            popl.indv[i+1].append(indv) # Appends individual to Pop2
                            popl.indv[i+1].remove(indv) # Removes from Pop1
                    
#                    else:
 #                       move = random.choices(migrate, weight2) # Weighted Random movement from pop 2 to pop 1

  #                      if move == "leave":
   #                         popl.indv[i-1].append(indv) # Appends the individual to Pop1
    #                        popl.indv[i-1].remove(indv) # Removes from Pop2




popl = population(popSize=10,phenotype="Fluffy")

landscape = landscape(5,10)

for i in range(1): # how to call population
    print(popl.indv[i].phen)

for i in range(1): # how to call landscape
    print(landscape.lands[0].indv[i].phen)