# Denner Ayres (dennerayres@gmail.com)
# Guilherme Azambuja (guilhermevazambuja@gmail.com)
# Lucas Rondon (lucasrondonn@gmail.com)
# https://github.com/lucassrondon/trabalho-ipv4-ipv6.git

from utils.parser import Parser

RIB_DATA = "data_files/ribs/converted/"

if __name__ == '__main__':
    parser = Parser(RIB_DATA)
    parser.run()
