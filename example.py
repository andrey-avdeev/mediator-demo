from callback import DemoCallback
from fun_callback import FunCallback
from mediator import Mediator
from runner import DemoRunner


def run():
    mediator = Mediator()
    runner = DemoRunner(mediator, {'name': 'super_future_framework'})
    DemoCallback(mediator)
    FunCallback(mediator)

    runner.train_sota()


if __name__ == '__main__':
    run()
