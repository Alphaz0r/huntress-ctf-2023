# TODO Human-two
## During the MOVEit Transfer exploitation, there were tons of "indicators of compromise" hashes available for the human2.aspx webshell! We collected a lot of them, but they all look very similar... except for very minor differences. Can you find an oddity? 

A file is attached to the challenge.

---

Let's download the file and extract it.

As we extract we see a lot of files coming up, as the challenge context suggest we must find the oddity hidden inside these files.


## The oddity

First I compared the very first file with the second with `diff` tool on my Kali machine. I noticed just one line is different.

> TODO: Add screenshot or smth

To be sure I compared the second file and the third one again with `diff`. Same result, one line is different. I assumed this was the same for all the files.

Then I used this bash command to gather all these lines:

`cat * | grep 'TODO'`

After I checked a bit I noticed one line isn't similar to the others.

> TODO: Add screenshot or smth

It's a string concatenation but it looks like hexadecimal. Let's put that to the chef

> TODO: Add screenshot or smth

We got the flag!