from PIL import ImageOps
import pytesseract
import os
import urllib.request

def cleanImage(imagePath):
    image = Image.open(imagePath)
    image = image.point(lambda x: 0 if x<143 else 255)
    borderImage = ImageOps.expand(image)
    borderImage.save(imagePath)
    pass

def getCaptha(captchaUrl):
    urllib.request.urlretrieve(captchaUrl, "captcha.gif")
    captcha_path = os.getcwd() + "\\captcha.gif"
    cleanImage("captcha.gif")
    tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
    text = pytesseract.image_to_string(Image.open(captcha_path), lang='eng',config=tessdata_dir_config)
    return text

if __name__ == '__main__':
    #tracking_id = 'RM719962415IN EP470107781IN'
    tracking_id = input()
    url ='https://www.indiapost.gov.in/VAS/Pages/TrackConsignment.aspx'
    response = requests.get(url)
    soup = bs(response.content, 'html.parser')
    
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
    
    consignment_number = soup.find('input', attrs={'id':'ctl00_SPWebPartManager1_g_d6d774b9_498e_4de6_8690_a93e944cbeed_ctl00_txtOrignlPgTranNo'})
    captcha_image = soup.find('img', attrs={'id':'ctl00_SPWebPartManager1_g_d6d774b9_498e_4de6_8690_a93e944cbeed_ctl00_imgCaptcha'})
    captcha_box = soup.find('input', attrs={'id':'ctl00_SPWebPartManager1_g_d6d774b9_498e_4de6_8690_a93e944cbeed_ctl00_txtCaptcha'})
    captch_src = 'https://www.indiapost.gov.in/VAS/' + captcha_image['src'][3:]
    print(captch_src)
    captch_text = getCaptha(captch_src)
    print(captch_text)
    
