from pygame import font

level_map1 = [
    'XXXXX                             ',
    'XXXXX         G                   ',
    'XXXXX       XXXXX           P     ',
    'X XXXG XX            G     XXX    ',
    'XXXXXXXXXP        XXXX            ',
    'XXXXXXXXXXX       XXXX        XXXX',
    'XXXXX  XXXX   GG  XX        G     ',
    'XXXXX  XX    XXXXXXX       XX     ',
    'XXX X      G XXXXXXX   XX  XXX    ',
    'XXXXX     XXXXX XXXXXX XX  XXXX   ',
    'XXXXX  XXXXXXXX XXXXXX XX  XXXX  X']

level_map2 = [
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'X XXX                           ',
    'XXX X         GG                ',
    'XXXXXG XX P  XXXX         XX    ',
    'XX XXXXXX           G           ',
    'XXXXXXXXXXX        XXX       XX ',
    'X XXX  XXXX   G  GXX       G    ',
    'XXXXX  XX    XXXXXXX   XX XX    ',
    'XXX X      G XX XXXX   XX XXX   ',
    'XXXXX     XXXXX XXXXXX XX XXXX  ',
    'XXXXX  XXXXXXXX XXXXXX XX XXXX  ']

tile_size = 80
screen_width = 1200
screen_height = len(level_map1) * tile_size
