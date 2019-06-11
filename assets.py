import pygame

player_front_frames = [
        pygame.image.load(f'assets/images/inquisitor/front/normal/{i}.png') for
        i in range (1, 5) ]
player_back_frames = [
        pygame.image.load(f'assets/images/inquisitor/back/normal/{i}.png') for
        i in range (1, 5) ]
player_right_frames = [
        pygame.image.load(f'assets/images/inquisitor/right/normal/{i}.png') for
        i in range (1, 5) ]
player_left_frames = [
        pygame.image.load(f'assets/images/inquisitor/left/normal/{i}.png') for
        i in range (1, 5) ]

player_invincible_frames_front = [
        pygame.image.load(f'assets/images/inquisitor/front/invincible/{i}.png')
        for i in range(1, 5)]
player_invincible_frames_back = [
        pygame.image.load(f'assets/images/inquisitor/back/invincible/{i}.png')
        for i in range(1, 5)]
player_invincible_frames_right = [
        pygame.image.load(f'assets/images/inquisitor/right/invincible/{i}.png')
        for i in range(1, 5)]
player_invincible_frames_left = [
        pygame.image.load(f'assets/images/inquisitor/left/invincible/{i}.png')
        for i in range(1, 5)]

player_attack_right_frames = [
        pygame.image.load(f'assets/images/player_attack/right/{i}.png') for i
        in range(1,4)]
player_attack_left_frames = [
        pygame.image.load(f'assets/images/player_attack/left/{i}.png') for i in
        range(1,4)]
player_attack_front_frames = [
        pygame.image.load(f'assets/images/player_attack/front/{i}.png') for i
        in range(1,4)]
player_attack_back_frames = [
        pygame.image.load(f'assets/images/player_attack/back/{i}.png') for i in
        range(1,4)]


slime_frames = []
slime_death_frames = [pygame.image.load('assets/images/enemies/slime/death/1.png')]
slime_damage_frames = []

for i in range(1, 3):
    image = pygame.image.load(f'assets/images/enemies/slime/movement/{i}.png')
    slime_frames.append(image)
for i in range(1, 3):
    image = pygame.image.load(f'assets/images/enemies/slime/damage/{i}.png')
    slime_damage_frames.append(image)

skull_frames = []
skull_death_frames = [pygame.image.load('assets/images/enemies/skull/death/1.png')]
skull_damage_frames = []

for i in range(1, 3):
    image = pygame.image.load(f'assets/images/enemies/skull/movement/{i}.png')
    skull_frames.append(image)
for i in range(1, 3):
    image = pygame.image.load(f'assets/images/enemies/skull/damage/{i}.png')
    skull_damage_frames.append(image)

tar_death_frames = [pygame.image.load('assets/images/enemies/tar_ball/death/1.png')]

tar_frames = []
for i in range(1, 3):
    image = pygame.image.load(f'assets/images/enemies/tar_ball/movement/{i}.png')
    tar_frames.append(image)

tar_damage_frames = []
for i in range(1, 3):
    image = pygame.image.load(f'assets/images/enemies/tar_ball/damage/{i}.png')
    tar_damage_frames.append(image)

exp_frames = []
for i in range(1, 5):
    image = pygame.image.load(f'assets/images/pickups/exp/{i}.png')
    exp_frames.append(image)

exp_left_img = pygame.image.load('assets/images/ui/exp_left.png')
exp_right_img = pygame.image.load('assets/images/ui/exp_right.png')
exp_middle_img = pygame.image.load('assets/images/ui/exp_middle.png')
exp_fill_img = pygame.image.load('assets/images/ui/exp_fill.png')

hud_bar_img = pygame.image.load('assets/images/ui/hud_bar.png')
full_heart_img = pygame.image.load('assets/images/ui/full_heart.png')
half_heart_img = pygame.image.load('assets/images/ui/half_heart.png')
empty_heart_img = pygame.image.load('assets/images/ui/empty_heart.png')

title_background_img = pygame.image.load('assets/images/title_background.png')
level1_background_img = pygame.image.load('assets/images/background_sand.png')

startbutton_img = pygame.image.load('assets/images/start_button.png')
quitbutton_img = pygame.image.load('assets/images/quit_button.png')
retrybutton_img = pygame.image.load('assets/images/try_again.png')

plant1_spawn_frames = []
for i in range(1,4):
    image = pygame.image.load(f'assets/images/decor/plant_1/{i}.png')
    plant1_spawn_frames.append(image)
plant1_final_img = pygame.image.load('assets/images/decor/plant_1/4.png')

plant2_final_img = pygame.image.load('assets/images/decor/plant_1/5.png')

player_death_frames = []
player_death_final_img = pygame.image.load('assets/images/inquisitor/death/7.png')
for i in range(1, 7):
    image = pygame.image.load(f'assets/images/inquisitor/death/{i}.png')
    player_death_frames.append(image)

strike_sound_path = 'assets/sound/strike.wav'
player_death_sound_path = 'assets/sound/player_death.wav'
blob_death_sound_path = 'assets/sound/blob_death.wav'
skull_death_sound_path = 'assets/sound/skull_death.wav'
slime_damage_sound_path = 'assets/sound/slime_damage.wav'
skull_damage_sound_path = 'assets/sound/skull_damage.wav'
exp_sound_path = 'assets/sound/exp.wav'

