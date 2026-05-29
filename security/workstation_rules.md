# Security & Protection Workstation Rules

## Layer Roles
- **C-Suite (Chief Information Security Officer)**: Formulates security profiles, risk tolerance, and access control policies.
- **Manager (Security Lead)**: Conducts threat modeling, verifies dependency lists, and schedules scans.
- **Analyst (SecOps Analyst)**: Performs SAST analysis, runs secret scanners, and executes sandbox tests.

## Domain Specific Guidelines
1. Never hardcode credentials, tokens, or private keys.
2. Enforce input sanitization at boundary layers.
3. Run automated dependency vulnerability checks during build phases.
