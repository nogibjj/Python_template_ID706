import pandas as pd
import locale
import matplotlib.pyplot as plt

def find_mean(df):
    mean = round(df['Loan Amount(in USD)'].mean())
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    formatted_mean = locale.currency(mean, grouping=True)
    print("Mean:", formatted_mean)

def find_median(df):
    median = round(df['Loan Amount(in USD)'].median())
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    formatted_median = locale.currency(median, grouping=True)
    print("Median:", formatted_median)

def find_std(df):
    std = round(df['Loan Amount(in USD)'].std())
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    formatted_std = locale.currency(std, grouping=True)
    print("Standard deviation:", formatted_std)

def create_graph(df):
    x = df['School Country']
    y = df['Loan Amount(in USD)']
    plt.plot(x,y)
    plt.savefig("plot.png")


def main():
    df = pd.read_excel('raw.xlsx')
    new_column_names = {'Эцэг /эх/-ийн нэр / Өөрийн нэр': 'First and Last Name', 'Суралцаж байгаа улс': 'School Country', 'Сургуулийн нэр': 'School Name', 'Мэргэжил':'Intended Major', 'Суралцах хугацаа': 'Study Duration(in years)', 'Олгосон санхүүжил':'Loan Amount(in USD)'}
    df.rename(columns=new_column_names, inplace=True)
    find_mean(df)
    find_median(df)
    find_std(df)
    create_graph(df)

    


if __name__ == "__main__":
    main()
