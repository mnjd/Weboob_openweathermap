# -*- coding: utf-8 -*-

# Copyright(C) 2018      manojd
#
# This file is part of weboob.
#
# weboob is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# weboob is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with weboob. If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals


from weboob.tools.backend import Module
from weboob.capabilities.weather import CapWeather

from .browser import OpenWeatherMapBrowser


__all__ = ['OpenWeatherMapModule']


class OpenWeatherMapModule(Module, CapWeather):
    NAME = 'openweathermap'
    DESCRIPTION = u'openweathermap website'
    MAINTAINER = u'manojd'
    EMAIL = 'manoj.ducher@gmail.com'
    LICENSE = 'AGPLv3+'
    VERSION = '1.4'

    BROWSER = OpenWeatherMapBrowser

    def iter_city_search(self, pattern):
        return self.browser.iter_city_search(pattern)

    def get_current(self, city_id):
        return self.browser.get_current(city_id)

    def iter_forecast(self, city_id):
        return self.browser.iter_forecast(city_id)
