"""

Submitted By: Md Mehedee Zaman Khan
Matrikel-Nr.: 665630
Email: mehedee.zaman95@gmail.com


Problem: Write a script for performing the experiment defined in problem 1 (i.e., for investigating
the effect of the parameter value p).
Hint: You can start with the script below and modify the script accordingly.
"""

""" Import modules"""
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

""" Class definitions"""

""" Class for agents
"""
class Agent():
    def __init__(self, id_number, S):
        """
        Constructor method

        Parameters
        ----------
        id_number : int
            ID number of the agent
        S : Simulation object
            Simulation the agent belongs to

        Returns
        -------
        Agent object.
        """
        """ Record ID and Simulation of the Agent"""
        self.S = S
        self.ID = id_number
        
        """ Initialize attributes"""
        self.infected = 0
        self.immune = 0
        self.exposed = False

    def get_status(self):
        """
        Getter method for infection and immune status of the agent

        Returns
        -------
        Tuple (bool, bool) 
            Is the agent infected?, is the agent immune?
        """
        return bool(self.infected), bool(self.immune)
    
    def be_exposed(self):
        """
        Method for marking the agent as exposed to the infection.

        Returns
        -------
        None.
        """
        self.exposed = True
    
    def get_neighbors(self):
        """
        Method for returning the list of neighbors of the agent.

        Returns
        -------
        List if int:
            Index numbers of the neighbors
        """
        return nx.neighbors(self.S.G, self.ID)
    
    def iterate(self):
        """
        Method for iterating the agent; exposing neighbors; handling
        infection and immunity periods, etc.

        Returns
        -------
        None.
        """
        """ Expose neighbors if the agent is infected with a certain 
            probability"""
        if self.infected:
            neighbors = self.get_neighbors()
            for neighbor_ID in neighbors:
                if np.random.random() < self.S.infection_probability:
                    A = self.S.agent_list[neighbor_ID]
                    A.be_exposed()
        
        """ Decrement immunity period, switch to susceptible"""
        if self.immune:
            self.immune -= 1

        """ Decrement infection period, switch to immune"""
        if self.infected:
            self.infected -= 1
            if self.infected == 0:
                self.immune = self.S.time_immune

    def become_infected(self):
        """
        Method for setting agent infected if the agent has been exposed 
        and is not already infected or immune

        Returns
        -------
        None.
        """
        if self.exposed and (not self.infected) and (not self.immune):
            self.infected = self.S.time_infected
        self.exposed = False

"""Simulation class"""    
class Simulation():
    def __init__(self):
        """
        Constructor method

        Returns
        -------
        Simulation instance.

        """
        """ Define variables"""
        self.n_agents = 1000
        self.time_infected = 10
        self.time_immune = 20
        self.t_max = 200
        self.infection_probability = 0.004
        self.p =p
        """ Generate the network"""
        """ Erdös-Renyi network"""
        self.G = nx.erdos_renyi_graph(n=self.n_agents, p=p)
        
        """ You can also try other network structures. They will lead 
            to very different dynamics"""
        """Barabasi-Albert network"""
        #self.G = nx.barabasi_albert_graph(n=self.n_agents, m=40)
        """Watts-Strogatz network"""
        #self.G = nx.watts_strogatz_graph(n=self.n_agents, k=40, p=0.15)
        
        """ Create agents"""
        self.agent_list = []
        
        for i in range(self.G.number_of_nodes()):
            A = Agent(i, self)
            self.agent_list.append(A)
            self.G.nodes[i]["agent"] = A
        
        """ Prepare history variables"""
        self.history_susceptible = []
        self.history_infected = []
        self.history_immune = []
        self.history_time = []
        
        """ Infect patient zero"""
        patient_zero = np.random.choice(self.agent_list)
        patient_zero.be_exposed()
        
    def run(self):
        """
        Method for running the simulation. For each time step, it 
        completes the following sequence of events:
            1. Set counters to zero
            2. Loop over all agents and 
                - set neighbors to exposed
                - collect statistics (infection, immunity)
            3. Loop over all agents and set exposed agents to infected
            4. Calculate the number of susceptible (non-immune, 
               non-exposed) agents
            5. Record statistics 
        It also calls self.plotting() after the end of the time 
        iteration.

        Returns
        -------
        None.

        """
        """ Time iteration"""
        for t in range(self.t_max):
            """ Set counters for immune and infected agents to zero"""
            n_infected = 0
            n_immune = 0
            
            """ Iterate through the agents"""
            for A in self.agent_list:
                
                """ Iterate agent"""
                A.iterate()
                
                """ Obtain state of the agent"""
                infected, immune = A.get_status()
                
                """ Adjust counters"""
                if infected:
                    n_infected += 1
                if immune:
                    n_immune += 1
                
            """ Infect exposed agents"""
            for A in self.agent_list:
                A.become_infected()
            
            """ Compute number of susceptible agents"""
            n_susceptible = self.n_agents - n_infected - n_immune

            """ Record into history"""
            self.history_susceptible.append(n_susceptible)
            self.history_infected.append(n_infected)
            self.history_immune.append(n_immune)
            self.history_time.append(t)

        """ Call plotting method"""
        self.plotting()
            
    def plotting(self):
        """
        Method for plotting the development of the simulation.

        Returns
        -------
        None.

        """
        fig, ax = plt.subplots(nrows=1, ncols=1, squeeze=False)
        ax[0][0].plot(self.history_time, 
                      self.history_susceptible, 
                      color='g', 
                      label="Susceptible")
        ax[0][0].plot(self.history_time, 
                      self.history_infected, 
                      color='r', 
                      label="Infected")
        ax[0][0].plot(self.history_time, 
                      self.history_immune, 
                      color='b', 
                      label="Immune")
        ax[0][0].set_xlabel("Time")
        ax[0][0].set_xlabel("Number of agents")
        ax[0][0].legend()
        plt.tight_layout()
        plt.savefig("SIR.pdf")
        plt.show()
        
        
        
    
""" Main entry point"""
if __name__ == '__main__':
    """Define range of infection probabilities to test"""
    p_values = [0.1, 0.2, 0.3, 0.4, 0.5]
    
    """Dictionary to store simulation results"""
    results = {}
    
    for p in p_values:
        """Create simulation with current infection probability"""
        S = Simulation()
        """Run simulation"""
        S.run()
        """ Store simulation results in dictionary"""
        results[p] = {
            "susceptible": S.history_susceptible,
            "infected": S.history_infected,
            "immune": S.history_immune,
            "time": S.history_time
        }
        
    """ Plot results """
    for p in p_values:
        plt.plot(results[p]["time"], results[p]["infected"], label=f"p={p}")
    
    plt.xlabel("Time")
    plt.ylabel("Number of infected agents")
    plt.legend()
    plt.show()
        