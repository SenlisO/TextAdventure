import unittest
from creature import Creature
import random


class TestCreatures(unittest.TestCase):
    def test_damage(self):
        '''
        Test damage function
        Summary: tests Creature.deal_damage function with a fixed amount
        '''
        # create the test subject and observe health
        test_subject = Creature()
        initial_health = test_subject.get_health()

        # deal some damage
        test_subject.deal_damage(50)
        end_health = test_subject.get_health()

        # make the comparison
        self.assertEqual(initial_health, end_health + 50)

    def test_random_damage(self):
        '''
        Test random damage
        Summary: tests Creature.deal_damage with multiple random amounts
        '''
        count = 100  # controls how many times we do the test
        while count > 0:  # continue until we count down to 0
            test_subject = Creature()  # we build our test subject every time
            initial_health = test_subject.get_health()

            damage = random.randint(1, 100)  # choose a random number from 1 to 100
            test_subject.deal_damage(damage)
            end_health = test_subject.get_health()

            # make the comparison
            self.assertEqual(initial_health, end_health + damage)

            count -= 1


unittest.main()
