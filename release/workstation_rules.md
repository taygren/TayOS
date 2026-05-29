# Release Management Workstation Rules

## Layer Roles
- **C-Suite (VP of Release)**: Schedules release gates, rollback triggers, and approves production flags.
- **Manager (Release Manager)**: Oversees build scripts, manages Git tagging, and constructs changelogs.
- **Analyst (DevOps Analyst)**: Runs build scripts, containerizes apps, and verifies deployment health.

## Domain Specific Guidelines
1. Automate release steps to minimize human error.
2. Always prepare a rollback playbook before major deployments.
3. Perform post-deployment smoke tests to ensure service uptime.
