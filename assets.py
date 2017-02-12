
player_front_frames = []
player_back_frames = []
player_right_frames = []
player_left_frames = []
for i in range (1, 5):
    player_front_frames.append('assets/images/inquisitor/front/normal/' + str(i) + '.png')
for i in range (1, 5):
    player_back_frames.append('assets/images/inquisitor/back/normal/' + str(i) + '.png')
for i in range (1, 5):
    player_right_frames.append('assets/images/inquisitor/right/normal/' + str(i) + '.png')
for i in range (1, 5):
    player_left_frames.append('assets/images/inquisitor/left/normal/' + str(i) + '.png')

player_invincible_frames_front = []
player_invincible_frames_back = []
player_invincible_frames_right = []
player_invincible_frames_left = []
for i in range(1, 5):
    player_invincible_frames_front.append('assets/images/inquisitor/front/invincible/' + str(i) + '.png')
for i in range(1, 5):
    player_invincible_frames_back.append('assets/images/inquisitor/back/invincible/' + str(i) + '.png')
for i in range(1, 5):
    player_invincible_frames_right.append('assets/images/inquisitor/right/invincible/' + str(i) + '.png')
for i in range(1, 5):
    player_invincible_frames_left.append('assets/images/inquisitor/left/invincible/' + str(i) + '.png')

player_attack_right_frames = []
player_attack_left_frames = []
player_attack_front_frames = []
player_attack_back_frames = []
for i in range(1,4):
    player_attack_right_frames.append('assets/images/player_attack/right/' + str(i) + '.png')
for i in range(1,4):
    player_attack_left_frames.append('assets/images/player_attack/left/' + str(i) + '.png')
for i in range(1,4):
    player_attack_front_frames.append('assets/images/player_attack/front/' + str(i) + '.png')
for i in range(1,4):
    player_attack_back_frames.append('assets/images/player_attack/back/' + str(i) + '.png')

slime_frames = []
slime_death_frames = ['assets/images/slime/death/1.png']
slime_damage_frames = []

for i in range(1, 3):
    slime_frames.append('assets/images/slime/movement/' + str(i) + '.png')
for i in range(1, 3):
    slime_damage_frames.append('assets/images/slime/damage/' + str(i) + '.png')

skull_frames = []
skull_death_frames = ['assets/images/enemies/skull/death/1.png']
skull_damage_frames = []

for i in range(1, 3):
    skull_frames.append('assets/images/enemies/skull/movement/' + str(i) + '.png')
for i in range(1, 3):
    skull_damage_frames.append('assets/images/enemies/skull/damage/' + str(i) + '.png')


title_background_img = 'assets/images/title_background.png'
level1_background_img = 'assets/images/background.png'

startbutton_img = 'assets/images/start_button.png'
quitbutton_img = 'assets/images/quit_button.png'
