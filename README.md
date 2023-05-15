# Nightingale - Bug prioritizer



![](https://raw.githubusercontent.com/kjgarza/nightingale/master/nigthtingale_logo.png)

Uses a [binary insert sort](https://en.wikipedia.org/wiki/Insertion_sort) to prioritarise bugs (from github issues) in terms of importance. To run it, generate a list of bugs into a CSV file (issues.csv) and execute the script. Then answer T (for true) or else for every question you get prompted.


```shell

python -m nightingale.cli issues.csv

Which issue is more important?
1. 782  `relatedItems` is erroring when `publicationYear` is not supplied       bug     about 18 days ago
2. 764  REST API does not return optional affiliation properties        bug     about 1 month ago
Enter 1 or 2:

```
