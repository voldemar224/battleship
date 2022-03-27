import string


player_field_height = 10  # in blocks
player_field_width = 10  # in blocks

upper_field_shift = 2  # in blocks
lower_field_shift = 2  # in blocks

left_field_shift = 2  # in blocks
right_field_shift = 2  # in blocks

between_fields = 2  # in blocks

field_height = upper_field_shift + player_field_height + lower_field_shift
field_width = left_field_shift + player_field_width + between_fields + player_field_width + right_field_shift


cell_size_pxl = 50
button_size_pxl = cell_size_pxl-4

letters = string.ascii_uppercase[0:player_field_width]

font = "Times"
font_size = "20"
