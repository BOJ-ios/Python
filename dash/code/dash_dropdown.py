from dash import Dash, dcc, html, Input, Output, callback

app = Dash(__name__)
app.layout = html.Div([
    dcc.Dropdown(options=[{'label': '서울', 'value': '서울'}, {'label': '부산', 'value': '부산'}, {
                 'label': '울산', 'value': '울산'}], value='부산', id='demo-dropdown'),
    html.Button('Click me', id='button'),
    html.Div(id='select'),
    html.Div(id='select2')
])


@app.callback(
    [Output('select', 'children'),
     Output('select2', 'children')],
    [Input('demo-dropdown', 'value'),
     Input('button', 'n_clicks')]
)
def update_output(value, n_clicks):
    return f'선택된 도시: {value}', f'버튼이 {n_clicks}번 클릭 되었습니다.'


if __name__ == '__main__':
    app.run_server(debug=True)
