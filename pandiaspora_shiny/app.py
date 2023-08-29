from shiny import App, render, ui
from shinywidgets import output_widget, render_widget
import pandas as pd
import plotnine as gg
import plotly.express as px
import plotly.graph_objs as go
choices_select = {
    "year": "Year",
    "country": "Country",
    "probem": "Problem",
    "all" : "All Data"
}
choices_graph = {
    "bargraph": "Bar Graph",
    "linegraph": "Line Graph"
}
choices_check = {
    "frequency": "Frequency"
}
app_ui = ui.page_fluid(
    ui.layout_sidebar(
        ui.panel_sidebar(
            ui.input_select(
                id="x", label="X-axis Variable", choices=choices_select, selected="year"
            ),
            ui.input_select(
                id="t", label="Graph Type", choices=choices_graph, selected="Bar Graph"
            ),
        ),
        ui.panel_main(
            output_widget("my_widget"), ui.output_text("text"), output_widget("table"),

        )
    )
)


def server(input, output, session):
    @output
    @render_widget
    def my_widget():
        if input.x() == "year":
            if input.t() == "bargraph":
                file = pd.read_csv(r'D:\PanDiaspora\pandiaspora_shiny\Data\barByYear.csv')
                fig = px.bar(
                            file,
                            x = "Year",
                            y = 'Frequency',
                            title = "Bar Graph of Year vs Frequency",
                            barmode='stack',
                            
                )
                fig.update_layout(
                    xaxis = dict(
                        tickmode = 'array',
                        ticktext = file['Year'].values
                    )
                )
                return fig
            if input.t() == "linegraph":
                        file = pd.read_csv(r'D:\PanDiaspora\pandiaspora_shiny\Data\barByYear.csv')
                        fig = px.line(
                                    file,
                                    x = "Year",
                                    y = 'Frequency',
                                    title = "Bar Graph of Year vs Frequency",
                                    
                        )
                        # fig.update_layout(
                        #     xaxis = dict(
                        #         tickmode = 'array',
                        #         ticktext = file['Country'].values
                        #     )
                        # )
                        return fig
        if input.x() == "country":
                if input.t() == "bargraph":
                    file = pd.read_csv(r'D:\PanDiaspora\pandiaspora_shiny\Data\barByCountry.csv')
                    fig = px.bar(
                                file,
                                x = "Country",
                                y = 'Frequency',
                                title = "Bar Graph of Country vs Frequency",
                                barmode='stack',
                                
                    )
                    fig.update_layout(
                        xaxis = dict(
                            tickmode = 'array',
                            ticktext = file['Country'].values
                        )
                    )
                    return fig
    @output
    @render_widget
    def table():
            df = pd.read_csv(r"D:\PanDiaspora\pandiaspora_shiny\Data\data_new.csv")
            df = df.fillna('')
            fig = go.Figure(data=[go.Table(
            header=dict(values=list(["PMID", "Title", "First Author", "Journal/Book", "Publication Year", "Create Date", "DOI", "Mesh Terms"]),
                        fill_color='paleturquoise',
                        align='left'),
            cells=dict(values=[df.PMID, df["Title"].values, df["First Author"].values, df["Journal/Book"].values, df["Publication Year"].values, df["Create Date"].values, df.DOI, df["Mesh Terms"].values],
                    fill_color='lavender',
                    align='left'))
            ])  
            fig.update_layout(
                height=800  # Set the desired height in pixels
            )
            return fig
                
    # @output
    # @render.plot
    # def plot():
    #     custom_palette = ["#1f77b4", "#ff7f0e"]

    #     if input.x() == "year":
    #         file = pd.read_csv(r'D:\PanDiaspora\pandiaspora_shiny\Data\barByYear.csv')
    #         fig = px.bar(file,
    #                      x = "x",
    #                      y = 'y',
    #                      title = "Bar Graph of Year vs Frequency",
    #                      barmod='stack')
    #         # plot = (
    #         #     gg.ggplot(file, gg.aes(x="x", y="y")) 
    #         #     + gg.geom_bar(stat='identity')
    #         #     + gg.geom_col(position="dodge")
    #         #     + gg.geom_text(gg.aes(label="y"), position=gg.position_dodge(width=0.9), nudge_y=13)
    #         #     + gg.labs(title="Bar Graph of Year vs Frequency", x="Year", y="Frequency")
    #         #     + gg.scale_fill_brewer(
    #         #         type="qual",
    #         #         palette="Dark2",
    #         #         name="Interaction",
    #         #     )
    #         #     + gg.scale_x_continuous(breaks= file['x'].values)
    #         #     + gg.theme_seaborn()
    #         # )
    #         # return plot
    #     if input.x() == "country":
    #         file = pd.read_csv(r'D:\PanDiaspora\pandiaspora_shiny\Data\barByCountry.csv')
    #         fig = (
    #             gg.ggplot(file, gg.aes(x="x", y="y")) 
    #             + gg.geom_bar(stat='identity')
    #             + gg.geom_col(position="dodge")
    #             + gg.labs(title="Bar Graph of Country vs Frequency", x="Country", y="Frequency")
    #             + gg.scale_fill_brewer(
    #                 type="qual",
    #                 palette="Dark2",
    #                 name="Interaction",
    #             )
    #             # + gg.scale_x_continuous(expand=(0.05, 0.05))
    #             + gg.theme_seaborn()
    #             + gg.theme(
    #                 axis_text_x = gg.element_text(),
    #                 # plot_margin={"t": 20, "r": 20, "b": 20, "l": 20},
    #             )
    #         )
    #         return fig
            
    def txt():
        return f"n*2 is {input.n() * 2}"

df = pd.read_csv(r"D:\PanDiaspora\pandiaspora_shiny\Data\data_new.csv")
app = App(app_ui, server)
