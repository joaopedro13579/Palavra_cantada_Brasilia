#!/bin/bash

PROJECT_DIR="$(pwd)"

run_torneira() {
    echo "🚰 Iniciando TORNEIRA..."
    node backend/torneira/torneira.js &
}

run_karaoke() {
    echo "🎤 Iniciando KARAOKE..."
    node backend/karaoke/karaoke.js &
}

run_mapa() {
    echo "🗺️ Iniciando MAPA..."
    python3 backend/mapa/mapa.py &
}

run_pomar() {
    echo "🌳 Iniciando POMAR..."
    python3 backend/cocos/pomar.py &
}

run_todos() {
    run_torneira
    run_karaoke
    run_mapa
    run_pomar
}

menu() {
    clear
    echo "======================================="
    echo "  PALAVRA CANTADA BRASÍLIA - CONTROLE"
    echo "======================================="
    echo
    echo "1) Rodar TORNEIRA"
    echo "2) Rodar KARAOKE"
    echo "3) Rodar MAPA"
    echo "4) Rodar POMAR"
    echo "5) Rodar TORNEIRA + KARAOKE"
    echo "6) Rodar TODOS"
    echo "0) Sair"
    echo
    read -p "Escolha uma opção: " opt
}

while true; do
    menu
    case $opt in
        1)
            run_torneira
            ;;
        2)
            run_karaoke
            ;;
        3)
            run_mapa
            ;;
        4)
            run_pomar
            ;;
        5)
            run_torneira
            run_karaoke
            ;;
        6)
            run_todos
            ;;
        0)
            echo "👋 Saindo..."
            exit 0
            ;;
        *)
            echo "❌ Opção inválida"
            ;;
    esac

    echo
    read -p "Pressione ENTER para continuar..."
done
