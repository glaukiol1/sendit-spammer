# Sendit Spammer Python 

### ⚠️ I am not responsible for how you use this tool. This tool is against "Sendit" ToS and shall not be used in a production enviroment. You might be blacklisted from "Sendit" services for using this tool.⚠️

Senditapp.com bot spammer

## How to get the JSON payload.

Sadly, there is no easy way to get the payload, unless you have some knowledge in this field.

Steps:

  **1.** Get the Sendit link, this usually looks something like; *web.getsendit.com/s/...* you can find this in your friends post. 
  
  **2.** Open your browser, open that link.
  
  **3.** Open the developer tools, this is where *inspect* is, then, go to the *network* section.
  
  **4.** Put a demo message in the sendit box, and press *submit*
  
  **5.** In the developer tools, under network, you should now see a new request, a *post* request. Tap this.
  
  **6.** In the new menu that has popped up, press *request*.
  
  **7.** In this new menu, there should be place named "Request Payload"
  
  **8.** Copy this, this is the JSON payload.

## Running

To run the bot, run
```sh
#> python3 run.py
```
Then, the script will ask for 2 things,
- The number of instances of bots to spawn (please take note that you may not be able to spawn a lot if you have low CPU performance), the higher this number is the more bots will spawn. I recommend at the upmost with should be 200. 
- The JSON Payload, this you got from the previous step, make sure you dont include outer qoutation marks!


**Good luck!**

