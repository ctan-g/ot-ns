#!/usr/bin/env python3
# Copyright (c) 2020, The OTNS Authors.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. Neither the name of the copyright holder nor the
#    names of its contributors may be used to endorse or promote products
#    derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
import logging
import os
import tracemalloc
import unittest

from otns.cli import OTNS

_NON_VIRTUAL_TIME_UART_CONSERVATIVE_FACTOR = 1 if os.getenv('VIRTUAL_TIME_UART') == '1' else 3


class OTNSTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        tracemalloc.start()
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)-15s - %(levelname)s - %(message)s')

    def setUp(self) -> None:
        self.ns = OTNS(otns_args=['-log', 'debug'])
        self.ns.speed = OTNS.MAX_SIMULATE_SPEED

    def tearDown(self) -> None:
        self.ns.close()

    def assertFormPartitions(self, count: int):
        pars = self.ns.partitions()
        self.assertTrue(len(pars) == count and 0 not in pars, pars)

    def goConservative(self, duration: float) -> None:
        """
        Run the simulation for a given duration.

        :param duration: the duration to simulate (multipled by `_NON_VIRTUAL_TIME_UART_CONSERVATIVE_FACTOR`
                         if virtual time UART is not used)
        """
        self.ns.go(duration * _NON_VIRTUAL_TIME_UART_CONSERVATIVE_FACTOR)

    def assertNodeState(self, nodeid: int, state: str):
        cur_state = self.ns.get_state(nodeid)
        self.assertEqual(state, cur_state, f"Node {nodeid} state mismatch: expected {state}, but is {cur_state}")
