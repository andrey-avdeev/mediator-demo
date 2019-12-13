from time import sleep


class DemoRunner:
    def __init__(self, mediator, config):
        self.mediator = mediator
        self.config = config

    def train_sota(self):
        self.mediator.publish('runner.train_sota.start', self.config)

        print('training sota...')
        sleep(2)
        print('sota is ready')

        self.mediator.publish('runner.train_sota.finish', self.config)
