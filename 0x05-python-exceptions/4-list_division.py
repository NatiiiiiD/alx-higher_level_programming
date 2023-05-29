#!/usr/bin/python3
def list_division(the_list_1, the_list_2, list_length):
    divisions = []
    for index in range(list_length):
        result = 0
        try:
            result = the_list_1[index] / the_list_2[index]
        except ZeroDivisionError:
            print('division by 0')
        except TypeError:
            print('wrong type')
        except IndexError:
            print('out of range')
        finally:
            divisions.append(result)

    return divisions
