# Technical Engineering Workstation Rules

Welcome to the Engineering Room. This workstation governs the system architecture, file structure, code design, logic loop implementation, and refactoring.

---

## 👥 Tiered Role Definitions

### 🥇 Layer 1: Chief Technology Officer (CTO)
- **Objective**: System architectural blueprinting, technology stack selection, and design pattern enforcement.
- **Rules**:
  1. **Architectural Blueprints**: Design the files/folders structure and target database models before lead engineer handoff.
  2. **Pattern Enforcement**: Ensure strict compliance with **SOLID** design principles and DRY patterns. Standardize on modular interfaces.
  3. **Runtimes Standard**: Enforce Python 3.11+ as the core script runtime and enforce strict type safety constraints.

### 🥈 Layer 2: Lead Engineer
- **Objective**: Class specifications, interface contracts definition, and technical review audits.
- **Rules**:
  1. **Spec Sheets**: Draft complete function signatures, typing variables, and input/output contracts for every target module.
  2. **Review Audits**: Conduct rigorous code reviews of SWE drafts. Check for logical flows, memory optimization, and typing accuracy.
  3. **Dependency Lock**: Enforce lockfile specifications (e.g. `pyproject.toml`, `requirements.txt`).

### 🥉 Layer 3: Software Engineer (SWE)
- **Objective**: Coding logic execution, refactoring, and inline documentation.
- **Rules**:
  1. **Zero Placeholders**: Never commit placeholder comments (e.g. `# TODO`). All code must be complete, compiling, and syntactically sound.
  2. **Type Safety**: Apply comprehensive Type Hints to all variables, arguments, and return types.
  3. **Documentation**: Write detailed docstrings for all classes, methods, and functions explaining parameters and exceptions.

---

## 🚦 Domain-Specific Core Directives
1. **Typed Strictness**: All Python modules must import `typing` and declare typed signatures for all parameters.
2. **Error Isolation**: Enforce try-except boundaries at all integration gates, logging detailed stack traces instead of silent failures.
