#Author:sidious
import os
import time
import lxml
import requests
from bs4 import BeautifulSoup

CYA = '\033[96m'
GRE = '\033[92m'
RED = '\033[31m'
NOR = '\033[0m'

def banner():
    print(f'''\n{CYA}


 ██████╗  ██████╗██╗      ██████╗ ███╗   ██╗███████╗
██╔════╝ ██╔════╝██║     ██╔═══██╗████╗  ██║██╔════╝
██║  ███╗██║     ██║     ██║   ██║██╔██╗ ██║█████╗  
██║   ██║██║     ██║     ██║   ██║██║╚██╗██║██╔══╝  
╚██████╔╝╚██████╗███████╗╚██████╔╝██║ ╚████║███████╗
 ╚═════╝  ╚═════╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
                /!\\ {GRE}sidious{NOR} /!\\
    {NOR}''')


def main():
    try:
        
        git_repo = input("Enter a github account: ")
        comp_rep = input("Would you like to compress the repositories? y/n: ")
        git_url = requests.get(f"https://github.com/{git_repo}?tab=repositories")
        if git_url.status_code == 404:
            print("Not a valid repository.")
            main()
        else:
            pass
        git_soup = BeautifulSoup(git_url.text, 'lxml')
        git_payload = git_soup.find_all('h3', class_='wb-break-all')
        
        for rep in git_payload:
            git_rname = rep.find('a').text.strip()
            clone = os.popen(f"git clone https://github.com/{git_repo}/{git_rname} > /dev/null 2>&1")
            os.wait()
            
            if comp_rep == "y":
                print(f"[{CYA}*{NOR}]Status: {git_rname} cloning", end="\r", flush=True)
                time.sleep(1)
                os.popen(f"tar cfv {git_rname}.tar {git_rname} > /dev/null 2>&1",'w')
                os.wait()
                os.popen(f"rm -rf {git_rname}")
                os.wait()
                print(f"[{CYA}*{NOR}]Status: {git_rname} {GRE}completed{NOR}")
            else:
                pass
                print(f"[{CYA}*{NOR}]Status: {git_rname} cloning", end="\r", flush=True)
                time.sleep(1)
                print(f"[{CYA}*{NOR}]Status: {git_rname} {GRE}completed{NOR}")

    except KeyboardInterrupt:
        print(f"\n{RED}Exited by user..\n{NOR}")

    except (ConnectionResetError, ConnectionRefusedError) as error:
        print(error)
        exit(1)

if __name__ == '__main__':
    banner()
    main()
