import unittest
from unittest import TestCase

from project.team import Team


class TestTeam(TestCase):
    def setUp(self) -> None:
        self.team = Team('One')

    def test_initialization(self):
        self.assertEqual(self.team.name, 'One')
        self.assertEqual(self.team.members, {})

    def test_setter_name_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.team.name = 'One1'
        self.assertEqual(str(ve.exception), "Team Name can contain only letters!")

    def test_add_member(self):
        res = self.team.add_member()
        self.assertEqual(self.team.members, {})
        self.assertEqual(len(self.team.members), 0)
        self.assertEqual(res, "Successfully added: ")

    def test_remove_member(self):
        self.team.members = {'Ivan': 30, 'Peter': 29}
        res = self.team.remove_member('Ivan')
        self.assertEqual(res, "Member Ivan removed")
        self.assertEqual(len(self.team.members), 1)
        res1 = self.team.remove_member('Ivan')
        self.assertEqual(res1, "Member with name Ivan does not exist")

    def test__gt__(self):
        self.team.members = {'Ivan1': 30, 'Peter1': 29}
        team = Team('Two')
        team.members = {'Ivan': 30, 'Peter': 29, 'Maria': 25}
        self.assertEqual(self.team.__gt__(team), False)
        team = Team('Two')
        team.members = {'Ivan': 30}
        self.assertEqual(self.team.__gt__(team), True)

    def test__len__(self):
        self.team.members = {'Ivan1': 30, 'Peter1': 29}
        self.assertEqual(self.team.__len__(), 2)

    def test__add__(self):
        self.team.members = {'Peter': 29}
        team = Team('Two')
        team.members = {'Ivan': 30}
        new_team = self.team.__add__(team)
        self.assertEqual(new_team.name, "OneTwo")
        self.assertEqual(len(new_team.members), 2)
        self.assertEqual(new_team.members, {'Peter': 29, 'Ivan': 30})

    def test__str__(self):
        self.team.members = {'Ivan': 30, 'Peter': 29, 'Maria': 25}
        res = 'Team name: One\nMember: Ivan - 30-years old\nMember: Peter - 29-years old\nMember: Maria - 25-years old'
        self.assertEqual(self.team.__str__(), res)


if __name__ == '__main__':
    unittest.main()
