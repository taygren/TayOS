import os
import sys
import argparse
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.syntax import Syntax

# Local imports
from ui_design.ux_reviewer import UXLawReviewer, LAWS_OF_UX
from memory_palace.memory_sync import MemoryPalaceSync

console = Console()

class AgentOrchestratorCLI:
    def __init__(self, workspace_path: str):
        self.workspace_path = os.path.abspath(workspace_path)
        self.memory_sync = MemoryPalaceSync(self.workspace_path)
        self.ux_reviewer = UXLawReviewer()

    def print_welcome(self):
        title = """[bold cyan]Tay's Multi-Layered Autonomous Agent System[/bold cyan]\n[dim]3x6 Agent Grid & Hierarchical Memory Palace[/dim]"""
        console.print(Panel(title, border_style="cyan", expand=False))

    def init_project(self, project_name: str):
        proj_paths = self.memory_sync.get_project_paths(project_name)
        os.makedirs(proj_paths["dir"], exist_ok=True)
        os.makedirs(proj_paths["src"], exist_ok=True)
        
        # Write base Project MEMORY.md if not exists
        if not os.path.exists(proj_paths["memory"]):
            with open(proj_paths["memory"], "w", encoding="utf-8") as f:
                f.write(f"# Project Memory Palace: {project_name}\n\n## Learnings Ledger\n- **[SYSTEM]** (orchestration): Project workspace initialized.\n")
                
        # Create base project rules file
        proj_rules_file = os.path.join(proj_paths["dir"], "project_rules.md")
        if not os.path.exists(proj_rules_file):
            with open(proj_rules_file, "w", encoding="utf-8") as f:
                f.write(f"# Project-Specific Rules: {project_name}\n\n- Follow target framework layout specifications.\n")

        console.print(f"[bold green][OK][/bold green] Initialized project [bold yellow]{project_name}[/bold yellow]")
        console.print(f"Directory: [blue]{proj_paths['dir']}[/blue]")

    def run_ux_audit(self, project_name: str, design_desc: str, platform: str = "Web"):
        self.init_project(project_name)
        console.print(Panel(f"Running UX Law Reviewer in **Review Mode**\nPlatform: {platform}", title="[bold magenta]Domain 5: UI & Design[/bold magenta]", border_style="magenta"))
        
        # Context dict
        context = {
            "platform": platform,
            "user_type": "Strategy/AI Consultant (Tay)",
            "task_type": "Productivity/Enterprise Platform",
            "stage": "Development Audit"
        }
        
        with console.status("[bold yellow]Auditing layout against 30 Laws of UX..."):
            report = self.ux_reviewer.run_review(design_desc, context)
            
        console.print("\n[bold green]=== UX Review Report ===[/bold green]")
        console.print(report)
        
        # Write back to Project Memory
        self.memory_sync.log_learning(
            project_name=project_name,
            domain="ui_design",
            category="ux_review",
            content="Executed audit. Logged violations & recommended adjustments.",
            elevate=False
        )

    def run_pipeline(self, project_name: str, idea: str):
        self.init_project(project_name)
        self.print_welcome()
        
        console.print(Panel(f"Starting Multi-Layered Agent Grid for idea:\n[bold yellow]'{idea}'[/bold yellow]", border_style="cyan"))
        
        pipeline_steps = [
            ("Strategic Orchestration", "orchestration", ["CSO: Master Plan", "PM: Tasks Breakdown", "Ops: Backlog"]),
            ("Technical Engineering", "engineering", ["CTO: Architecture Specs", "Lead Eng: File Specs", "Software Eng: Code"]),
            ("QA & Testing", "qa", ["QA VP: Checklists", "QA Lead: Test Scenarios", "QA Eng: Unit Tests"]),
            ("Security & Protection", "security", ["CISO: Threat Model", "Security Lead: Scan Review", "SecOps: Sandbox"]),
            ("Frontend, UI, & Design", "ui_design", ["CDO: UX Reviewer Checklist", "UI Mgr: Layout Spec", "UI Dev: CSS Assets"]),
            ("Release Management", "release", ["Release VP: Rollback Plan", "Release Mgr: Build Tagging", "DevOps: Deployment"])
        ]
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            for domain_title, domain_key, layers in pipeline_steps:
                task_id = progress.add_task(description=f"Running {domain_title}...", total=len(layers))
                
                # Fetch hierarchical rules & memories
                rules = self.memory_sync.load_rules(domain=domain_key, project_name=project_name)
                memories = self.memory_sync.load_memory_context(domain=domain_key, project_name=project_name)
                
                for layer_name in layers:
                    progress.update(task_id, description=f"Executing {layer_name}...")
                    # Simulating layer action (in production this calls LLM with rules & memories context)
                    progress.advance(task_id)
                
                # Simulate milestone completion writeback
                self.memory_sync.log_learning(
                    project_name=project_name,
                    domain=domain_key,
                    category="milestone",
                    content=f"Completed {domain_title} layer processing. Outputs formatted.",
                    elevate=True
                )
                
                progress.update(task_id, description=f"[bold green][OK][/bold green] Completed {domain_title}")

        console.print("\n[bold green][SUCCESS] Orchestration Pipeline successfully completed![/bold green]")
        console.print(f"Updated memory tracking folders and learning logs in project [bold yellow]{project_name}[/bold yellow].")

    def print_rules(self, domain: str, project_name: str):
        rules = self.memory_sync.load_rules(domain=domain, project_name=project_name)
        console.print(Panel(rules, title=f"Rules Chain: {domain}", border_style="blue"))

    def print_memory(self, domain: str, project_name: str):
        mem = self.memory_sync.load_memory_context(domain=domain, project_name=project_name)
        console.print(Panel(mem, title=f"Memory Context Chain: {domain}", border_style="green"))

    def analyze_patterns(self, project_name: str, file_path: str):
        if not os.path.exists(file_path):
            console.print(f"[red]Error: file {file_path} does not exist.[/red]")
            return
            
        with open(file_path, "r", encoding="utf-8") as f:
            sample_content = f.read()
            
        with console.status("Analyzing work sample behavior patterns..."):
            extracted_rules = self.memory_sync.analyze_work_samples(sample_content)
            
        console.print(Panel(extracted_rules, title="Extracted Behavior Guidelines", border_style="yellow"))
        
        # Write back to Project rules
        proj_paths = self.memory_sync.get_project_paths(project_name)
        proj_rules_file = os.path.join(proj_paths["dir"], "project_rules.md")
        with open(proj_rules_file, "a", encoding="utf-8") as f:
            f.write(f"\n## Calibrated Behavioral Rules (from {os.path.basename(file_path)})\n{extracted_rules}\n")
            
        console.print(f"[bold green][OK][/bold green] Appended calibrated guidelines to {proj_rules_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tay's Multi-Layered Agent System Controller")
    parser.add_argument("action", choices=["init-project", "audit-ux", "run-pipeline", "analyze-behavior", "print-rules", "print-memory"])
    parser.add_argument("--project", required=True, help="Name of the project")
    parser.add_argument("--query", help="The user prompt, layout, or path to work sample file")
    parser.add_argument("--domain", default="ui_design", help="Agent workstation domain")
    parser.add_argument("--platform", default="Web", help="Platform target for UX Review")
    
    args = parser.parse_args()
    
    workspace = "C:\\Users\\TaylorGrenawalt\\.gemini\\antigravity\\scratch\\tay-agent-orchestrator"
    cli = AgentOrchestratorCLI(workspace)
    
    if args.action == "init-project":
        cli.init_project(args.project)
    elif args.action == "audit-ux":
        if not args.query:
            print("Error: --query description is required for audit-ux")
            sys.exit(1)
        cli.run_ux_audit(args.project, args.query, args.platform)
    elif args.action == "run-pipeline":
        if not args.query:
            print("Error: --query idea details are required for run-pipeline")
            sys.exit(1)
        cli.run_pipeline(args.project, args.query)
    elif args.action == "analyze-behavior":
        if not args.query:
            print("Error: --query path to file is required for analyze-behavior")
            sys.exit(1)
        cli.analyze_patterns(args.project, args.query)
    elif args.action == "print-rules":
        cli.print_rules(args.domain, args.project)
    elif args.action == "print-memory":
        cli.print_memory(args.domain, args.project)
