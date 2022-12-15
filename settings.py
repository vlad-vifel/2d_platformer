first_map = [
    'XXXXX                                                   XXXXX',
    'XXXXX        GGG                         G              XXXXX',
    'XXXXX      XXXXXX                   P   XX              XXXXX',
    'XGXXX P              G             XXX      GG          XXXXX',
    'XXXXXXXXXGG         XX                     XXXX    GG   XXGXX',
    'XXXXXXXXXXX       XXXX       G  XX         XXXX   XXXGG XXXXX',
    'XXXXX  XXXX   GG GXX        XX             XXXX   XXXXXXXXXXX',
    'XXXXX  XX    XXXXXXX    XX  XX           XXXGXX      XXXXXXGX',
    'XXGXX      G XXXXXXXGG  XX  XXXX         XXXXXX        XXXXXX',
    'XXXXX   GGXXXXX  XXXXX  XX  XXXXXXXX   XXXGXXXX    G FGXXGXXX',
    'XXXXX  XXXXXXXX  XXXXX  XX  XXXXXXXX   XXXXXXXX   XXXXXXXXXXX']

second_map = [
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XGXXX                                XXXXX           XXXXXXXX',
    'XXXGX     X X          XX            XXXXX              XXXXX',
    'XXXXX                       G        XXXXX            FGXXXXX',
    'XXGXX    XXXXX             XX        XXGXX           XXXXXXXX',
    'XXXXX                  PG  XX        XXXXX       G   XXXXXXXX',
    'XGXXX                GXXX            XXXXX      XXX  XXXXXXXX',
    'XXXXX       G       XXXXX                       XXX  XXXXXXXX',
    'XXXXX P    XX    G  XXX                     XX  XXX  XXXXXXXX',
    'XXXGXXXXGG XX   XX                     GGG GXX  XXX  XXXXXXXX',
    'XXXXXXXXXX      XX                 XXXXXXXXXXX  XXX  XXXXXXXX']

level_maps = [first_map, second_map]

player_size = 64
tile_size = 80
screen_width = 1280
screen_height = len(level_maps[0]) * tile_size
