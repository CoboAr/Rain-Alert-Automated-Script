# Rain-Alert-Automated-Script

## Requirements 
pip install requests
pip install twilio

## What is Rain Alert?
It is an automated script implemented using twilio package; os and requests python modules, and pythonanywhere to automatize it.

## How does it work?
The script gets data from OpenWeathermap API: https://openweathermap.org/current   
In order to use this api, the user needs to create an account and creat an API_KEY. The API_KEY is used as an environmental variable. The request on the OpenWeathermap API takes as an argument a dictionary named weather_params which contains Latitude, Longitude, API_KEY and exlusion of current, minutes, and daily data. We are interested only for the hourly weather forecats. The latitude and longitude of any place can be found here: https://www.latlong.net/   
The scrip slices the data in the first 12 hourly keyes. It gets the value of id and check if it is higher or lower than 700. If it is higher it sets the will_rain variable to True. If it is lower than 700 the will_rain variable remains False.    
Next, if the will_rain variable is True the script sends a text message to the phone number registerd in the twilio account.


## Twilio account setup
Create an account at: https://console.twilio.com/
Note: Only the phone number used to register will serve as the phone number that will  get the text message rain alert.   
Upon registering and validating the Twilio account, the user has access to the 1) Account SID, 2) AUTH TOKEN, 3) The Twilio phone number assigned and a free trial credit of $15. 

![Screenshot 2023-11-11 at 2 52 28 PM](https://github.com/CoboAr/Rain-Alert-Automated-Script/assets/144629565/1d794533-bb8f-44c1-97b9-e20d8f49f3b4)    

This is an example how to use Twilio package in python:

![Screenshot 2023-11-11 at 2 59 34 PM](https://github.com/CoboAr/Rain-Alert-Automated-Script/assets/144629565/90d6bcde-4a11-430f-bf18-9de0c2a22ab5)

Next step is to Automatize the script so it can run independently on daily basis at a certain time.

## Automation

To automatize the script I am using pythonanywhere which is is an online integrated development environment and web hosting service based on the Python programming language.

Step1: Create/Sign in in PythonAnywhere

https://www.pythonanywhere.com/    

Step 2: Click Files

<img width="820" alt="Click Files" src="https://github.com/CoboAr/Automated-Birthday-Wish-Email/assets/144629565/329c0449-7cdb-4843-84a4-59944fa05368">

Step 3: Upload main.py file

<img width="1439" alt="Screenshot 2023-11-11 at 3 13 06 PM" src="https://github.com/CoboAr/Rain-Alert-Automated-Script/assets/144629565/b215e074-e8b8-4619-af1a-c36c01a20a13">   

Step 4: Click main.py and then $Bash console here

<img width="826" alt="Screenshot 2023-11-11 at 3 18 43 PM" src="https://github.com/CoboAr/Rain-Alert-Automated-Script/assets/144629565/2202d64a-273b-4c8d-8e18-949c61848b0e">

<img width="830" alt="Screenshot 2023-11-11 at 3 23 09 PM" src="https://github.com/CoboAr/Rain-Alert-Automated-Script/assets/144629565/25d4e1c8-62ca-49c0-8104-3938069dcbc7">  

Step 5: Modify the main.py code so it can run on pythonanywhere.

<img width="767" alt="Screenshot 2023-11-11 at 3 26 13 PM" src="https://github.com/CoboAr/Rain-Alert-Automated-Script/assets/144629565/714b3840-c903-408c-a843-75aaf5a249fe">

![Screenshot 2023-11-11 at 3 26 23 PM](https://github.com/CoboAr/Rain-Alert-Automated-Script/assets/144629565/7f9ee89b-fe9e-4f43-b20a-95b73e169bd7)  

Step 6: Add environmental variables    

export (name of environmental variable)=value   (no space on the left and right side of equal sign and no quotation marks for the value of environmental variable  

![Screenshot 2023-11-11 at 3 35 20 PM](https://github.com/CoboAr/Rain-Alert-Automated-Script/assets/144629565/2be149d9-481d-40d2-b72b-188006e3c567)  

Step 7: Run scrip with command "python3 main.py"

<img width="1423" alt="Screenshot 2023-11-11 at 3 43 26 PM" src="https://github.com/CoboAr/Rain-Alert-Automated-Script/assets/144629565/3833591b-fa7b-4d1c-a9ea-063793d492b9">     


![WhatsApp Image 2023-11-11 at 3 46 46 PM_321x714 (1)](https://github.com/CoboAr/Rain-Alert-Automated-Script/assets/144629565/c171d8a8-10b1-4f51-a77c-7dd917cc87e3)


Step 8: Click Tasks and setup a daily task for 1 month

After setting the time when we want to run the script on a daily basis, we need to add the run command including the environmental variables otherwise the script won't run:    

export OWM_API_KEY=*************************; export ACCOUNT_SID=********************; export AUTH_TOKEN=*******************; python3 main.py    

The server time is different from the user local time so it needs to be set up accordingly calculating the time difference.

![Screenshot 2023-11-11 at 4 04 28 PM](https://github.com/CoboAr/Rain-Alert-Automated-Script/assets/144629565/2d9ad63d-59b3-4752-9c2a-e3ec2629dec8) 

Enjoy! And please do let me know if you have any comments, constructive criticism, and/or bug reports.
## Author
## Arnold Cobo





