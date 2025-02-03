* navigate to /ftp
* open eastere.gg file
* apply null injection by inserting %2500.md in the url
* you will successfully install the file

## why it works
* because when we add the 0 in the url, it escape all any string after it, so the server will think that the string ends at .gg, however, you have appended .md at the end to allow the server to install the file.