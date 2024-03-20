# dash 라이브러리를 import합니다.
import dash
# dash의 그래프 관련 기능을 사용하기 위해 import합니다.
import dash_core_components as dcc
import dash_html_components as html

# 애플리케이션을 생성합니다.
app = dash.Dash(__name__)

# 그래프의 데이터를 정의합니다.
data = {'x': [1, 2, 3, 4, 5], 'y': [1, 3, 2, 4, 5]}

# 애플리케이션의 레이아웃을 정의합니다.
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),  # H1 태그를 사용하여 텍스트를 출력합니다.
    dcc.Graph(  # 그래프를 생성합니다.
        id='example-graph',
        figure={
            'data': [
                {'x': data['x'], 'y': data['y'],
                    'type': 'line', 'name': 'data'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'  # 그래프의 제목을 설정합니다.
            }
        }
    )
])

# 애플리케이션을 실행합니다.
if __name__ == '__main__':
    app.run_server(debug=True)
