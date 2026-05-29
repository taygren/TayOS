import os
import sys

# Append parent dir to path so we can import modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from memory_palace.memory_sync import MemoryPalaceSync
from ui_design.ux_reviewer import UXLawReviewer

def run_tests():
    workspace = "C:\\Users\\TaylorGrenawalt\\.gemini\\antigravity\\scratch\\tay-agent-orchestrator"
    print("=== VERIFYING SYSTEM INTEGRITY ===")
    
    # 1. Check folder/file existence
    print("\n[Test 1] Core Path Checks...")
    required_paths = [
        "global_rules.md",
        "MEMORY.md",
        "orchestration/workstation_rules.md",
        "engineering/workstation_rules.md",
        "ui_design/workstation_rules.md",
        "qa/workstation_rules.md",
        "security/workstation_rules.md",
        "release/workstation_rules.md"
    ]
    all_exist = True
    for p in required_paths:
        full_p = os.path.join(workspace, p)
        if os.path.exists(full_p):
            print(f"  [OK] Found: {p}")
        else:
            print(f"  [MISSING] Missing: {p}")
            all_exist = False
            
    assert all_exist, "Missing core system assets!"
    
    # 2. Test Rules Resolver
    print("\n[Test 2] Testing Hierarchical Rules Loading...")
    sync = MemoryPalaceSync(workspace)
    rules_chain = sync.load_rules(domain="ui_design", project_name="verification_test")
    print(f"  [OK] Rules Chain Loaded Length: {len(rules_chain)} chars")
    assert "=== GLOBAL RULES ===" in rules_chain
    assert "=== UI_DESIGN WORKSTATION RULES ===" in rules_chain
    
    # 3. Test Memory Logging and Elevation
    print("\n[Test 3] Testing Memory Logging & Elevation...")
    test_project = "verification_test"
    sync.log_learning(
        project_name=test_project,
        domain="engineering",
        category="verification_test",
        content="Verification execution completed successfully.",
        elevate=True
    )
    
    proj_paths = sync.get_project_paths(test_project)
    assert os.path.exists(proj_paths["memory"]), "Project memory file was not created!"
    
    # Check project memory contents
    with open(proj_paths["memory"], "r", encoding="utf-8") as f:
        proj_mem_text = f.read()
    assert "VERIFICATION_TEST" in proj_mem_text, "Failed to write learning to project memory!"
    print("  [OK] Project memory log successful.")
    
    # Check workstation elevated memory contents
    workstation_mem_path = os.path.join(workspace, "engineering", "MEMORY.md")
    with open(workstation_mem_path, "r", encoding="utf-8") as f:
        workstation_mem_text = f.read()
    assert "verification_test" in workstation_mem_text.lower(), "Failed to elevate learning to workstation!"
    print("  [OK] Workstation elevated memory log successful.")
    
    # 4. Test UX Reviewer
    print("\n[Test 4] Testing UX Reviewer Output Format...")
    reviewer = UXLawReviewer()
    test_layout = "Landing page with 30 options. Button click has no response visual indicator."
    report = reviewer.run_review(test_layout, {"platform": "Mobile"})
    
    assert "Doherty Threshold" in report, "UX reviewer failed to flag Doherty Threshold violation!"
    assert "Miller's Law" in report or "Hick's Law" in report or "Choice Overload" in report, "UX reviewer failed to flag option density!"
    print("  [OK] UX Review report generated correctly and formatted.")
    
    print("\n[ALL TESTS PASSED] System verified and running smoothly!")

if __name__ == "__main__":
    run_tests()
