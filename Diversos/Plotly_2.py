import random
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
import plotly.graph_objs as go
import plotly.offline as offline


# Classe para manipular as requisições HTTP
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            # Gera um novo valor aleatório
            new_value = random.randint(1, 100)

            # Adiciona o novo valor à lista de valores
            values.append(new_value)

            # Atualiza o gráfico
            update_graph()

            # Envia a resposta HTTP
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes('OK', 'utf-8'))
        elif self.path == '/graph':
            # Envia a resposta HTTP com o gráfico
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(graph_html, 'utf-8'))


# Classe para permitir o uso de threads no servidor HTTP
class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass


# Atualiza o gráfico com a lista de valores atualizada
def update_graph():
    trace = go.Scatter(
        x=list(range(1, len(values) + 1)),
        y=values,
        mode='lines',
        name='Values'
    )
    data = [trace]
    layout = go.Layout(title='Valores Aleatórios', xaxis=dict(title='Iteração'), yaxis=dict(title='Valor'))
    fig = go.Figure(data=data, layout=layout)

    global graph_html
    graph_html = offline.plot(fig, output_type='div')


# Lista para armazenar os valores
values = []

# Gera o gráfico inicial
update_graph()

# Configura e inicia o servidor HTTP
server = ThreadedHTTPServer(('localhost', 56111), RequestHandler)
print('Servidor iniciado na porta 56111')
server.serve_forever()
