#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright 2017, Advanced Remanufacturing and Technology Centre
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#  * Neither the name of the Southwest Research Institute, nor the names
#    of its contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#

from opcua import Client, ua
from opcua.ua import ua_binary as uabin
from opcua.common.methods import call_method
from opcua import common

import time

class HelloClient:
    def __init__(self, endpoint):
        self.client = Client(endpoint)

    def __enter__(self):
        self.client.connect()
        return self.client

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.disconnect()


if __name__ == '__main__':
    with HelloClient("opc.tcp://172.16.32.107:4840/freeopcua/server/") as client:
        root = client.get_root_node()
        print("Root node is: ", root)
        objects = client.get_objects_node()
        print("Objects node is: ", objects)

        print("Children of objects are: ", objects.get_children())

        # Check the state status in PLC
        stopped_0 = client.get_node("ns=3;s=\"PackML_Status\".\"Sts\".\"State\".\"Stopped\"")
        idle_0 = client.get_node("ns=3;s=\"PackML_Status\".\"Sts\".\"State\".\"Idle\"")
        starting_0 = client.get_node("ns=3;s=\"PackML_Status\".\"Sts\".\"State\".\"Starting\"")
        execute_0 = client.get_node("ns=3;s=\"PackML_Status\".\"Sts\".\"State\".\"Execute\"")
        completing_0 = client.get_node("ns=3;s=\"PackML_Status\".\"Sts\".\"State\".\"Completing\"")
        complete_0 = client.get_node("ns=3;s=\"PackML_Status\".\"Sts\".\"State\".\"Complete\"")
       
        print("Initial Stopped State: ", stopped_0.get_value())
        print("Initial Idle State: ", idle_0.get_value())
        print("Initial Starting State: ", starting_0.get_value())
        print("Initial Execute State: ", execute_0.get_value())
        print("Initial Completing State: ", completing_0.get_value())
        print("Initial Complete State: ", complete_0.get_value())
 


