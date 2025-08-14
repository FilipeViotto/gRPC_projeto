proto:
	@echo "Gerando código a partir de saudacao.proto..."
	python3 -m grpc_tools.protoc \
		-I. \
		--python_out=. \
		--pyi_out=. \
		--grpc_python_out=. \
		saudacao.proto
	@echo "Código gRPC gerado com sucesso!"

.PHONY: proto
