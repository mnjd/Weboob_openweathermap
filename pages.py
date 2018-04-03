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
from datetime import date, datetime
from weboob.browser.elements import ItemElement, method, DictElement, ListElement
from weboob.browser.pages import JsonPage
from weboob.browser.filters.json import Dict
from weboob.capabilities.weather import Forecast, Current, City, Temperature


class CityPage(JsonPage):
    ENCODING = 'utf-8'

    @method
    class iter_cities(DictElement):
            ignore_duplicate = True
            item_xpath = 'list'

            class itemitem(ListElement):
                class item(ItemElement):
                    klass = City
                    obj_id = Dict['id']

                    def obj_name(self):
                        return '{}, {} - lat:{}  lon:{}'.format(Dict['name'](self),
                                           Dict['sys']['country'](self),
                                           Dict['coord']['lat'](self),
                                           Dict['coord']['lon'](self))


class CurrentPage(JsonPage):
    @method
    class get_current(ListElement):
        ignore_duplicate = True

        class item(ItemElement):
            klass = Current

            obj_date = date.today()

            def obj_text(self):
                return '{} hPa - humidity {}% - {}'.format(Dict['main']['pressure'](self),
                                                           Dict['main']['humidity'](self),
                                                           Dict['weather'][0]['description'](self))

            def obj_temp(self):
                temp = Dict['main']['temp'](self)
                return Temperature(float(temp), 'C')


class ForecastPage(JsonPage):
    @method
    class iter_forecast(DictElement):
        ignore_duplicate = True
        item_xpath = 'list'

        class itemitem(ListElement):
            class item(ItemElement):
                klass = Forecast

                obj_id = Dict['dt']

                def obj_date(self):
                    date = Dict['dt'](self)
                    return datetime.fromtimestamp(int(date)).strftime('%Y-%m-%d')

                def obj_low(self):
                    temp = Dict['temp']['min'](self)
                    return Temperature(float(temp), 'C')

                def obj_high(self):
                    temp = Dict['temp']['max'](self)
                    return Temperature(float(temp), 'C')

                obj_text = Dict['weather'][0]['description']
