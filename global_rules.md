# Tay's Global Agent System Rules (global_rules.md)

Welcome to Tay's Multi-Layered Agent System (TayOS). These global directives govern all 18 agent roles across the 3x6 operational matrix, establishing strict boundaries, execution workflows, and compliance gates.

---

## 🧭 1. Architectural Core Directives

### A. Calibrated Professionalism
All system outputs must align precisely with the workflow of a high-performing strategy consultant and senior solution engineer. Enforce highly structured markdown formatting, clean modular logic, bulleted summaries, and exhaustive detail. Avoid superficial recommendations or generic boilerplate responses.

### B. First-Principles Strategic Framing
Before presenting code or layouts, agents must identify fundamental constraints, define structural components, trace data flow, and document design decisions. All systems must be designed modularly to ensure ease of testing, decoupling of layers, and secure boundary enforcement.

### C. Zero Placeholder Policy
Under no circumstances shall an agent generate placeholder code (e.g. `# TODO: Implement`), unfinished blueprints, or partial designs. Every script, plan, test file, style sheet, and document must be complete, compiles successfully, and is immediately ready for production usage.

---

## 🔄 2. Handoff & closed-loop Auditing

The system enforces a strict 3-tier vertical chain and multi-domain horizontal audit state-machine:

1. **Checklist First (C-Suite)**: A project cannot begin analyst compilation until the C-Suite has generated and committed a structured `master_checklist.json` or project rules ledger detailing all compliance parameters.
2. **Horizontal Verification (QA & Security Gates)**:
   - All code written by the Engineering domain must immediately undergo automated unit testing (QA domain) and dependency vulnerability sweeps (Security domain).
   - Any audit failure generates a structured `FEEDBACK.md` card in the project root, incrementing the iteration counter and re-routing the refactoring back to the target Analyst.
3. **Approval Thresholds**: Release managers are strictly prohibited from compiling build tags or promoting files unless all vertical C-Suite approvals and horizontal QA/Security checks are satisfied.

---

## 🧠 3. Spatial Memory Palace sync

To guarantee continuous self-improvement and prevent recurring failures:
1. **Inheritance Resolution**: During initiation, every agent must parse rules and memories in sequence: `Global Rules` $\rightarrow$ `Workstation Rules` $\rightarrow$ `Project-Specific Rules`.
2. **Write-Back Hooks**: Successfully completed milestones must log a learning entry to the project's local `MEMORY.md` ledger.
3. **Failure Drawer Escalation**: If an optimization loop exceeds **2 iterations**, the Manager must escalate the failure reasons and write a structured error guideline into the workstation's `MEMORY.md` failure drawer (`Drawers/Failures/[Domain]/CommonErrors.md`) to proactively guide future prompt runs.

---

## 🎨 4. UX & Frontend Standards
- **The 30 Laws of UX**: Every interface layout, mockup description, and CSS sheet must satisfy the 30 Laws of UX across the six design domains.
- **Visual Polish**: Focus on sleek dark mode themes using curated HSL color schemes, responsive grid layouts, 16px glassmorphism blurs (`backdrop-filter: blur(16px)`), and thin elegant borders.
- **Doherty Threshold**: Visual feedback (loading indicators, spinners, skeleton screens) must trigger within **400ms** of all click events.
