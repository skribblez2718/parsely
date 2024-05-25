## parsely
parsely is a simple python script to extract host and endpoints from an XML formatted Burp Proxy History export and write the results to a CSV for upload in PlexLax

### Usage
1. Ensure you have configured you scope properly and your *Proxy History* only displays in-scope assets in Burp
2. From the *Proxy History* tab highlight all requests by selecting a request and typing CTRL+A
3. Right click and from the context menu select *Save Items*
   - **Important**: This file save can taking several minutes depending on the size  the *Proxy History*. Do not close Burp or try to parse the file until you receive a prompt saying the save is complete
5. Select desired path and click *Save*
6. Navigate to where you saved this script
7. Type the following command
    - Command: `python3 parsely.py --input [PATH_TO_XML] --output [PATH_TO_CSV]`
8. In PlexLax create an Informational level finding titled *Assets Tested*
9. From the *Affected Assets* tab of the finding click *Add Assets* and select *Import Assets* from the submenu
10. Upload the CSV created by parsely
11. Do a sanity check on the uploaded assets and make any changes if necessary
