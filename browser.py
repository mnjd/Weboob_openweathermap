# -*- coding: utf-8 -*-

# Copyright(C) 2018      Manoj D
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


from weboob.browser import PagesBrowser, URL

from .pages import CityPage, CurrentPage, ForecastPage

__all__ = ['OpenWeatherMapBrowser']


class OpenWeatherMapBrowser(PagesBrowser):
    BASEURL = 'https://openweathermap.org'
    API_KEY = 'b6907d289e10d714a6e88b30761fae22'

    city_page = URL('data/2.5/find\?q=(?P<pattern>.*)&appid=(?P<api>.*)', CityPage)
    current_page = URL('data/2.5/weather\?id=(?P<city_id>.*)&units=metric&appid=(?P<api>.*)', CurrentPage)
    forecast_page = URL('data/2.5/forecast/daily\?id=(?P<city_id>.*)&units=metric&appid=(?P<api>.*)', ForecastPage)


    def iter_city_search(self, pattern):
        return self.city_page.go(pattern=pattern, api=self.API_KEY).iter_cities()

    def get_current(self, city_id):
        return self.current_page.go(city_id=city_id, api=self.API_KEY).get_current()

    def iter_forecast(self, city_id):
        return self.forecast_page.go(city_id=city_id, api=self.API_KEY).iter_forecast()
