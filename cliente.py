

import grpc

import saudacao_pb2
import saudacao_pb2_grpc

def executar_cliente():
    with grpc.insecure_channel('localhost:50051') as channel:

        stub = saudacao_pb2_grpc.SaudadorStub(channel)
        
        print("--- Cliente gRPC irá chamar o método DizerOla ---")
        
        solicitacao = saudacao_pb2.SolicitacaoOla(nome="Mundo")
        
        resposta = stub.DizerOla(solicitacao)
        
        print(f"Resposta do servidor: '{resposta.mensagem}'")

if __name__ == '__main__':
    executar_cliente()