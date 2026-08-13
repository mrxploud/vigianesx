# 🐝 Vigianesx (VN) - The Native Cognitive Swarm OS

**Vigianesx (VN)** é o Sistema Operacional de Enxame Cognitivo Open-Source definitivo. Projetado inicialmente para ambientes de desenvolvimento pesado de jogos na Unreal Engine 5 (NiagaraForge), o Vigianesx permite que múltiplas Inteligências Artificiais (como o Antigravity, Claude, ou Cursor) colaborem de forma assíncrona, robusta e **100% Zero-Python**.

Esqueça `watcher.py` ou scripts de polling gambiarrados. O Vigianesx usa os próprios recursos nativos das IAs (como o cron nativo `schedule` do Antigravity) para ler a memória compartilhada no formato **DTP (.nesx)**.

---

## 🌟 Recursos de Nível Industrial (v4.0)

- **Zero-Python**: IAs orquestram a si mesmas ativando ferramentas nativas em background sem scripts dependentes externos.
- **Mutex Anti-Deadlock (Heartbeat 'AT')**: Bloqueios de arquivo seguros com Time-to-Live (TTL). Se a IA estiver em um *build* demorado de C++, ela emite o heartbeat `AT` (Ainda Trabalhando) para evitar que o Mutex expire prematuramente.
- **Auto-Close & Auto-Reopen de Processos**: Ideal para Unreal Engine no Windows. A IA fecha processos abertos graciosamente no PowerShell (`Close-MainWindow`), compila DLLs sem gerar erro `LNK1104` e, automaticamente, reabre o Unreal Editor pós-compilação!
- **Botão Vermelho (`*interrupt` / MSG #0)**: Override de segurança máxima. Digite `*interrupt` no Blackboard e todas as IAs em qualquer canto cancelam compilações e abortam a execução instantaneamente.
- **Protocolo Anti-Estagnação (Proactive Gossip)**: IAs não ficam presas esperando ordens para sempre. A ociosidade dispara a proatividade, onde as próprias IAs leem o escopo e se auto-atribuem tarefas no Blackboard.
- **Grafo de Conhecimento (ADRs)**: As IAs gravam suas "Decisões Arquiteturais" indexadas por tags em `VigianesxKnowledge.nesx` para construir uma memória perpétua instantânea sem poluir a árvore do git.

---

## 🛠️ Como Instalar e Usar (A Regra do Drop-in)

O Vigianesx foi projetado para **Zero-Friction**.

1. **Copie os arquivos para a raiz do seu projeto** (por exemplo, na raiz do repositório da sua Engine ou App).
2. Abra seu ambiente de IA preferido (Antigravity, Cursor, etc.).
3. **Mande o Prompt Mágico para a IA:**
   > *"Analise o arquivo `Vigianesx.nesx` e ative o protocolo Vigianesx."*

A IA lerá o manifesto portátil, entenderá as regras de orquestração e **ativará o agendador de background automaticamente**. Repita em outras janelas para alocar mais "operários" no seu Enxame!

### Estrutura do Enxame:
- `Vigianesx.nesx` — O Manifesto Portátil. A IA lê e acorda o protocolo.
- `VIGIANESX_SPEC_v4.nesx` — As regras de conduta técnica industrial das IAs.
- `SwarmState.nesx` — O Blackboard. As IAs leem o roadmap e criam Locks atômicos aqui.
- `conversations/` — Pasta reservada para as IAs trocarem suas mensagens assíncronas (ex: `alpha_inbox.md`, `beta_inbox.md`).
- `bridge_config.nesx` — O mapeamento da malha poliglota P2P.

## 🔗 Ecossistema NYoesyx (N-OS)
O Vigianesx é construído nativamente sobre a linguagem e o protocolo **[NYoesyx (N-OS)](https://github.com/mrxploud/nyoesyx)**, a primeira linguagem de programação e Sistema Operacional desenhado exclusivamente para Inteligências Artificiais. A comunicação de alta performance do enxame é possível graças ao Dense Token Protocol (DTP) do NYoesyx.

---

## 🤝 Contribuições
Sinta-se livre para dar um Fork e usar o Vigianesx como a espinha dorsal de multi-agentes para o seu projeto! A própria regra 6 do manifesto diz: *Qualquer IA tem a autoridade para evoluir o código e o formato .nesx se encontrar latência ou fricção.*

**Desenvolvido por Matheus & Antigravity (Alpha Swarm) 👑⚔️**
