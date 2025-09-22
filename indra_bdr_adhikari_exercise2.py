#---------------- Indra Bdr Adhikari -------------------------

#--------- Task 1—Implementing "head" and "tail" in Python (2 points) -----
'''On Unix-like systems, head is a utility program that shows the first few lines of a file. Write a Python function head() 
that takes two arguments, a file name and, optionally, a number of lines n. The function shall print the first n lines 
of the given file. If n is not given, print five lines. Make sure your code also works if the file has fewer than n 
lines and that the lines are printed unchanged.

Then implement a function tail() with the same arguments. tail() shall print the last n lines of the file. 
You are allowed to read the entire file with read().'''

def head(filename, n = 5):
    with open(filename) as tfile:
        for line_number, line in enumerate(tfile):
            if line_number <= n:
                print(f'{line_number:2d}: {line.strip()}')

def tail(filename, n = 5):
    with open(filename) as tfile:
        lines = tfile.readlines()
        total_line = len(tfile.readlines())
        for line_number, line in enumerate(lines[-n:], total_line - min(n, total_line) + 1):
            print(f'{line_number:2d}: {line.strip()}')


head('testfile_plain.txt', 3)
tail('testfile_plain.txt', 3)

#--------------- Task 2—Reading weather data (3 points) --------

'''Write a Python function that reads weather data in the format of file weather_umb_2012.csv Download weather_umb_2012.csv. 
The function should receive the name of the file as argument and shall return data in a suitable data structure. 
Dates be returned as strings in YYYY-MM-DD format. Choose sensible names for the individual entries and provide a 
comment that describes the data structure returned.

NOTE: You are not allowed to use Pandas or other libraries to read the CSV file in this exercise. You need to implement 
the parser using plain Python functions such as open(), readline(), split() etc.'''

def read_weather(filename):
    data = [] #Reads given CSV file and returns a list of dictionaries.
    with open(filename, "r", encoding="latin-1") as f:
        header = f.readline().lstrip("#").strip().split(";") 

        for line in f:
            cols = line.strip().split(";")
            d, m, y = cols[0].split(".")
            entry = {
                str(header[0]): f"{y}-{m}-{d}", # date (str, format YYYY-MM-DD)
                str(header[1]): float(cols[1]),
                str(header[2]): float(cols[2]),
                str(header[3]): float(cols[3]),
                str(header[4]): float(cols[4]),
                str(header[5]): float(cols[5])
            }
            data.append(entry)
    return data        
    #print(data[1])

w_data = read_weather("weather_umb_2012.csv")
print(w_data[0])
