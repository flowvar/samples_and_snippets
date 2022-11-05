from xml.etree.ElementInclude import include
import plotly.express as px
import tempfile



def create_html_plot():

    df = px.data.stocks()
    fig = px.line(df, x='date', y="GOOG")
    x = tempfile.SpooledTemporaryFile()
    return fig.to_html(x, include_plotlyjs="cdn")


def create_plot_using_values(group1: str, group2: str, title: str):
    fig = px.pie(values=[10, 20], names=[group1, group2], title=title)
    x = tempfile.SpooledTemporaryFile()
    return fig.to_html(x, include_plotlyjs="cdn")


# fig = create_plot_using_values(group1="Whites", group2="Blacks", title="White vs. Black")
# fig.show()
