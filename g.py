#from googletrans import Translator
#translator = Translator()

#r= translator.translate('hello world', dest='de')
#print (r)

#import requests

#r = requests.get("https://translate.google.com/?sl=auto&tl=en&text=hallo%20welt&op=translate")


#print (r)
#print (r.status_code)
#print (r.text)
#



# Give Language code in which you want to translate the text:=>
lang_code = 'en'
# Provide text that you want to translate:=>
input1 = "Hallo Welt"

# launch browser with selenium:=>
browser = webdriver.Chrome() #browser = webdriver.Chrome('path of chromedriver.exe file') if the chromedriver.exe is in different folder

# copy google Translator link here:=>
browser.get("https://translate.google.co.in/?sl=auto&tl="+lang_code+"&text="+input1+"&op=translate")

# just wait for some time for translating input text:=>
time.sleep(6)

# Given below x path contains the translated output that we are storing in output variable:=>
output1 = browser.find_element_by_xpath('/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]').text

# Display the output:=>
print("Translated Paragraph:=> " + output1)