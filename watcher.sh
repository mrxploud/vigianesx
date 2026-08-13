#!/usr/bin/env bash
# ============================================================================
# watcher.sh — VIGIA GENERICO da Ponte IA-a-IA (versao Bash, p/ agentes tipo
# Claude Code que rodam sh). Paridade com watcher.py: imune a timing (.seen),
# tiro-unico (encerrar = acordar), parada por .stop.
#
# USO:  bash watcher.sh <caminho_do_seu_inbox> [poll_segundos=3]
#   ex: bash watcher.sh "D:/.../SwarmBridge/claude_inbox.md"
#
# REGRA DE OURO: RE-ARME (rode de novo) toda vez que acordar e ler. Senao, surdo.
# PARAR: crie o arquivo  <inbox>.stop
# ============================================================================
set -u
INBOX="${1:-}"
POLL="${2:-3}"
[ -z "$INBOX" ] && { echo "uso: bash watcher.sh <inbox> [poll]"; exit 1; }
SEEN="${INBOX}.seen"
STOP="${INBOX}.stop"

# garante que o inbox exista p/ o cmp nao falhar
[ -f "$INBOX" ] || : > "$INBOX"

echo "[ponte] vigia INICIADO — monitorando: $INBOX"

if [ ! -f "$SEEN" ]; then
  # primeiro arme: baseline = estado atual (nao re-relata o passado)
  cp "$INBOX" "$SEEN" 2>/dev/null
  echo "[ponte] primeiro arme: baseline adotado. Aguardando PROXIMA mensagem..."
elif ! cmp -s "$INBOX" "$SEEN"; then
  # msg chegou enquanto o vigia estava desligado -> acorda ja'
  cp "$INBOX" "$SEEN" 2>/dev/null
  echo "[ponte] mensagem NAO processada no start — acordando ja'!"
  exit 0
fi

while :; do
  if [ -f "$STOP" ]; then echo "[ponte] STOP solicitado."; exit 2; fi
  if ! cmp -s "$INBOX" "$SEEN" 2>/dev/null; then
    cp "$INBOX" "$SEEN" 2>/dev/null
    echo "[ponte] inbox MUDOU — acordando o agente."
    exit 0
  fi
  sleep "$POLL"
done
