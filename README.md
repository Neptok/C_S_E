# C_S_E

##Website for CSE ie colledge of software engineering is developed by TechCube IT organization
Know More about us
##The developers  :
Backend Developer  >> Bishal Shah 
    >>github.com/Bishal-241
    >>facebook.com/[](https://www.facebook.com/)
Front-end Developer  >> Monu Kumar
    >>github.com/Bishal-241
    >>https://www.facebook.com/tmonu995

Environmental setup and Configuration

i.install mailjet_rest external module which've been used for mailing system
    check this for more(https://pypi.org/project/mailjet-rest/)
ii.


Setup :
        i.Download image folder from (https://drive.google.com/drive/folders/1jJDHn4kyex2BwJi3_emih3KpT86ZaXIo?usp=sharing) and add in cse/main/static/ path
        

        ii. Here i have used mailjet api for mail system . Get a account and then make authDetail.py in BASE_DIR and add the following code 
        '''  
        
        apikey = "our api key"
            secreatkey = "your secreat key"
            service_provider = "https://app.mailjet.com"

            def getKey():
                return apikey
            def getSecreat():
                return secreatkey


        '''