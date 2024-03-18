from load_csv import load
import matplotlib.pyplot as plt


def print_graph(data: list):
    try:
        if data is None:
            raise ValueError("Data is empty")

        data_fr = data[data['country'] == 'France'].iloc[0, 1:]
        x = data_fr.index.astype(int)
        y = data_fr.values.astype(float)

        plt.plot(x, y)
        plt.title("France Life expentancy Projection") 
        plt.xlabel("Year")
        plt.ylabel("Life expentancy")

        plt.show()

    except ValueError as ve:
        print(ve)
        return None


def main():
    print_graph(load("life_expectancy_years.csv"))


if __name__ == "__main__":
    main()