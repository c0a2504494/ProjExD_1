import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img_flip = pg.transform.flip(bg_img, True, False)


    gazoukadai = pg.image.load("fig/3.png")
    gazoukadai = pg.transform.flip(gazoukadai,True,False)
    

    tmr = 0
    i=0
    k=0
    kk_rct=gazoukadai.get_rect()
    kk_rct.center = 300, 200
    

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        if k % 2 == 0:
            screen.blit(bg_img, [i, 0])
            screen.blit(bg_img_flip, [i+1600, 0])
        else:
            screen.blit(bg_img_flip, [i, 0])
            screen.blit(bg_img, [i+1600, 0])

        key_list=pg.key.get_pressed()
        if key_list[pg.K_UP]:
            kk_rct.move_ip((0, -1))
        if key_list[pg.K_DOWN]:
            kk_rct.move_ip((0, 1))
        if key_list[pg.K_LEFT]:
            kk_rct.move_ip((-1, 0))
        if key_list[pg.K_RIGHT]:
            kk_rct.move_ip((1, 0))  
        else:
            kk_rct.move_ip((-1, 0))  
            
        screen.blit(gazoukadai, [kk_rct.x, kk_rct.y])
        i-=1
        



        
        
        if i==-1600:
            i=0
            k+=1
        pg.display.update()
        tmr += 1        
        clock.tick(200)
    



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()