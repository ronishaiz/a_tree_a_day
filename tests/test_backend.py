import unittest

from backend.get_url import get_today_str, map_date_to_index
from backend.tree_ids import TREE_IDS


class TestBackend(unittest.TestCase):

    def test_get_today_str(self):
        today_str = get_today_str()
        self.assertEqual(8, len(today_str))

    def test_map_date_to_index_twice(self):
        ind_1 = map_date_to_index('01/18/24')
        ind_2 = map_date_to_index('01/18/24')

        self.assertEqual(ind_1, ind_2)

    def test_map_date_to_index_diff_day(self):
        ind_1 = map_date_to_index('01/18/24')
        ind_2 = map_date_to_index('02/18/24')

        self.assertNotEqual(ind_1, ind_2)
        self.assertLess(ind_1, len(TREE_IDS))
        self.assertLess(ind_2, len(TREE_IDS))
