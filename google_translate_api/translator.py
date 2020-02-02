# importing Translator class
from googletrans import Translator

# creating Translator class object
translator = Translator()

# using its translate() method
res = translator.translate('Bonjour')

print(res.src)   # source
print(res.dest)  # destination
print(res.text)  # translated text
print(f'{res.origin} => {res.text}')

# Now we read a dummy file to translate from english to German
txt_file = open('someText.txt', 'r')
contents = txt_file.read()
print(contents)

res = translator.translate(contents, dest='de')
print(res.text)

# Now writing the translated text into a file
# using 'with' to automatically open-close write stream
with open('translated.txt', 'w') as f:
    f.write(res.text)
