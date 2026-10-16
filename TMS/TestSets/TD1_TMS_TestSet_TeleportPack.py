"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TwelfthDoctor1's Teleport Memory System

> TeleportPack TestSet

(C) Copyright TD1 & TWoCC 2020 - 2021
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Licensed under MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Codes from other parties are not part of the License and Copyright.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from event_testing.results import TestResult
from event_testing.test_base import BaseTest
from caches import cached_test
from sims4.tuning.tunable import HasTunableSingletonFactory, AutoFactoryInit, TunableEnumEntry, Tunable
from sims4.common import Pack, is_available_pack
from teleport.teleport_enums import TeleportStyle
from TMS.MainLib.TD1_TMS_ModuleHandler import TD1TMSModuleHandler

"""
TestSet Notation: This TeleportPack Test requires either input from pack or teleport_type. By default, pack should be used. Should teleport_type be used,
it relies on TD1TMSModuleHandler to get the associated pack related to the teleport.

The is_installed acts as a whitelist/blacklist modifier to either show as True if Pack exists and set to True and vice versa.

Currently this does not support custom teleports excluding the Custom Wellness Teleport, TD1 Teleports will be integrated at a later time due to some
inconsistencies that needs to be rectified such as double pack requirements like Mist Teleport Spell.
"""


class TD1TMSTeleportPackTest(HasTunableSingletonFactory, AutoFactoryInit, BaseTest):
    FACTORY_TUNABLES = {
        'pack': TunableEnumEntry(
            description='The Pack to test for. Should teleport_type be filled in, it will use ModuleHandler Pack Listings to fill in accordingly.',
            tunable_type=Pack,
            default=Pack.BASE_GAME
        ),
        'teleport_type': TunableEnumEntry(
            description='The Teleport Type to test for. Can be left as None by default if not required.',
            tunable_type=TeleportStyle,
            default=TeleportStyle.NONE
        ),
        'is_installed': Tunable(
            description='Modifier to determine if the pack is installed.',
            tunable_type=bool,
            default=True
        ),
    }

    __slots__ = ('pack', 'is_installed', 'teleport_type')

    def get_expected_args(self):
        return {}

    @cached_test
    def __call__(self):
        if self.teleport_type is not None:
            if self.teleport_type == 'td1_teleport_wellness':
                self.pack = TD1TMSModuleHandler.WELLNESS_TELEPORT_PACK
            elif self.teleport_type == 'teleport_bat':
                self.pack = TD1TMSModuleHandler.VAMPIRE_BAT_TELEPORT_PACK
            elif self.teleport_type == 'teleport_mist':
                self.pack = TD1TMSModuleHandler.VAMPIRE_MIST_TELEPORT_PACK
            elif self.teleport_type == 'teleport_witch' or self.teleport_type == 'teleport_witch_fail' or self.teleport_type == 'teleport_witch_always_teleport':
                self.pack = TD1TMSModuleHandler.WITCH_SPELL_TELEPORT_PACK
            elif self.teleport_type == 'teleport_witch_broom':
                self.pack = TD1TMSModuleHandler.VAMPIRE_MIST_TELEPORT_PACK

        if self.pack is not None:
            if is_available_pack(self.pack):
                if self.is_installed is True:
                    return TestResult.TRUE
                else:
                    return TestResult(False, f'{self.pack} exists in pack list.', tooltip=self.tooltip)
            else:
                if self.is_installed is False:
                    return TestResult.TRUE
                else:
                    return TestResult(False, f'{self.pack} is not found within the pack list.', tooltip=self.tooltip)
        else:
            return TestResult(False, f'No pack specified.', tooltip=self.tooltip)
