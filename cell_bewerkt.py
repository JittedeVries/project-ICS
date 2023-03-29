import random
from mesa import Agent

class Cell(Agent):
    '''Description of the grid points of the CA'''

    # Definitions of state variables    
    Susceptible = 1
    Infected = 2
    Recovered = 3
    
    def __init__(self,pos,model,init_state=0):
        '''Create cell in given x,y position, with given initial state'''
        super().__init__(pos,model)
        self.x,self.y = pos
        self.state = init_state
        self.timecounter = 0
        self.timecounter2 = 0
        self.inf = 0.0
        self.infduration = 0
        self._nextstate = None
        self._nextinf = None
        self._nextinfduration = None

    def step(self):
        '''Compute the next state of a cell'''
        # Assume cell is unchanged, unless something happens below
        self._nextinf = self.inf
        self._nextinfduration = self.infduration
        self._nextstate = self.state
        

        # Susceptibles - might die or get infected
        if self.state == self.Susceptible:
                neis = self.model.grid.get_neighbors((self.x, self.y), moore=True, include_center=False)
                tot_inf = 0.0
                for nei in neis:
                    if nei.state == self.Infected:
                        tot_inf += nei.inf
                infprob = 0.0
                if tot_inf > 0:
                    infprob = tot_inf / (tot_inf + self.model.h_inf)
                if random.random() < infprob:
                    self._nextstate = self.Infected
                    # Inherit infectivity of one infecting neighbour
                    infprobsum = 0.0
                    rand = random.uniform(0, tot_inf)
                    for nei in neis:
                        if nei.state == self.Infected:
                            infprobsum += nei.inf
                            if rand < infprobsum:
                                # Inherit pathogen characteristics from infecting neighbour
                                self._nextinf = nei.inf
                                self._nextinfduration = nei.infduration
                                break

        # Infected - might die naturally or die after disease_duration
        elif self.state == self.Infected:
            # Natural death or death by disease
            if self.timecounter > self.infduration:
                self._nextstate = 3
                self._nextinf = 0.0
                self._nextinfduration = 0
                self.timecounter = 0
                self.timecounter2 = 0
            # Else count how long it has been ill and apply potential mutations
            else:
                self.timecounter += 1
        elif self.state == self.Recovered:
            if self.timecounter2 > self.model.immunity_duration:
                self._nextstate = 1
            else:
                self.timecounter2 += 1
                

    def advance(self): 
        self.state = self._nextstate
        self.inf = self._nextinf
        self.infduration = self._nextinfduration
