import unittest
from simulation import Seat, seats_are_adjacent, BasicAirplane

class Test_Seat(unittest.TestCase):

    def test_equal_returns_true(self,):
        self.assertTrue(Seat(0, 0) == Seat(0, 0))
    
    def test_not_equal_returns_false(self, ):
        self.assertFalse(Seat(0, 1) == Seat(0, 2))

class Test_seats_are_adjacent(unittest.TestCase):

    def test_different_row_false(self):
        self.assertFalse(seats_are_adjacent(Seat(0, 1), Seat(1, 1)))
        self.assertFalse(seats_are_adjacent(Seat(10, 4), Seat(15, 3)))
    
    def test_same_row_false(self):
        self.assertFalse(seats_are_adjacent(Seat(20, 0), Seat(20, 2)))
        self.assertFalse(seats_are_adjacent(Seat(15, 3), Seat(15, 5)))
        self.assertFalse(seats_are_adjacent(Seat(17, 0), Seat(17, 5)))

    def test_same_aisle_false(self):
        self.assertFalse(seats_are_adjacent(Seat(19, 2), Seat(19, 3)))

    def test_adjacent_window_middle(self):
        self.assertTrue(seats_are_adjacent(Seat(10, 0), Seat(10, 1)))
        self.assertTrue(seats_are_adjacent(Seat(14, 4), Seat(14, 5)))
    
    def test_adjacent_middle_aisle(self):
        self.assertTrue(seats_are_adjacent(Seat(15, 1), Seat(15, 2)))
        self.assertTrue(seats_are_adjacent(Seat(15, 3), Seat(15, 4)))
    
    def test_all(self):
        self.assertTrue(seats_are_adjacent(Seat(15, 0), Seat(15, 1)))
        self.assertTrue(seats_are_adjacent(Seat(15, 1), Seat(15, 2)))
        self.assertTrue(seats_are_adjacent(Seat(15, 3), Seat(15, 4)))
        self.assertFalse(seats_are_adjacent(Seat(15, 0), Seat(15, 2)))
        self.assertFalse(seats_are_adjacent(Seat(15, 2), Seat(15, 3)))
        self.assertFalse(seats_are_adjacent(Seat(15, 0), Seat(15, 5)))


class TestBasicAirplane(unittest.TestCase):

    def test_random_seats(self):
        seat1, seat2 = BasicAirplane(1).random_seats()
        self.assertFalse(seat1 == seat2)