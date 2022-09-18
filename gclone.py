#Author:sidious
import os
import lxml
import requests
from bs4 import BeautifulSoup

def banner():
    print('''


 ██████╗  ██████╗██╗      ██████╗ ███╗   ██╗███████╗
██╔════╝ ██╔════╝██║     ██╔═══██╗████╗  ██║██╔════╝
██║  ███╗██║     ██║     ██║   ██║██╔██╗ ██║█████╗  
██║   ██║██║     ██║     ██║   ██║██║╚██╗██║██╔══╝  
╚██████╔╝╚██████╗███████╗╚██████╔╝██║ ╚████║███████╗
 ╚═════╝  ╚═════╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
                /!\\ sidious /!\\
    ''')


def main():
    try:
        
        git_repo = input("Enter a github account: ")
        comp_rep = input("Would you like to compress the repositories? y/n: ")
        git_url = requests.get(f"https://github.com/{git_repo}?tab=repositories")
        git_soup = BeautifulSoup(git_url.text, 'lxml')
        git_payload = git_soup.find_all('h3', class_='wb-break-all')
        
        for rep in git_payload:
            git_rname = rep.find('a').text.strip()
            clone = os.popen(f"git clone https://github.com/{git_repo}/{git_rname}")
            os.wait()
            if comp_rep == "y":
                os.popen(f"tar cfv {git_rname}.tar {git_rname}")
                os.wait()
                os.popen(f"rm -rf {git_rname}")
                os.wait()
            else:
                pass

    except KeyboardInterrupt:
        print("\nExited by user..\n")

    except Exception as error:
        print(error)
        exit(1)

if __name__ == '__main__':
    banner()
    main()
