
from src.user import User, Roles
from src.actions import Action


def add_user_action(): 
    pass

def get_action(selection: str):
    return next(filter(lambda item: item.selection is selection, actions), None)

def process_action(action: str):
    pass

actions = [
    Action('1', 'Add User', add_user_action)
]
if __name__ == "__main__":

    print('Select your action:')

    [print(f'{i.selection}: {i.name}') for i in actions]


    while True:

        action = None
        action = get_action(input('Selection: '))

        if not action:
            continue

        print(action)
        

    
    pass