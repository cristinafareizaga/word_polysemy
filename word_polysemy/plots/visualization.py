import matplotlib.pyplot as plt
import pandas as pd


def plots(mode):

    df = pd.read_csv("palabras_polysemy.csv", index_col=0)
    print(df)

    polysemy = df["polysemy"].values
    words = df.index.values

    if mode == "barplot":
        plt.bar(words, polysemy)

    elif mode == "scatter":
        plt.scatter(range(len(words)), polysemy)

    elif mode == "boxplot":
        plt.boxplot(polysemy)

    plt.show()

if __name__ == "__main__":
    plots("boxplot")