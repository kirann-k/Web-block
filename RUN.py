from MAIN import *

class RUN:
    def run():
            hosts_path = MAIN.hosts_path() #fetching the hosts_path  
            hosts_temp = "hosts"
            redirect = "127.0.0.1"
            web_sites_list=MAIN.website_list()  #fetching the websitelist to block 

            print("THE PROGRAM IS RUNNING")
            with open(hosts_path, "r+") as file:
                content = file.read()
                for website in web_sites_list:
                    if website in content:
                        pass     #do nothing in this case
                    else:
                        file.write(redirect+" "+website+"\n")#add the entry of website in hosts file so it redirects to 127.0.0.1
