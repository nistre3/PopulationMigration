# Master File 
#
# A simulation of Warbling Babbler movement with different phenotypes betwee several populations
# in different landscapes aver the course of several weeks. This uses a randomized dispersal matrix
# to determine a rate of migration between populations. 

import random
import matplotlib.pyplot as plt


class individual:
"""Class of Individual Warbling Babblers which will be moving around different populations"""

    def __init__(self,id = 1, phen = "Fluffy"):
        """Constructor for the individual class that sets and ID and phenotype for each individual"""
        self.id = id
        self.phen = phenotype

    def migration(self):
        # Chance of migration between populations
        # May be better to have in Landscapes
    

class population:

    def __init__(self,popSize = 0,phen = 1):
    """Population constructor that initializes the contents of each population and its size, while making sure that
        there are no duplicate individuals"""

        self.popSize = popSize
        self.phen = phenotype

        # Test populations
        # Checks which phenotype each population is initially classified as and then creates corresponding individuals
        self.indv = []

        if phen = 1:
            for i in range(popSize):
                self.indv.append( individual(id=I+1,phen = "Fluffy") )
        elif phen = 2:
            for i in range(popSize):
                self.indv.append( individual(id=I+1,phen = "Fuzzy") )

        #include a test to check for duplicates

    def move(self):
        # Add movement between populations
        # maybe a 'for' loop iterating over each individual 
        # or movement can be in the landscape class as a 'self.landscape.indv.move()'




class landscape:
"""Defines the landscape class that defines a list of populations and executes the migration between populations"""


    def __init__(self,popSize = 0):
        self.popSize = popSize

        #Test Landscape
        self.landscape = [population(popSize = 5,phen=1),population(popSize = 10,phen=2)]



    def move(self):
    """Executes all movement between populations"""

        for indv in self.landscape: # this is probably wrong

            # weighted random movement
            # Dispersion Matrix - needs to be implemented
            move = random.choices(migrate =["stay","leave"], weights=[0.9, 0.1])

            if move == "leave":
                #self.landscape[0].indiv.move()

                #self.landscape[1].indiv.append
                #self.landscape[0].indiv.remove
