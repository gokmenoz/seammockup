import dill

from bokeh.models import (LinearColorMapper, CategoricalColorMapper,FixedTicker,ColorBar,GMapOptions, Patches, GMapPlot,
                          Range1d,HoverTool,Panel, Tabs,WheelZoomTool,PanTool,TapTool,CustomJS,BoxZoomTool,OpenURL,ColumnDataSource)
from bokeh.models.mappers import CategoricalColorMapper
from bokeh.plotting import gmap

def map_zoning_districts():
    zoningdist=dill.load(open('static/zoningdist.pkd','rb'))
    source= ColumnDataSource(
        data=dict(
            lat=zoningdist[1],
            lon=zoningdist[0],
            d=zoningdist[2]
        )
    )
    palette = ['#f03b20','#feb24c','#bdbdbd','#a1d99b']

    color_mapper=CategoricalColorMapper(palette=palette, factors=['C','R','M','P'])
    color_mapper_bar=LinearColorMapper(palette=palette, low=-0.5,high=3.5)

    map_options=GMapOptions(lat=40.71455, lng=-73.90012,map_type="roadmap",zoom=11)

    plot=GMapPlot(x_range=Range1d(), y_range=Range1d(), map_options=map_options,width=1200,height=1000)
    plot.api_key="AIzaSyAG6g5nqyGVnwHjvA-l4bpG0sBoOJZ75yA"

    #Add patch renderers to figure. 
    patch=Patches(xs='lon',ys='lat',fill_color={'field':'d', 'transform' : color_mapper},line_color = 'black', fill_alpha = 0.3)
    plot.add_glyph(source,patch)

    #Add colorbar
    ticker = FixedTicker(ticks=list(range(4)))
    colorbar=ColorBar(color_mapper=color_mapper_bar, ticker=ticker, major_label_overrides={0:'Commercial',1:'Residential',2:'Manufacturing',3:'Parks and Playgrounds'},
                      width = 500, height = 20,
                      border_line_color=None,location = (0,0), orientation = 'horizontal')
   
    #Add hover tool
    plot.add_tools(PanTool(),BoxZoomTool(),WheelZoomTool())
    plot.add_layout(colorbar,'above')
    
    return plot