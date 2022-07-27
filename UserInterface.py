from DataBase import DataBase
import dicTest


def user_interface():
    print("Loading the files and preparing the system...")
    db = DataBase()
    user_text = input("The system is ready. enter your text:")
    if user_text == '#':
        return False
    print("Here are 5 suggestions:")
    suggestions = dicTest.find_in_data_base(user_text)
    if not suggestions:
        print("No suggestion")
    for i, suggestion in enumerate(suggestions):
        print(i + 1, ". ", suggestion)
        if i == 4:
            break
    return True


if __name__ == '__main__':
    run = True
    while run:
        run = user_interface()
