# Scanner SQLi

Search through Google Dorking the vulnerability SQL injection.

## Getting Started

### Prerequisites

You need to install sqlmap and python. And if you are going to use anonymity, you must install tor.

## Running

To launch the tool, you have to put:
```
python googledorking.py -d Dork
```
*Replace Dork for what you want to look for. For example:
```
python googledorking.py -d inallurl:php?id=
```
To put the anonymizer, you have to add -t:
```
python googledorking.py -t -d Dork
```
If you want the results in a file:
```
python googledorking.py -d Dork -f output.txt
```
If you want a maximum of pages:
```
python googledorking.py -d Dork -p number
```
*Replace number with the number of pages you want. By default it is 10.
It's used a specific User-agent (Mozilla/11.0) to search in google. If you wanna change:
```
python googledorking.py -d Dork -u newuser
```


