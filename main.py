@namespace
class SpriteKind:
    Sword = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    global Jabberwocky_Health
    if otherSprite == Sword2:
        statusbar_2.value += -5
        Jabberwocky_Health += -1
        sprites.destroy(otherSprite)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.Sword, on_on_overlap)

def on_a_pressed():
    global Sword2
    Sword2 = sprites.create_projectile_from_sprite(img("""
            . . . . . . . f . . . . . . . . 
                    . . . . . . f 1 f . . . . . . . 
                    . . . . . . f 1 1 f . . . . . . 
                    . . . . . . f 1 1 f . . . . . . 
                    . . . . . . f 1 1 f . . . . . . 
                    . . . . . . f 1 1 f . . . . . . 
                    . . . . . . f 1 1 f . . . . . . 
                    . . . . . . f 1 1 f . . . . . . 
                    . . . . . . f 1 1 f . . . . . . 
                    . . . . . . f 1 1 f . . . . . . 
                    . . . . f . f 1 1 f 1 f . . . . 
                    . . . f e f f 4 4 f f e f . . . 
                    . . . . f e e e e e e f . . . . 
                    . . . . . f f 2 2 f f . . . . . 
                    . . . . . . f e e f . . . . . . 
                    . . . . . . f 2 2 f . . . . . . 
                    . . . . . . f e e f . . . . . . 
                    . . . . . . f f f f . . . . . .
        """),
        Alice,
        0,
        -70)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap2(sprite2, otherSprite2):
    global Alice_Health
    if otherSprite2 == Fireball:
        statusbar.value += -5
        Alice_Health += -1
        sprites.destroy(otherSprite2)
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap2)

Count = 0
Fireball: Sprite = None
Sword2: Sprite = None
statusbar_2: StatusBarSprite = None
statusbar: StatusBarSprite = None
Alice: Sprite = None
Jabberwock = sprites.create(img("""
        ..............ff......ff..............
            .............ff........ff.............
            ............ff..........ff............
            ...........f5f..........f5f...........
            ..........f55f.ffffffff.f55f..........
            ..........f55ff77777777ff55f..........
            ..........f55f7777777777f55f..........
            ..........f55f7ff7777ff7f55f..........
            ..........f5f7777f77f7777f7f..........
            ..........f7777227777227777f..........
            ..........f77772f7777f27777f..........
            ..........f7777777777777777f..........
            ..........f7777777777777777f..........
            ..........f7777777337777777f..........
            ..........f7777773113777777f..........
            ..........f7777773223777777f..........
            ..........f7777773223777777f..........
            ..ffffffff.f77777311377777f.ffffffff..
            .f77777777f.f777773377777f.f77777777f.
            f77ffffff77f.f7777777777f.f77ffffff77f
            f7f5f5f55f77f.ff777777ff.f77f55f5f5f7f
            ff55f5ff55f77f77ffffff77f77f55ff5f55ff
            .fff555ff55fff7777777777fff55ff555fff.
            ..f55555f5555f7777777777f5555f55555f..
            ...ff555f5fff777777777777fff5f5555f...
            ....ffffff..f777f7777f777f..ffffff....
            ............f777f7777f777f............
            ............f7777f77f7777f............
            ...........f7f777f77f777f7f...........
            ..........f77f777f77f777f77f..........
            ..........f777f777ff777f777f..........
            ..........f777f777ff777f777f..........
            ...........ffff777ff777ffff...........
            ..............ffffffffff..............
    """),
    SpriteKind.enemy)
Alice = sprites.create(img("""
        ......55555555555......
            .....5555555555555.....
            ....555555555555555....
            ...55555555555555555...
            ...55555555555555555...
            ...55555555555555555...
            ..5555555555555555555..
            ..5555555555555555555..
            ..5555555555555555555..
            ..55555555555555555555.
            .555555555555555555555.
            .555555555555555555555.
            .555555555555555555555.
            .555555555555555555555.
            .555555555555555555555.
            .5555555555555555555555
            55555555555555555555555
            55555555555555555555555
            .555555555555555555555.
            ..5555555555555555555..
            ....555555555555555....
            ....f5555555555555f....
            ....f8888888888888f....
            ....f8888888888888f....
            ...f888888888888888f...
            ...f8888888888888888f..
            ..f888888888888888888f.
            ..f888888888888888888f.
            .f88888f88888888f88888f
            .f8f888f88888888f888f8f
            ..ff88f8888888888f88ff.
            ....fff88f8888f88fff...
            .......ffff88ffff......
            .........11fff11.......
            .........111.111.......
            .........111.111.......
            .........fff.fff.......
            ........fffffffff......
            ........fffffffff......
            .........fff.fff.......
    """),
    SpriteKind.player)
Jabberwock.set_position(72, 21)
Alice.set_position(77, 90)
controller.move_sprite(Alice, 100, 0)
Alice.set_stay_in_screen(True)
tiles.set_current_tilemap(tilemap("""
    level1
"""))
statusbar = statusbars.create(20, 4, StatusBarKind.health)
statusbar.set_label("HP")
statusbar.attach_to_sprite(Alice)
statusbar_2 = statusbars.create(20, 4, StatusBarKind.health)
statusbar_2.attach_to_sprite(Jabberwock)
statusbar_2.set_label("HP")
Jabberwocky_Health = 20
Alice_Health = 20

def on_forever():
    global Count, Fireball
    Count += 1
    Jabberwock.follow(Alice, 50)
    Jabberwock.y = 21
    if Count == 30:
        Fireball = sprites.create_projectile_from_sprite(img("""
                . . . . c c c b b b b b . . . . 
                            . . c c b 4 4 4 4 4 4 b b b . . 
                            . c c 4 4 4 4 4 5 4 4 4 4 b c . 
                            . e 4 4 4 4 4 4 4 4 4 5 4 4 e . 
                            e b 4 5 4 4 5 4 4 4 4 4 4 4 b c 
                            e b 4 4 4 4 4 4 4 4 4 4 5 4 4 e 
                            e b b 4 4 4 4 4 4 4 4 4 4 4 b e 
                            . e b 4 4 4 4 4 5 4 4 4 4 b e . 
                            8 7 e e b 4 4 4 4 4 4 b e e 6 8 
                            8 7 2 e e e e e e e e e e 2 7 8 
                            e 6 6 2 2 2 2 2 2 2 2 2 2 6 c e 
                            e c 6 7 6 6 7 7 7 6 6 7 6 c c e 
                            e b e 8 8 c c 8 8 c c c 8 e b e 
                            e e b e c c e e e e e c e b e e 
                            . e e b b 4 4 4 4 4 4 4 4 e e . 
                            . . . c c c c c e e e e e . . .
            """),
            Jabberwock,
            0,
            70)
        Count = 0
    if Jabberwocky_Health == 0:
        game.game_over(True)
    if Alice_Health == 0:
        game.game_over(False)
forever(on_forever)
