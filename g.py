from googletrans import Translator
translator = Translator()

r= translator.translate('hello world', dest='de')
print (r)

