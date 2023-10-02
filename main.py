from repository import Repository
from controller import Controller

if __name__ == '__main__':
    path_to_text = "data.txt"

    print("------------------------------------")
    print('Text Splitter')
    print("------------------------------------")

    repos = Repository(path_to_text)
    text = repos.text_reader()

    control = Controller(text)
    words = control.text_splitter()
    print("Your separate text word for word :")
    for word in words:
        print(word)






