# InventromBolt
 Python script which will scrape the India Post website to obtain the tracking details of the given shipment tracking details. The output by the script should be in JSON format.

Scraping Indian Post to track consignment details

Steps:

    1.Install python 3.x

    2.Install geckodriver for Firefox:
      URL: https://github.com/mozilla/geckodriver/releases
      
    3.Install BeautifulSoup:
          command:pip install BeautifulSoup
   
    4.Install pillow (Python Image Library):
          command:pip install pillow
          URL:https://wp.stolaf.edu/it/installing-pil-pillow-cimage-on-windows-and-mac/
         
    5.Install tesseract:
    
          URL: https://github.com/tesseract-ocr/tesseract/wiki
    
    6.Install Json:
           If json is not already installed, then we can install from
           
           URL:https://pypi.python.org/pypi/simplejson/
           command:pip install Json
          
    7.Run the code
       
 Working:
       
       1Input Consignment Number in the terminal.
       
       2.Opens Firefox Browser.
       
       3.BeautifulSoup does the task of entering the input and fetching the output.
       
       4.Prints the JSON in the terminal as desired.
