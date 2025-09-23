#----------------------- Indra Bdr Adhikari ---------------

# -------- Task 1—Regex (2 points) ----------
import re

text = '''Ali and Per and friends.
Kari and Joe know each other.
James has known Peter since school days.'''

sentences = re.split(r'(?<=[.!?])\s+', text.strip())

pattern = r"\b[A-Z][a-zA-Z]*\b" #\b = word start, [A-Z] = first char is uppercase, [a-zA-Z]* = rest of string (letters only),\b = word end

print('Friendships'.center(20))
print('----------------------'.center(20))

for i, sentence in enumerate(sentences, 1):
    words = re.findall(pattern, sentence)
    #print(f"Sentence {i}: {sentence}")
    name = words[0]+' - '+words[1]
    print(name.center(20))

#%%
  
# -------- Task 2 — Collecting data via an API (3 points) ----------
import requests
import pandas as pd
import matplotlib.pyplot as plt

client_id = open('clientid.txt').read().strip()

endpoint = 'https://frost.met.no/observations/v0.jsonld'

parameters = [{
    'sources': 'SN17850', #Blindern (SN18700)
    'elements': 'mean(air_temperature P1D)',
    'referencetime': '2025-01-01/2025-09-14',
    },
    {
    'sources': 'SN18700', #Blindern (SN18700)
    'elements': 'mean(air_temperature P1D)',
    'referencetime': '2025-01-01/2025-09-14',   
    }
]

a = 0 # variable for the index for Places dic

final_df = pd.DataFrame() #empty df

for i in parameters:

    Place = ['Ås', 'Blindern']

    frost_response = requests.get(endpoint, i, auth=(client_id,' '))
    assert frost_response.status_code == 200

    #print(frost_response.url)

    #for header_name, header_value in frost_response.headers.items():
        #print(f'{header_name:16s}: {header_value}')

    frost_payload = frost_response.json()
    #print(frost_payload)

    for field_name, field_value in frost_payload.items():
        if field_name == 'data':
            continue
        #print(f'{field_name:16s}: {field_value}')

    #print(frost_payload['data'][:2])

    temp_data = [{'Time' : pd.to_datetime(entry['referenceTime']), 
              'T_avg': entry['observations'][0]['value']}
             for entry in frost_payload['data']]
    #print(temp_data[:4])


    df = pd.DataFrame.from_records(temp_data).set_index('Time')

    #print(df.head())

    p = Place[a] #variable to the place name

    a = a+1

    t = 'Temperature at ' + p # variable for plot title.

    final_df[f'T_avg_{p}'] = df['T_avg']
    #print(final_df[:4])

    plt.figure(figsize=(10,5))
    plt.plot(df)
    plt.title(t)
    plt.show()


#print(final_df[:4])
plt.figure(figsize=(10,5))
plt.scatter(final_df["T_avg_Ås"], final_df["T_avg_Blindern"],c="red", alpha=0.5, edgecolors="k")

plt.grid(True)
plt.xlabel("Temperature at Ås")
plt.ylabel("Temperature at Blindern")
plt.title("Ås vs Blindern")
plt.show()