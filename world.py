import pygal.maps.world
from pygal.style import Style

style = Style(font_family='googlefont:Raleway')

blue = Style(colors=('blue',))
worldmap_chart = pygal.maps.world.World(style=blue)
worldmap_chart.title = 'Country of residence'
worldmap_chart.add('Students', {
  'by': 1,
  'ca': 1,
  'ch': 1,
  'cn': 1,
  'de': 4,
  'eg': 1,
  'in': 7,
  'kr': 1,
  'ru': 1,
  'sg': 1,
  'us': 2,
})
worldmap_chart.render_to_png("./world.png")
