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

from application.controller.plugins_controller import PluginsController


class EffectHandler(AbstractRequestHandler):
    _manager = None
    _plugins = None

    def initialize(self, app, webservice):
        super(EffectHandler, self).initialize(app, webservice)

        self._manager = self.app.manager
        self._plugins = self.app.controller(PluginsController)

    @integer('bank_index', 'pedalboard_index', 'effect_index')
    def get(self, bank_index, pedalboard_index, effect_index):
        try:
            effect = self._manager.banks[bank_index].pedalboards[pedalboard_index].effects[effect_index]

            return self.write(effect.json)

        except IndexError:
            return self.error("Invalid index")

        except Exception:
            self.print_error()
            return self.send(500)

    @integer('bank_index', 'pedalboard_index')
    def post(self, bank_index, pedalboard_index):
        try:
            pedalboard = self._manager.banks[bank_index].pedalboards[pedalboard_index]
            uri = self.request_data

            effect = self._plugins.lv2_effect(uri)
            pedalboard.append(effect)

            return self.created({"index": effect.index, "effect": effect.json})

        except IndexError:
            return self.error("Invalid index")

        except Exception:
            self.print_error()
            return self.send(500)

    @integer('bank_index', 'pedalboard_index', 'effect_index')
    def delete(self, bank_index, pedalboard_index, effect_index):
        try:
            pedalboard = self._manager.banks[bank_index].pedalboards[pedalboard_index]
            del pedalboard.effects[effect_index]

            return self.success()

        except IndexError:
            return self.error("Invalid index")

        except Exception:
            self.print_error()
            return self.send(500)
