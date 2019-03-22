# Split a string into two columns.

from pandas import *

def g_fun(_id):

    """ This function helps parsing the _id into product_id and 
	vehicle_id.
    """
    split_id = _id.split('_')
    return split_id[0], split_id[1]

data_frame[n1], data_frame[n2] = zip(*data_frame[n3].apply(g_fun))
