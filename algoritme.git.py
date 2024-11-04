def draw_rectangle(width, height): 
    print("|"+"-"*(width-2)+"|")
    for _ in range(height - 2):
        print("|" + " "*(width-2) + "|")
    print("|"+"-"*(width-2)+"|")
draw_rectangle(12, 5)
