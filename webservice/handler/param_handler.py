# Copyright 2017 SrMouraSilva
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

from webservice.handler.abstract_request_handler import AbstractRequestHandler
from webservice.util.handler_utils import integer


class ParamHandler(AbstractRequestHandler):
    _manager = None

    def initialize(self, app, webservice):
        super(ParamHandler, self).initialize(app, webservice)

        self._manager = self.app.manager

    @integer('bank_index', 'pedalboard_index', 'effect_index', 'param_index')
    def get(self, bank_index, pedalboard_index, effect_index, param_index):
        try:
            bank = self._manager.banks[bank_index]

            param = bank.pedalboards[pedalboard_index].effects[effect_index].params[param_index]
            return self.write(param.json)

        except IndexError:
            return self.error("Invalid index")

        except Exception:
            self.print_error()
            return self.send(500)

    @integer('bank_index', 'pedalboard_index', 'effect_index', 'param_index')
    def put(self, bank_index, pedalboard_index, effect_index, param_index):
        try:
            bank = self._manager.banks[bank_index]
            param = bank.pedalboards[pedalboard_index].effects[effect_index].params[param_index]
            value = self.request_data

            param.value = value

            return self.success()

        except IndexError:
            return self.error("Invalid index")

        except Exception:
            self.print_error()
            return self.send(500)
