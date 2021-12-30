# Sendit Spammer

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
  
## Making changes

Now, after you have copied the JSON payload, go and create a new file, you can name this whatever you like.

Then, in line 30 of main.py, change the '/home/kali/Desktop/json_payload.txt' with your new path.
That new path should be the full path to your JSON payload file.

Open sendit.sh, and change '/home/kali/Desktop/main.py' to the full path to your main.py file.

Note, the *sendit.sh* file only works in GNU-linux systems, for windows, you can create your own batch file, it should be straight forward. Or if you cant create a batch file, go further down to the **Running** section.

## Running
In GNU-linux systems, these commands should work;
```sh
glaukiol1@github $ chmod +x ./sendit.sh # make the file excecutable.
glaukiol1@github $ ./sendit.sh # run the file, this will show the help page. Arguments: [number of instances to run]
```

In windows, if you haven't created a batch file, you can run the file directly, although this will only spawn 1 instance of the bot;
```
python3 main.py
```

**Good luck!**

