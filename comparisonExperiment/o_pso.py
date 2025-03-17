'''
Created on Dec 8, 2020

@author: DingYang
'''

import numpy as np
# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt
from service.atomService import multipleTasksAggregation

class PSO(object):
    def __init__(self, population_size, max_steps,dim,weights,candidateServSets):
        self.w = 0.6  # weight of inertia
        self.c1 = self.c2 = 2
        self.population_size = population_size  # number of particle
        self.dim = dim  # dimensions of search space,as well as presenting number of the service activities 
        self.max_steps = max_steps  # number of iterate
        self.weights=weights# weights for attributes of QoS
        self.candidateServSets=candidateServSets
        self.x_bound = [0, 100]  # space of solutions
        self.x = np.random.randint(self.x_bound[0], self.x_bound[1],
                                   (self.population_size, self.dim))  # To initiate positions for particles
        self.v = np.random.randint(1,25,(self.population_size, self.dim))  # To initiate velocities for particles
        fitness = self.calculate_fitness()
        self.p = self.x  # A position of best of single particle 
        self.pg = self.x[np.argmin(fitness)]  # Global best position
        self.individual_best_fitness = fitness  # fitness values of all single particles
        self.global_best_fitness = np.min(fitness)  # global fitness value
 
    def calculate_fitness(self):# w are weights for attributes
        fitnessList=[]
        for i in range(len(self.x)):
            cs=[]
            fitness=0.0
            # To process list elements these are out of the list 
            for j in range(len(self.x[i])):
                # To initiate positions of particles if the list is out
                if (self.x[i][j]>99)|(self.x[i][j]<0):
                    self.x[i][j] = np.random.randint(0,100)
                cs.append(self.candidateServSets[j][self.x[i][j]])
            fitness=multipleTasksAggregation(cs,self.weights)
            fitnessList.append(fitness)
        return np.array(fitnessList) #convert to numpy array
 
    def evolve(self):
        for step in range(self.max_steps):
            step
            r1 = np.random.rand(self.population_size, self.dim)*10
            r2 = np.random.rand(self.population_size, self.dim)*10
            # update velocity and weight
            self.v = self.w*self.v+self.c1*r1*(self.p-self.x)+self.c2*r2*(self.pg-self.x)
            self.x = self.v.astype(int) + self.x
            fitness = self.calculate_fitness()
            # single particle update if it need update
            update_id = np.greater(self.individual_best_fitness, fitness)
            self.p[update_id] = self.x[update_id]
            self.individual_best_fitness[update_id] = fitness[update_id]
            # update global fitness and best position
            if np.min(fitness) < self.global_best_fitness:
                self.pg = self.x[np.argmin(fitness)]
                self.global_best_fitness = np.min(fitness)
            servPosition=self.pg
            print('best fitness: %.8f, mean fitness: %.8f, best position%s' % (self.global_best_fitness, np.mean(fitness),servPosition))