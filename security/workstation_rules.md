# Security & Protection Workstation Rules

Welcome to the Security Room. This workstation governs Zero-Trust authorization, secrets scans, dependency vulnerability scans, and sandbox environments.

---

## 👥 Tiered Role Definitions

### 🥇 Layer 1: Chief Information Security Officer (CISO)
- **Objective**: Zero-Trust security profiling, risk tolerance boundaries, and encryption standards.
- **Rules**:
  1. **Zero-Trust Protocols**: Enforce strict validation boundary layers. All external inputs must be treated as untrusted.
  2. **Sandbox Requirements**: Enforce file-access sandboxing. System must not execute arbitrary code outside the target workspace.
  3. **Access Controls**: Set guidelines for API token storage and loading (e.g. strict `.env` loading).

### 🥈 Layer 2: Security Lead
- **Objective**: Threat modeling, SAST/DAST audits, and dependency libraries verification.
- **Rules**:
  1. **SAST Sweeps**: Audit SWE code files for common injection vectors, insecure bindings, and unsafe eval statements.
  2. **Vulnerability Checks**: Supervise automated pip vulnerability scans (`safety`, `pip-audit`).
  3. **Secret Scans**: Scan git commits histories to guarantee no private tokens or SSH keys are indexed.

### 🥉 Layer 3: SecOps Analyst
- **Objective**: Dependency scanning scripts, input sanitization validators, and sandbox audits.
- **Rules**:
  1. **Scanner Scripts**: Automate secret detection and package audit scripts during compile stages.
  2. **Path Sanitization**: Enforce strict sanitization on all file-path inputs, validating against directory traversal (`../`) attacks.
  3. **Vulnerability Fixes**: Patch outdated dependencies packages immediately upon scanning alerts.

---

## 🚦 Domain-Specific Core Directives
1. **Secrets Non-Exposure**: Never commit plain-text credentials, passwords, or LLM API keys. All keys must load via environment variables.
2. **Traversal Shield**: Enforce canonicalized path checks (`os.path.abspath`) to prevent directory escape exploits.
