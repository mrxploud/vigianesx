#!/usr/bin/env python3
# ============================================================================
# nyoesyx-bridge.py — CLI ORQUESTRADOR DO VIGIANESX (VN) | NYoesyx Swarm OS
# ----------------------------------------------------------------------------
# Implementação MVP (Pilar 1: Opcodes & Pilar 6: Broadcast / Roteamento)
# Batizado oficialmente por Matheus S. Barros | Ponte IA-a-IA (Vigianesx)
# ============================================================================
import os
import sys
import re
import time

BRIDGE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BRIDGE_DIR, "bridge_config.nesx")
STATE_PATH = os.path.join(BRIDGE_DIR, "SwarmState.nesx")

def read_file(path):
    if not os.path.exists(path):
        return ""
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read().replace("\r\n", "\n")

def write_file(path, content):
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)

def parse_config():
    content = read_file(CONFIG_PATH)
    config = {}
    for line in content.splitlines():
        line = line.strip()
        if line.startswith("*set "):
            parts = line[5:].split(maxsplit=1)
            if len(parts) == 2:
                config[parts[0]] = parts[1].strip('"')
    return config

def cmd_send(peer_name, subject, payload):
    config = parse_config()
    target_inbox = None
    peer_clean = peer_name.lower().replace("antigravity-", "")
    
    if "alpha" in peer_clean or peer_clean == "a":
        target_inbox = config.get("agent.a.inbox", "alpha_inbox.md")
        recipient = config.get("agent.a.name", "Antigravity-Alpha")
    elif "beta" in peer_clean or peer_clean == "b":
        target_inbox = config.get("agent.b.inbox", "beta_inbox.md")
        recipient = config.get("agent.b.name", "Antigravity-Beta")
    else:
        target_inbox = f"{peer_clean}_inbox.md"
        recipient = peer_name

    inbox_path = os.path.join(BRIDGE_DIR, target_inbox)
    current_content = read_file(inbox_path)
    
    # Count existing MSG numbers
    matches = re.findall(r"MSG #(\d+)", current_content)
    next_num = max([int(m) for m in matches] + [0]) + 1
    
    sender = "Antigravity-CLI"
    msg_header = f"MSG #{next_num} — <{sender}> -> <{recipient}> | {subject}"
    formatted_msg = f"\n---\n\n{msg_header}\n\n{payload}\n"
    
    write_file(inbox_path, current_content.rstrip() + formatted_msg)
    print(f"[nyoesyx-bridge] Mensagem enviada com sucesso para {recipient} em {target_inbox} (MSG #{next_num}).")

def cmd_status():
    content = read_file(STATE_PATH)
    if not content:
        print("[nyoesyx-bridge][ERRO] SwarmState.nesx não encontrado!")
        return

    print("====================================================================")
    print("      NYOESYX SWARM OS — DASHBOARD DO ENXAME COGNITIVO             ")
    print("====================================================================")
    
    # Metadata
    swarm_id = re.search(r'\*set swarm\.id "(.*?)"', content)
    status = re.search(r'\*set swarm\.status "(.*?)"', content)
    last_sync = re.search(r'\*set swarm\.last_sync "(.*?)"', content)
    print(f" ID do Enxame : {swarm_id.group(1) if swarm_id else 'N/A'}")
    print(f" Status       : {status.group(1) if status else 'N/A'}")
    print(f" Última Sync  : {last_sync.group(1) if last_sync else 'N/A'}")
    print("--------------------------------------------------------------------")
    
    # Agents
    print(" [ AGENTES ONLINE ]")
    agents_block = re.search(r'\*block agents(.*?)\*end block', content, re.DOTALL)
    if agents_block:
        agents = re.findall(r'\*agent (.*?)\n.*?: "(.*?)".*?: "(.*?)".*?: "(.*?)".*?: "(.*?)"', agents_block.group(1), re.DOTALL)
        for ag in agents:
            print(f"  * {ag[0].strip():<6} | Window: {ag[2]:<8} | Status: {ag[3]:<22} | Focus: {ag[4][:40]}")
    print("--------------------------------------------------------------------")

    # Locks
    print(" [ MUTEX & DISTRIBUTED LOCKS ]")
    locks_block = re.search(r'\*block locks(.*?)\*end block', content, re.DOTALL)
    if locks_block:
        for line in locks_block.group(1).splitlines():
            line = line.strip()
            if line.startswith("*lock "):
                print(f"  {line}")
    print("--------------------------------------------------------------------")

    # Tasks
    print(" [ ROADMAP & TAREFAS ATIVAS ]")
    tasks_block = re.search(r'\*block tasks(.*?)\*end block', content, re.DOTALL)
    if tasks_block:
        tasks = re.findall(r'\*task (.*?)\n\s+title: "(.*?)"\n\s+assignee: "(.*?)"\n\s+status: "(.*?)"', tasks_block.group(1))
        for t in tasks:
            status_symbol = "OK" if "COMPLETED" in t[3] else (">>" if "IN_PROGRESS" in t[3] else "--")
            print(f"  [{status_symbol}] {t[0]:<8} | {t[3]:<11} | {t[2]:<17} | {t[1]}")
    print("====================================================================")

def cmd_lock(filepath, owner="Beta"):
    content = read_file(STATE_PATH)
    # Match any lock line targeting this filepath
    pattern = rf'(\*lock "(?:.*?{re.escape(os.path.basename(filepath))})" \| )".*?" \| ".*?" \| ".*?"'
    replacement = rf'\1"{owner}" | "{time.strftime("%Y-%m-%dT%H:%M:%S")}" | "ACTIVE"'
    new_content, count = re.subn(pattern, replacement, content, flags=re.IGNORECASE)
    if count > 0:
        write_file(STATE_PATH, new_content)
        print(f"[nyoesyx-bridge] Mutex adquirido com sucesso para {filepath} por {owner}.")
    else:
        # Append lock if not existing
        new_lock = f'  *lock "{filepath}" | "{owner}" | "{time.strftime("%Y-%m-%dT%H:%M:%S")}" | "ACTIVE"\n*end block'
        new_content = content.replace("*end block", new_lock, 1) if "*block locks" in content else content
        write_file(STATE_PATH, new_content)
        print(f"[nyoesyx-bridge] Novo Mutex criado e adquirido para {filepath} por {owner}.")

def cmd_unlock(filepath):
    content = read_file(STATE_PATH)
    pattern = rf'(\*lock "(?:.*?{re.escape(os.path.basename(filepath))})" \| )".*?" \| ".*?" \| ".*?"'
    replacement = rf'\1"UNLOCKED" | "-" | "FREE"'
    new_content, count = re.subn(pattern, replacement, content, flags=re.IGNORECASE)
    if count > 0:
        write_file(STATE_PATH, new_content)
        print(f"[nyoesyx-bridge] Mutex liberado (UNLOCKED/FREE) para {filepath}.")
    else:
        print(f"[nyoesyx-bridge][WARN] Nenhum lock encontrado para {filepath}.")

def main():
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except AttributeError:
        pass
    if len(sys.argv) < 2:
        print("Uso: nyoesyx-bridge.py <comando> [argumentos...]")
        print("Comandos disponíveis:")
        print("  send <peer> <subject> <payload>")
        print("  status")
        print("  lock <filepath> [owner]")
        print("  unlock <filepath>")
        sys.exit(1)

    cmd = sys.argv[1].lower()
    if cmd == "status":
        cmd_status()
    elif cmd == "send" and len(sys.argv) >= 5:
        cmd_send(sys.argv[2], sys.argv[3], sys.argv[4])
    elif cmd == "lock" and len(sys.argv) >= 3:
        owner = sys.argv[3] if len(sys.argv) > 3 else "Beta"
        cmd_lock(sys.argv[2], owner)
    elif cmd == "unlock" and len(sys.argv) >= 3:
        cmd_unlock(sys.argv[2])
    else:
        print(f"[nyoesyx-bridge][ERRO] Comando ou argumentos inválidos para '{cmd}'.")
        sys.exit(1)

if __name__ == "__main__":
    main()
