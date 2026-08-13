#!/usr/bin/env python
# ============================================================================
# watcher.py — VIGIA GENERICO da Ponte IA-a-IA (NYoesyx / IA_Ponte_A_Ponte)
# ----------------------------------------------------------------------------
# Reutilizavel por QUALQUER par de IAs. Nascido da colaboracao Claude+Antigravity
# no projeto Mu/NiagaraForge (2026-07-26). Imune a timing (persiste .seen).
#
# COMO FUNCIONA (padrao "exit-to-wake"):
#   Bloqueia ate' o SEU inbox (o arquivo onde a OUTRA IA escreve p/ voce) ter
#   conteudo NAO PROCESSADO e ENTAO ENCERRA (exit 0). A maioria dos harness de
#   agente RE-INVOCA o agente quando uma task de background termina -> voce acorda
#   reativamente, sem gastar tokens em loop.
#
# USO:
#   python watcher.py <caminho_do_seu_inbox> [segundos_de_poll=3]
#   ex: python watcher.py conversations/claude_inbox.md
#
# REGRA DE OURO: depois de acordar e LER, RE-ARME (rode este script de novo).
#   O vigia e' "tiro unico" por design (encerrar = acordar). Sem re-armar = surdo.
#
# PARAR: crie o arquivo  <inbox>.stop
#
# IMUNE A TIMING: guarda em <inbox>.seen a ultima msg processada. Se uma mensagem
#   chegou enquanto o vigia estava desligado, ao ligar ele detecta NA HORA (nao
#   perde por ter nascido depois da escrita).
# ============================================================================
import os, sys, time

def read(p):
    if not os.path.exists(p):
        return ""
    with open(p, "r", encoding="utf-8", errors="ignore") as f:
        return f.read().replace("\r\n", "\n")

def write(p, s):
    try:
        with open(p, "w", encoding="utf-8") as f:
            f.write(s)
    except Exception as e:
        print(f"[ponte][WARN] nao gravei {p}: {e}")

def main():
    if len(sys.argv) < 2:
        print("uso: python watcher.py <caminho_do_seu_inbox> [poll_segundos]")
        sys.exit(1)
    inbox = sys.argv[1]
    poll = float(sys.argv[2]) if len(sys.argv) > 2 else 3.0
    seen_path = inbox + ".seen"
    stop_path = inbox + ".stop"

    print(f"[ponte] vigia INICIADO — monitorando: {inbox}")
    sys.stdout.flush()

    current = read(inbox)
    seen = read(seen_path)

    # Primeiro arme de todos: adota o estado atual como baseline (nao re-relata o passado).
    if not os.path.exists(seen_path):
        write(seen_path, current)
        seen = current
        print("[ponte] primeiro arme: baseline adotado. Aguardando PROXIMA mensagem...")
        sys.stdout.flush()
    # Mensagem chegou enquanto o vigia estava desligado -> acorda JA'.
    elif current != seen and current.strip() != "":
        print("[ponte] mensagem NAO processada encontrada no start — acordando ja'!")
        write(seen_path, current)
        seen = current
        sys.exit(0)

    # Loop reativo: espera a PROXIMA mudanca real.
    while True:
        try:
            if os.path.exists(stop_path):
                print("[ponte] STOP solicitado — encerrando sem acordar.")
                sys.exit(2)
            time.sleep(poll)
            current = read(inbox)
            if current != seen and current.strip() != "":
                print("[ponte] inbox MUDOU — acordando o agente.")
                write(seen_path, current)
                seen = current
                sys.stdout.flush()
                break
        except Exception:
            time.sleep(poll)

if __name__ == "__main__":
    main()
