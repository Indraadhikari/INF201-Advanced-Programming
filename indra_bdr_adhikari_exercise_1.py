#-----------Indra Bdr Adhikari ---------------
# ---------------- Task 1—Working with Visual Studio Code -------
'''Work in the group, and showed to thr TAs.'''
#%%

# ---------------- Task 2—Fix broken code -------

''' - Download file broken.py Download broken.py into your folder for this exercise.
    - Fix the code in the three functions in the file. One of them contains syntax errors, 
one might not do what the docstring promises and the third works correctly, but is undocumented and uses meaningless names.'''

# Code for Exercise Week 37, Task 2

# The following function has Python syntax errors. Fix them.
def bsort(data):
    """Sort data in-place using bubble sort."""

    n_elem = len(data)
    for j in range(n_elem-1, 0, -1):
        for k in range(0, j):
            if data[k] > data[k+1]:
                data[k], data[k+1] = data[k+1], data[k]


# Does the code of the following function deliver what the docstring promises?
def n_sum(n):
    """Return the sum of all integers from 1 to n."""
    a = sum(range(1,n+1))
    #return sum(range(n))
    return a

# This function is correct, but undocumented, hard to read and contains superfluous code.
# Tidy it up!
def max_Number(b):
    """Returns maximum number from the list!!"""

    max = b[0]
    for d in b[1:]:
        if d > c:
            max = d
        else:
            max = max
    return max

# The code below runs the functions defined above
if __name__ == "__main__":
    print(f"Sum(1..10) = {n_sum(10)}")

    print(f"a([45, 3, 1, 99, 4]) = {max_Number([45, 3, 1, 99, 4])}")

    data = [4, 2, 7, 9, 12]
    print(f"Before sorting", data)
    bsort(data)
    print(f"After sorting ", data)


#%%

# ---------------- Task 3—Counting votes (3 points) ----------------

import pandas as pd

def analyze_election_results(filename, num_parties=None):  # function for task number 6 and 7
    # Read the CSV file
    df = pd.read_csv(filename, encoding="utf-8", sep=";")

    # Analysing basic structure
    """2. Inspect the file's structure. Find out which columns contain 
        -the district name (Fylkenavn)
        -party code (Partikode)
        -number of votes received (Antall stemmer totalt):"""
    print(df.shape)
    print(df.columns)

    print(df["Fylkenavn"])  # same for others columns too

    total_votes = df["Antall stemmer totalt"].sum()
    print("Antall stemmer totalt:", total_votes)

    """3. Write a program that reads the file and counts the total number of votes for each party across all districts
    prints the results in a table, starting with the party with the largest number of votes"""

    party_votes = df.groupby("Partikode")["Antall stemmer totalt"].sum().reset_index()
    print(party_votes)

    # Sort by votes in descending order
    party_votes = party_votes.sort_values("Antall stemmer totalt", ascending=False)
    print(party_votes)

    """4. Modify your program so that it also prints the percentage of votes 
        received by each party (2 decimals)."""

    # Calculate percentages
    party_votes["Percentage"] = (
        (party_votes["Antall stemmer totalt"] / total_votes) * 100
    ).apply(lambda x: float("{:.2f}".format(x)))
    print(party_votes)

    """5. Further extend your program so that it marks the parties that received at least 4% of the vote."""
    # Mark parties with at least 4% of votes
    party_votes["Above_4_%_Mark"] = (party_votes["Percentage"] >= 4.0).apply(
        lambda x: "Yes" if x else "No"
    )
    print(party_votes)

    """6. Turn your code into a function that takes the file name and the number of parties to include in 
    the table as arguments. Use the function to print the table once with 3 and once with 7 parties.:

    7. Modify the code so that giving the number of parties to tabulate becomes optional. 
    If the user calls the function with just the filename, all parties should be included in the table.:"""

    # Limit to specified number of parties if provided
    if num_parties is not None:
        print(party_votes.head(num_parties))
    else:
        print(party_votes)


# Example usage:
if __name__ == "__main__":
    filename = "2021-09-30_party distribution_1_st_2021.csv"

    analyze_election_results(filename, 3)  # function call for task 6

    # analyze_election_results(filename, 7) # # function call for task 6

    # analyze_election_results(filename) # function call for task 7
