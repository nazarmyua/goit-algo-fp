def generate_color(step, delta=15):
    base_color = "#102030"
    r = int(base_color[1:3], 16)
    g = int(base_color[3:5], 16)
    b = int(base_color[5:7], 16)

    r = min(255, int(r + step * delta))
    g = min(255, int(g + step * delta))
    b = min(255, int(b + step * delta))

    return f"#{r:02X}{g:02X}{b:02X}"
