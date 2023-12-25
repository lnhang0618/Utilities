from matplotlib import font_manager

fonts = sorted(set([f.name for f in font_manager.fontManager.ttflist]))
for font in fonts:
    print(font)
