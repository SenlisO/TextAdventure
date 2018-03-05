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

        # conduct random tests
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

    def test_alive(self):
        '''
        Test is alive function
        Summary: Tests creatures:is_alive function's ability to determine if object is still alive
        '''
        test_subject = Creature()
        damage = int(test_subject.get_health() / 2)  # calculate approx half of the creatures health
        test_subject.deal_damage(damage)

        # test if creatures is still alive
        self.assertTrue(test_subject.is_alive())

        test_subject.deal_damage(damage * 2)  # this should clearly go into the negative health
        self.assertFalse(test_subject.is_alive())

        # begin random damage tests
        count = 100
        while count > 0:
            test_random_subject = Creature()
            beggining_health = test_random_subject.get_health()  # get initial health
            damage = random.randint(0, beggining_health * 2)  # find a random damage number that will often be more thanb creature health

            # deal the damage
            test_random_subject.deal_damage(damage)

            if damage >= beggining_health:  # damage was more than the poor creature could stand
                self.assertFalse(test_random_subject.is_alive())
            else:  # the brave and valliant creature is alive!!!
                self.assertTrue(test_random_subject.is_alive())

            count -= 1


unittest.main()
