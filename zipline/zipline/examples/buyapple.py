#!/usr/bin/python
#
# Copyright 2012 Quantopian, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import matplotlib.pyplot as plt

from zipline.algorithm import TradingAlgorithm
from zipline.utils.factory import load_from_yahoo


class BuyApple(TradingAlgorithm):  # inherit from TradingAlgorithm
    """This is the simplest possible algorithm that does nothing but
    buy 1 apple share on each event.
    """
    def handle_data(self, data):  # overload handle_data() method
        self.order('SPY', 1)  # order SID (=0) and amount (=1 shares)


if __name__ == '__main__':
    data = load_from_yahoo(stocks=['SPY'], indexes={}, start="1990-01-01", end="2012-01-01")
    simple_algo = BuyApple()
    results = simple_algo.run(data)
    results.portfolio_value.plot()
    plt.show()
