class FunCallback:
    def __init__(self, mediator):
        self.mediator = mediator
        self.mediator.subscribe('runner.train_sota.start', self.telegram_log)

    def telegram_log(self, data):
        print('FunCallback.FuckCatalyst', data)
