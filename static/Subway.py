from bokeh.models.mappers import CategoricalColorMapper,LinearColorMapper
from bokeh.models import (GMapOptions, Patches,GMapPlot,Range1d,ColorBar,
                         WheelZoomTool,PanTool,TapTool,ColumnDataSource, Circle,FixedTicker)
import dill
from bokeh.plotting import gmap
from bokeh.models.glyphs import MultiLine


def map_subway():
    label_routes=dill.load(open('static/label_routes.pkd','rb'))
    distinct_labels=dill.load(open('static/distinct_labels.pkd','rb'))
    subway=dill.load(open('static/subway.pkd','rb'))
    source_subway_points=ColumnDataSource(
        data=dict(lon=subway[0],lat=subway[1])
    )
    source_subway_routes=ColumnDataSource(
        data=dict(lon=subway[2],lat=subway[3],line_num=subway[5],line=subway[4])
    )
    palette=['#de2d26','#feb24c','#ffeda0','#d95f0e','#31a354','#3182bd','#f0f0f0','#bdbdbd','#c51b8a','#e5f5e0','#636363']
    
    map_options=GMapOptions(lat=40.71455, lng=-74.00012,map_type="roadmap",zoom=11)
    plot=GMapPlot(x_range=Range1d(), y_range=Range1d(), map_options=map_options,width=1200,height=1000)
    plot.api_key="AIzaSyAG6g5nqyGVnwHjvA-l4bpG0sBoOJZ75yA"

    color_mapper=CategoricalColorMapper(palette=palette, factors=distinct_labels)
    color_mapper_bar=LinearColorMapper(palette=palette,low=-0.5,high=10.5)

    circle=Circle(x="lon", y="lat", line_color='black', 
                  fill_color="white", line_width=0.5)
    lines = MultiLine(xs="lon", ys="lat", line_color={'field':'line','transform':color_mapper}, 
                      line_width=2, line_alpha=1)
    ticker = FixedTicker(ticks=list(range(11)))
    d=dict()
    for i in range(11):
        d[i]=distinct_labels[i]

    colorbar=ColorBar(color_mapper=color_mapper_bar, ticker=ticker, major_label_overrides=d,
                      width = 500, height = 20,
                      border_line_color=None,location = (0,0), orientation = 'horizontal')
    
    plot.add_layout(colorbar,'above')
    plot.add_tools(WheelZoomTool(), PanTool())
    plot.add_glyph(source_subway_points, circle)
    plot.add_glyph(source_subway_routes,lines)
    return plot