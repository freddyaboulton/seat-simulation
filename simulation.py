from collections import namedtuple
from typing import Tuple
import numpy as np
import tqdm

NUM_SEATS = 6

Seat = namedtuple("Seat", ['row', 'letter'])

def seats_are_adjacent(seat1: Seat, seat2: Seat) -> bool:

    if seat1.row == seat2.row:
        if seat1.letter == 2:
            return seat2.letter == 1
        elif seat1.letter == 3:
            return seat2.letter == 4
        else:
            return abs(seat1.letter - seat2.letter) == 1
    else:
        return False

class BasicAirplane:
    """Airplane with two aisles per row. Each row has 3 seats"""

    def __init__(self, num_rows: int) -> None:
        self.num_rows = num_rows

    def random_seats(self,) -> Tuple[Seat, Seat]:
        index1, index2 = np.random.choice(NUM_SEATS * self.num_rows, 2, replace=False)
        
        return Seat(index1 // NUM_SEATS, index1 % NUM_SEATS), Seat(index2 // NUM_SEATS, index2 % NUM_SEATS)


def simulation(sample_size: int, num_rows: int) -> float:

    airplane = BasicAirplane(num_rows)
    count = 0
    for _ in tqdm.tqdm(range(sample_size)):

        pair_of_seats = airplane.random_seats()
        count += seats_are_adjacent(*pair_of_seats)
    
    return count / sample_size


if __name__ == "__main__":

    print(simulation(int(1e6), 30))
    

        

