
"""

Submitted By: Md Mehedee Zaman Khan
Matrikel-Nr.: 665630
Email: mehedee.zaman95@gmail.com


"""
""" Import modules"""
import numpy as np
import matplotlib.pyplot as plt

""" Class definitions"""
""" Agent class"""
class Agent():
    def __init__(self, id_number):
        """
        Agent class constructor method

        Parameters
        ----------
        id_number : int
            The agent's ID number'

        Returns
        -------
        None.

        """
        """ initialize class level variables"""
        self.id = id_number
        self.money = 1000
        


    def pay(self, amount, Receiver):
        """
        Method for paying other agents.

        Parameters
        ----------
        amount : float or int
            Amount being paid
        Receiver : Agent instance
            Agent being paid

        Returns
        -------
        None.

        """
        self.money -= amount
        Receiver.receive(amount)
    
    def receive(self, amount):
        """
        Method for receiving payments

        Parameters
        ----------
        amount : float or int
            Amount being received.

        Returns
        -------
        None.

        """
        self.money += amount
    
    def get_money(self):
        """
        Getter method for Agent.money

        Returns
        -------
        float or int
            Money currently owned by the agent 

        """
        return self.money

    def invest(self):
        """
        Investment method. Yields stochastic returns to agent's money 
        following a Kesten process.

        Returns
        -------
        None.
        """
        self.money = 0.9 * self.money * \
                     (0.92 + np.random.exponential(0.2)) +\
                     np.random.exponential(0.3)
        
        
""" Simulation class"""
class Simulation():
    def __init__(self):
        """
        Simulation class constructor method

        ...
        """
        """ Define simulation-level parameters"""
        self.number_of_agents = 1000
        self.number_of_time_periods = 1000
        self.number_of_interactions_per_time_period = 100
        
        """ Create the agents"""
        self.list_of_agents = []
        for i in range(self.number_of_agents):
            A = Agent(i)
            self.list_of_agents.append(A)
    
    def run(self):
        
        """Time iteration"""
        for j in range(self.number_of_time_periods):
            for A in self.list_of_agents:
                A.invest()
                """each agent participates on average once every ca. 5 timesteps"""
                if (j % 5 == 0):
                    B = np.random.choice(self.list_of_agents)
                    payment_amount = np.random.uniform(0, A.get_money())
                    A.pay(payment_amount, B)
            print("Time step is ", j, " of ", self.number_of_time_periods)
        
        self.assess_money_distribution()
            
    def assess_money_distribution(self):
        """
        Method for collecting and visualizing the results of the 
        simulation.

        Returns
        -------
        None.

        """
        """ Collect data on money owned by each agent"""
        self.money_distribution = []
        """ Loop over agents"""
        for A in self.list_of_agents:
            """ How much money does this agent have"""
            money = A.get_money()
            """ Record into list"""
            self.money_distribution.append(money)
        
        """ Plot money distribution in (1) linear, (2) semi-log, and (3) 
            log-log plots"""
        fig, ax = plt.subplots(nrows=3, ncols=1, squeeze=False)
        
        """ Linear plot in [0][0]"""
        ax[0][0].hist(self.money_distribution, bins=75, color='b', 
                     alpha=0.6, rwidth=0.85)
        ax[0][0].set_xlabel("Money")
        ax[0][0].set_ylabel("Frequency")

        """ Semi-log plot in [1][0]"""
        ax[1][0].hist(self.money_distribution, bins=75, color='b', 
                     alpha=0.6, rwidth=0.85)
        ax[1][0].set_xlabel("Money")
        ax[1][0].set_ylabel("Frequency")
        ax[1][0].set_yscale("log")
        
        """ Log-log plot in [2][0]"""
        ax[2][0].hist(np.log(self.money_distribution), bins=75, color='b', 
                     alpha=0.6, rwidth=0.85)
        ax[2][0].set_xlabel("log(Money)")
        ax[2][0].set_ylabel("Frequency")
        ax[2][0].set_yscale("log")
        
        """ Save and show figure"""
        plt.tight_layout()
        plt.savefig("distribution_a4.pdf")
        plt.show()
        
        
""" Definitions of global functions?"""

""" Main script"""
if __name__ == '__main__':
    """ Create Simulation object"""
    S = Simulation()
    """ Run simulation"""
    S.run()
