from concurrent import futures
import time
import grpc

import saudacao_pb2
import saudacao_pb2_grpc

class ServicoSaudador(saudacao_pb2_grpc.SaudadorServicer):
    
    def DizerOla(self, request, context):
        print(f"Recebi uma solicitação de {request.nome}")
        mensagem_resposta = f"Olá, {request.nome}!"
        return saudacao_pb2.RespostaOla(mensagem=mensagem_resposta)


def iniciar_servidor():
    servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    saudacao_pb2_grpc.add_SaudadorServicer_to_server(ServicoSaudador(), servidor)
    
    print("Iniciando servidor na porta 50051...")
    servidor.add_insecure_port('[::]:50051')
    servidor.start()
    
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        print("Parando o servidor...")
        servidor.stop(0)

if __name__ == '__main__':
    iniciar_servidor()