import dill

from bokeh.models import (LinearColorMapper, ColorBar,GMapOptions, Patches,GMapPlot,Range1d,HoverTool,Panel, Tabs,
                         WheelZoomTool,PanTool,BoxZoomTool,ColumnDataSource)
from bokeh.palettes import brewer
from bokeh.plotting import gmap
import pandas as pd
from Get_coords import get_coords

def map_2024():

    commdist_pred=dill.load(open('static/commdist_pred.pkd','rb'))

    source= ColumnDataSource(
        data=dict(
            lat=commdist_pred[1],
            lon=commdist_pred[0],
            cd=commdist_pred[5],
            pred_1=commdist_pred[2],
            pred_2=commdist_pred[3],
            pred_3=commdist_pred[4]
        )
    )
    palette = brewer['Pastel2'][5]

    color_mapper=LinearColorMapper(palette=palette,low=100,high=500)

    TOOLTIPS_PRED="""
    <div>
        <div>
            <span style="font-size: 16px; font-weight:bold; color: #00BFFF;">District:</span> <span style="font-size: 14px; color: #000000"> @cd </span><br>
            <span style="font-size: 14px; font-weight:bold; color: #00BFFF;">1st need:</span> <span style="font-size: 14px; color: #000000"> @pred_1 </span><br>
            <span style="font-size: 12px; font-weight:bold; color: #00BFFF;">2nd need: </span> <span style="font-size: 12px; color: #000000">@pred_2</span><br>
            <span style="font-size: 10px; font-weight:bold; color: #00BFFF;">3rd need: </span> <span style="font-size: 10px; color: #000000">@pred_3</span>
        </div>
    </div>
    """
 
    map_options=GMapOptions(lat=40.71455, lng=-74.00712,map_type="roadmap",zoom=11)

    plot_pred=GMapPlot(x_range=Range1d(), y_range=Range1d(), map_options=map_options,width=1200,height=1000)
    plot_pred.api_key="AIzaSyAG6g5nqyGVnwHjvA-l4bpG0sBoOJZ75yA"

    patch=Patches(xs='lon',ys='lat',fill_color={'field':'cd', 'transform' : color_mapper},line_color = 'black', fill_alpha = 0.5)
    plot_pred.add_glyph(source,patch)  

    hover_pred = HoverTool(tooltips=TOOLTIPS_PRED)
    plot_pred.add_tools(hover_pred, PanTool(),BoxZoomTool())

    return plot_pred
