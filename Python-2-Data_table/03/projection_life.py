from load_csv import load
import matplotlib.pyplot as plt


def print_pointGraph(data_income: list, data_life: list):
    try:
        if data_income is None or data_life is None:
            raise ValueError("Data is empty")

        income_nineteenth = data_income[['country', '1900']]
        life_nineteenth = data_life[['country', '1900']]
        print(income_nineteenth)
        print(life_nineteenth)

        for index, row in income_nineteenth.iterrows():
            if row['country'] in life_nineteenth['country'].values:
                plt.scatter(row['1900'],
                            life_nineteenth[life_nineteenth['country']
                                            == row['country']]['1900'])

        plt.title("Income vs Life Expectancy 1900")
        plt.xlabel("Gross Domestic Product")
        plt.ylabel("Life Expectancy")

        plt.xscale('log')
        plt.xticks([1000, 10000], ['1K', '10K'])

        plt.show()

    except ValueError as ve:
        print(ve)
        return None


def main():
    data_income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    data_life = load("life_expectancy_years.csv")
    print_pointGraph(data_income, data_life)


if __name__ == "__main__":
    main()