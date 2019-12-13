class DemoCallback:
    def __init__(self, mediator):
        self.mediator = mediator
        self.mediator.subscribe('runner.train_sota.start', self.telegram_log)
        self.mediator.subscribe('runner.train_sota.finish', self.tensorboard_log)

    def telegram_log(self, data):
        print('DemoCallback.telegram log', data)

    def tensorboard_log(self, data):
        print('DemoCallback.tensorboard_log', data)
