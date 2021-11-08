from time import time
from math import inf
from collections import deque, defaultdict
import unittest
from datetime import datetime, timedelta
a = time()


if __name__ == "__main__":
    # unittest.main()
    start_date = datetime(1901, 1, 1)
    end_date = datetime(2001, 1, 1)
    current_date = start_date
    sunday_first_day_amount = 0
    while current_date != end_date:
        if current_date.weekday() == 6 and current_date.day == 1:
            sunday_first_day_amount += 1
        current_date = current_date + timedelta(days=1)
    print(f"The answer is {sunday_first_day_amount}")
    print(time()-a)

