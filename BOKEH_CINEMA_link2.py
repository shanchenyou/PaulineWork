#點選 電影院名 連結網址
from bokeh.plotting import figure, output_file, show
from bokeh.models import CustomJS, ColumnDataSource
from bokeh.models import Div, Row, OpenURL, TapTool
#from bokeh.io import output_file , show


output_file("toolbar.html")


p = figure(plot_width=600, plot_height=600, tools="tap",
           title="Mouse over the dots") 
   
source = ColumnDataSource(
        data=dict(
            x=[0,0.2, 1.5, 1.5, 2.5, 2.3, 5],
            y=[0,2.5, 3,    1, 4.4, 2, 5],
            #color=["palegreen", "blue", "blue", "blue", "blue", "blue", "red"]
            #cinema=['-','國賓大戲院', '台北長春國賓影城', '東南亞秀泰影城', '美麗華大直影城', '台北信義威秀影城', '-'],
            href=['-','https://www.ambassador.com.tw/home/Showtime?ID=453b2966-f7c2-44a9-b2eb-687493855d0e','https://www.ambassador.com.tw/home/Showtime?ID=453b2966-f7c2-44a9-b2eb-687493855d0e', 'https://www.showtimes.com.tw/events?corpId=8', 'https://www.miramarcinemas.tw/timetable', 'http://www.vscinemas.com.tw/vsweb/theater/detail.aspx?id=1#week', 'https://www.google.com/'],
            color=["palegreen", "blue", "blue", "blue", "blue", "blue", "red"] #  default COLOR last one
        )
    )


p.circle('x', 'y', size=20, color = 'color', alpha=0.6, source=source) #color = 'color'


p.background_fill_color = None  #fig.background_fill_color = "#0" None  OR fig.background_fill_alpha= 0.0

pic = "TAIPEI8.jpg"
d1 = Div(text = '<div style="position: absolute; left:25px; top:22px"><img src=' + pic + ' style="width:550px; height:550px; opacity: 0.9"></div>')
       

url = "@href"
taptool = p.select(type=TapTool)
taptool.callback = OpenURL(url=url)
show(Row(d1, p))
