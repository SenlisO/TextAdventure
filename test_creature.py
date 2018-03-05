import unittest
from creature import Creature


class TestCreatures(unittest.TestCase):
    def test_damage(self):
        # create the test subject and observe health
        test_subject = Creature()
        initial_health = test_subject.get_health()

        # deal some damage
        test_subject.deal_damage(50)
        end_health = test_subject.get_health()

        # make the comparison
        self.assertEqual(initial_health, end_health + 50)


unittest.main()
