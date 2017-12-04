# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
RAINCOAT for POX
Based off l2_learning.py
"""

from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpid_to_str, str_to_dpid
from pox.lib.util import str_to_bool
import time

log = core.getLogger()


class Raincoat(object):
    """
    RAINCOAT

    Upon receiving a DNP3 Read Request (from control center):
        - read sequence number from DNP3 request
        - decide randomization sequence for this request (ex - break 20 substations into 5 groups of 4 online devices)
        - for each group:
            - forward request to online devices
            - install rules for online devices with timeout = XXX seconds
            - spoof decoy for remaining messages
            - sleep for YYY seconds before moving onto next group
            - something to keep in mind:
                * don't send out spoofed packets immediately, add in an artificial delay
                * we don't want a situation where decoy packets go out immediately
                * and real measurements come in a bit later (due to standard network delays)


    """

    def __init__(self, args=None):
        core.openflow.addListeners(self)
        if args:
            log.info("Raincoat launched with %s" % args)
        else:
            log.warn("no args provided")

    def read_topology(self):
        log.info("readTopology called")
        pass

    def start_randomization(self):
        log.info("startRandomization called")
        pass

    def _handle_ConnectionUp(self, event):
        log.info("_handle_ConnectionUp Connection %s" % (event.connection,))

    def _handle_PacketIn(self, event):
        log.info("_handle_PacketIn Connection %s" % (event.connection,))

        # you should be able to intercept other openflow events
        # with _handle_<event_name>


def launch(args):
    """
    Starts RAINCOAT
    """

    raincoat_component = Raincoat(args)

    core.register("raincoat", raincoat_component)
    core.raincoat.read_topology()
    core.raincoat.start_randomization()
