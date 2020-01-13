# SAGE-Web-Scraping
SAGE Project - Web Scraping Assignment



For this assignment we need to find an automated way of getting the number of orbital
launches in the 'Orbital launches' table in Wikipedia Orbital Launches if at least one of its
payloads is reported as 'Successful', 'Operational', or 'En Route'. For each launch, listed by date,
the first line is the launch vehicle and any lines below it correspond to the payloads, of which
there could be more than one. Please note that there might be multiple launches on a single
day with multiple payloads within a single launch (we are only interested in the number of
distinct launches). Please refer to the screenshot below highlighting a single payload in the
table.


Data source
https://en.wikipedia.org/wiki/2019_in_spaceflight#Orbital_launches
Deliverable
You can use any web scraping tool or library as long as the final script is written in python 3. This
script should be a pure-script, meaning that the result of the script is the same regardless of
how many times you run it (we will run this script daily). The output format is a .csv file where

the first column is `date` and the second column is `value`. All dates should be formatted in the
ISO 8601 format and all values should be integers. Include all dates in 2019 and fill in a 0 value
for any date where there are no orbital launches. Please refer to the example output below:
Example_output.csv (numbers are fake for example purposes)
date, value
2019-01-01T00:00:00+00:00, 0
2019-01-02T00:00:00+00:00, 1
2019-01-03T00:00:00+00:00, 2
2019-01-04T00:00:00+00:00, 3
2019-01-05T00:00:00+00:00, 2
...
2019-12-31T00:00:00+00:00, 1
