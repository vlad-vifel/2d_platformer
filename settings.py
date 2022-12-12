from pygame import font

level_map1 = [
    'XXXXX                           ',
    'XKXXX                           ',
    'XXXKX         GG                ',
    'XXXXXG XX P  XXXX         XX    ',
    'XXKXXXXXX           G           ',
    'XXXXXXXXXXX        XXX       XX ',
    'XKXXX  XXXX   GKKGXX       G    ',
    'XXXXX  XX    XXXXXXX   XX XX    ',
    'XXXKX      G XX XXXX   XX XXX   ',
    'XXXXX   KKXXXXX XXXXXX XX XXXX  ',
    'XXXXX  XXXXXXXX XXXXXX XX XXXX  ']

level_map2 = [
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XKXXX                           ',
    'XXXKX         GG                ',
    'XXXXXG XX P  XXXX         XX    ',
    'XXKXXXXXX           G           ',
    'XXXXXXXXXXX        XXX       XX ',
    'XKXXX  XXXX   GKKGXX       G    ',
    'XXXXX  XX    XXXXXXX   XX XX    ',
    'XXXKX      G XX XXXX   XX XXX   ',
    'XXXXX   KKXXXXX XXXXXX XX XXXX  ',
    'XXXXX  XXXXXXXX XXXXXX XX XXXX  ']

tile_size = 80
screen_width = 1200
screen_height = len(level_map1) * tile_size
