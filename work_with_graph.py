import networkx as nx
from bokeh.models import Plot, Range1d, Circle, HoverTool, BoxZoomTool, ResetTool
from bokeh.models.graphs import from_networkx


class GraphWorker(nx.Graph):

    def rendering_graph(self):
        """Задаем параметры отрисовки графа"""
        plot = Plot(plot_width=1600, plot_height=1400,
                    x_range=Range1d(-1.1, 1.1), y_range=Range1d(-1.1, 1.1))
        node_hover_tool = HoverTool(tooltips=[("Name", "@index")])
        plot.add_tools(node_hover_tool, BoxZoomTool(), ResetTool())
        graph_renderer = from_networkx(self, nx.spring_layout, scale=1, center=(0, 0))
        graph_renderer.node_renderer.glyph = Circle(size=15, fill_color="blue")
        plot.renderers.append(graph_renderer)
        return plot

    def create_graph(self, dictionary):
        """Строим ссылочный граф"""
        for key in dictionary.keys():
            self.add_node(key)
            for item in dictionary[key]:
                self.add_node(item)
                self.add_edge(key, item)

    def create_base_graph(self, list_links, start_link):
        """Создаем основу для графа по первой ссылке"""
        for link in list_links:
            self.add_node(link)
            self.add_edge(start_link, link)

