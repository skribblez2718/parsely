## parsely
parsely is a simple python script to extract host and endpoints from an XML formatted Burp Proxy History export and write the results to a CSV for upload in PlexTrac

### Usage
1. Ensure you have configured your scope properly and your *Proxy History* only displays in-scope assets in Burp
2. From the *Proxy History* tab highlight all requests by selecting a request and typing CTRL+A
3. Right click and from the context menu select *Save Items*
   - **Important**: This file save can taking a while depending on the size  the *Proxy History*. Do not close Burp or try to parse the file until you receive a prompt saying the save is complete
5. Select desired path and click *Save*
6. Navigate to where you saved this script
7. Type the following command
    - Command: `python3 parsely.py --input [PATH_TO_XML] --output [PATH_TO_CSV]`
