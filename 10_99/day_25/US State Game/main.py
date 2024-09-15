import pandas
from pathlib import Path
import turtle

ALIGMENT="CENTER"
FONT=('Arial', 6, 'normal')

# Configura o caminho do arquivo CSV
file_path = Path(__file__).parent / "50_states.csv"
data = pandas.read_csv(file_path)

# Configura a tela
screen = turtle.Screen()
screen.title('U.S States Game')

# Configura o caminho da imagem e a adiciona como shape
file_path_image = Path(__file__).parent / "blank_states_img.gif"
screen.addshape(str(file_path_image))

# Cria uma tartaruga para exibir a imagem
image_turtle = turtle.Turtle()
image_turtle.shape(str(file_path_image))

def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)
states_csv = data['state']



answer_state = 'init'
while answer_state != '':
    # Get one state of user
    answer_state = screen.textinput(title='Guess the State', prompt="What's another state's name?")
    # Search State in file
    state_found = ''
    for state in states_csv:
        if state.lower() == answer_state.lower():
            state_found = state


    if(state_found != ''):
        search_state = data[data.state == state_found]
        print(search_state)
        
        state_dict = search_state.to_dict()
        # Put Name on Map with the coordinates
        t  = turtle.Turtle()
        t.hideturtle()
        t.penup()
        print(state_dict)
        
        name_state = x_position =  state_dict['state']
        key_sate, value_state = next(iter(name_state.items()))
        x_position =  state_dict['x']
        key_x, value_x = next(iter(x_position.items()))
        y_position =  state_dict['y']
        key_y, value_y = next(iter(y_position.items()))
        
        t.goto(value_x, value_y)
        t.write(f'{value_state}', font=FONT)
    else:
        answer_state = ''

# Mantém a tela aberta até que seja clicada
screen.mainloop()
