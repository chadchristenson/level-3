namespace SpriteKind {
    export const Sword = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Sword, function (sprite, otherSprite) {
    if (otherSprite == Sword) {
        statusbar_2.value += -5
        Jabberwocky_Health += -1
        sprites.destroy(otherSprite)
    }
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    Sword = sprites.createProjectileFromSprite(img`
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
        `, Alice, 0, -70)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Projectile, function (sprite, otherSprite) {
    if (otherSprite == Fireball) {
        statusbar.value += -5
        Alice_Health += -1
        sprites.destroy(otherSprite)
    }
})
let Count = 0
let Fireball: Sprite = null
let Sword: Sprite = null
let statusbar_2: StatusBarSprite = null
let statusbar: StatusBarSprite = null
let Alice: Sprite = null
let Jabberwock = sprites.create(img`
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
    `, SpriteKind.Enemy)
Alice = sprites.create(img`
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
`, SpriteKind.Player)
Jabberwock.setPosition(72, 21)
Alice.setPosition(77, 90)
controller.moveSprite(Alice, 100, 0)
Alice.setStayInScreen(true)
tiles.setCurrentTilemap(tilemap`level1`)
statusbar = statusbars.create(20, 4, StatusBarKind.Health)
statusbar.setLabel("HP")
statusbar.attachToSprite(Alice)
statusbar_2 = statusbars.create(20, 4, StatusBarKind.Health)
statusbar_2.attachToSprite(Jabberwock)
statusbar_2.setLabel("HP")
let Jabberwocky_Health = 20
let Alice_Health = 20
forever(function () {
    Count += 1
    Jabberwock.follow(Alice, 50)
    Jabberwock.y = 21
    if (Count == 30) {
        Fireball = sprites.createProjectileFromSprite(img`
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
            `, Jabberwock, 0, 70)
        Count = 0
    }
    if (Jabberwocky_Health == 0) {
        game.gameOver(true)
    }
    if (Alice_Health == 0) {
        game.gameOver(false)
    }
})
