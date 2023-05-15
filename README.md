# Nightingale - Bug prioritizer


<img src="https://github.com/kjgarza/nightingale/master/nigthtingale_logo.png" width="300" >

Uses a [binary insert sort](https://en.wikipedia.org/wiki/Insertion_sort) to prioritarise bugs (from github issues) in terms of importance. To run it, generate a list of bugs into a CSV file (issues.csv) and execute the script. Then answer T (for true) or else for every question you get prompted.


```shell

python nightingale.py

Is A more importan than B?
A:  ['MLA citation format duplicates the publisher name for some DOIs\n']
B:  ['Improve error message from json api\n']
T

```
