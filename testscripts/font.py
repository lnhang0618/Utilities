from matplotlib import font_manager
import matplotlib

fonts = sorted(set([f.name for f in font_manager.fontManager.ttflist]))
for font in fonts:
    print(font)

matplotlib.font_manager._rebuild()
