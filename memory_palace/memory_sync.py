import os
import re
from typing import Dict, List, Any, Optional

class MemoryPalaceSync:
    def __init__(self, root_dir: str):
        self.root_dir = os.path.abspath(root_dir)
        self.global_rules_path = os.path.join(self.root_dir, "global_rules.md")
        self.global_memory_path = os.path.join(self.root_dir, "MEMORY.md")

    def get_project_paths(self, project_name: str) -> Dict[str, str]:
        """Resolves project paths under the workspace root."""
        project_dir = os.path.join(self.root_dir, "projects", project_name)
        return {
            "dir": project_dir,
            "memory": os.path.join(project_dir, "MEMORY.md"),
            "src": os.path.join(project_dir, "src")
        }

    def load_rules(self, domain: Optional[str] = None, project_name: Optional[str] = None) -> str:
        """
        Loads hierarchical rules:
        Global Rules -> Workstation Domain Rules -> Project Rules (if any)
        """
        rules_chain = []
        
        # 1. Global Rules
        if os.path.exists(self.global_rules_path):
            with open(self.global_rules_path, "r", encoding="utf-8") as f:
                rules_chain.append(f"=== GLOBAL RULES ===\n{f.read()}")

        # 2. Workstation Domain Rules
        if domain:
            workstation_rules = os.path.join(self.root_dir, domain, "workstation_rules.md")
            if os.path.exists(workstation_rules):
                with open(workstation_rules, "r", encoding="utf-8") as f:
                    rules_chain.append(f"=== {domain.upper()} WORKSTATION RULES ===\n{f.read()}")

        # 3. Project specific rules (if any)
        if project_name:
            proj_paths = self.get_project_paths(project_name)
            project_rules = os.path.join(proj_paths["dir"], "project_rules.md")
            if os.path.exists(project_rules):
                with open(project_rules, "r", encoding="utf-8") as f:
                    rules_chain.append(f"=== PROJECT: {project_name.upper()} RULES ===\n{f.read()}")

        return "\n\n".join(rules_chain)

    def load_memory_context(self, domain: Optional[str] = None, project_name: Optional[str] = None) -> str:
        """
        Loads hierarchical memories:
        Global MEMORY.md -> Workstation MEMORY.md -> Project MEMORY.md
        """
        memory_chain = []

        # 1. Global MEMORY
        if os.path.exists(self.global_memory_path):
            with open(self.global_memory_path, "r", encoding="utf-8") as f:
                memory_chain.append(f"=== GLOBAL MEMORY ===\n{f.read()}")

        # 2. Domain Workstation MEMORY
        if domain:
            workstation_mem = os.path.join(self.root_dir, domain, "MEMORY.md")
            if os.path.exists(workstation_mem):
                with open(workstation_mem, "r", encoding="utf-8") as f:
                    memory_chain.append(f"=== {domain.upper()} WORKSTATION MEMORY ===\n{f.read()}")

        # 3. Project MEMORY
        if project_name:
            proj_paths = self.get_project_paths(project_name)
            if os.path.exists(proj_paths["memory"]):
                with open(proj_paths["memory"], "r", encoding="utf-8") as f:
                    memory_chain.append(f"=== PROJECT MEMORY ===\n{f.read()}")

        return "\n\n".join(memory_chain)

    def log_learning(self, project_name: str, domain: str, category: str, content: str, elevate: bool = False):
        """
        Writes a learning point back into the memory system.
        Writes to project MEMORY.md, and optionally elevates to Workstation MEMORY.md.
        """
        proj_paths = self.get_project_paths(project_name)
        os.makedirs(proj_paths["dir"], exist_ok=True)
        
        # 1. Project level write
        proj_memory_file = proj_paths["memory"]
        log_entry = f"\n- **[{category.upper()}]** ({domain}): {content}\n"
        
        if not os.path.exists(proj_memory_file):
            with open(proj_memory_file, "w", encoding="utf-8") as f:
                f.write(f"# Project Memory Palace: {project_name}\n\n## Learnings Ledger\n")
                
        with open(proj_memory_file, "a", encoding="utf-8") as f:
            f.write(log_entry)
            
        print(f"Logged learning to project memory: {proj_memory_file}")

        # 2. Elevation to Workstation
        if elevate:
            workstation_mem = os.path.join(self.root_dir, domain, "MEMORY.md")
            if os.path.exists(workstation_mem):
                with open(workstation_mem, "a", encoding="utf-8") as f:
                    f.write(f"- **[ELEVATED]** (Project: {project_name}): {content}\n")
                print(f"Elevated learning to workstation memory: {workstation_mem}")

    def analyze_work_samples(self, sample_text: str) -> str:
        """
        Heuristic behavioral rules extractor. Inspects user's work samples to formulate guidelines.
        """
        rules = []
        # Look for code styles (e.g. typing, naming, commenting)
        if "def " in sample_text and ":" in sample_text:
            if "-> " in sample_text or "def " in sample_text and any(arg in sample_text for arg in [": int", ": str", ": bool"]):
                rules.append("- Type annotations are heavily preferred for python functions.")
            else:
                rules.append("- Function structures are simple, but type hints should be added for clarity.")
        
        # Look for styling cues
        if "hsl(" in sample_text.lower():
            rules.append("- Styling relies on tailored HSL values for premium aesthetics.")
        if "border-radius" in sample_text.lower() or "backdrop-filter" in sample_text.lower():
            rules.append("- Uses cards with border-radius and glassmorphism elements.")
            
        # Look for planning cues
        if "checklist" in sample_text.lower() or "goals" in sample_text.lower():
            rules.append("- Prefers structured checklist-first validation plans.")

        if not rules:
            rules.append("- Ensure code contains docstrings and minimal decorative elements.")
            
        formatted_rules = "# Extracted Behavioral Principles\n" + "\n".join(rules)
        return formatted_rules

if __name__ == "__main__":
    # Quick verification
    sync = MemoryPalaceSync("C:\\Users\\TaylorGrenawalt\\.gemini\\antigravity\\scratch\\tay-agent-orchestrator")
    print(sync.load_rules("ui_design"))
    sync.log_learning("sample_project", "ui_design", "bug", "Button components should be at least 44px for accessibility.", elevate=True)
