'''
Created on Dec 8, 2020

@author: DingYang
'''

import numpy as np
# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt

class AtomService:
    def __init__(self,asId,asName,price,reponseTime,availability,reputation,throughput,reliability):
        self.asId=asId
        self.asName=asName
        self.price=price
        self.reponseTime=reponseTime
        self.availability=availability
        self.reputation=reputation
        self.throughput=throughput
        self.reliability=reliability
    aggregationValue=0.0 
       
    def getAtomServices(self,fileName):
        atomServices=[]
        try:
            with open(fileName,'r') as file:
                datas=file.readlines()
                datas=datas[24:2524]
                for line in datas:
                    line=line.strip().split(',')
                    atomService=AtomService(line[14],line[13],float(line[11]),float(line[0]),int(line[1]),int(line[12]),float(line[2]),int(line[4]))
                    atomServices.append(atomService)
            del datas
            return atomServices
        except IOError as ioerr:
            print("File error:" + str(ioerr))
            return None
        finally:
            file.close()
    
    # uniform for attributes
    def aggregation(self,w):
            price=self.price/100
            reponseTime=self.reponseTime/5000
            availability=1/self.availability
            if self.reputation==0:
                reputation=1
            else:
                reputation=1/self.reputation
            throughput=(1/self.throughput)/10
            reliability=1/self.reliability
            return(w[0]*price+w[1]*reponseTime+w[2]*availability+w[3]*reputation+w[4]*throughput+w[5]*reliability)

# To aggregate for services in current composition scheme        
def multipleTasksAggregation(cs,w):
    cPrice=0.0
    cReponseTime=0.0
    cAvailability=1.0
    cReputation=0.0
    cThroughput=0.0
    cReliability=1.0
    length=len(cs)
    for serv in cs:
        cPrice+=serv.price
        cReponseTime+=serv.reponseTime
        cAvailability*=serv.availability
        cReputation+=serv.reputation
        cThroughput+=serv.throughput
        cReliability*=serv.reliability
    cPrice/=(100*length)
    cReponseTime/=(5000*length)
    cAvailability=((1/cAvailability)**length)/100
    if cReputation==0:
        cReputation=1
    cReputation=1/cReputation
    cThroughput=(1/cThroughput)/10
    cReliability=((1/cReliability)**length)/100
    return (w[0]*cPrice+w[1]*cReponseTime+w[2]*cAvailability+w[3]*cReputation+w[4]*cThroughput+w[5]*cReliability)

# To arise or descent sort for candidate service sets based on max weight
def sortOfservSetsByWeight(candidateServSets,w):
    servsets=[]
    mark=np.argmax(w)
    if mark==0:
        for servset in candidateServSets:
            servset.sort(key=lambda x:x.price, reverse=False)
            servsets.append(servset)
    if mark==1:
        for servset in candidateServSets:
            servset.sort(key=lambda x:x.reponseTime, reverse=False)
            servsets.append(servset)
    if mark==2:
        for servset in candidateServSets:
            servset.sort(key=lambda x:x.availability, reverse=True)
            servsets.append(servset)
    if mark==3:
        for servset in candidateServSets:
            servset.sort(key=lambda x:x.reputation, reverse=True)
            servsets.append(servset)
    if mark==4:
        for servset in candidateServSets:
            servset.sort(key=lambda x:x.throughput, reverse=True)
            servsets.append(servset)
    if mark==5:
        for servset in candidateServSets:
            servset.sort(key=lambda x:x.reliability, reverse=True)
            servsets.append(servset)
    return servsets

def sortOfservSetsByAggregationValue(candidateServSets,w):
    servsets=[]
    # Calculate aggregation value for per service
    for servSet in candidateServSets:
        for serv in servSet:
            serv.aggregationValue=serv.aggregation(w)
    for servset in candidateServSets:
            servset.sort(key=lambda x:x.aggregationValue, reverse=False)
            servsets.append(servset)
    return servsets

class PSO(object):
    def __init__(self, population_size, max_steps,dim,weights,candidateServSets):
        self.w = 0.6  # weight of inertia
        self.c1 = self.c2 = 2
        self.population_size = population_size  # number of particle
        self.dim = dim  # dimensions of search space,as well as presenting number of the service activities 
        self.max_steps = max_steps  # number of iterate
        self.weights=weights# weights for attributes of QoS
        self.candidateServSets=sortOfservSetsByWeight(candidateServSets,weights)
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
        noUpadateNum=0
        referNum=200# referring percentage of no updating 
        refer_global_best_fitness=0.0
        for step in range(self.max_steps):
            step
            if refer_global_best_fitness==self.global_best_fitness:
                noUpadateNum+=1
            if noUpadateNum>=referNum:
                self.x = np.random.randint(self.x_bound[0], self.x_bound[1],
                               (self.population_size, self.dim))  # To initiate positions for particles
                noUpadateNum=0# reset count
            else:
                r1 = np.random.rand(self.population_size, self.dim)*10
                r2 = np.random.rand(self.population_size, self.dim)*10
                # update velocity and position
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
            refer_global_best_fitness=self.global_best_fitness
            servPosition=self.pg
            print('best fitness: %.8f, mean fitness: %.8f, best position%s' % (self.global_best_fitness, np.mean(fitness),servPosition))
            
def optimizationServs(candidateServSets,weights):
    minFitnesses=[]# minimum aggregation value of per candidate service set
    bestPosition=[]# minimum position of per candidate service set
    cs=[]# service scheme
    for candidateServSet in candidateServSets:
        fitnesses=[]
        for candidateServ in candidateServSet:
            aggregationValue=candidateServ.aggregation(weights)
            fitnesses.append(aggregationValue)
        fitnesses=np.array(fitnesses)
        minFitnesses.append(np.min(fitnesses))
        bestPosition.append(np.argmin(fitnesses))
    for i in range(len(candidateServSets)):
        cs.append(candidateServSets[i][bestPosition[i]])
    bestValue=multipleTasksAggregation(cs,weights)  
    print('best fitness: %.5f, best position: %s'%(bestValue,bestPosition))