import random
import plotly.graph_objects as go
import plotly.io as pio
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

# Lista para armazenar os valores
values = []


# Classe para manipular as requisições HTTP
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Configurar o cabeçalho de resposta
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Gerar o gráfico com a lista de valores atualizada
        fig = go.Figure(data = go.Scatter(y = values))
        graph_html = pio.to_html(fig, full_html = False)

        # Enviar o gráfico como resposta
        self.wfile.write(graph_html.encode('utf-8'))


# Função para atualizar o gráfico com novos valores
def update_graph():
    while True:
        # Gerar um novo valor aleatório
        value = random.randint(1, 100)

        # Adicionar o valor à lista
        values.append(value)


# Função para iniciar o servidor HTTP
def start_server():
    server_address = ('', 56111)
    httpd = HTTPServer(server_address, RequestHandler)
    httpd.serve_forever()


# Iniciar uma thread para atualizar o gráfico
update_thread = threading.Thread(target = update_graph)
update_thread.start()

# Iniciar uma thread para iniciar o servidor HTTP
server_thread = threading.Thread(target = start_server)
server_thread.start()
