#!/usr/bin/python

# Ubuntu Tweak - PyGTK based desktop configure tool
#
# Copyright (C) 2007-2008 TualatriX <tualatrix@gmail.com>
#
# Ubuntu Tweak is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# Ubuntu Tweak is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ubuntu Tweak; if not, write to the Free Software Foundation, Inc.,

import os
from common.Settings import *

class Config:
    dir = '/apps/ubuntu-tweak'

    def set_value(self, key, value):
        if not key.startswith("/"):
            key = self.build_key(key)

        if type(value) == int:
            IntString(key).set_int(value)
        elif type(value) == float:
            FloatString(key).set_float(value)
        elif type(value) == str:
            StringSetting(key).set_string(value)
        elif type(value) == bool:
            BoolSetting(key).set_bool(value)

    def get_value(self, key):
        if not key.startswith("/"):
            key = self.build_key(key)

        if type(value) == int:
            return IntString(key).get_int()
        elif type(value) == float:
            return FloatString(key).get_float()
        elif type(value) == str:
            return StringSetting(key).get_string()
        elif type(value) == bool:
            return BoolSetting(key).get_bool()

    def build_key(self, key):
        return os.path.join(self.dir, key)

if __name__ == '__main__':
    print Config.build_key('hello')
