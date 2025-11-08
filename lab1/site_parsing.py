import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

folder_path = "lab1"


def fetch_gdp_data_to_excel(country_tag):
    url = f"https://api.worldbank.org/v2/country/{country_tag}/indicator/NY.GDP.MKTP.CD?format=json&per_page=100"

    response = requests.get(url, headers=headers)
    data = response.json()

    gdp_data = []
    is_start = False

    if len(data) > 1:
        records = data[1][::-1]
        for record in records:
            year = record["date"]
            value = record["value"]
            if value is None:
                value = 0.0
            else:
                value = float(value)

            if value != 0.0:
                gdp_data.append({"Year": year, "Gdp": value})
                is_start = True
            elif is_start and value == 0.0:
                gdp_data.append({"Year": year, "Gdp": 0.0})
    else:
        raise ValueError("No data found for the specified country tag.")

    df = pd.DataFrame(data=gdp_data)
    df.to_excel(f"{folder_path}/gdp.xlsx")
    return



def fetch_earth_population_data_to_excel():
    url = "https://en.wikipedia.org/wiki/World_population"
    r = requests.get(url, headers=headers)
    soup = bs(r.text, 'html.parser')

    table = None
    for t in soup.find_all('table', class_='wikitable'):
        cap = t.find('caption')
        if cap and 'Global annual population growth' in cap.get_text():
            table = t
            break

    if table is None:
        raise ValueError("Could not find the population table on the page.")

    rows = table.find_all('tr')

    population_data = []
    for row in rows[2:]:
        year_cell = row.find(['th', 'td'])
        if not year_cell:
            continue
        year = year_cell.get_text(strip=True)

        tds = row.find_all('td')

        pop_text = tds[0].get_text(strip=True).replace(',', '')


        population = int(pop_text)

        population_data.append({
            "Year": year,
            "Population": population
        })

    df = pd.DataFrame(population_data, columns=["Year", "Population"])
    df.to_excel(f"{folder_path}/world_population.xlsx")
    return


def fetch_usa_inflation_data_to_excel():
    url = "https://www.usinflationcalculator.com/inflation/historical-inflation-rates/"

    r = requests.get(url, headers=headers)
    soup = bs(r.text, 'html.parser')

    table = soup.find('table')
    rows = table.find_all('tr')

    inflation_data = []
    for row in rows[1:-1]:
        cols = row.find_all('td')
        year_col = row.find('th')
        if len(cols) >= 2:
            year = year_col.get_text(strip=True)
            inflation_rate = cols[-1].get_text(strip=True).replace('%', '')
            inflation_data.append({
                "Year": year,
                "Inflation": float(inflation_rate)
            })

    df = pd.DataFrame(inflation_data, columns=["Year", "Inflation"])
    df.to_excel(f"{folder_path}/usa_inflation.xlsx")
    return

