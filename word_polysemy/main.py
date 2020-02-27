import load_csv as lo
import plots.visualization as vi
import argparse
import average as av
import top_ten as top

CSV_FILE = "palabras_polysemy.csv"

def pepito(mode, average, number, print_top):
    url = "https://en.wikipedia.org/wiki/Most_common_words_in_English"
    lo.load_words_polysemy(url)
    vi.plots(mode)
    av.calculate_average(CSV_FILE, average)
    top.calculate_top(number, CSV_FILE, print_top)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Plot words polysemy')
    parser.add_argument('type', type=str,  help='choose the type of plot: "boxplot", "scatter", "barplot"')
    parser.add_argument('--average_yes', action="store_true", help='Use this flag to compute polysemy average. Otherwise it wont be done')
    parser.add_argument('--top_no', action="store_false",help='Use this flag to NOT compute polysemy top N. Otherwise it won')
    parser.add_argument('--n_top', type=int , default=10, help='Introduce the number of top words to print to screen')
    args = parser.parse_args()
    pepito(args.type, args.average_yes, args.n_top, args.top_no)


