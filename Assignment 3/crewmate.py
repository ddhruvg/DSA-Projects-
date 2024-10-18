'''
    Python file to implement the class CrewMate
'''

class CrewMate:
    '''
    Class to implement a crewmate
    '''
    
    def __init__(self):
        '''
        Arguments:
            None
        Returns:
            None
        Description:
            Initializes the crewmate
        '''
        # Write your code here
        self.load = 0
        self.treasure = []
        self.working = False
        self.starting_time = 0
        pass
    def add_treasure(self,treasure):
        self.load += treasure.size
        self.treasure.append(treasure)
# Add more methods if required

