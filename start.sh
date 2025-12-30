#!/bin/bash

BASE_DIR="/home/joao-pedro/PALAVRA_CANTADA_BRASILIA"
SERVICE_NAME="palavra_cantada_auto"
SERVICE_FILE="/etc/systemd/system/${SERVICE_NAME}.service"

echo "=============================="
echo " PALAVRA CANTADA BRASILIA "
echo "=============================="
echo "Escolha o programa para iniciar no boot:"
echo ""
echo "1) Mapa"
echo "2) Karaoke"
echo "3) Torneira"
echo ""
read -p "Digite a opção: " OPTION

case $OPTION in
  1)
    CMD="python3 $BASE_DIR/backend/mapa/mapa.py"
    ;;
  2)
    CMD="node $BASE_DIR/backend/karaoke/karaoke.js"
    ;;
  3)
    CMD="node $BASE_DIR/backend/torneira/torneira.js"
    ;;
  *)
    echo "Opção inválida"
    exit 1
    ;;
esac

echo "Criando serviço systemd..."

sudo bash -c "cat > $SERVICE_FILE" <<EOF
[Unit]
Description=Palavra Cantada - Auto
After=network.target sound.target

[Service]
Type=simple
User=joao-pedro
WorkingDirectory=$BASE_DIR
ExecStart=$CMD
Restart=always
RestartSec=2
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
EOF

echo "Registrando serviço..."
sudo systemctl daemon-reload
sudo systemctl enable ${SERVICE_NAME}.service

echo ""
echo "Serviço criado e habilitado:"
echo "  ${SERVICE_NAME}.service"
echo ""
echo "Reiniciando em 5 segundos..."
sleep 5
sudo reboot
