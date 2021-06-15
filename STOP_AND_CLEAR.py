from MAIN import *

class STOP_AND_CLEAR:
    def stop_and_clear():
        print("THE PROGRAM IS STOPPED")
        hosts_path=MAIN.hosts_path() #fetching the hosts_path
        web_sites_list = MAIN.website_list() #fetching the websitelist
        with open(hosts_path, "r+") as file:
                    content = file.readlines()
                    file.seek(0)  # reset the pointer to the top of the text file host
                    for line in content:
                        if not any(website in line for website in web_sites_list):
                            file.write(line)
                        # do nothing otherwise
                    file.truncate() # this line is used to delete the trailing lines (that contain DNS)
