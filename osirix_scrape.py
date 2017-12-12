######################################################################################################################################
"""
# @author: Nichollette Acosta
# @title: OsiriX Subject Scraper
  @Description: This script is used to scrape OsiriX viewer and grab
                our subject ids. We will give it a specifc ID to gather,
                then we will iterate through our IDS and run our setup_subjects.py
                on the given ID.

"""

######################################################################################################################################



import dryscrape
from bs4 import BeautifulSoup
##############################################################################################


### Here is where we add our base and target OsiriX URLs - we are using OsiriX web

## This address base is unique for your viewer
url_base = 'http://152.2.112.193:3333/main'
## The target base - this is the URL where all your subjects are listed
url_target = "http://152.2.112.193:3333/studyList?browse=all"



##############################################################################################
# Here is where we are opening up our Osirix Viewer so we can grab data
dryscrape.start_xvfb()
session = dryscrape.Session()
session.visit(url_base)



##############################################################################################

# Here is where you enter your OsiriX username -- add here your information

x = session.at_xpath('//*[@name="username"]')
x = session.at_xpath('//*[@name="password"]')

# Add your username here:
username = 'nibl'
x.set(username)


# Add your password here:
password = 'eatthisnotthat'
x.set(password)

##############################################################################################
login = session.at_xpath('//*[@name="login"]')
login.click()/

session.visit(url_target)
page = session.body()
soup = BeautifulSoup(page, 'lxml')



#####################################################################################3
# --Need to  edit this for reproducibility

# declaring a list that will hold our subject subject ids
target_ids = []
# using the BeautifulSoup package to find ALL of our ids in OsiriX
patient_tag_ids = soup.find_all('span', class_="study-list-patient-id")


# declare our target ID
target_id = "SM"
# here we loop through our ids we retrieved above, and we find our target ids and append
# them to our target_id list
for id in patient_tag_ids:
    if target_id in id.text:
        target_ids.append(id.text)


# Here is where I am adding ids to a file -->
# --> NEED TO : REPLACE WITH GET DICOMS LINE BELOW:
# python setup_subjects.py --getdata --keepdata --osirix_username nibl --osirix_password eatthisnotthat --osirix_subjName "BF20v2 18Dec2015" --studyname SugarMama -s "BF20v2" -o
# Then add command below to add data to HPC
# scp -r -p SM* nbytes@ht0.renci.org:/projects/niblab/test/output/SugarMama2
#    sshpass -p 'sweetbbcs'
#    sudo rm -rf SM*


"""
file = open("SM_names.txt", "w")

for id in SMpatient_ids:
    print(id)
    id_out = id.split(' ')[0]
    file.write(id + "," + id_out + "\n")

file.close()
"""
