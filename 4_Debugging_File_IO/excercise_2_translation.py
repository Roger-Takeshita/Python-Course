from translate import Translator

translator = Translator(to_lang="ja")

try:
    with open('./english_text.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        with open('./japanese_text.txt', mode='w') as my_file2:
            my_file2.write(translation)
except FileExistsError as error:
    print("Original file not found")
