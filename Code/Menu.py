import Varis, Play
from MenuTabs import *
pg = pygame

pygame.init()
flags = pygame.HWSURFACE | pygame.FULLSCREEN
#flags = pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE
screen = pygame.display.set_mode((Varis.screen_w, Varis.screen_h), flags)

Elements = ["Continue", "New Game", "Pers Selector", "Tutorial", "None", "Exit"]
Elem_info = []
Arial = pygame.font.SysFont('arial', round(Varis.screen_h / 2 / len(Elements)))

game = Play.Game()

pygame.display.set_icon(Varis.Game_window_icon)



class Menu:
    def __init__(self):
        self.chose_index = 0
        self.is_in_menu = True
        self.Menu_elem = Elements.copy()
        self.Elem_info = Elem_info
        self.PSelector = PersSelector()

    def clear_temp_data(self):
        global game
        Varis.pers_weapon_angle = 0
        Varis.can_continue = False
        Varis.pers_pos = [round(Varis.game_screen_w / 2), round(Varis.game_screen_h / 2)]
        Varis.hp = 10
        Varis.Pers_current_weapon_info_list[1] = 0
        Varis.Weapon_type_select_list = [True, False]
        Varis.Select_weapon_id = Varis.Select_weap_list_of_id[0][Varis.Select_pers_list_index[Varis.Pers_current_weapon_info_list[1]]]

        for bullet_group in Varis.Guns_bullets_group_list:
            bullet_group.empty()
        Varis.create_tile_map()

        game = Play.Game()

    def EXIT(self):
        pygame.display.quit()
        pygame.quit()
        sys.exit()

    def play_game(self):
        Varis.for_but_is_click = False
        game.in_game()
        self.chose_index = 0

    def continue_game(self):
        pass

    def PersSelector(self):
        self.PSelector.inSelector()
        self.chose_index = self.Menu_elem.index("Pers Selector")


    def draw_menu(self):
        screen.fill(Varis.BLACK)
        self.Menu_elem = Elements.copy()
        if not Varis.can_continue:
            self.Menu_elem.pop(0)
        self.Elem_info = self.Menu_elem.copy()
        tab = round(Varis.screen_h / (len(self.Menu_elem) + 1) / 1.2)
        for q in range(0, len(self.Menu_elem)):
            if q == self.chose_index:
                #Arial = pygame.font.Font(None, round(Varis.screen_h / 2 / len(Elements) * 1.2))
                Arial = pygame.font.SysFont('arial', round(Varis.screen_h / 2 / len(Elements) * 1.2))
                elem_name = Arial.render(self.Menu_elem[q], False, Varis.GREY200)
                elem_rect = elem_name.get_rect()
                elem_rect.center = (round(Varis.screen_w / 2), round(tab * 2 + tab * q))
                self.Elem_info[q] = (elem_rect.x, elem_rect.y, elem_rect.width, elem_rect.height)
            else:
                Arial = pygame.font.SysFont('arial', round(Varis.screen_h / 2 / len(Elements)))
                elem_name = Arial.render(self.Menu_elem[q], False, Varis.GREY120)
                elem_rect = elem_name.get_rect()
                elem_rect.center = (round(Varis.screen_w / 2), round(tab * 2 + tab * q))
                self.Elem_info[q] = (elem_rect.x, elem_rect.y, elem_rect.width, elem_rect.height)
            screen.blit(elem_name, elem_rect)

        #screen.blit(Varis.Pers_Icon, (10, 10))
        pygame.display.update()

    def Buttons_and_Mouse(self):
        global screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.EXIT()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.EXIT()

                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.chose_index -= 1
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.chose_index += 1
                if self.chose_index <= -1:
                    self.chose_index = len(self.Menu_elem) - 1
                elif self.chose_index >= len(self.Menu_elem):
                    self.chose_index = 0
                if event.key == pygame.K_RETURN:
                    if self.Menu_elem[self.chose_index] == "Exit":
                        self.EXIT()
                    elif self.Menu_elem[self.chose_index] == "New Game":
                        self.clear_temp_data()
                        self.play_game()
                    elif self.Menu_elem[self.chose_index] == "Continue":
                        self.play_game()
                    elif self.Menu_elem[self.chose_index] == "Pers Selector":
                        self.PersSelector()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    select = 999
                    for i in range(len(self.Elem_info)):
                        elem = self.Elem_info[i]
                        if ((mouse_pos[0] >= elem[0] - Varis.tile * 4) and (mouse_pos[1] >= elem[1] - 16)) and ((mouse_pos[0] <= elem[0] + elem[2] + Varis.tile * 4) and (mouse_pos[1] <= elem[1] + elem[3] + 16)):
                            select = i
                    if select != 999:
                        if self.Menu_elem[select] == "Exit":
                            self.EXIT()
                        elif self.Menu_elem[select] == "New Game":
                            self.clear_temp_data()
                            self.play_game()
                        elif self.Menu_elem[select] == "Continue":
                            self.play_game()
                        elif self.Menu_elem[select] == "Pers Selector":
                            self.PersSelector()


    def in_menu(self):
        while self.is_in_menu:
            self.draw_menu()
            self.Buttons_and_Mouse()




