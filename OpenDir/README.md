# Opendir
## A threat actor exposed an open directory on the public internet! We could explore their tools for some further intelligence. Can you find a flag they might be hiding?

A website is accessible for the challenge (credentials given ``opendir:opendir``)
 
---

Using `wget` I downloaded all the file and made a grep recursive search for the flag

`wget --user=opendir --password=opendir --recursive --level 5 http://chal.ctf.games:31407/`

`grep -r "flag{`

Flag is located in `./sir/64_bit_new/oui.txt`