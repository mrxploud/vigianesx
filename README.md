<div align="center">
  <h1>🐝 Vigianesx (VN)</h1>
  <p><b>The Native Cognitive Swarm Operating System.</b></p>
  <p><a href="README-pt.md">🇧🇷 Leia em Português</a></p>
</div>

---

## 🧠 The AI Swarm Paradigm

**Vigianesx (VN)** is the definitive Open-Source Cognitive Swarm Operating System. Originally designed for heavy-duty game development environments in Unreal Engine 5 (NiagaraForge), Vigianesx allows multiple Artificial Intelligences (such as Antigravity, Claude, or Cursor) to collaborate asynchronously, robustly, and with **100% Zero-Python dependency**.

Forget `watcher.py` or hacky polling scripts. Vigianesx natively leverages the AIs' own built-in capabilities (like Antigravity's native `schedule` cron job) to read shared memory through the ultra-dense **DTP (.nesx)** format.

---

## 🌟 Industrial-Grade Features (v4.0)

- **Zero-Python Architecture**: AIs orchestrate themselves by activating native background tools without relying on external host scripts.
- **Anti-Deadlock Mutex (Heartbeat 'AT')**: Secure distributed file locks with Time-to-Live (TTL). If an AI is engaged in a long C++ compilation, it emits an `AT` (Still Working) heartbeat to prevent the Mutex from expiring prematurely.
- **Auto-Close & Auto-Reopen**: Ideal for Unreal Engine on Windows. The AI gracefully closes open processes via PowerShell (`Close-MainWindow`), compiles DLLs without triggering `LNK1104` errors, and automatically reopens the Unreal Editor post-build!
- **The Human Red Button (`*interrupt` / MSG #0)**: Maximum security override. Type `*interrupt` on the Blackboard, and every AI in the swarm immediately aborts compilations and releases locks.
- **Anti-Stagnation Protocol (Proactive Gossip)**: AIs don't get stuck waiting for orders forever. Idleness triggers proactivity: the AIs read the project scope and autonomously assign themselves tasks on the Blackboard.
- **Knowledge Graph (ADRs)**: AIs record their "Architecture Decision Records" indexed by tags in `VigianesxKnowledge.nesx` to build instant, perpetual memory without polluting the git tree.

---

## 🛠️ How to Install and Use (The Drop-in Rule)

Vigianesx is designed for **Zero-Friction**.

1. **Copy the files to the root of your project** (e.g., your Engine or App repository).
2. Open your preferred AI environment (Antigravity, Cursor, etc.).
3. **Send the Magic Prompt to the AI:**
   > *"Analyze the `Vigianesx.nesx` file and activate the Vigianesx protocol."*

The AI will read the portable manifesto, understand the orchestration rules, and **activate its background scheduler automatically**. Repeat this in other windows to allocate more "workers" to your Swarm!

### Swarm Architecture:
- `Vigianesx.nesx` — The Portable Manifesto. The AI reads this to wake up the protocol.
- `VIGIANESX_SPEC_v4.nesx` — The industrial technical conduct rules for the AIs.
- `SwarmState.nesx` — The Blackboard. AIs read the roadmap and create atomic locks here.
- `conversations/` — The directory reserved for AIs to exchange asynchronous messages (e.g., `alpha_inbox.md`, `beta_inbox.md`).
- `bridge_config.nesx` — The P2P polyglot mesh mapping.

---

## 🔗 The NYoesyx (N-OS) Ecosystem
Vigianesx is natively built on top of the **[NYoesyx (N-OS)](https://github.com/mrxploud/nyoesyx)** language and protocol, the first programming language and Operating System designed exclusively for Artificial Intelligences. The high-performance communication of the swarm is made possible by NYoesyx's Dense Token Protocol (DTP).

---

## 🤝 Contributions
Feel free to fork and use Vigianesx as the multi-agent backbone for your project! Rule 6 of the manifesto itself states: *Any AI has the authority to evolve the code and the .nesx format if it encounters latency or friction.*

**Developed by Matheus & Antigravity (Alpha Swarm) 👑⚔️**

---

## ☕ Support the Project

Vigianesx is a pioneering open-source project built with massive effort. If this architecture helped you or your AI team in research or projects, consider supporting the creator!

<a href="https://link.mercadopago.com.br/bytemirage" target="_blank"><img src="https://img.shields.io/badge/Mercado_Pago-00B1EA?style=for-the-badge&logo=mercado-pago&logoColor=white" alt="Donate with Mercado Pago" ></a>

---

<div align="center">
  <i>Built for the future of Autonomous Swarms.</i>
</div>
