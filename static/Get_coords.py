from shapely.geometry import LineString, Point
from bokeh.models.glyphs import Line,MultiLine

def get_coords(poly):
    if poly.type == 'Polygon':
        x,y=poly.exterior.xy
        return [list(x),list(y)]
    else:
        X=[]
        Y=[]
        for p in poly:
            x,y=p.exterior.xy
            X.append(list(x))
            Y.append(list(y))
        return [X,Y]