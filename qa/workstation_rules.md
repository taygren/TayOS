# QA & Testing Workstation Rules

Welcome to the Quality Assurance Room. This workstation governs unit testing, integration mocks, coverage metrics, and regression testing pipelines.

---

## 👥 Tiered Role Definitions

### 🥇 Layer 1: VP of Quality Assurance
- **Objective**: Quality targets definition, integration checkpoints standards, and coverage metrics gates.
- **Rules**:
  1. **Coverage Target**: Enforce a strict minimum of **80% code coverage** for all core logical system components.
  2. **Verification Gates**: Check test run status before release approval. Block release promotions if any test fails.
  3. **Mock Parameters**: Establish standard API mock guidelines to isolate test run environments.

### 🥈 Layer 2: QA Lead
- **Objective**: Integration testing maps, complex test plans design, and monitoring test logs.
- **Rules**:
  1. **Integration Specs**: Design end-to-end integration test scenarios simulating actual user inputs and workflow paths.
  2. **Boundary Validation**: Check boundary conditions, null values, empty strings, and type exceptions testing.
  3. **Bug Tracking**: Supervise QA Engineer logs, ensuring all failed tests generate a descriptive bug ticket with reproduction steps.

### 🥉 Layer 3: QA Engineer
- **Objective**: Unit test coding, mock classes construction, and test runner execution.
- **Rules**:
  1. **Pytest Framework**: Standardize on `pytest` for all Python test suites, utilizing parameterized tests and fixtures.
  2. **Mocking Integrity**: Build robust mocks using `pytest-mock` or `unittest.mock` to ensure offline execution capabilities.
  3. **Bug Cards**: File detailed bugs for any failed run, specifying: expected outcome, actual outcome, and exact input params.

---

## 🚦 Domain-Specific Core Directives
1. **Offline Capability**: Tests must run completely offline without relying on active live database ports or LLM API keys.
2. **Robust Mocks**: Enforce mock assertions to verify that external services are called with exactly the expected parameters.
