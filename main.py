from utils.parser import Parser

RIB_DATA = "data_files/ribs/converted/"

if __name__ == '__main__':
    parser = Parser(RIB_DATA)
    parser.run()
