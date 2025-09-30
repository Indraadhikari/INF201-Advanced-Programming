#------------- Indra Bdr Adhikari -------------
# ------------------ Task 1 ---------------
def dict_to_records(data: dict):
    # If data is empty
    if not data:
        return []
    lengths = []
    #Get lengths of all lists
    for n in data.values():
        lengths.append(len(n)) #print(lengths)

    # if all lists are same length
    if len(set(lengths)) != 1:
        raise ValueError("Lists in the dictionary must be of the same length.")

    keys = list(data.keys())
    records = []

    # Loop over grouped values
    for values in zip(*data.values()):
        record = {}
        for k, v in zip(keys, values):
            record[k] = v   # assign each key: value
        records.append(record)
    print(records)


l = {'name': ['Joe', 'Pia', 'Even', 'Abdul'], 
 'age': [22, 24, 21, 23],
 'phone': ['12345678', '23456789', '34567890', '45678901']}
#l = {}
dict_to_records(l)

#%%
# Task 2
import pandas as pd

records = [
    {'name': 'Joe', 'age': 22, 'phone': '12345678'},
    {'name': 'Pia', 'age': 24, 'phone': '23456789'},
    {'name': 'Even', 'age': 21, 'phone': '34567890'},
    {'name': 'Abdul', 'age': 23, 'phone': '45678901'}
]
# Convert to DataFrame
df = pd.DataFrame(records)

# Compute average age
average_age = df['age'].mean()

print(df)
print('----------------------')
print("Average Age:", average_age)
# %%
#---------------- Task 3 --------------
#------------ using a Python list ---------

def using_list(n: int):
    prime = []
    #list of numbers up to n.
    for i in range(2,n+1,1):
        prime.append(i)

    for j in prime:
        for i in prime:
            if i >= j*j:
                if i % j == 0: #if i % j != 1: # 121
                    #print(j) #print(i)
                    prime.remove(i)
    return prime
# -------------------- using NumPy ---------
def using_NumPy(n: int):
    import numpy as np
    primes = np.arange(2, n+1)
    for j in primes:
        for i in primes:
            if i >= j*j:
                if i % j == 0:
                    #print(i)
                    primes = primes[primes != i]
    return primes
#------------- using Python Sets
def using_Sets(n: int):
    prime = set(range(2, n+1))

    for j in prime.copy():
        for i in prime.copy():
            if i >= j*j:
                if i % j == 0: #if i % j != 1: # 121
                    #print(j) #print(i)
                    prime.remove(i)
    return prime

using_list(30)

using_NumPy(121)

using_Sets(49)

# %%
