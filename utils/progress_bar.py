from utils.prints import log_print

"""
Example of use:

    prg_bar = ProgressBar(1000000000, 0.001)

    for i in range(0, 1000000000):
        prg_bar.update(1)

will print:
    GraphOS: Completed 0.1%
    GraphOS: Completed 0.2%
    GraphOS: Completed 0.3%
    GraphOS: Completed 0.4%
    GraphOS: Completed 0.5%
    GraphOS: Completed 0.6%
"""


class ProgressBar:

    def __init__(self, size, fraction=0.1):
        self.counter = 0
        self.threshold = size * fraction
        self.past_fraction = 0
        self.fraction = fraction

    def update(self, update):
        self.counter += update
        if self.counter > self.threshold*(self.past_fraction+1):
            self.past_fraction += 1
            log_print('Completed ' + str(self.fraction*self.past_fraction*100) + '%')
