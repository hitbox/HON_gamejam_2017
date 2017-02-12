all_assets = []

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

all_assets += player_front_frames + player_back_frames + player_right_frames + player_left_frames

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

all_assets += player_invincible_frames_front + player_invincible_frames_back + player_invincible_frames_right + player_invincible_frames_left

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

all_assets += player_attack_back_frames + player_attack_front_frames + player_attack_left_frames + player_attack_right_frames



slime_frames = []
slime_death_frames = ['assets/images/slime/death/1.png']
slime_damage_frames = []

for i in range(1, 3):
    slime_frames.append('assets/images/slime/movement/' + str(i) + '.png')
for i in range(1, 3):
    slime_damage_frames.append('assets/images/slime/damage/' + str(i) + '.png')

all_assets += slime_frames + slime_death_frames + slime_damage_frames

skull_frames = []
skull_death_frames = ['assets/images/enemies/skull/death/1.png']
skull_damage_frames = []

for i in range(1, 3):
    skull_frames.append('assets/images/enemies/skull/movement/' + str(i) + '.png')
for i in range(1, 3):
    skull_damage_frames.append('assets/images/enemies/skull/damage/' + str(i) + '.png')

all_assets += skull_frames + skull_damage_frames + skull_death_frames

tar_frames = []
tar_death_frames = ['assets/images/enemies/tar_ball/death/1.png']
tar_damage_frames = []

for i in range(1, 3):
    tar_frames.append('assets/images/enemies/tar_ball/movement/' + str(i) + '.png')
for i in range(1, 3):
    tar_damage_frames.append('assets/images/enemies/tar_ball/damage/' + str(i) + '.png')

all_assets += tar_frames + tar_damage_frames + tar_death_frames

exp_frames = []
for i in range(1, 5):
    exp_frames.append('assets/images/pickups/exp/' + str(i) + '.png')

all_assets += exp_frames

exp_left_img = 'assets/images/ui/exp_left.png'
exp_right_img = 'assets/images/ui/exp_right.png'
exp_middle_img = 'assets/images/ui/exp_middle.png'
exp_fill_img = 'assets/images/ui/exp_fill.png'

all_assets.append(exp_left_img + exp_right_img + exp_middle_img + exp_fill_img)

hud_bar_img = 'assets/images/ui/hud_bar.png'
full_heart_img = "assets/images/ui/full_heart.png"
half_heart_img = 'assets/images/ui/half_heart.png'
empty_heart_img = 'assets/images/ui/empty_heart.png'

all_assets.append(hud_bar_img + full_heart_img + half_heart_img + empty_heart_img)

title_background_img = 'assets/images/title_background.png'
level1_background_img = 'assets/images/background_sand.png'

all_assets.append(title_background_img + level1_background_img)

startbutton_img = 'assets/images/start_button.png'
quitbutton_img = 'assets/images/quit_button.png'
retrybutton_img = 'assets/images/try_again.png'

all_assets.append(startbutton_img + quitbutton_img + retrybutton_img)

plant1_spawn_frames = []
plant1_final_img = 'assets/images/decor/plant_1/4.png'
plant2_final_img = 'assets/images/decor/plant_1/5.png'
for i in range(1,4):
    plant1_spawn_frames.append('assets/images/decor/plant_1/' + str(i) + '.png')

player_death_frames = []
player_death_final_img = 'assets/images/inquisitor/death/7.png'
for i in range(1, 7):
    player_death_frames.append('assets/images/inquisitor/death/' + str(i) + '.png')

strike_sound_path = 'assets/sound/strike.wav'
player_death_sound_path = 'assets/sound/player_death.wav'
blob_death_sound_path = 'assets/sound/blob_death.wav'
skull_death_sound_path = 'assets/sound/skull_death.wav'
slime_damage_sound_path = 'assets/sound/slime_damage.wav'
skull_damage_sound_path = 'assets/sound/skull_damage.wav'
exp_sound_path = 'assets/sound/exp.wav'
