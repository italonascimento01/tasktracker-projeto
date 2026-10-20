# Imagem base enxuta: traz o Python 3.11 sem pacotes desnecessarios,
# o que reduz bastante o tamanho final da imagem.
FROM python:3.11-slim

# Pasta de trabalho dentro do container. Todos os comandos seguintes
# sao executados a partir dela.
WORKDIR /app

# Garante que o print() apareca na hora no terminal, sem ficar preso
# no buffer de saida. Sem isso, uma aplicacao interativa como esta
# poderia exibir o menu so depois que o usuario digitasse algo.
ENV PYTHONUNBUFFERED=1

# Copia o codigo-fonte da maquina local para dentro da imagem.
COPY src/ /app/src/

# Comando disparado quando o container sobe.
CMD ["python", "src/main.py"]
