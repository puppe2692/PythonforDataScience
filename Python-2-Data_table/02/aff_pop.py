import sys
import math
from load_csv import load
import numpy as np
import matplotlib.pyplot as plt


def convert_value(value: str):
    if value.endswith("M"):
        return float(value[:-1]) * 1000000
    elif value.endswith("B"):
        return float(value[:-1]) * 1000000000
    elif value.endswith("k"):
        return float(value[:-1]) * 1000
    else:
        return value


def print_dblGraph(data: list, country: str):
    try:
        if data is None:
            raise ValueError("Data is empty")

        is_country = country in data['country'].values
        if not is_country:
            raise ValueError("Country not found")

        data_fr = data[data['country'] == 'France'].iloc[0, 1:]
        data_country = data[data['country'] == country].iloc[0, 1:]

        data_fr = data_fr.apply(convert_value)
        data_country = data_country.apply(convert_value)
        
        x = data_fr.index.astype(int)
        y = data_fr.values.astype(float)
        xc = data_country.index.astype(int)
        yc = data_country.values.astype(float)

        plt.plot(x, y, label="France")
        plt.plot(xc, yc, label=country)

        y_max = max(max(y), max(yc))
        print(y_max)
        y_max_rounded = math.ceil(y_max // 10000000) * 10000000
        print(y_max_rounded)
        yticks_values = np.arange(0, y_max_rounded + 1, y_max_rounded / 3)
        print(yticks_values)
        yticks_labels = [f"{int(val/1000000)}M" for val in yticks_values]
        plt.yticks(yticks_values, yticks_labels)

        plt.title("Population Projection France vs " + country)
        plt.xlabel("Year")
        plt.ylabel("Population")

        plt.legend(loc='lower right')

        plt.show()

    except ValueError as ve:
        print(ve)
        return None


def main():
    if len(sys.argv) != 2:
        print("Please enter a country name as argument.")
        return None
    data = load("population_total.csv")
    print_dblGraph(data, sys.argv[1])


if __name__ == "__main__":
    main()