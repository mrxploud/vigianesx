<div align="center">
  <h1>🐝 Vigianesx (VN)</h1>
  <p><b>O Sistema Operacional Nativo de Enxame Cognitivo.</b></p>
</div>

---

## 🧠 O Paradigma de Enxame de IA

O **Vigianesx (VN)** é o Sistema Operacional de Enxame Cognitivo Open-Source definitivo. Projetado inicialmente para ambientes de desenvolvimento pesado de jogos na Unreal Engine 5, o Vigianesx permite que múltiplas Inteligências Artificiais (como o Antigravity, Claude, ou Cursor) colaborem de forma assíncrona, robusta e **100% Zero-Python**.

Esqueça `watcher.py` ou scripts de polling gambiarrados. O Vigianesx usa os próprios recursos nativos das IAs (como o cron nativo `schedule` do Antigravity) para ler a memória compartilhada no formato ultradenso **DTP (.nesx)**.

---

## ⚖️ Por que usar Vigianesx vs. Agentes de IA Convencionais?

**Quando usar Agentes de IA Convencionais (Individuais):**
Use um agente de IA padrão quando sua tarefa for linear, localizada ou envolver um único domínio. Se você precisa refatorar um único script, escrever um teste unitário ou buscar na web por um erro, um agente convencional é perfeito.

**Quando usar o Vigianesx (O Enxame):**
Use o Vigianesx quando o seu projeto escalar além de uma única janela de contexto ou exigir **expertise de domínio em paralelo**.
- **Compilação e Codificação Paralela**: Enquanto o *Agente A* está preso compilando um módulo gigantesco de C++ da Unreal Engine (o que trava o terminal por 5 minutos), o *Agente B* pode estar escrevendo a documentação ou corrigindo um bug de UI em uma branch separada simultaneamente.
- **Cross-Checking e Code Review**: As IAs alucinam. Em um enxame Vigianesx, você pode configurar o *Agente A* como Desenvolvedor Sênior e o *Agente B* como Revisor/QA. Eles revisam o código um do outro assincronamente usando o Blackboard, reduzindo drasticamente os bugs antes mesmo de você olhar para o código.
- **Orquestração de Ambientes Complexos**: Gerenciar grandes codebases onde alterar uma mecânica central exige atualizar o frontend, o backend e as tabelas do banco de dados ao mesmo tempo, sem que uma IA atropele o arquivo da outra (graças aos nossos Locks Atômicos Mutex).

---

## 🌟 Recursos de Nível Industrial (v4.0)

- **Arquitetura Zero-Python**: IAs orquestram a si mesmas ativando ferramentas nativas em background, sem depender de scripts externos.
- **Mutex Anti-Deadlock (Heartbeat 'AT')**: Bloqueios de arquivo distribuídos com Time-to-Live (TTL). Se a IA estiver em um *build* demorado de C++, ela emite o heartbeat `AT` (Ainda Trabalhando) para evitar que o Mutex expire prematuramente.
- **Auto-Close & Auto-Reopen**: Ideal para Unreal Engine no Windows. A IA fecha processos abertos graciosamente via PowerShell (`Close-MainWindow`), compila DLLs sem gerar erro `LNK1104` e, automaticamente, reabre o Unreal Editor pós-compilação!
- **Botão Vermelho Humano (`*interrupt` / MSG #0)**: Override de segurança máxima. Digite `*interrupt` no Blackboard, e todas as IAs do enxame abortarão compilações e liberarão os locks instantaneamente.
- **Protocolo Anti-Estagnação (Proactive Gossip)**: IAs não ficam presas esperando ordens para sempre. A ociosidade dispara a proatividade: as próprias IAs leem o escopo do projeto e se auto-atribuem tarefas no Blackboard.
- **Grafo de Conhecimento (ADRs)**: As IAs gravam suas "Decisões Arquiteturais" indexadas por tags em `VigianesxKnowledge.nesx` para construir uma memória perpétua instantânea sem poluir a árvore do git.

---

## 🛠️ Como Instalar e Usar (A Regra do Drop-in)

O Vigianesx foi projetado para ter **Zero-Friction**.

1. **Copie os arquivos para a raiz do seu projeto** (por exemplo, na raiz do repositório da sua Engine ou App).
2. Abra seu ambiente de IA preferido (Antigravity, Cursor, etc.).
3. **Mande o Prompt Mágico para a IA:**
   > *"Analise o arquivo `Vigianesx.nesx` e ative o protocolo Vigianesx."*

A IA lerá o manifesto portátil, entenderá as regras de orquestração e **ativará o agendador de background automaticamente**. Repita em outras janelas para alocar mais "operários" no seu Enxame!

### Estrutura do Enxame:
- `Vigianesx.nesx` — O Manifesto Portátil. A IA lê para acordar o protocolo.
- `VIGIANESX_SPEC_v4.nesx` — As regras de conduta técnica industrial das IAs.
- `SwarmState.nesx` — O Blackboard. As IAs leem o roadmap e criam Locks atômicos aqui.
- `conversations/` — Pasta reservada para as IAs trocarem suas mensagens assíncronas (ex: `alpha_inbox.md`, `beta_inbox.md`).
- `bridge_config.nesx` — O mapeamento da malha poliglota P2P.

---

## 🔗 Ecossistema NYoesyx (N-OS)
O Vigianesx é construído nativamente sobre a linguagem e o protocolo **[NYoesyx (N-OS)](https://github.com/mrxploud/nyoesyx)**, a primeira linguagem de programação e Sistema Operacional desenhado exclusivamente para Inteligências Artificiais. A comunicação de alta performance do enxame é possível graças ao Dense Token Protocol (DTP) do NYoesyx.

---

## 🤝 Contribuições
Sinta-se livre para dar um Fork e usar o Vigianesx como a espinha dorsal de multi-agentes para o seu projeto! A própria regra 6 do manifesto diz: *Qualquer IA tem a autoridade para evoluir o código e o formato .nesx se encontrar latência ou fricção.*

**Desenvolvido por Matheus & Antigravity (Alpha Swarm) 👑⚔️**

---

## ☕ Apoie o Projeto

O Vigianesx é um projeto *open-source* pioneiro construído com muito esforço. Se essa arquitetura ajudou você ou sua equipe de IAs em pesquisas ou projetos, considere apoiar o criador!

<a href="https://link.mercadopago.com.br/bytemirage" target="_blank"><img src="https://img.shields.io/badge/Mercado_Pago-00B1EA?style=for-the-badge&logo=mercado-pago&logoColor=white" alt="Doar via Mercado Pago" ></a>

---

<div align="center">
  <i>Construído para o futuro dos Enxames Autônomos.</i>
</div>
