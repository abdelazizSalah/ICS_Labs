* first we need to get benders email from the administration panel
  * ![alt text](image.png)
* then we can use benders email to log in
  * ![alt text](image-1.png)
* now we should go to change password
  * ![alt text](image-2.png)
* then we should open **BurpSuite** to see what is sent in the request when we fill the data
  * ![alt text](image-3.png)
* then we can send it to the repeater and check what can we do
* then we can try to remove the current password parameter, and set the new password to as wanted in the task, and the task will be solved. 
  * ![alt text](image-4.png)

## again the problem with front-end validation.