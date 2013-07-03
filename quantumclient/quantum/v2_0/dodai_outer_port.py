# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2013 National Institute of Informatics.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import argparse
import logging

from quantumclient.quantum import v2_0 as quantumv20


class ListDodaiOuterPort(quantumv20.ListCommand):
    """List dodai_outer_port."""

    resource = 'dodai_outer_port'
    log = logging.getLogger(__name__ + '.ListDodaiOuterPort')
    list_columns = ['id', 'dpid', 'outer_port']


class ShowDodaiOuterPort(quantumv20.ShowCommand):
    """Show information of a given Dodai OuterPort."""

    resource = 'dodai_outer_port'
    log = logging.getLogger(__name__ + '.ShowDodaiOuterPort')
    allow_names = False


class CreateDodaiOuterPort(quantumv20.CreateCommand):
    """Create a Dodai OuterPort."""

    resource = 'dodai_outer_port'
    log = logging.getLogger(__name__ + '.CreateDodaiOuterPort')

    def add_known_arguments(self, parser):
        parser.add_argument(
            '--dpid',
            help='the datapath ID')
        parser.add_argument(
            '--outer_port',
            help='the outer port no')

    def args2body(self, parsed_args):
        body = {self.resource: {
            'dpid': parsed_args.dpid,
            'outer_port': parsed_args.outer_port}}
        return body


class DeleteDodaiOuterPort(quantumv20.DeleteCommand):
    """Delete a given Dodai OuterPort."""

    resource = 'dodai_outer_port'
    log = logging.getLogger(__name__ + '.DeleteDodaiOuterPort')
    allow_names = False
