import csv
import argparse
from runners import *


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', type=str, required=True, help='Type model name: YOEO')
    parser.add_argument('--mode', type=str, required=True, help='inference or test')
    parser.add_argument('--data_path', type=str, help='path to the data')
    parser.add_argument('--result_path', type=str, help='path to the folder in which to place the results')
    args = parser.parse_args()

    if args.model == 'YOEO':
        yoeo = Runner_YOEO(args)
    yoeo.run_model()


if __name__ == '__main__':
    run()
