from pygal_maps_world.maps import World
from pygal.style import Style

style = Style(font_family='googlefont:Raleway')

blue = Style(colors=('blue',))
worldmap_chart = World(style=blue)
worldmap_chart.title = 'Country of residence'
worldmap_chart.add('Students', {
  'by': 1,
  'ca': 1,
  'ch': 1,
  'cn': 1,
  'de': 4,
  'eg': 1,
  'in': 11,
  'kr': 1,
  'ru': 1,
  'sg': 1,
  'us': 4,
  'gr': 1
})
worldmap_chart.render_to_png("./world.png")
