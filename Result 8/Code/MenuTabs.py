import Varis
from Varis import *

pygame.init()

screen = pygame.display.set_mode((Varis.screen_w, Varis.screen_h))


# noinspection PyStatementEffect
class PersSelector:
    def __init__(self):
        self.start_pos = 0
        self.min_start_pos = -Varis.one * 2000
        self.max_start_pos = 0

        self.IsInSelector = True
        self.mouse_pos = pygame.mouse.get_pos()
        self.old_mouse_pos = self.mouse_pos
        self.floors_size = [Varis.one * 10, 0, 0, 0]
        self.floors_size[1] = Varis.one * 950 + self.floors_size[0]
        self.floors_size[2] = Varis.one * 720 + self.floors_size[1]
        self.floors_size[3] = Varis.one * 720 + self.floors_size[2]

        self.select_gun_width = Varis.block

        self.RightArrow = pygame.transform.scale(Varis.RightArrow, (block * 2, block * 2))
        self.LeftArrow = pygame.transform.scale(Varis.LeftArrow, (block * 2, block * 2))

        # Text
        self.text_color = (Varis.GREY120)

        # Pers selector
        self.pers_name_font = pygame.font.SysFont('arial', Varis.block * 2)
        self.pers_name_text = self.pers_name_font.render("", False, self.text_color)
        self.pers_name_rect = self.pers_name_text.get_rect()

        self.pers_description_font = pygame.font.SysFont('arial', math.ceil(Varis.block * 1))
        self.pers_description_text = self.pers_description_font.render("", False, self.text_color)
        self.pers_description_rect = self.pers_description_text.get_rect()

        self.icons_line_count = 10

        # Gun selector
        self.gun_name_font = pygame.font.SysFont('arial', Varis.block * 2)
        self.gun_name_text = self.gun_name_font.render("", False, self.text_color)
        self.gun_name_rect = self.gun_name_text.get_rect()

        self.GunRightArrow = self.RightArrow
        self.GunRightArrow_rect = self.GunRightArrow.get_rect()
        self.GunLeftArrow = self.LeftArrow
        self.GunLeftArrow_rect = self.GunLeftArrow.get_rect()

        self.gun_description_font = pygame.font.SysFont('arial', Varis.block * 1)
        self.gun_description_text = self.gun_description_font.render("", False, self.text_color)
        self.gun_description_rect = self.gun_description_text.get_rect()

        # Melee selector
        self.melee_name_font = pygame.font.SysFont('arial', Varis.block * 2)
        self.melee_name_text = self.melee_name_font.render("", False, self.text_color)
        self.melee_name_rect = self.melee_name_text.get_rect()

        self.MeleeRightArrow = self.RightArrow
        self.MeleeRightArrow_rect = self.MeleeRightArrow.get_rect()
        self.MeleeLeftArrow = self.LeftArrow
        self.MeleeLeftArrow_rect = self.MeleeLeftArrow.get_rect()

        self.melee_description_font = pygame.font.SysFont('arial', Varis.block * 1)
        self.melee_description_text = self.melee_description_font.render("", False, self.text_color)
        self.melee_description_rect = self.melee_description_text.get_rect()



    def draw_pers_tab(self):
        pygame.draw.rect(screen, self.text_color, (Varis.block, self.start_pos + self.floors_size[0], Varis.screen_w - Varis.block * 2, Varis.tile), 0, math.ceil(Varis.one * 1))
        screen.blit(pygame.transform.scale(Varis.Pers_info_list[Varis.Pers_chose_index][0], (Varis.block * 8, Varis.block * 8)), (Varis.block * 4, self.start_pos + self.floors_size[0] + Varis.block * 3))

        self.pers_name_text = self.pers_name_font.render(Varis.Pers_info_list[Varis.Pers_chose_index][1], False, self.text_color)
        self.pers_name_rect = self.pers_name_text.get_rect()
        self.pers_name_rect.left = Varis.block * 14
        self.pers_name_rect.top = self.start_pos + self.floors_size[0] + Varis.block * 3

        screen.blit(self.pers_name_text, self.pers_name_rect)

        self.pers_description_text = self.pers_description_font.render(Varis.Pers_info_list[Varis.Pers_chose_index][2], False, self.text_color)
        self.pers_description_rect = self.pers_description_text.get_rect()
        self.pers_description_rect.left = Varis.block * 14
        self.pers_description_rect.top = self.start_pos + self.floors_size[0] + Varis.block * 7

        screen.blit(self.pers_description_text, self.pers_description_rect)

        for i in range(self.icons_line_count):
            tab_size = (screen_w - Varis.block * 5) / self.icons_line_count
            icon_rect = [Varis.block * 4 + tab_size * i, self.start_pos + self.floors_size[0] + Varis.block * 14, Varis.Pers_icon_size[0], Varis.Pers_icon_size[1]]
            Varis.Pers_info_list[i][3] = icon_rect
            screen.blit(pygame.transform.scale(Varis.Pers_info_list[i][0], (Varis.Pers_info_list[i][3][2], Varis.Pers_info_list[i][3][3])), Varis.Pers_info_list[i][3])

        for i in range(self.icons_line_count):
            tab_size = (screen_w - Varis.block * 5) / self.icons_line_count
            icon_rect = [Varis.block * 4 + tab_size * i, self.start_pos + self.floors_size[0] + Varis.block * 14 + tab_size, Varis.Pers_icon_size[0], Varis.Pers_icon_size[1]]
            Varis.Pers_info_list[i + 10][3] = icon_rect
            screen.blit(pygame.transform.scale(Varis.Pers_info_list[i + 10][0], (Varis.Pers_info_list[i + 10][3][2], Varis.Pers_info_list[i + 10][3][3])), Varis.Pers_info_list[i + 10][3])
        for i in range(len(Varis.Pers_info_list)):
            if Varis.Pers_chose_index == i:
                pygame.draw.rect(screen, self.text_color, ((Varis.Pers_info_list[i][3][0] - Varis.one * 5, Varis.Pers_info_list[i][3][1] - Varis.one * 5, Varis.Pers_info_list[i][3][2] + Varis.one * 10, Varis.Pers_info_list[i][3][3] + Varis.one * 10)), math.ceil(Varis.one * 6), math.ceil(Varis.one * 3))


    def draw_long_range_weapon(self):
        pygame.draw.rect(screen, self.text_color, (Varis.block, self.start_pos + self.floors_size[1], Varis.screen_w - Varis.block * 2, Varis.tile), 0, math.ceil(Varis.one * 1))

        self.gun_name_text = self.gun_name_font.render(Varis.pers_gun_info_list[Varis.Select_pers_list_index[0]][2], False, self.text_color)
        self.gun_name_rect = self.gun_name_text.get_rect()
        self.gun_name_rect.center = (round(Varis.screen_w / 2), self.start_pos + self.floors_size[1] + Varis.block * 6)

        screen.blit(self.gun_name_text, self.gun_name_rect)

        #self.select_gun_width = Varis.pers_gun_info_list[Varis.Select_pers_list_index][0].get_rect()[2]
        Varis.pers_gun_info_list[Varis.Select_pers_list_index[0]][4].center = (round(Varis.screen_w / 2), self.start_pos + self.floors_size[1] + Varis.block * 10)
        Varis.pers_gun_info_list[Varis.Select_pers_list_index[0]][4].size = (Varis.pers_gun_info_list[Varis.Select_pers_list_index[0]][0].get_rect()[2], Varis.pers_gun_info_list[Varis.Select_pers_list_index[0]][0].get_rect()[3])

        #Varis.pers_gun_info_list[Varis.Select_pers_list_index][4] = [round((Varis.screen_w - self.select_gun_width) / 2), self.start_pos + self.floors_size[1] + Varis.block * 5, self.select_gun_width, Varis.pers_gun_info_list[Varis.Select_pers_list_index][0].get_rect()[3]]
        screen.blit(Varis.pers_gun_info_list[Varis.Select_pers_list_index[0]][0], Varis.pers_gun_info_list[Varis.Select_pers_list_index[0]][4])

        Varis.Select_gun_id_right = Varis.Select_pers_list_index[0] + 1
        Varis.Select_gun_id_left = Varis.Select_pers_list_index[0] - 1

        if Varis.Select_gun_id_right > len(Varis.Select_weap_list_of_id[0]) - 1:
            Varis.Select_gun_id_right = 0
        elif Varis.Select_gun_id_right < 0:
            Varis.Select_gun_id_right = len(Varis.Select_weap_list_of_id[0]) - 1

        if Varis.Select_gun_id_left > len(Varis.Select_weap_list_of_id[0]) - 1:
            Varis.Select_gun_id_left = 0
        elif Varis.Select_gun_id_left < 0:
            Varis.Select_gun_id_left = len(Varis.Select_weap_list_of_id[0]) - 1


        Varis.side_gun_info_list[0][0] = pygame.transform.scale(Varis.pers_gun_info_list[Varis.Select_gun_id_left][0], (round(Varis.pers_gun_info_list[Varis.Select_gun_id_left][4][2] / 2), round(Varis.pers_gun_info_list[Varis.Select_gun_id_left][4][3] / 2)))
        Varis.side_gun_info_list[1][0] = pygame.transform.scale(Varis.pers_gun_info_list[Varis.Select_gun_id_right][0], (round(Varis.pers_gun_info_list[Varis.Select_gun_id_left][4][2] / 2), round(Varis.pers_gun_info_list[Varis.Select_gun_id_left][4][3] / 2)))


        Varis.side_gun_info_list[0][1] = Varis.side_gun_info_list[0][0].get_rect()
        Varis.side_gun_info_list[1][1] = Varis.side_gun_info_list[1][0].get_rect()

        Varis.side_gun_info_list[0][1].center = (Varis.pers_gun_info_list[Varis.Select_pers_list_index[0]][4].centerx - Varis.block * 12, Varis.pers_gun_info_list[Varis.Select_pers_list_index[0]][4].centery)
        Varis.side_gun_info_list[1][1].center = (Varis.pers_gun_info_list[Varis.Select_pers_list_index[0]][4].centerx + Varis.block * 12, Varis.pers_gun_info_list[Varis.Select_pers_list_index[0]][4].centery)

        screen.blit(Varis.side_gun_info_list[0][0], Varis.side_gun_info_list[0][1])
        screen.blit(Varis.side_gun_info_list[1][0], Varis.side_gun_info_list[1][1])

        self.GunRightArrow_rect.center = (Varis.pers_gun_info_list[Varis.Select_pers_list_index[0]][4].centerx + Varis.block * 6, Varis.pers_gun_info_list[Varis.Select_pers_list_index[0]][4].centery)
        screen.blit(self.GunRightArrow, self.GunRightArrow_rect)

        self.GunLeftArrow_rect.center = (Varis.pers_gun_info_list[Varis.Select_pers_list_index[0]][4].centerx - Varis.block * 6, Varis.pers_gun_info_list[Varis.Select_pers_list_index[0]][4].centery)
        screen.blit(self.GunLeftArrow, self.GunLeftArrow_rect)

        self.gun_description_text = self.gun_description_font.render(Varis.pers_gun_info_list[Varis.Select_pers_list_index[0]][3], False, self.text_color)
        self.gun_description_rect = self.gun_description_text.get_rect()
        self.gun_description_rect.center = (Varis.pers_gun_info_list[Varis.Select_pers_list_index[0]][4].centerx, Varis.pers_gun_info_list[Varis.Select_pers_list_index[0]][4].centery + Varis.block * 3)
        screen.blit(self.gun_description_text, self.gun_description_rect)

    def draw_melee_weapon(self):
        pygame.draw.rect(screen, self.text_color, (Varis.block, self.start_pos + self.floors_size[2], Varis.screen_w - Varis.block * 2, Varis.tile), 0, math.ceil(Varis.one * 1))


        self.melee_name_text = self.melee_name_font.render(Varis.pers_melee_info_list[Varis.Select_pers_list_index[1]][2], False, self.text_color)
        self.melee_name_rect = self.melee_name_text.get_rect()
        self.melee_name_rect.center = (round(Varis.screen_w / 2), self.start_pos + self.floors_size[2] + Varis.block * 6)

        screen.blit(self.melee_name_text, self.melee_name_rect)

        #self.select_gun_width = Varis.pers_gun_info_list[Varis.Select_pers_list_index][0].get_rect()[2]
        Varis.pers_melee_info_list[Varis.Select_pers_list_index[1]][4].center = (round(Varis.screen_w / 2), self.start_pos + self.floors_size[2] + Varis.block * 10)
        Varis.pers_melee_info_list[Varis.Select_pers_list_index[1]][4].size = (Varis.pers_melee_info_list[Varis.Select_pers_list_index[1]][0].get_rect()[2], Varis.pers_melee_info_list[Varis.Select_pers_list_index[1]][0].get_rect()[3])

        #Varis.pers_gun_info_list[Varis.Select_pers_list_index][4] = [round((Varis.screen_w - self.select_gun_width) / 2), self.start_pos + self.floors_size[1] + Varis.block * 5, self.select_gun_width, Varis.pers_gun_info_list[Varis.Select_pers_list_index][0].get_rect()[3]]
        screen.blit(Varis.pers_melee_info_list[Varis.Select_pers_list_index[1]][0], Varis.pers_melee_info_list[Varis.Select_pers_list_index[1]][4])

        Varis.Select_melee_id_right = Varis.Select_pers_list_index[1] + 1
        Varis.Select_melee_id_left = Varis.Select_pers_list_index[1] - 1

        if Varis.Select_melee_id_right > len(Varis.Select_weap_list_of_id[1]) - 1:
            Varis.Select_melee_id_right = 0
        elif Varis.Select_melee_id_right < 0:
            Varis.Select_melee_id_right = len(Varis.Select_weap_list_of_id[1]) - 1

        if Varis.Select_melee_id_left > len(Varis.Select_weap_list_of_id[1]) - 1:
            Varis.Select_melee_id_left = 0
        elif Varis.Select_melee_id_left < 0:
            Varis.Select_melee_id_left = len(Varis.Select_weap_list_of_id[1]) - 1


        Varis.side_melee_info_list[0][0] = pygame.transform.scale(Varis.pers_melee_info_list[Varis.Select_melee_id_left][0], (round(Varis.pers_melee_info_list[Varis.Select_melee_id_left][4][2] / 2), round(Varis.pers_melee_info_list[Varis.Select_melee_id_left][4][3] / 2)))
        Varis.side_melee_info_list[1][0] = pygame.transform.scale(Varis.pers_melee_info_list[Varis.Select_melee_id_right][0], (round(Varis.pers_melee_info_list[Varis.Select_melee_id_right][4][2] / 2), round(Varis.pers_melee_info_list[Varis.Select_melee_id_right][4][3] / 2)))


        Varis.side_melee_info_list[0][1] = Varis.side_melee_info_list[0][0].get_rect()
        Varis.side_melee_info_list[1][1] = Varis.side_melee_info_list[1][0].get_rect()

        Varis.side_melee_info_list[0][1].center = (Varis.pers_melee_info_list[Varis.Select_pers_list_index[1]][4].centerx - Varis.block * 12, Varis.pers_melee_info_list[Varis.Select_pers_list_index[1]][4].centery)
        Varis.side_melee_info_list[1][1].center = (Varis.pers_melee_info_list[Varis.Select_pers_list_index[1]][4].centerx + Varis.block * 12, Varis.pers_melee_info_list[Varis.Select_pers_list_index[1]][4].centery)

        screen.blit(Varis.side_melee_info_list[0][0], Varis.side_melee_info_list[0][1])
        screen.blit(Varis.side_melee_info_list[1][0], Varis.side_melee_info_list[1][1])

        self.MeleeRightArrow_rect.center = (Varis.pers_melee_info_list[Varis.Select_pers_list_index[1]][4].centerx + Varis.block * 6, Varis.pers_melee_info_list[Varis.Select_pers_list_index[1]][4].centery)
        screen.blit(self.MeleeRightArrow, self.MeleeRightArrow_rect)

        self.MeleeLeftArrow_rect.center = (Varis.pers_melee_info_list[Varis.Select_pers_list_index[1]][4].centerx - Varis.block * 6, Varis.pers_melee_info_list[Varis.Select_pers_list_index[1]][4].centery)
        screen.blit(self.MeleeLeftArrow, self.MeleeLeftArrow_rect)

        self.melee_description_text = self.melee_description_font.render(Varis.pers_melee_info_list[Varis.Select_pers_list_index[1]][3], False, self.text_color)
        self.melee_description_rect = self.melee_description_text.get_rect()
        self.melee_description_rect.center = (Varis.pers_melee_info_list[Varis.Select_pers_list_index[1]][4].centerx, Varis.pers_melee_info_list[Varis.Select_pers_list_index[1]][4].centery + Varis.block * 3)
        screen.blit(self.melee_description_text, self.melee_description_rect)

    def drawSelector(self):

        if self.start_pos > self.max_start_pos:
            self.start_pos = self.max_start_pos
        elif self.start_pos < self.min_start_pos:
            self.start_pos = self.min_start_pos

        screen.fill(Varis.BLACK)
        #screen.blit(pygame.transform.scale(Box_Icon, (Varis.screen_w, Varis.screen_w)), (0, self.start_pos))
        #screen.blit(pygame.transform.scale(Box_Icon, (Varis.screen_w, Varis.screen_w)), (0, self.start_pos + Varis.screen_w))

        self.draw_pers_tab()
        self.draw_long_range_weapon()
        self.draw_melee_weapon()

        pygame.display.update()





    def MouseAndKeys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.IsInSelector = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.IsInSelector = False


                if event.key == pygame.K_UP or event.key == pygame.K_w or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 4):
                    self.start_pos = min(self.start_pos + Varis.block, self.max_start_pos)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 5):
                    self.start_pos = max(self.start_pos - Varis.block, self.min_start_pos)


            pressed = pygame.mouse.get_pressed()
            if pressed[0]:
                if event.type == pygame.MOUSEMOTION:
                    self.mouse_pos = pygame.mouse.get_pos()
                    self.start_pos = self.start_pos + (self.mouse_pos[1] - self.old_mouse_pos[1])
                    self.old_mouse_pos = self.mouse_pos
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for q in range(len(Varis.Pers_info_list)):
                        if Varis.is_point_in_box(mouse_pos, Varis.Pers_info_list[q][3]):
                            Varis.Pers_chose_index = q
                            Varis.Pers_Icon = pygame.transform.scale(Varis.Pers_info_list[Varis.Pers_chose_index][0], Varis.pers_size)
                            Varis.can_continue = False


                    if Varis.is_point_in_box(mouse_pos, self.GunLeftArrow_rect):
                        Varis.Select_pers_list_index[0] -= 1
                        Varis.can_continue = False
                    elif Varis.is_point_in_box(mouse_pos, self.GunRightArrow_rect):
                        Varis.Select_pers_list_index[0] += 1
                        Varis.can_continue = False
                    elif Varis.is_point_in_box(mouse_pos, self.MeleeLeftArrow_rect):
                        Varis.Select_pers_list_index[1] -= 1
                        Varis.can_continue = False
                    elif Varis.is_point_in_box(mouse_pos, self.MeleeRightArrow_rect):
                        Varis.Select_pers_list_index[1] += 1
                        Varis.can_continue = False

                    if Varis.Select_pers_list_index[0] > len(Varis.Select_weap_list_of_id[0]) - 1:
                        Varis.Select_pers_list_index[0] = 0
                    elif Varis.Select_pers_list_index[0] < 0:
                        Varis.Select_pers_list_index[0] = len(Varis.Select_weap_list_of_id[0]) - 1

                    if Varis.Select_pers_list_index[1] > len(Varis.Select_weap_list_of_id[1]) - 1:
                        Varis.Select_pers_list_index[1] = 0
                    elif Varis.Select_pers_list_index[1] < 0:
                        Varis.Select_pers_list_index[1] = len(Varis.Select_weap_list_of_id[1]) - 1
                    Varis.Select_weapon_id = Varis.Select_weap_list_of_id[Varis.Pers_current_weapon_info_list[1]][Varis.Select_pers_list_index[Pers_current_weapon_info_list[1]]]


            elif event.type == pygame.MOUSEWHEEL:
                if event.y == 1:
                    for q in range(8):
                        self.start_pos = min(self.start_pos + Varis.tile, self.max_start_pos)
                        self.drawSelector()
                if event.y == -1:
                    for q in range(8):
                        self.start_pos = max(self.start_pos - Varis.tile, self.min_start_pos)
                        self.drawSelector()

            self.mouse_pos = pygame.mouse.get_pos()
            self.old_mouse_pos = self.mouse_pos







    def inSelector(self):
        self.IsInSelector = True

        for i in range(len(Varis.pers_gun_info_list)):
            self.select_gun_width = Varis.pers_gun_info_list[i][0].get_rect()[2]
            Varis.pers_gun_info_list[i][4].center = (round((Varis.screen_w + Varis.pers_gun_info_list[i][0].get_rect()[2]) / 2), self.start_pos + self.floors_size[1] + Varis.block * 5)
            Varis.pers_gun_info_list[i][4].size = (Varis.pers_gun_info_list[i][0].get_rect()[2], Varis.pers_gun_info_list[i][0].get_rect()[3])
        for i in range(len(Varis.pers_melee_info_list)):
            self.select_gun_width = Varis.pers_melee_info_list[i][0].get_rect()[2]
            Varis.pers_melee_info_list[i][4].center = (round((Varis.screen_w + Varis.pers_melee_info_list[i][0].get_rect()[2]) / 2), self.start_pos + self.floors_size[2] + Varis.block * 5)
            Varis.pers_melee_info_list[i][4].size = (Varis.pers_melee_info_list[i][0].get_rect()[2], Varis.pers_melee_info_list[i][0].get_rect()[3])



        while self.IsInSelector:
            self.MouseAndKeys()
            self.drawSelector()

