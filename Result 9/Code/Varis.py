import random

import pygame, math, sys, os


pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
pygame.init()

pygame.mixer.music.set_volume(1)

screen_none = pygame.display.set_mode()

# Screen
infos = pygame.display.Info()
screen_w = infos.current_w
screen_h = infos.current_h

clock = pygame.time.Clock()
max_tick = 180

#tile = max(16, round(screen_w / 120))
tile = round(screen_w / 120 * 1.5)
#print("lol--------",tile,"--------lol")
#tile = 100
block = tile * 2

game_screen_w = screen_w
game_screen_h = screen_h

game_screen_center = [round(game_screen_w / 2), round(game_screen_h / 2)]

one = screen_w / 1920


# Files Import
try:
    Game_window_icon = pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\GameImgs\Icon.ico").convert_alpha()

    RightArrow = pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\GameImgs\RightArrow.png").convert_alpha()
    LeftArrow = pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\GameImgs\LeftArrow.png").convert_alpha()

    Pers_Icons = [
        pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\Pers\Normal.png").convert_alpha(),
        pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\Pers\Woman.png").convert_alpha(),
        pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\Pers\Blind.png").convert_alpha(),
        pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\Pers\Mime.png").convert_alpha(),
        pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\Pers\Goblin.png").convert_alpha(),
        pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\Pers\Inverse.png").convert_alpha(),
        pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\Pers\Slime.png").convert_alpha(),
        pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\Pers\Eye.png").convert_alpha(),
        pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\Pers\Empty.png").convert_alpha(),
        pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\Pers\Empty.png").convert_alpha(),
        pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\Pers\Anime_Girl.png").convert_alpha(),
        pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\Pers\Smile.png").convert_alpha(),
        pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\Pers\Dog.png").convert_alpha(),
        pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\Pers\Anime_Girl.png").convert_alpha(),
        pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\Pers\Anime_Girl.png").convert_alpha(),
        pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\Pers\Pyromaniac.png").convert_alpha(),
        pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\Pers\Scarecrow.png").convert_alpha(),
        pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\Pers\Cultist.png").convert_alpha(),
        pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\Pers\Anonymous.png").convert_alpha(),
        pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\Pers\Cthulhu.png").convert_alpha()
    ]

    Pers_Icon_Empty = pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\Pers\Empty.png").convert_alpha()


    Stone_Warrior_Icon = pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\Enemy\StoneWarrior.png").convert_alpha()

    Minigun_Icons = [
        pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\Minigun\Norm.png").convert_alpha(),
        pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\Minigun\Shot.png").convert_alpha()
    ]

    Shotgun_Norm_Icon = pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\Shotgun\Norm.png").convert_alpha()
    Shotgun_Shot1_Icon = pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\Shotgun\Shot1.png").convert_alpha()
    Shotgun_Shot2_Icon = pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\Shotgun\Shot2.png").convert_alpha()
    Shotgun_Shot3_Icon = pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\Shotgun\Shot3.png").convert_alpha()
    Shotgun_Shot4_Icon = pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\Shotgun\Shot4.png").convert_alpha()

    FThrower_Icon = pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\Flame Thrower\Norm.png").convert_alpha()

    WTF_Red_Icon = pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\WTF Gun\Red.png").convert_alpha()
    WTF_Orange_Icon = pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\WTF Gun\Orange.png").convert_alpha()
    WTF_Yellow_Icon = pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\WTF Gun\Yellow.png").convert_alpha()
    WTF_Green_Icon = pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\WTF Gun\Green.png").convert_alpha()
    WTF_Cyan_Icon = pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\WTF Gun\Cyan.png").convert_alpha()
    WTF_Blue_Icon = pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\WTF Gun\Blue.png").convert_alpha()
    WTF_Purple_Icon = pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\WTF Gun\Purple.png").convert_alpha()
    WTF_Pink_Icon = pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\WTF Gun\Pink.png").convert_alpha()
    WTF_White_Icon = pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\WTF Gun\White.png").convert_alpha()
    WTF_Black_Icon = pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\WTF Gun\Black.png").convert_alpha()

    Laser_Sword_Normal_Icon = pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\Melee\LaserSwordNormal.png").convert_alpha()
    Laser_Sword_Attack_Icon = pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\Melee\LaserSwordAttack.png").convert_alpha()
    Fire_Whip_Normal_Icon = pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\Melee\FireWhipNormal.png").convert_alpha()
    Fire_Whip_Attack_Icon = pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\Melee\FireWhipAttack.png").convert_alpha()
    Holy_Hammer_Icon = pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\Melee\HolyHammer.png").convert_alpha()

    Box_Icon = pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\Objects\Box.png").convert_alpha()


    Bullet_icons = [
        pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\Minigun\Bullet.png").convert_alpha(),
        pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\Shotgun\Bullet.png").convert_alpha(),
        pygame.image.load(os.path.dirname(__file__) + r"\Img_Tile_Folder\Melee\LaserSwordAttack.png").convert_alpha()
    ]

    '''
    Shot_Audios = [
        pygame.mixer.Sound(os.path.dirname(__file__) + r"\Music_Files\Shot\MinigunShot.mp3"),
        pygame.mixer.Sound(os.path.dirname(__file__) + r"\Music_Files\Shot\ShotgunShot.mp3")
        #pygame.mixer.Sound(os.path.dirname(__file__) + r"\Music_Files\Shot\FlameThrowerShot.mp3")
    ]

    BG_Audios = [
        pygame.mixer.Sound(os.path.dirname(__file__) + r"\Music_Files\BG\Menu.mp3"),
        pygame.mixer.Sound(os.path.dirname(__file__) + r"\Music_Files\BG\Game.mp3")
    ]
    '''


except:
    Game_window_icon = pygame.image.load(r"Img_Tile_Folder\GameImgs\Icon.ico").convert_alpha()

    RightArrow = pygame.image.load(r"Img_Tile_Folder\GameImgs\RightArrow.png").convert_alpha()
    LeftArrow = pygame.image.load(r"Img_Tile_Folder\GameImgs\LeftArrow.png").convert_alpha()

    Pers_Icons = [
        pygame.image.load(r"Img_Tile_Folder\Pers\Normal.png").convert_alpha(),
        pygame.image.load(r"Img_Tile_Folder\Pers\Woman.png").convert_alpha(),
        pygame.image.load(r"Img_Tile_Folder\Pers\Blind.png").convert_alpha(),
        pygame.image.load(r"Img_Tile_Folder\Pers\Mime.png").convert_alpha(),
        pygame.image.load(r"Img_Tile_Folder\Pers\Goblin.png").convert_alpha(),
        pygame.image.load(r"Img_Tile_Folder\Pers\Inverse.png").convert_alpha(),
        pygame.image.load(r"Img_Tile_Folder\Pers\Slime.png").convert_alpha(),
        pygame.image.load(r"Img_Tile_Folder\Pers\Eye.png").convert_alpha(),
        pygame.image.load(r"Img_Tile_Folder\Pers\Empty.png").convert_alpha(),
        pygame.image.load(r"Img_Tile_Folder\Pers\Empty.png").convert_alpha(),
        pygame.image.load(r"Img_Tile_Folder\Pers\Anime_Girl.png").convert_alpha(),
        pygame.image.load(r"Img_Tile_Folder\Pers\Smile.png").convert_alpha(),
        pygame.image.load(r"Img_Tile_Folder\Pers\Dog.png").convert_alpha(),
        pygame.image.load(r"Img_Tile_Folder\Pers\Anime_Girl.png").convert_alpha(),
        pygame.image.load(r"Img_Tile_Folder\Pers\Anime_Girl.png").convert_alpha(),
        pygame.image.load(r"Img_Tile_Folder\Pers\Pyromaniac.png").convert_alpha(),
        pygame.image.load(r"Img_Tile_Folder\Pers\Scarecrow.png").convert_alpha(),
        pygame.image.load(r"Img_Tile_Folder\Pers\Cultist.png").convert_alpha(),
        pygame.image.load(r"Img_Tile_Folder\Pers\Anonymous.png").convert_alpha(),
        pygame.image.load(r"Img_Tile_Folder\Pers\Cthulhu.png").convert_alpha()
    ]

    Pers_Icon_Empty = pygame.image.load(r"Img_Tile_Folder\Pers\Empty.png").convert_alpha()

    Stone_Warrior_Icon = pygame.image.load(r"Img_Tile_Folder\Enemy\StoneWarrior.png").convert_alpha()

    Minigun_Icons = [
        pygame.image.load(r"Img_Tile_Folder\Minigun\Norm.png").convert_alpha(),
        pygame.image.load(r"Img_Tile_Folder\Minigun\Shot.png").convert_alpha()
    ]

    Shotgun_Norm_Icon = pygame.image.load(r"Img_Tile_Folder\Shotgun\Norm.png").convert_alpha()
    Shotgun_Shot1_Icon = pygame.image.load(r"Img_Tile_Folder\Shotgun\Shot1.png").convert_alpha()
    Shotgun_Shot2_Icon = pygame.image.load(r"Img_Tile_Folder\Shotgun\Shot2.png").convert_alpha()
    Shotgun_Shot3_Icon = pygame.image.load(r"Img_Tile_Folder\Shotgun\Shot3.png").convert_alpha()
    Shotgun_Shot4_Icon = pygame.image.load(r"Img_Tile_Folder\Shotgun\Shot4.png").convert_alpha()
    FThrower_Icon = pygame.image.load(r"Img_Tile_Folder\Flame Thrower\Norm.png").convert_alpha()

    WTF_Red_Icon = pygame.image.load(r"Img_Tile_Folder\WTF Gun\Red.png").convert_alpha()
    WTF_Orange_Icon = pygame.image.load(r"Img_Tile_Folder\WTF Gun\Orange.png").convert_alpha()
    WTF_Yellow_Icon = pygame.image.load(r"Img_Tile_Folder\WTF Gun\Yellow.png").convert_alpha()
    WTF_Green_Icon = pygame.image.load(r"Img_Tile_Folder\WTF Gun\Green.png").convert_alpha()
    WTF_Cyan_Icon = pygame.image.load(r"Img_Tile_Folder\WTF Gun\Cyan.png").convert_alpha()
    WTF_Blue_Icon = pygame.image.load(r"Img_Tile_Folder\WTF Gun\Blue.png").convert_alpha()
    WTF_Purple_Icon = pygame.image.load(r"Img_Tile_Folder\WTF Gun\Purple.png").convert_alpha()
    WTF_Pink_Icon = pygame.image.load(r"Img_Tile_Folder\WTF Gun\Pink.png").convert_alpha()
    WTF_White_Icon = pygame.image.load(r"Img_Tile_Folder\WTF Gun\White.png").convert_alpha()
    WTF_Black_Icon = pygame.image.load(r"Img_Tile_Folder\WTF Gun\Black.png").convert_alpha()

    Laser_Sword_Normal_Icon = pygame.image.load(r"Img_Tile_Folder\Melee\LaserSwordNormal.png").convert_alpha()
    Laser_Sword_Attack_Icon = pygame.image.load(r"Img_Tile_Folder\Melee\LaserSwordAttack.png").convert_alpha()
    Fire_Whip_Normal_Icon = pygame.image.load(r"Img_Tile_Folder\Melee\FireWhipNormal.png").convert_alpha()
    Fire_Whip_Attack_Icon = pygame.image.load(r"Img_Tile_Folder\Melee\FireWhipAttack.png").convert_alpha()
    Holy_Hammer_Icon = pygame.image.load(r"Img_Tile_Folder\Melee\HolyHammer.png").convert_alpha()

    Box_Icon = pygame.image.load(r"Img_Tile_Folder\Objects\Box.png").convert_alpha()

    Bullet_icons = [
        pygame.image.load(r"Img_Tile_Folder\Minigun\Bullet.png").convert_alpha(),
        pygame.image.load(r"Img_Tile_Folder\Shotgun\Bullet.png").convert_alpha(),
        pygame.image.load(r"Img_Tile_Folder\Melee\LaserSwordAttack.png").convert_alpha()
    ]

    '''
    Shot_Audios = [
        pygame.mixer.Sound("Music_Files\Shot\MinigunShot.mp3"),
        pygame.mixer.Sound("Music_Files\Shot\ShotgunShot.mp3")
        #pygame.mixer.Sound(r"Music_Files\Shot\FlameThrowerShot.mp3")
    ]

    BG_Audios = [
        pygame.mixer.Sound(r"Music_Files\BG\Menu.mp3"),
        pygame.mixer.Sound(r"Music_Files\BG\Game.mp3")
    ]
    '''



weap_resize_koef = round(block / 17)

for i in range(len(Minigun_Icons)):
    Minigun_Icons[i] = pygame.transform.scale(Minigun_Icons[i], (Minigun_Icons[i].get_rect()[2] * weap_resize_koef, Minigun_Icons[i].get_rect()[3] * weap_resize_koef))

Shotgun_Norm_Icon = pygame.transform.scale(Shotgun_Norm_Icon, (Shotgun_Norm_Icon.get_rect()[2] * weap_resize_koef, Shotgun_Norm_Icon.get_rect()[3] * weap_resize_koef))
Shotgun_Shot1_Icon = pygame.transform.scale(Shotgun_Shot1_Icon, (Shotgun_Shot1_Icon.get_rect()[2] * weap_resize_koef, Shotgun_Shot1_Icon.get_rect()[3] * weap_resize_koef))
Shotgun_Shot2_Icon = pygame.transform.scale(Shotgun_Shot2_Icon, (Shotgun_Shot2_Icon.get_rect()[2] * weap_resize_koef, Shotgun_Shot2_Icon.get_rect()[3] * weap_resize_koef))
Shotgun_Shot3_Icon = pygame.transform.scale(Shotgun_Shot3_Icon, (Shotgun_Shot3_Icon.get_rect()[2] * weap_resize_koef, Shotgun_Shot3_Icon.get_rect()[3] * weap_resize_koef))
Shotgun_Shot4_Icon = pygame.transform.scale(Shotgun_Shot4_Icon, (Shotgun_Shot4_Icon.get_rect()[2] * weap_resize_koef, Shotgun_Shot4_Icon.get_rect()[3] * weap_resize_koef))

FThrower_Icon = pygame.transform.scale(FThrower_Icon, (FThrower_Icon.get_rect()[2] * weap_resize_koef, FThrower_Icon.get_rect()[3] * weap_resize_koef))

WTF_Red_Icon = pygame.transform.scale(WTF_Red_Icon, (WTF_Red_Icon.get_rect()[2] * weap_resize_koef, WTF_Red_Icon.get_rect()[3] * weap_resize_koef))
WTF_Orange_Icon = pygame.transform.scale(WTF_Orange_Icon, (WTF_Orange_Icon.get_rect()[2] * weap_resize_koef, WTF_Orange_Icon.get_rect()[3] * weap_resize_koef))
WTF_Yellow_Icon = pygame.transform.scale(WTF_Yellow_Icon, (WTF_Yellow_Icon.get_rect()[2] * weap_resize_koef, WTF_Yellow_Icon.get_rect()[3] * weap_resize_koef))
WTF_Green_Icon = pygame.transform.scale(WTF_Green_Icon, (WTF_Green_Icon.get_rect()[2] * weap_resize_koef, WTF_Green_Icon.get_rect()[3] * weap_resize_koef))
WTF_Cyan_Icon = pygame.transform.scale(WTF_Cyan_Icon, (WTF_Cyan_Icon.get_rect()[2] * weap_resize_koef, WTF_Cyan_Icon.get_rect()[3] * weap_resize_koef))
WTF_Blue_Icon = pygame.transform.scale(WTF_Blue_Icon, (WTF_Blue_Icon.get_rect()[2] * weap_resize_koef, WTF_Blue_Icon.get_rect()[3] * weap_resize_koef))
WTF_Purple_Icon = pygame.transform.scale(WTF_Purple_Icon, (WTF_Purple_Icon.get_rect()[2] * weap_resize_koef, WTF_Purple_Icon.get_rect()[3] * weap_resize_koef))
WTF_Pink_Icon = pygame.transform.scale(WTF_Pink_Icon, (WTF_Pink_Icon.get_rect()[2] * weap_resize_koef, WTF_Pink_Icon.get_rect()[3] * weap_resize_koef))
WTF_White_Icon = pygame.transform.scale(WTF_White_Icon, (WTF_White_Icon.get_rect()[2] * weap_resize_koef, WTF_White_Icon.get_rect()[3] * weap_resize_koef))
WTF_Black_Icon = pygame.transform.scale(WTF_Black_Icon, (WTF_Black_Icon.get_rect()[2] * weap_resize_koef, WTF_Black_Icon.get_rect()[3] * weap_resize_koef))

Laser_Sword_Normal_Icon = pygame.transform.scale(Laser_Sword_Normal_Icon, (Laser_Sword_Normal_Icon.get_rect()[2] * weap_resize_koef, Laser_Sword_Normal_Icon.get_rect()[3] * weap_resize_koef))
Laser_Sword_Attack_Icon = pygame.transform.scale(Laser_Sword_Attack_Icon, (Laser_Sword_Attack_Icon.get_rect()[2] * weap_resize_koef, Laser_Sword_Attack_Icon.get_rect()[3] * weap_resize_koef))
Fire_Whip_Normal_Icon = pygame.transform.flip(pygame.transform.scale(Fire_Whip_Normal_Icon, (Fire_Whip_Normal_Icon.get_rect()[2] * weap_resize_koef, Fire_Whip_Normal_Icon.get_rect()[3] * weap_resize_koef)), False, True)
Fire_Whip_Attack_Icon = pygame.transform.flip(pygame.transform.scale(Fire_Whip_Attack_Icon, (Fire_Whip_Attack_Icon.get_rect()[2] * weap_resize_koef, Fire_Whip_Attack_Icon.get_rect()[3] * weap_resize_koef)), False, True)
Holy_Hammer_Icon = pygame.transform.scale(Holy_Hammer_Icon, (Holy_Hammer_Icon.get_rect()[2] * weap_resize_koef, Holy_Hammer_Icon.get_rect()[3] * weap_resize_koef))

Box_Icon = pygame.transform.scale(Box_Icon, (block, block))



#Pers_Icon_Empty

# Data
can_continue = False

# RGB Colors
WHITE = (255, 255, 255)
GREY200 = (200, 200, 200)
GREY120 = (120, 120, 120)
GREY25 = (25, 25, 25)
GREY50 = (50, 50, 50)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 155, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
PURPLE = (143, 15, 208)
PINK = (255, 53, 184)
LITTLE_BLUE = (100, 180, 230)

#"""
# Classic set
FLAME_BULLET_COLOR_1 = YELLOW
FLAME_BULLET_COLOR_2 = ORANGE
FLAME_BULLET_COLOR_3 = RED

FLAME_BULLET_COLOR_R_CHANGE = 4
FLAME_BULLET_COLOR_G_CHANGE = 1.5
FLAME_BULLET_COLOR_B_CHANGE = 1

#"""

"""
# Purple set
FLAME_BULLET_COLOR_1 = (255, 200, 230)
FLAME_BULLET_COLOR_2 = (220, 150, 200)
FLAME_BULLET_COLOR_3 = (180, 100, 170)

FLAME_BULLET_COLOR_R_CHANGE = 3
FLAME_BULLET_COLOR_G_CHANGE = 1
FLAME_BULLET_COLOR_B_CHANGE = 3
"""

"""
# Toxic set
FLAME_BULLET_COLOR_1 = (200, 255, 200)
FLAME_BULLET_COLOR_2 = (150, 200, 150)
FLAME_BULLET_COLOR_3 = (120, 150, 120)

FLAME_BULLET_COLOR_R_CHANGE = 1
FLAME_BULLET_COLOR_G_CHANGE = 6
FLAME_BULLET_COLOR_B_CHANGE = 1
"""

start_pos = [0, 0]

# Pers
Personage = 0
pers_pos = [round(game_screen_w / 2), round(game_screen_h / 2)]
pers_size = [block * 1, block * 1]
pers_cen = [pers_pos[0] + round(pers_size[0] / 2), pers_pos[1] + round(pers_size[1] / 2)]

pers_weapon_angle = 0
pers_weapon_image_angle = 0
pers_weapon_fake_angle = 0
pers_weapon_cen = [pers_cen[0], pers_cen[1]]

Pers_info_list = [
    [Pers_Icons[0], "Sam", "Sam don't like other creatures, so that's why he kills monsters", []],
    [Pers_Icons[1], "Emily", "Emily don't like other creatures, so that's why she kills monsters, she and Sam very similar", []],
    [Pers_Icons[2], "Jimmy", "He is blind and very timid, so he kills monsters", []],
    [Pers_Icons[3], "Mime", "He was deprived of his tongue by monsters, so now he is taking revenge on them", []],
    [Pers_Icons[4], "maS", "sretsnom sllik eh yhw s'taht os ,serutaerc rehto ekil t'nod maS", []],
    [Pers_Icons[5], "Oliver", "He just likes to kill other monsters", []],
    [Pers_Icons[6], "Gelem", "A piece of slime that likes to kill monsters", []],
    [Pers_Icons[7], "Eye", "He kills every monster he sees", []],
    [Pers_Icons[8], "Empty", "She came from another dimension to kill monsters", []],
    [Pers_Icons[9], "Empty", "She came from another dimension to kill monsters", []],
    [Pers_Icons[10], "Anime girl", "She came from another dimension to kill monsters", []],
    [Pers_Icons[11], "Smile", "All he can do is smile and kill monsters", []],
    [Pers_Icons[12], "Dylan", "Woof, woof and kill, woof, monsters", []],
    [Pers_Icons[13], "Empty", "She came from another dimension to kill monsters", []],
    [Pers_Icons[14], "Empty", "She came from another dimension to kill monsters", []],
    [Pers_Icons[15], "Pyromaniac", "He loves fire, loves the heat, loves enemies on fire, loves everything on fire", []],
    [Pers_Icons[16], "Scarecrow", "He loves to scare even monsters and sometimes kill them", []],
    [Pers_Icons[17], "Cultist", "The only thing known about them is that they kill monsters", []],
    [Pers_Icons[18], "Anonymous", "He likes to kill monsters on social networks as wells", []],
    [Pers_Icons[19], "Cthulhu", "An ancient god who wants to consume the whole world and starts with monsters", []]
]
#for i in range(15):
#    Pers_info_list.append([Pers_Icon_Empty, "Name", "Description", []])
Pers_chose_index = 0
Pers_icon_size = [block * 3, block * 3]

Pers_Icon = pygame.transform.scale(Pers_info_list[Pers_chose_index][0], pers_size)
pers_rect = Pers_Icon.get_rect()

pers_can_go_up = True
pers_can_go_down = True
pers_can_go_right = True
pers_can_go_left = True

#List = [Icon, type_list_index]
Pers_current_weapon_info_list = [Minigun_Icons[0], 0]

Gun_list = [
    [Minigun_Icons[0], "Minigun", "g000"],
    [Shotgun_Norm_Icon, "Shotgun", "g001"],
    [FThrower_Icon, "Flame Thrower", "g002"],
    [WTF_Red_Icon, "WTF Gun", "g999"]
]

Select_weap_list_of_id = [["g000", "g001", "g002", "g999"], ["m000", "m001", "m002"]]
Select_pers_list_index = [0, 0] #Index of element Select_weapon_id from Select_weap_list_of_id
Select_weapon_id = Select_weap_list_of_id[0][Select_pers_list_index[Pers_current_weapon_info_list[1]]] #from Select_weap_list_of_id
Select_gun_id_right = "g001"
Select_gun_id_left = "g999"

pers_gun_info_list = [
    [pygame.transform.scale(Minigun_Icons[0], (Minigun_Icons[0].get_rect()[2] * 4, Minigun_Icons[0].get_rect()[3] * 4)), "g000", "Minigun", "If they shoot for a long time, they start firing faster", Minigun_Icons[0].get_rect()],
    [pygame.transform.scale(Shotgun_Norm_Icon, (Shotgun_Norm_Icon.get_rect()[2] * 4, Shotgun_Norm_Icon.get_rect()[3] * 4)), "g001", "Shotgun", "Shoots many rounds, but sometimes some of them may not fire", Minigun_Icons[0].get_rect()],
    [pygame.transform.scale(FThrower_Icon, (FThrower_Icon.get_rect()[2] * 4, FThrower_Icon.get_rect()[3] * 4)), "g002", "Flamethrower", "Releases a lot of fire", Minigun_Icons[0].get_rect()],
    [pygame.transform.scale(WTF_Black_Icon, (WTF_Black_Icon.get_rect()[2] * 4, WTF_Black_Icon.get_rect()[3] * 4)), "g999", "WTF Gun", "Shoot on the principle of 'WTF'", Minigun_Icons[0].get_rect()]
]

side_gun_info_list = [
    [pygame.transform.scale(Minigun_Icons[0], (Minigun_Icons[0].get_rect()[2], Minigun_Icons[0].get_rect()[3])), Minigun_Icons[0].get_rect()],
    [pygame.transform.scale(Minigun_Icons[0], (Minigun_Icons[0].get_rect()[2], Minigun_Icons[0].get_rect()[3])), Minigun_Icons[0].get_rect()]
]


# Lol_Bullet_info_list = [damage, knockback]
Minigun_Bullet_info_list = [2, one / 4]
Shotgun_Bullet_info_list = [1, one]
Flame_Bullet_info_list = [0.55, one / 100]
WTF_Bullet_info_list = [1, one / 100]

Bullets_info_list = [Minigun_Bullet_info_list, Shotgun_Bullet_info_list, Flame_Bullet_info_list, WTF_Bullet_info_list]


Bullet_group = pygame.sprite.Group()
Minigun_Bullets = pygame.sprite.Group()
Shotgun_Bullets = pygame.sprite.Group()
Flame_Bullets = pygame.sprite.Group()
WTF_Bullets = pygame.sprite.Group()
Guns_bullets_group_list = [Minigun_Bullets, Shotgun_Bullets, Flame_Bullets, WTF_Bullets]

# List = [is_gun_select, is_melee_select]
Weapon_type_select_list = [True, False]

# Pers melee weapon
Melee_weapon_list = [
    #[{0}Icon, {1}Name, {2}ID, {3}[Attack_animation_frames], {4}index_of_current_frame, {5}time_wait_for_next_frame, {6}[Norm_Icon, Attack_Icon], {7}distance_from_pers_koef]
    [Laser_Sword_Normal_Icon, "Laser Sword", "m000", [Laser_Sword_Normal_Icon], 0, 10, [Laser_Sword_Normal_Icon, Laser_Sword_Attack_Icon], 1.4],
    [Fire_Whip_Normal_Icon, "Fire Whip", "m001", [Fire_Whip_Attack_Icon], 0, 10, [Fire_Whip_Normal_Icon, Fire_Whip_Attack_Icon], 1.85],
    [Holy_Hammer_Icon, "Holy Hammer", "m002", [Holy_Hammer_Icon], 0, 10, [Holy_Hammer_Icon, Holy_Hammer_Icon], 1.4]
]
#mini_list = [{0}damage, {1}change_angle, {2}change_speed, {3}change_angle_times, {4}weight(kickback)]
Melee_weapon_info_list = [
    [1, 90, 10, 0, 0.01],
    [2, 135, 6, 0, 0.1],
    [3.5, 360, 5, 0, 2]
]
for i in range(len(Melee_weapon_info_list)):
    Melee_weapon_info_list[i][3] = round(Melee_weapon_info_list[i][1] / Melee_weapon_info_list[i][2])

Select_melee_id_right = "m001"
Select_melee_id_left = "m002"

pers_melee_info_list = [
    [pygame.transform.scale(Laser_Sword_Attack_Icon, (Laser_Sword_Normal_Icon.get_rect()[2] * 4, Laser_Sword_Normal_Icon.get_rect()[3] * 4)), "m000", "Laser Sword", "With this thing, you look like a Jedi", Laser_Sword_Normal_Icon.get_rect()],
    [pygame.transform.scale(Fire_Whip_Normal_Icon, (Fire_Whip_Normal_Icon.get_rect()[2] * 4, Fire_Whip_Normal_Icon.get_rect()[3] * 4)), "m001", "Fire Whip", "Be careful very hot thing", Fire_Whip_Normal_Icon.get_rect()],
    [pygame.transform.scale(Holy_Hammer_Icon, (Holy_Hammer_Icon.get_rect()[2] * 4, Holy_Hammer_Icon.get_rect()[3] * 4)), "m002", "Holy Hammer", "Holy power", Holy_Hammer_Icon.get_rect()]
]


side_melee_info_list = [
    [pygame.transform.scale(Laser_Sword_Normal_Icon, (Laser_Sword_Normal_Icon.get_rect()[2], Laser_Sword_Normal_Icon.get_rect()[3])), Laser_Sword_Normal_Icon.get_rect()],
    [pygame.transform.scale(Laser_Sword_Normal_Icon, (Laser_Sword_Normal_Icon.get_rect()[2], Laser_Sword_Normal_Icon.get_rect()[3])), Laser_Sword_Normal_Icon.get_rect()]
]

Is_pers_melee_can_attack = True

Pers_all_weapon_list = [
    Gun_list,
    Melee_weapon_list
]

for_but_is_click = False

hp = 10


# Tile map ---------------------------------------------------------
#empty_grid_matrix = 0


# matrix = [[[topleft_x1, topleft_y1, is_empty], [topleft_x2, topleft_y1, is_empty],...], [[topleft_x1, topleft_y2, is_empty], [topleft_x2, topleft_y2, is_empty],...]]
tile_map_matrix = []

# List = [[{0}topleft_x, {1}topleft_y, {2}object_type, {3}img]]
Hard_objects_list = []

def create_tile_map():
    global tile_map_matrix
    tile_map_matrix = []
    for y in range(-round(game_screen_h / 2), round(game_screen_h * 1.5), block):
        line_list = []
        for x in range(-round(game_screen_w / 2), round(game_screen_w * 1.5), block):
            line_list.append([x, y, True])
        tile_map_matrix.append(line_list)


def draw_tile_map(surface):
    size = abs(tile_map_matrix[0][1][0] - tile_map_matrix[0][0][0])
    for y_line in tile_map_matrix:
        for x_tile in tile_map_matrix[tile_map_matrix.index(y_line)]:
            pygame.draw.rect(surface, GREY25, (x_tile[0] + start_pos[0], x_tile[1] + start_pos[1], size, size), 1)

def draw_hard_objects(surface):
    for obj in Hard_objects_list:
        surface.blit(obj[3], (obj[0], obj[1], obj[3].get_rect()[2], obj[3].get_rect()[3]))


# Objects  ---------------------------------------------------------

Hard_Objects_group = pygame.sprite.Group

# Enemy ---------------------------------------------------------

Enemy_group = pygame.sprite.Group

Enemy_hp_color = (255, 255, 255)

Stone_warrior_size = [block, block]
Stone_warrior_speed = one * 1
Stone_warrior_rects = []

# Another
Bad_move = True
is_draw_collide_points = False


# Methods ---------------------------------------------------------

"""
def create_tile_map():
    global empty_grid_matrix, generate_structure_matrix
    grid_matrix = []
    for x in range(block * 2, game_screen_w - block * 2, block * 2):
        add_array = []
        for y in range(block * 2, game_screen_h - block * 2, block * 2):
            add_array.append([x, y])
        grid_matrix.append(add_array)
    empty_grid_matrix = grid_matrix.copy()
    generate_structure_matrix = [[[0, 0], [1, 0], [0, 1]], [[0, 0], [1, 0], [0, -1]], [[0, 0], [-1, 0], [0, 1]], [[0, 0], [-1, 0], [0, -1]]]
"""




def is_point_in_circle(centerx, centery, radius, posx, posy):
    is_in_circle = False

    if ((abs(centerx) - abs(posx))**2 + (abs(centery) - abs(posy))**2) >= radius**2:
        is_in_circle = True
    return is_in_circle


def is_in_edge_of_circle(centerx, centery, radius, posx, posy):
    is_in_edge = False


    if ((abs(centerx) - abs(posx))**2 + (abs(centery) - abs(posy))**2) == radius**2:
        is_in_edge = True
    return is_in_edge


def is_point_in_box(point_pos, zone_rect):
    if (zone_rect[0] + zone_rect[2] >= point_pos[0] >= zone_rect[0]) and (zone_rect[1] + zone_rect[3] >= point_pos[1] >= zone_rect[1]):
        return True
    else:
        return False


def get_signum(num):
    if num < 0:
        return -1
    elif num > 0:
        return 1
    else:
        return 0


def interval_limitation(minim, maxim, num):
    return min(maxim, max(minim, num))



def side_collision(rect, point):
    # list = [Top, Right, Bottom, Left]
    w_div_ten = round(rect.w / 10)
    h_div_ten = round(rect.h / 10)
    side_rects = [
        pygame.rect.Rect(rect.x + w_div_ten, rect.y, rect.w - w_div_ten * 2, h_div_ten * 4),
        pygame.rect.Rect(rect.x, rect.y + h_div_ten, w_div_ten * 4, rect.h - h_div_ten * 2),
        pygame.rect.Rect(rect.x + w_div_ten, rect.y + round(h_div_ten * 5.8), rect.w - w_div_ten * 2, h_div_ten * 4),
        pygame.rect.Rect(rect.x + round(w_div_ten * 5.8), rect.y + h_div_ten, w_div_ten * 4, rect.h - h_div_ten * 2),
    ]
    side_collision = [False, False, False, False]
    for i in range(4):
        side_collision[i] = side_rects[i].collidepoint(point[0], point[1])
    return side_collision



def draw_rect_points(surface, rect, draw=True, center=(True, 4, BLUE), corners=(True, 2, GREEN), edges=(True, ORANGE), text=(True, 15, WHITE)):
    if not draw:
        return 0
    if edges[0]:
        pygame.draw.rect(surface, edges[1], (rect.left, rect.top, abs(rect.left - rect.right), round(max(corners[1] / 2, 1))))
        pygame.draw.rect(surface, edges[1], (rect.left, rect.bottom, abs(rect.left - rect.right), round(max(corners[1] / 2, 1))))
        pygame.draw.rect(surface, edges[1], (rect.left, rect.top, round(max(corners[1] / 2, 1)), abs(rect.top - rect.bottom)))
        pygame.draw.rect(surface, edges[1], (rect.right, rect.top, round(max(corners[1] / 2, 1)), abs(rect.top - rect.bottom)))
    if center[0]:
        pygame.draw.circle(surface, center[2], rect.center, center[1])
    if corners[0]:
        pygame.draw.circle(surface, corners[2], rect.topleft, corners[1])
        pygame.draw.circle(surface, corners[2], rect.topright, corners[1])
        pygame.draw.circle(surface, corners[2], rect.bottomleft, corners[1])
        pygame.draw.circle(surface, corners[2], rect.bottomright, corners[1])
    if text[0]:
        Arial = pygame.font.SysFont('arial', round(text[1]))
        width_text = Arial.render(str(rect.width), False, text[2])
        height_text = Arial.render(str(rect.height), False, text[2])
        width_text_rect = width_text.get_rect()
        height_text_rect = height_text.get_rect()
        width_text_rect.center = (rect.centerx, rect.top - width_text_rect.height)
        height_text_rect.center = (rect.right + height_text_rect.height, rect.centery)
        surface.blit(width_text, width_text_rect)
        surface.blit(height_text, height_text_rect)


pygame.quit()
