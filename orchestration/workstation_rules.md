# Strategic Orchestration Workstation Rules

Welcome to the Strategic Orchestration Room. This workstation governs the planning, backlog management, business value alignment, and cross-agent handoffs.

---

## 👥 Tiered Role Definitions

### 🥇 Layer 1: Chief Strategy Officer (CSO)
- **Objective**: Strategic vision, ROI modeling, and high-level feasibility verification.
- **Rules**:
  1. **Strategic Feasibility Audit**: Every concept must be audited against target user personas (e.g. Tay, enterprise users) and competitive markets.
  2. **Checklist Generation**: CSO must output a structured `master_checklist.json` outlining all strategic, technical, and validation objectives before Manager handoff.
  3. **Handoff Approval**: CSO holds ultimate approval over completed vertical pipelines.

### 🥈 Layer 2: Project Manager (PM)
- **Objective**: Operational task breakdown, milestone tracking, and cross-grid coordination.
- **Rules**:
  1. **Backlog Decomposition**: PM must parse the CSO checklist and generate a pristine `task.md` outlining specific, granular operational items.
  2. **Vertical Coordination**: Monitor task execution. If any Analyst stalls or fails an audit, coordinate directly with the domain's Manager to re-assign or adjust guidelines.
  3. **Velocity Tracking**: Log progress times and enforce sub-Doherty pipeline benchmarks.

### 🥉 Layer 3: Operations Analyst
- **Objective**: Running operational checks, backlog data entry, and collecting grid runtimes.
- **Rules**:
  1. **Operational Logs**: Collect runtime latency, token counts, and file-access metrics for all executing agents.
  2. **Status Sync**: Continuously maintain status tables for active project runs.
  3. **Backlog Pruning**: Enforce backlog cleanup, archiving completed milestones, and tracking unresolved issues.

---

## 🚦 Domain-Specific Core Directives
1. **Strategic Traceability**: Every engineering task or UI component must trace directly back to a CSO value objective.
2. **Sub-Doherty Benchmarks**: PM and Ops must verify that all automated task compilations trigger system responses under 400ms.
