def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """
    num_list = list(range(start, stop + 1))
    for num in num_list:
        print(num)


count_up(5, 7)        
count_up(20, 40)        
