import pandas as pd

def comma_url():
    return 'https://github.com/commaai/openpilot'

def read_html(url):
    return pd.read_html(url)

def write_csv(*tables):
    supported = pd.concat(tables, ignore_index=True).sort_values(by=['Make'])
    supported.to_csv('comma_vehicles.csv', index=False)
    return supported

url = comma_url()
read_page = read_html(url)
csv = write_csv(read_page[1], read_page[2])
