from datetime import datetime


class Runner:
    def run_model(self):
        pass

    def calc_metric(self):
        pass


class Runner_YOEO(Runner):
    def __init__(self, args):
        now = datetime.now()
        self.mode = args.mode
        self.path_data = args.data_path or '../data/torso/'
        self.path_result = args.result_path or f'{args.model}-{now.strftime("%H:%M:%S")}.csv'

    def run_model(self):
        print(f'passed and')


class Runner_UNet(Runner):
    pass

