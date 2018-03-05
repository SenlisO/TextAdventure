class Creature:
    '''
    Class creature
    Tracks characteristics and status of all living objects in game world
    '''
    def __init__(self):
        '''
        Initialization function
        Summary: Right now, it only creates the health attribute
        '''
        self.health = 100

    def deal_damage(self, damage):
        '''
        Deal damage function
        Summary: reduces creature's health by param damage
        Paramters: init damage -- indicates how much damage to deal
        '''
        if not isinstance(damage, int):
            print("Debug error at Creature.deal_damage: damage is not in integer")
            raise ValueError

        self.health -= damage

    def is_alive(self):
        '''
        Is alive function
        Summary: Used to determine if the creature is above min health
        Returns: returns false if health is below or equals to 0, otherwise true
        '''
        if self.health <= 0:
            return False
        else:
            return True

    def get_health(self):
        '''
        Get health function
        Summary: Get function to return creatures health
        Returns: creatures health as int
        '''
        return self.health
