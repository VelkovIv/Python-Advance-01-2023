import unittest
from unittest import TestCase

from project.hero import Hero


class TestHero(TestCase):

    def setUp(self) -> None:
        self.hero = Hero('HeroName', 1, 10, 10)
        self.enemy = Hero('EnemyName', 1, 5, 5)

    def test_initialization_values(self):
        self.assertEqual(self.hero.username, 'HeroName')
        self.assertEqual(self.hero.level, 1)
        self.assertEqual(self.hero.health, 10)
        self.assertEqual(self.hero.damage, 10)

    def test_hero_battle_with_himself_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual(str(ex.exception), "You cannot fight yourself")

    def test_hero_battle_without_health_raise_value_error(self):
        self.hero.health = 0
        with self.assertRaises(Exception) as vr:
            self.hero.battle(self.enemy)
        self.assertEqual(str(vr.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_hero_battle_with_enemy_without_health_raise_value_error(self):
        self.enemy.health = 0
        with self.assertRaises(Exception) as vr:
            self.hero.battle(self.enemy)
        self.assertEqual(str(vr.exception), "You cannot fight EnemyName. He needs to rest")

    def test_battle_danage_takan_health_reduced_draw_results(self):
        self.enemy.health, self.enemy.damage = 10, 10
        result = self.hero.battle(self.enemy)
        self.assertEqual(self.hero.health, 0)
        self.assertEqual(result, "Draw")

    def test_battle_hero_wins(self):
        result = self.hero.battle(self.enemy)
        self.assertEqual(self.hero.health, 10)
        self.assertEqual(self.hero.damage, 15)
        self.assertEqual(self.hero.level, 2)
        self.assertEqual(result, "You win")

    def test_battle_hero_lose(self):
        self.hero, self.enemy = self.enemy, self.hero
        result = self.hero.battle(self.enemy)
        self.assertEqual(self.enemy.health, 10)
        self.assertEqual(self.enemy.damage, 15)
        self.assertEqual(self.enemy.level, 2)
        self.assertEqual(result, "You lose")

    def test__str__(self):
        self.assertEqual(self.hero.__str__(), f"Hero HeroName: 1 lvl\n" +
               f"Health: 10\n" +
               f"Damage: 10\n")


if __name__ == '__main__':
    unittest.main()
