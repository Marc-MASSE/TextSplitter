from repository import Repository
from controller import Controller

if __name__ == '__main__':
    path_to_text = "data.txt"


    print('Text Splitter')

    repos = Repository(path_to_text)
    text = repos.text_reader()
    print(text)

    control = Controller(text)
    words = control.text_splitter()
    for word in words:
        print(word)






