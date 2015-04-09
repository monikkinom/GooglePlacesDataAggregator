# GooglePlacesDataAggregator
A Python script to generate a list of all landmarks (schools, restaurants, colleges, malls, etc places) present in a city


## How does this work?
This makes google places requests, fetches all the results for a given category and stores it into a database.
This is extremely useful when you need localized data for your application and you cannot afford to spend
on buying databases. This is a nifty hack to get you started.

## How to make this work

<ol>
<li> Go to http://www.freemaptools.com/radius-around-point.htm </li>
<li> Search for your city / locality </li>
<li> Select the marker radius as 1/2 km. (you'll have to set that in the script as well) </li>
<li> Now keep plotting markers till the entire locality is covered </li>
<li> Once that is done, download the KML file. Select any one of those huge list of coordinates. </li>
<li> Copy them to a text file, change the script to point to the text file and there you go! </li>

</ol>

![alt tag](https://github.com/monikkinom/GooglePlacesDataAggregator/blob/master/mapview.png?raw=true)
![alt tag](https://github.com/monikkinom/GooglePlacesDataAggregator/blob/master/mapview2.png?raw=true)

I was able to generate a database of 6000 colleges and schools across few citites in India. I am also adding the coordinate files
for some popular cities in India.

