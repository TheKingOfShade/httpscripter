# HttpScripter
**HttpScripter** was built to generate a constant stream of HTTP traffic that is not TLS encrpyted. Its originial purpose was to aid in the instruction of wireshark analysis. 

####Disclaimer
This tool is only to be used for academic purposes and testing. It generates http traffic that is reasonably easy to sniff. The author bears no responsibility for any misuse of this tool.

####Usage
```
python3 httpscripter.py -h
```
**optional arguments:**
  -h, --help            show this help message and exit
  -U, --UASet           Sets a random User Agent String
  -T TIME, --time TIME  Set the delay between requests in seconds

**Usage Example**
```
python3 httpscripter.py
```
**__Default:__** This will give you the output
```
What would you like to search for?(Seperate queries by ;)
```
Here you would input your queries. If you want multiple queries, seperate them by a semicolon. It will send an HTTP GET request to a random unencrypted search engine with a random user agent string with a random query (that the user gave). It will repeat this process every 5 seconds by default. 

```
python3 httpscripter.py -U
```
This will set a random user agent string and use it every time you send a GET Request.
```
python3 httpscripter.py -T 30
```
This will decrease the frequency of sent GET requests to 30 seconds.

####Ending the process
So far the only way to end the process is Ctrl+C
