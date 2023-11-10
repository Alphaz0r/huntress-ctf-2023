# Rogue Inbox  
## You've been asked to audit the Microsoft 365 activity for a recently onboarded as a customer of your MSP.

## Your new customer is afraid that Debra was compromised. We received logs exported from Purview... can you figure out what the threat actor did? It might take some clever log-fu!

A file is included with the challenge

---

This is a CSV file. After investigation (= I put it to Excel to have a clearer view) one column is interesting: `AuditData`

After exporting this column I examined it with `jq` command and found out that on every line, a parameter (name) is a character of the flag.

Doing this command I managed to get the flag:

`cat audit.json | jq -r 'select(.Operation=="New-InboxRule") | .Parameters[] | select(.Name=="Name") | .Value' | tr -d '\n'`