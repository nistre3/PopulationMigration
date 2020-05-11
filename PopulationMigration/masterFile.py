# Master File 
#
# A simulation of Warbling Babbler movement with different phenotypes between several populations
# in different landscapes aver the course of several weeks. This uses a randomized dispersal matrix
# to determine a rate of migration between populations. 
#
#
# !! Only Functional with Two Populations !!

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

        fluffPercent = round((fluffles/(fluffles+fuzzles)*100),2)
        fuzzPercent = round((fuzzles/(fluffles+fuzzles)*100),2)

        print("Population",popnum,"is",fluffPercent, "% Fluffy")
        print("Population",popnum,"is",fuzzPercent, "% Fuzzy\n")


class landscape:
    """Defines the landscape class that defines a list of populations and executes the migration between populations 
    and their initial phenotype"""


    def __init__(self,popSize1 = 0,popSize2 = 0,weight1 = [0.9,0.1],weight2 = [0.8,0.2]):
        """Constructor for Landscape that defines a population size that is passed to the populations inside of it"""

        self.popSize1 = popSize1 # PopSize of Pop1
        self.popSize2 = popSize2 # PopSize of Pop2
        self.weight1 = weight1
        self.weight2 = weight2

        # Landscapes - Only 2 Allowed
        self.lands = [population(popSize1,phenotype="Fluffy",weights=weight1),population(popSize2,phenotype="Fuzzy",weights=weight2)]

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






"""!!! Changeable Variables !!!"""
Pop1Size = 20   # Fluffy Population
Pop2Size = 15   # Fuzzy Population
Weeks = 100     # Number of Weeks
Weight1 = [0.5,0.5] # Pop1 Dispersal Values [stay value,leave value]
Weight2 = [0.5,0.5] # Pop2 Dispersal Values [stay value,leave value]






if ((Weight1[0]+Weight1[1]) != 1) & ((Weight2[0]+Weight2[1]) == 1): # Error Function
  exit("Weights must add up to one")

landscape = landscape(Pop1Size,Pop2Size,Weight1,Weight2)


pop1tot = []    # Contains Fluffy and Fuzzy count for Pop2
pop2tot = []    # Contains Fluffy and Fuzzy count for Pop2
size1tot = []   # List that contains total Pop1 Size
size2tot = []   # List that contains total Pop2 Size
weeknum = []    # List that contains total week number

for time in range(Weeks):
    """Iterates per week"""
    weeknum.append(time+1)
    
    fluff = 0 
    fuzz = 0
    pop = []

    for i in landscape.lands[0].indv: # Iterates over Pop1

        if i.phen == "Fluffy": # Counts Fluffy and Fuzzy for Pop1
            fluff+=1
        else:
            fuzz+=1

    size1tot.append(fluff+fuzz)
    pop.append(fluff)
    pop.append(fuzz)
    pop1tot.append(pop)

    fluff = 0 # Resets Fluff, Fuzz, and pop counts
    fuzz = 0
    pop = []

    for i in landscape.lands[1].indv: # Iterates over Pop2

        if i.phen == "Fluffy": # Counts Fluffy and Fuzzy for Pop1
            fluff+=1
        else:
            fuzz+=1
    
    size2tot.append(fluff+fuzz)
    pop.append(fluff)
    pop.append(fuzz)
    pop2tot.append(pop)

    landscape.move() # Movement function for individuals

    if time == (Weeks-1): # Prints the Final Population count
        fluff=0
        fuzz=0

        for i in landscape.lands[0].indv: # how to call landscape
            if i.phen == "Fluffy": # Counts fluff and fuzz
                fluff+=1
            else:
                fuzz+=1

        print("\nPopulation 1 has %d Fluffy and %d Fuzzy individuals after %d weeks" % (fluff,fuzz,Weeks))
        fluff=0
        fuzz=0

        for i in landscape.lands[1].indv: # how to call landscape
            if i.phen == "Fluffy": # Count fluss and fuzz
                fluff+=1
            else:
                fuzz+=1
        
        print("Population 2 has %d Fluffy and %d Fuzzy individuals after %d weeks" % (fluff,fuzz,Weeks))
        print("~~~~~~~~~~~~~")



sizetot=[] # Total Size for each Pop in a list
sizetot.append(size1tot)
sizetot.append(size2tot)


"""Plots for Pop Contents vs Time and Pop Size vs Time"""
plt.figure(figsize=(10,4))        
plt.subplot(121)
plt.axis([1,(Weeks+1),0,(Pop1Size+Pop2Size)])
plt.ylabel("Pop1 Phenotype:\n Fluff (Blue) and Fuzz (Orange)")
plt.xlabel("Week Number")
plt.plot(weeknum,pop1tot)

plt.subplot(122)
plt.axis([1,(Weeks+1),0,(Pop1Size+Pop2Size)])
plt.ylabel("Pop2 Phenotype:\n Fluff (Blue) and Fuzz (Orange)")
plt.xlabel("Week Number")
plt.plot(weeknum,pop2tot)

plt.figure(figsize=(10,4))
plt.subplot(212)
plt.axis([1,(Weeks+1),0,(Pop1Size+Pop2Size)])
plt.ylabel("Population Size:\n Pop1 (Blue) and Pop2 (Orange)")
plt.xlabel("Week Number")
plt.plot(weeknum,size1tot)
plt.plot(weeknum,size2tot)


popnum=0
for i in landscape.lands:
    """Prints out the percentage of each Pop"""
    popnum += 1
    i.prob(popnum)




