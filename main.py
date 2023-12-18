# Denner Ayres (dennerayres@gmail.com)
# Guilherme Azambuja (guilhermevazambuja@gmail.com)
# Lucas Rondon (lucasrondonn@gmail.com)
# https://github.com/lucassrondon/trabalho-ipv4-ipv6.git

from utils.parser import Parser
from utils.graph_plotter import GraphPlotter
from os.path import exists
from pickle import load, dump

RIB_DATA = "data_files/ribs/converted/"
STATS_DATA = "data_files/stats/"
CHARTS_DIR = "charts/"
PICKLE_FILE_PATH = "data_files/parsed_data.pkl"

if __name__ == '__main__':
    print("Running...")
    if exists(PICKLE_FILE_PATH):
        # Load data from the pickle file if it exists
        print("Reading pickled data...")
        with open(PICKLE_FILE_PATH, "rb") as pickle_file:
            dados = load(pickle_file)
    else:
        # If the pickle file doesn't exist, run the parser to get the data
        print("Parsing data...")
        parser = Parser(RIB_DATA, STATS_DATA)
        dados = parser.run()

        # Save the parsed data to a pickle file
        with open(PICKLE_FILE_PATH, "wb") as pickle_file:
            dump(dados, pickle_file)
        print(f"Data saved to pickle file at {PICKLE_FILE_PATH}")

    # Plotando gráficos
    print("Plotting charts...")
    graph_plotter = GraphPlotter(CHARTS_DIR, dados)
    graph_plotter.plot_grafico_total_sa()
    graph_plotter.plot_grafico_quantidade_ipv4()
    graph_plotter.plot_grafico_quantidade_ipv6()
    graph_plotter.plot_grafico_ipv4_ipv6()
    graph_plotter.plot_grafico_sa_anunciando_ipv4()
    graph_plotter.plot_grafico_sa_anunciando_ipv6()
    graph_plotter.plot_grafico_sa_anunciando_ambos()
    print("Done!")
