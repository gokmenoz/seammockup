import dill

from bokeh.models import (LinearColorMapper, GMapOptions, Patches, GMapPlot, Range1d, HoverTool,
                         WheelZoomTool,PanTool,BoxZoomTool,ColumnDataSource)
from bokeh.palettes import brewer
from bokeh.plotting import gmap


def map_school_districts():
    school_districts=dill.load(open('static/school_districts.pkd','rb'))
    
    source_school_districts= ColumnDataSource(
        data=dict(
            lat=school_districts[1],
            lon=school_districts[0],
            sd=school_districts[2]
        )
    )

    palette_school_districts=brewer['Set1'][9]

    color_mapper_school_districts=LinearColorMapper(palette=palette_school_districts,low=min(source_school_districts.data['sd']),high=max(source_school_districts.data['sd']))


    TOOLTIPS_school_districts="""
        <div>
            <div>
                <span style="font-size: 16px; font-weight:bold; color: #00BFFF;">School District:</span> <span style="font-size: 14px; color: #000000"> @sd </span>
            </div>
        </div>
        """

    map_options=GMapOptions(lat=40.71455, lng=-74.00712,map_type="roadmap",zoom=11)

    plot_school_districts=GMapPlot(x_range=Range1d(), y_range=Range1d(), map_options=map_options,width=1200,height=1000)
    plot_school_districts.api_key="AIzaSyAG6g5nqyGVnwHjvA-l4bpG0sBoOJZ75yA"

    #Add patch renderers to figure. 

    patch_school_districts=Patches(xs='lon',ys='lat',fill_color={'field':'sd', 'transform' : color_mapper_school_districts},line_color = 'black', fill_alpha = 0.5)
    plot_school_districts.add_glyph(source_school_districts,patch_school_districts)


    #Add hover tool
    hover_school_districts = HoverTool(tooltips=TOOLTIPS_school_districts)
    plot_school_districts.add_tools(hover_school_districts,WheelZoomTool(), PanTool())

    return plot_school_districts