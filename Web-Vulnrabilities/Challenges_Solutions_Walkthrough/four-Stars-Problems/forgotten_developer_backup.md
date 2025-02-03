* open the /ftp folder
* open the package.json.bak file
* apply **null byte injection** by inserting %2500.md in the url
* you will successfully install the file
* Same for Forgotten's Sales Backup.

## why it works
* because when we add the 0 in the url, it escape all any string after it, so the server will think that the string ends at .gg, however, you have appended .md at the end to allow the server to install the file.
  
## how to prevent
* validate and Sanitize the input
  * if %00 exist -> prevent access.