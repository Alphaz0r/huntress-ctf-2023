# Dumpster Fire
## We found all this data in the dumpster! Can you find anything interesting in here, like any cool passwords or anything? Check it out quick before the foxes get to it! 

A file is included with the challenge.

---

First, before downloading the file, just by reading the challenge name and the context I can guess there's something related to Mozilla Firefox ("Dumpster *Fire*" and "Check it out quick before the *foxes* get to it").


Let's download the file.

Extracting it (twice) gives us a dump of what looks like a Linux filesystem.

Knowing Firefox config files are located in `/home/$user`, I went to `dumpster_fire\dumpster_fire\home\challenge\.mozilla\firefox\bc1m1zlr.default-release`

The file `logins.json` is interesting, we can find a login and a password but they are hashed. We also have the `key4.db` file which looks interesting.

Googling a bit for these files and Firefox I discovered that I can feed my own Firefox with these files in order to create a new profile and get the credentials.

After doing so I found the flag by opening Firefox and going to `about:profiles` in URL input.