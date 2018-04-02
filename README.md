# Accuweather module for weboob
## Description
This module uses openweathermap.org weather forecasting website as backend and weather capability for weboob. The module is accessible through wetboobs application.

## Getting started
Download the repository OpenWeatherMap into your modules folder of weboob. Make sure that the 

```
~/.config/weboob/sources.list
```

file has the path to the module folder. This step is important to be able to load this new module in weboob.

## Prerequisites
Install latest development branch of weboob (1.4), follow the instructions provided here:

```
http://weboob.org/install
```

The git can be found here:

```
https://git.weboob.org/weboob/devel.git
```

If you use the latest stable version (1.3), make sure to change the version from '1.4' to '1.3' in module.py.

## Using the module
Install the module in wetboobs:

```
backend add accuweather
```

Search for a city (Paris for instance):

```
cities Paris
```

From the list provided, choose one. To get the current weather for the city ranked "1" in the list provided by the search, type:

```
current 1
```

To get the forecast for the same city, type:

```
forecast 1
```

## Particularities of the module
OpenWeatherMap does not provide the state in which a city is located. For example, there are multiple cities called Paris in the USA. To be able to differentiate them, the cities GPS coordinates are displayed in the search list. 

All temperatures and pressures are displayed by default in Celsius (°C) and in hectopascal (hPa), respectively.
