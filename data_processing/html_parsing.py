# %%
import os
import re

import pandas as pd
from bs4 import BeautifulSoup


# Function to remove abbreviations in parentheses
def remove_abbreviations(text):
    return re.sub(r"\([^)]*\)", "", text).strip()


def html_dictionary_to_csv(html_file_path):
    """
    Reads an HTML file containing a table, processes it to remove abbreviations in parentheses,
    and writes the resulting DataFrame to a CSV file. The CSV file has the same name as the HTML file.

    Parameters:
        html_file_path (str): The path to the HTML file.
    """
    # Read the HTML file
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Extract table header for DataFrame columns
    header_row = soup.find("thead").find_all("td")
    columns = [col.text.strip() for col in header_row]

    # Initialize lists to hold the extracted data
    data = {col: [] for col in columns}

    # Loop through each row to populate the lists
    rows = soup.find_all("tr")
    for row in rows[1:]:  # Skip the header
        cols = row.find_all("td")
        if len(cols) != len(columns):
            continue
        for i, col in enumerate(cols):
            data[columns[i]].append(col.text.strip())

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Remove text within parentheses and the parentheses themselves in all string columns
    # for col in df.select_dtypes(include=['object']).columns:
    #     df[col] = df[col].apply(remove_abbreviations)

    # Write DataFrame to CSV
    csv_file_name = os.path.splitext(os.path.basename(html_file_path))[0] + ".csv"
    df.to_csv(csv_file_name, index=False, sep="|")


# %%

html_dictionary_to_csv(
    "files/diccionario_wayuunaiki.html"
)
# %%

html_dictionary_to_csv(
    "files/diccionario_nasa_yuwe.html"
)
# %%
