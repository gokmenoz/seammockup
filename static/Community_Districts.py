import dill

from bokeh.models import (LinearColorMapper, ColorBar,GMapOptions, Patches,GMapPlot,Range1d,HoverTool,Panel, Tabs,
                         WheelZoomTool,PanTool,BoxZoomTool,ColumnDataSource,TapTool)
from bokeh.models.callbacks import OpenURL
from bokeh.palettes import brewer
from bokeh.plotting import gmap
import pandas as pd
from Get_coords import get_coords


def map_community_districts():

    commdist=dill.load(open('static/commdist.pkd','rb'))

    source= ColumnDataSource(
        data=dict(
            lat=commdist[1],
            lon=commdist[0],
            son_issue_1=commdist[2],
            son_issue_2=commdist[3],
            son_issue_3=commdist[4],
            cd=commdist[5]         
        )
    )

    palette = brewer['Pastel2'][5]

    color_mapper=LinearColorMapper(palette=palette,low=100,high=500)

    TOOLTIPS="""
    <div>
        <div>
            <span style="font-size: 16px; font-weight:bold; color: #00BFFF;">District:</span> <span style="font-size: 14px; color: #000000"> @cd </span><br>
            <span style="font-size: 14px; font-weight:bold; color: #00BFFF;">1st need:</span> <span style="font-size: 14px; color: #000000"> @son_issue_1 </span><br>
            <span style="font-size: 12px; font-weight:bold; color: #00BFFF;">2nd need: </span> <span style="font-size: 12px; color: #000000">@son_issue_2</span><br>
            <span style="font-size: 10px; font-weight:bold; color: #00BFFF;">3rd need: </span> <span style="font-size: 10px; color: #000000">@son_issue_3</span>
        </div>
    </div>
    """

    map_options=GMapOptions(lat=40.71455, lng=-74.00712,map_type="roadmap",zoom=11)

    plot=GMapPlot(x_range=Range1d(), y_range=Range1d(), map_options=map_options,width=1200,height=1000)
    plot.api_key="AIzaSyAG6g5nqyGVnwHjvA-l4bpG0sBoOJZ75yA"


    #Add patch renderers to figure. 
    patch=Patches(xs='lon',ys='lat',fill_color={'field':'cd', 'transform' : color_mapper},line_color = 'black', fill_alpha = 0.5)
    plot.add_glyph(source,patch)

    #Add hover tool
    hover = HoverTool(tooltips=TOOLTIPS)
    plot.add_tools(hover,PanTool(),BoxZoomTool())

    #Add tap tool
    url='https://seammockup.herokuapp.com/district@cd.html'
    taptool = TapTool(callback=OpenURL(url=url,same_tab=True))
    plot.add_tools(taptool)
 
    return plot   