#!/bin/sh

echo "Iniciando client... Vou ficar chamando o servidor web a cada 5 segundos."
echo "---------------------------------------------"

# Loop infinito fazendo requisições para o servidor
while true; do
  echo ""
  echo "[CLIENT] Fazendo requisição para http://web:8080 ..."
  # -s = silent, para não imprimir barra de progresso
  curl -s http://web:8080
  echo ""
  echo "---------------------------------------------"
  sleep 5
done
