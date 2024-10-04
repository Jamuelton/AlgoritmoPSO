import math
import random
import matplotlib.pyplot as plt 

def fitness(particle,problem="sphere"):

    if(problem == "sphere"):
        resultado = 0
  
        for i in particle:
            resultado += i**2
        
        return resultado
    
    if(problem == "rastrigin"):
        resultado = 0
  
        for i in particle:
            numero = 2 * 3.1415 * i
            p = (numero/180) * math.pi
            resultado+= (i**2) - (10 * math.cos(p)) + 10
    
        return resultado
    
    if(problem == "rosenbrock"):
        resultado = 0
  
        for i in range(0,(len(particle)-1)):
            resultado += 100*(particle[i+1] - particle[i]**2)**2 + (particle[i] - 1)**2
    
        return resultado  


class Particle:
    def __init__(self,minLimit,maxLimit,dimentions,funcFit):
        self.position = [random.uniform(minLimit, maxLimit) for _ in range(dimentions)]
        self.velocity = [random.uniform(-20, 20) for _ in range(dimentions)]
        self.bestPosition = list(self.position)
        self.bestValue = fitness(self.position,funcFit)

    def __str__(self):
        return (f"Partícula: \n"
                f"Posição: {self.position}\n"
                f"Velocidade: {self.velocity}\n"
                f"Melhor Posição Pessoal: {self.bestPosition}\n"
                f"Melhor Valor Pessoal: {self.bestValue}\n")

    def updateVelocity(self, globalBestPosition,chooseW,c1,c2):

        newVelocity = []
        for i in range(len(self.position)):
            r1 = random.random()
            r2 = random.random()
            
            cognitiveComponent = c1 * r1 * (self.bestPosition[i] - self.position[i])
            socialComponent = c2 * r2 * (globalBestPosition[i] - self.position[i])
            inertiaComponent = chooseW * self.velocity[i]
            
            newVelocity.append(inertiaComponent + cognitiveComponent + socialComponent)
        
        self.velocity = newVelocity
    
    def updatePosition(self,minLimit,maxLimit):
       
        newPosition = []
        for i in range(len(self.position)):
            new = self.position[i] + self.velocity[i]

            new = max(minLimit, min(new, maxLimit))
            newPosition.append(new)
        
        self.position = newPosition

    def verifyOutLimit(self,minLimit,maxLimit):
        for i in range(len(self.position)):
            if not(minLimit <= i <= maxLimit): 
                print(f"Partícula {self} fora dos limites")
                self.position = [minLimit,maxLimit]

def pso(minLimit,maxLimit,dimentions,funcFit,particles,interations,typeW,w,wMin,wMax,cooperation,c1,c2):

    sworm = [Particle(minLimit,maxLimit,dimentions,funcFit) for _ in range(particles)]

    bestGlobal = sworm[0].bestPosition
    bestValueGlobal = fitness(bestGlobal,funcFit)
    # print("==================================================================")
    # print(f"Primeiro melhor global: {bestGlobal}")
    # print(f"Primeiro melhor valor global {bestValueGlobal}")
    # print("==================================================================")


    for interation in range(interations):

        if(typeW == "constant"):
            chooseW = w

        if(typeW == "decreasing"):
            chooseW = wMax - (wMax - wMin) * (interation / interations)

        #c = 1
        for particle in sworm:
            
            # print("==================================================================")
            # print(f"Número {c}")
            # print(particle)

            if(cooperation == "global"):
                particle.updateVelocity(bestGlobal,chooseW,c1,c2)

                particle.updatePosition(minLimit,maxLimit)

                particle.verifyOutLimit(minLimit,maxLimit)

            if(cooperation == "local"):

                leftParticle = (sworm.index(particle) - 1) % len(sworm)
                rightParticle = (sworm.index(particle) + 1) % len(sworm)
        
                localParticles = [sworm[leftParticle], sworm[sworm.index(particle)], sworm[rightParticle]]

                bestParticleLocal = min(localParticles, key=lambda particle: fitness(particle.position))

                particle.updateVelocity(bestParticleLocal.position,chooseW,c1,c2)

                particle.updatePosition(minLimit,maxLimit)

                particle.verifyOutLimit(minLimit,maxLimit)
            
            fit = fitness(particle.position)

            if (fit < particle.bestValue):
                particle.bestValue = fit
                particle.bestPosition = list(particle.position)

            if (fit < bestValueGlobal):
                bestValueGlobal = fit
                bestGlobal = list(particle.position)
           

            #c=c+1

        #print(f"Iteração {interation + 1}/{interations} - Melhor valor global: {bestValueGlobal}")
    
    print(f"Melhor solução encontrada: {bestGlobal} com valor: {bestValueGlobal}")

    return bestValueGlobal

def plotGraft(scenario1, scenario2,scenario3, execution=30):

    executions = execution

    scenarioConjunt = [scenario1,scenario2,scenario3]

    data = []

    for scenario in scenarioConjunt:
        resultsSceanrios = [] 
        for _ in range(executions):
            bestValue = pso(
                minLimit=scenario["minLimit"],
                maxLimit=scenario["maxLimit"],
                dimentions=scenario["dimentions"],
                funcFit=scenario["funcFit"],
                particles=scenario["particles"],
                interations=scenario["interations"],
                typeW=scenario["typeW"],
                w=scenario["w"],
                wMax=scenario["wMax"],
                wMin=scenario["wMin"],
                cooperation=scenario["cooperation"],
                c1=scenario["c1"],
                c2=scenario["c2"]
            ) 
            resultsSceanrios.append(bestValue)
    
    
        data.append(resultsSceanrios)


    plt.figure(figsize=(8, 6))
    plt.boxplot(data, labels=[f'Cenário {index + 1}' for index, _ in enumerate(scenarioConjunt)])


    plt.title('Boxplot dos Melhores Valores Globais em Diferentes Cenários', fontsize=14)
    plt.xlabel('Cenários', fontsize=12)
    plt.ylabel('Melhores Valores Globais', fontsize=12)


    plt.show()


scenarios1 = {'minLimit':-100,"maxLimit":100,"dimentions":2,"funcFit":"sphere","particles":30,"interations":100,"typeW":"constant","w":1,"wMin":0.7,"wMax":1.2,"cooperation":"global","c1":2.05,"c2":2.05}
        
scenarios2 = {"minLimit":-100,"maxLimit":100,"dimentions":2,"funcFit":"rastrigin","particles":30,"interations":100,"typeW":"constant","w":1,"wMin":0.7,"wMax":1.2,"cooperation":"global","c1":2.05,"c2":2.05}

scenarios3 = {"minLimit":-100,"maxLimit":100,"dimentions":2,"funcFit":"rosenbrock","particles":30,"interations":100,"typeW":"constant","w":1,"wMin":0.7,"wMax":1.2,"cooperation":"global","c1":2.05,"c2":2.05}

plotGraft(scenario1=scenarios1,
          scenario2=scenarios2,
          scenario3=scenarios3,
          execution=30)

#Instruções

# função fitnes - sphere - rastringin - rosenbrock
# tipoW - decreasing - constant
# tipo de comperação - local - global

