import os
from urllib.request import urlretrieve
import pandas as pd

Fremont_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

def get_Fremont_data(filename='Fremont.csv', url=Fremont_URL, force_download=False):
    """Download and cache the Fremont data
	
	Parameters
	----------
	filename: string (optional)
		location to save the data
	url: string (optional)
		web location of the data
	force_download : bool (optional)
		if True, force redownload of the data
	
	Returns
	----------
	data : pandas.DataFrame
		The Fremont bridge data
    """

    if force_download or not os.path.exists(filename):
        urlretrieve(url, filename)
    data = pd.read_csv(filename, index_col = 'Date', parse_dates=True)
    data.columns = ['West', 'East']
    data['Total'] = data['West'] + data['East']
    return data

#url_address = 'https://data.seattle.gov/resource/4xy5-26gy.json'

#resp = requests.get(url_address)

#result = resp.json()


#data = pd.DataFrame(requests.get(url_address).json())

#data = data.set_index('date')
#data.index = pd.to_datetime(data.index)
#data = data.sort_index()
#data = data.astype(dtype='float')
#data.dtypes 

#data.iloc[:100, :2]
#data.to_csv('Fremont_bridge.csv')


#req = urllib.request.urlopen(url_address).read()
#result = json.loads(req)

#data = pd.DataFrame(result, index =['date'])

#data.head()
#data = pd.read_csv(result, index_col = 'Date', parse_dates=True)
