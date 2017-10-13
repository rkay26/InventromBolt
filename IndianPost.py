# Import modules
import requests
from bs4 import BeautifulSoup as bs
from PIL import Image
from PIL import ImageOps
import pytesseract
import os
import urllib.request
import json

# Print in JSON format
def jsonFormat(tracking_id, booked_on, status, delivered_on):
    print(json.dumps(
            {
                    'tracking_id': tracking_id, 
                    'ship_date': booked_on,
                    'status':status,
                    'delivery date':delivered_on,
            }, sort_keys=False, indent=4)
    )
    pass

# Clean the captch
def cleanImage(imagePath):
    image = Image.open(imagePath)
    image = image.point(lambda x: 0 if x<143 else 255)
    borderImage = ImageOps.expand(image)
    borderImage.save(imagePath)
    pass

# Get text from the Captcha
def getCaptcha(captchaUrl):
    urllib.request.urlretrieve(captchaUrl, 'captcha.gif')
    captcha_path = os.getcwd() + '\\captcha.gif'
    cleanImage('captcha.gif')
    tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
    text = pytesseract.image_to_string(Image.open(captcha_path), lang='eng', config=tessdata_dir_config)
    return text

if __name__ == '__main__':
    
    import sys
    tracking_id = sys.argv[1]
    
    # URL of the website
    url ='https://www.indiapost.gov.in/VAS/Pages/TrackConsignment.aspx'
    
    retreived = True
    # Will run till successful log-in is made
    while retreived:
        
        # Create a session
        session = requests.Session()
        
        # Get data from the URL
        html = session.get(url).content
        
        # Parse the data received
        soup = bs(html, 'html.parser')
        
        # ID of text boxes on the web page
        consignment_number_id = 'ctl00_SPWebPartManager1_g_d6d774b9_498e_4de6_8690_a93e944cbeed_ctl00_txtOrignlPgTranNo'
        consignment_box_id = 'ctl00_SPWebPartManager1_g_d6d774b9_498e_4de6_8690_a93e944cbeed_ctl00_txtCaptcha'
        
        # Extract data of image tag to get URL of captcha
        captcha_image = soup.find('img', attrs={'id':'ctl00_SPWebPartManager1_g_d6d774b9_498e_4de6_8690_a93e944cbeed_ctl00_imgCaptcha'})
        captcha_src = url[:33] + captcha_image['src'][3:]
        
        pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
        captcha_text = getCaptcha(captcha_src)
        
        # Values for the form
        credentials = {
            consignment_number_id : tracking_id,
            consignment_box_id : captcha_text,
        }
        
        # Submit form
        session.post(url, data=credentials)
        
        # Get data after successful login
        response = session.get(url).content
        soup2 = bs(response, 'html.parser')
        
        # Extract values related to consignment
        booked_on = soup2.find('td', attrs={'data-th':'Booked OnTime'})
        status = soup2.find('span', attrs={'class':'bold_txt TrackConsignIntstatus'})
        delivered_on = soup2.find('td', attrs={'data-th':'Delivered On'})
        
        # If captcha matches the captcha text then print information in JSON format
        if booked_on is not None:
            jsonFormat(tracking_id, booked_on.text, status.text[18:], delivered_on.text)
            jsonFormat('EP470107781IN', '10/10/2017', 'Item delivered [To: ADDRESSEE ]', '12/10/2017')
            break
        
