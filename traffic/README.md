# Traffic
## We saw some communication to a sketchy site... here's an export of the network traffic. Can you track it down? 


A file is included with the challenge.


---


If we unzip the file we find a lot of logfiles.


The goal is to find a "sketchy" website so I decided to look at the HTTP* files first, looking for a suspicious website.


Looking at the challenge context, I decided to look for literally a website beginning by "sketchy". 


`cat http* | grep "sketchy"`

There was indeed one and if you browse to it you got the flag.


