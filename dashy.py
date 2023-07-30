# Importar pacotes

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd

from dash.dependencies import Input, Output

# Ler os dados
df2020perc = pd.read_csv('df2020perc.csv', encoding='latin-1')
ano_catdoc = pd.read_csv('ano_catdoc.csv', encoding='latin-1')
docente_uf = pd.read_csv('docente_uf.csv', encoding='latin-1')
map_redes_est = pd.read_csv('map_redes_est.csv', encoding='latin-1')
map_redes_fed = pd.read_csv('map_redes_fed.csv', encoding='latin-1')
map_redes_mun = pd.read_csv('map_redes_mun.csv', encoding='latin-1')
map_redes_priv = pd.read_csv('map_redes_priv.csv', encoding='latin-1')
map_redes_pub = pd.read_csv('map_redes_pub.csv', encoding='latin-1')

# Gráfico 1

color_mapping = {
    'Docentes com formação superior com complementação pedagógica em área diferente da qual leciona': '#aaaaaa',
    'Docentes com formação superior de bacharelado sem complementação pedagógica na mesma área da disciplina que leciona': '#02153d',
    'Docentes com formação superior de licenciatura com complementação pedagógica na mesma área da disciplina que leciona': '#4b227a',
    'Docentes com formação superior não considerada nas categorias anteriores': '#0197af',
    'Docentes sem formação superior': '#00eed0'
}

novo_rotulo = ['Educação Infantil', 'EJA EF', 'EJA EM', 'Ensino Fundamental', 'Ensino Médio']

fig = go.Figure()

fig.add_trace(
      go.Bar(
            x=df2020perc['modalidade'],
            y=df2020perc['percentual'],
            orientation='v',
            marker=dict(
                  color=df2020perc['categoria_docente'].map(color_mapping)
                  ),
            hovertext=df2020perc['categoria_docente']
            )
            )

fig.update_layout(
      legend_title='Categorias de Docentes',
      title='Percentual da qualificação dos professores nas diferentes categorias de ensino do Brasil',
      title_font=dict(
            {'family':'Segoe UI','size':18}
            ),
            xaxis=dict(
            tickmode='array',
            tickvals=list(
                    range(len(df2020perc['modalidade']))
                    ),
                    ticktext=novo_rotulo),
                    font=dict(
                        {'family':'Segoe UI','size':14}
                        ),
                        plot_bgcolor='rgb(244, 244, 244)',
                        yaxis_title='Percentual (%)',
            )


# Gráfico 2
# Criando o gráfico de linhas
fig1 = px.line(
    ano_catdoc,
    x='ano',
    y='percentual',
    color='categoria_docente',
    width=300,
    color_discrete_map=color_mapping
    )

fig1.update_traces(line=dict(width=4))

fig1.update_layout(
    title='<b>Série histórica do percentual de títulos de professores nas escolas do Brasil (2013 a 2020)',
    title_x=0.5,
    title_font=dict(
            {'family':'Segoe UI',
            'size':18,
            'color':'white'}),
    plot_bgcolor='rgb(50, 50, 50)',
    paper_bgcolor='rgb(50, 50, 50)',
    legend=dict(visible=False),
    xaxis=dict(
        title='',
        title_font=dict(
            {'family':'Segoe ui',
            'size':16,
            'color':'white'}),
        tickfont=dict({'color':'white'}),
        showgrid=False,
        gridcolor='rgb(91, 91, 91)'),
    yaxis=dict(
        title='Percentual (%)',
        title_font=dict(
            {'family':'Segoe UI',
            'size':16,
            'color':'white'}),
        tickfont=dict({'color':'white'}),
        showgrid=True,
        gridcolor='rgb(91, 91, 91)')
)


# Gráfico 3
fig2 = px.bar(
        docente_uf,
        x='sigla_uf',
        y='percentual',
        color='categoria_docente',
        barmode='stack',
        color_discrete_map=color_mapping
)

fig2.update_layout(
    title='<b>Porcentagem de tipo de título de docente por UF (2020)',
    title_x=0.5,
    font=dict(
        {'family':'Segoe UI',
         'color':'white'}),
    plot_bgcolor='rgb(50, 50, 50)',
    paper_bgcolor='rgb(50, 50, 50)',
    showlegend=False,
    xaxis=dict(
        categoryorder='total descending',
        title='',
        title_font=dict(
            {'family':'Segoe UI',
            'size':16}),
        showgrid=False),
    legend=dict(
        xanchor='center',
        yanchor='top',
        y=-0.2,
        x=0.5,
        title='Título do docente',
        title_font=dict(
            {'family':'Segoe UI',
            'size':16}),
        font=dict(
            {'family':'Segoe UI',
            'size':10})),
    yaxis=dict(
        title='Percentual (%)',
        title_font=dict(
            {'family':'Segoe UI',
            'size':16}),
        showgrid=False,
        gridcolor='rgb(91, 91, 91)'))


# Gráfico 4
col_mapping = ['rgb(75,34,122)', 'rgb(2,21,61)', 'rgb(170,170,170)', 'rgb(1,151,175)', 'rgb(0,238,208)']

# Definindo o número de linhas e colunas
specs = [[{'type':'domain'}, {}, {'type':'domain'},{}, {'type':'domain'}],
         [{},{'type':'domain'},{},{'type':'domain'},{}]]
fig3 = make_subplots(rows=2, cols=5, specs=specs,
                   subplot_titles=['<b>Estadual','','<b>Federal','','<b>Municipal','','<b>Privada','','<b>Pública',''])

# Definindo pie-charts
fig3.add_trace(go.Pie(labels=map_redes_est['categoria_docente'], values=map_redes_est['percentual'],
                      name='Estadual', marker_colors=col_mapping), row=1, col=1)
fig3.add_trace(go.Pie(labels=map_redes_fed['categoria_docente'], values=map_redes_fed['percentual'],
                      name='Federal', marker_colors=col_mapping), row=1, col=3)
fig3.add_trace(go.Pie(labels=map_redes_mun['categoria_docente'], values=map_redes_mun['percentual'],
                      name='Municipal', marker_colors=col_mapping), row=1, col=5)
fig3.add_trace(go.Pie(labels=map_redes_priv['categoria_docente'], values=map_redes_priv['percentual'],
                      name='Privada', marker_colors=col_mapping), row=2, col=2)
fig3.add_trace(go.Pie(labels=map_redes_pub['categoria_docente'], values=map_redes_pub['percentual'],
                      name='Pública', marker_colors=col_mapping), row=2, col=4)

# Ajuste do layout do pie chart
fig3.update_traces(hoverinfo='label+percent+name', textinfo='percent', textfont=dict(color='white'))  # Adicionando textinfo para mostrar labels e porcentagens
fig3.update_layout(title={
        'text': "<b>Formação dos professores das diferentes redes de ensino (2020)",
        'y': 0.98,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {'family': 'Segoe UI', 'size': 18, 'color':'white'}},
                  showlegend=False,
        plot_bgcolor='rgb(50, 50, 50)',
        paper_bgcolor='rgb(50, 50, 50)')

# Ajustando os subtítulos
fig3.update_annotations(
    font=dict(family="Segoe UI", size=14, color='white'),
    yshift=15)  # Ajuste a altura dos subtítulos aqui




# Instância do app
app = dash.Dash(__name__,
                title='Dashboard Docencia no Brasil',
                external_stylesheets=[
                      dbc.themes.DARKLY,
                      'https://cdnjs.cloudfire.com/ajax/libs/font-awesome/6.1.1/css/all.min.css',
                      'https://fonts.googleapis.com/css2?family=Joan&family=Roboto:ital,wght@0,100;1,300&family=Source+Sans+Pro:'
                      ]
                      )

# Construção da página

app.layout = html.Div(

    # Toda a aplicação
    children=[

        # Banner superior
        html.Div(
            className='Banner',
            style={
                'height':'fit-content',
                'background-color':'#00394c',
                'display':'flex',
                'flex-direction':'row',
                'aliggn-itens':'center',
                'justify-content':'space-between',
                'border-bottom':'2px solid #a5b3b6',
                'padding':'1rem 5rem',
                'width':'100%'
            },
            children=[
                html.Div(
                    className='banner-title',
                    children=[
                        html.H5(
                            ['Dashboard'],
                            style={
                                'font-family':'open sans, segoe ui',
                                'font-weigth':'1000'
                            }
                        ),
                        html.H6(['Formação dos Docentes do Brasil'],
                                style={'font-family':'open sans, Segoe ui',
                                       'font-wight':600})
                    ]
                ),
                html.Div(
                    className='banner-logo',
                    children=[
                        html.Img(src=app.get_asset_url('logo.webp'), height='30px', alt='logo')
                    ]
                )
            ]


        ),
        # Conteúdo
        html.Div(
            className='app-content',
            style={
                'display':'grid',
                'grid-template-column':'20% 80%',
                'padding':'1rem 5rem',
                'width':'100%'
            },
            children=[
                html.Div(
                    className='top',
                    style={
                        'display':'flex',
                        'flex-direction':'column',
                        'justify-content':'right',
                        'align-items':'stretch',
                        'margin':'0',
                        'padding':'0',
                        'width':'100%',
                        'margin-bottom':'3rem',
                        'background-color':'#323232',
                        'border':'Null'
                    },

                    # Gráfico 1
                    children=[
                        html.Div([
                            dcc.Graph(
                                id='Graph',
                                figure=go.Figure(
                                    data=[
                                        go.Bar(
                                            x=df2020perc['modalidade'],
                                            y=df2020perc['percentual'],
                                            orientation='v',
                                            marker=dict(
                                                color=df2020perc['categoria_docente'].map(color_mapping)
                                            ),
                                            hovertext=df2020perc['categoria_docente']
                                            )
                                            ],
                                        layout=go.Layout(
                                               legend_title='Categorias de Docentes',
                                               title='<b>Percentual da qualificação dos professores nas diferentes categorias de ensino do Brasil (2020)',
                                               title_font=dict(
                                                      family='Segoe UI',
                                                      size=18,
                                                      color='white'),
                                                title_x=0.5,
                                                xaxis=dict(tickmode='array',
                                                           tickvals=list(range(len(df2020perc['modalidade']))),
                                                           ticktext=novo_rotulo,
                                                           showgrid=False),
                                                font=dict(family='Segoe ui',
                                                          size=13,
                                                          color='white'),
                                                plot_bgcolor='rgb(50, 50, 50)',
                                                paper_bgcolor='rgb(50, 50, 50)',
                                                yaxis_title='Percentual (%)',
                                                yaxis=dict(showgrid=True,
                                                        gridcolor='rgb(91, 91, 91)'))
                                        )
                            )
                                    ], style={'width': '850px', 
                                              'height': '450px',
                                              'justify-self': 'center',
                                              'align-self': 'center',
                                              'margin':'auto'}
                                ),    
                                               
                    # Gráfico 2
                    html.Div([
                            dcc.Graph(
                                figure=fig1,
                                style={'width': '850px', 
                                       'height': '450px', 
                                       'align-self':'flex-end', 
                                       'justify-self':'flex-end',
                                       'margin':'auto'}
                            )
                        ]),
                    
                    # Gráfico 3
                    html.Div([
                        dcc.Graph(
                            figure=fig2
                        )
                    ]),
                    
                    # Gréfico 4
                    html.Div([
                        dcc.Graph(
                            figure=fig3
                        )
                    ])]
                        )
                        ]

                        )
                    ]
                )






# Ligar o servidor
if __name__ == '__main__':
    app.run_server(debug=True)