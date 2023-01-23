def color_scale(check):
    c = check * 255
    if c <= 255:
        r = c
    else:
        r = 255
    return r

print(color_scale(1.5))