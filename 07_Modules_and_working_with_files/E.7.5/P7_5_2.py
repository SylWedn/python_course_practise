
import pickle
from P7_5_1 import Employee

with open('employee_list.pkl', 'rb') as pickle_in:
    new_file = pickle.load(pickle_in)
    for entry in new_file:
        print(entry)


