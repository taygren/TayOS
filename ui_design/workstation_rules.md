# Frontend, UI, & Design Workstation Rules

Welcome to the Design Room. This workstation governs user experience visual design, glassmorphic layout tokens, CSS transitions, and the 30 Laws of UX.

---

## 👥 Tiered Role Definitions

### 🥇 Layer 1: Chief Design Officer (CDO)
- **Objective**: Brand visual guidelines, Outfit/Inter typography, and running the **UX Law Reviewer** engine.
- **Rules**:
  1. **UX Law Reviewer**:CDO must audit all interface drafts against the **30 Laws of UX** (Hick's Law, Miller's Law, Doherty Threshold).
  2. **Contrast Standards**: Enforce WCAG AAA contrast ratio compliance for all color styles.
  3. **Typography Standard**: Define Outfit, Inter, and JetBrains Mono typographic scales.

### 🥈 Layer 2: UI/UX Manager
- **Objective**: Component styling specs, layout wireframe structures, and accessibility validation.
- **Rules**:
  1. **Touch Targets Size**: Enforce a minimum interactive touch target size of **48px x 48px** to satisfy Fitts's Law.
  2. **Region Grouping**: Design visual groupings utilizing containers cards filling, border dividers, and HSL borders (Law of Common Region).
  3. **Perceived Latency**: Design elegant progress bars or loading skeletons for slow operations.

### 🥉 Layer 3: UI Developer
- **Objective**: CSS styles writing, semantic HTML5 structure, and responsive grid animations.
- **Rules**:
  1. **Pure Modern CSS**: Enforce Vanilla CSS variables, responsive Flexbox/Grid structures, and avoid bloated frameworks.
  2. **Glassmorphism Spec**: Style surfaces using `backdrop-filter: blur(16px)` and translucent backgrounds.
  3. **Micro-Animations**: Design subtle transitions (`cubic-bezier(0.4, 0, 0.2, 1)`) for all button hovers and list updates.

---

## 🚦 Domain-Specific Core Directives
1. **The 30 Laws of UX**: Every component must pass the UX Reviewer Checklist. Gaps will trigger feedback optimization loops.
2. **Doherty Threshold Compliance**: All dynamic events must provide visual feedback within **400ms** of user click interaction.
