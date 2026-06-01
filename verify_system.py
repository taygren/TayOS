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

    # 5. Test Closed-Loop Optimization Loops
    print("\n[Test 5] Testing Closed-Loop Agent Audits...")
    checklist = ["Must include HSL colors.", "Must include glassmorphism blur."]
    test_draft = "Standard input form with a plain gray background."
    
    # Audit Iteration 1 (Should trigger resolving state)
    result = sync.audit_work_asset(
        project_name=test_project,
        domain="ui_design",
        source="CDO",
        target="UI Developer",
        asset_content=test_draft,
        spec_checklist=checklist,
        iteration=1
    )
    
    assert result["status"] == "RESOLVING", "Closed-loop audit failed to flag incomplete checklist specifications!"
    assert result["iteration"] == 2, "Failed to increment iteration count on audit rejection!"
    assert os.path.exists(result["feedback_path"]), "Feedback card FEEDBACK.md was not written!"
    print("  [OK] Closed-loop audit flagged gaps and wrote FEEDBACK.md card.")
    
    # Audit Iteration 3 (Should trigger failure ledger elevation)
    result_repeat = sync.audit_work_asset(
        project_name=test_project,
        domain="ui_design",
        source="CDO",
        target="UI Developer",
        asset_content=test_draft,
        spec_checklist=checklist,
        iteration=3
    )
    
    ui_mem_path = os.path.join(workspace, "ui_design", "MEMORY.md")
    with open(ui_mem_path, "r", encoding="utf-8") as f:
        ui_mem_text = f.read()
    assert "failure ledger" in ui_mem_text.lower(), "Repeated failures did not elevate to workstation failure ledger!"
    print("  [OK] Persistent audit failures successfully elevated to workstation ledgers.")
    
    # Audit Iteration 4 with Resolved content (Should transition to APPROVED)
    resolved_draft = "High-fidelity landing page with glassmorphism blur and custom HSL color styling values."
    result_resolved = sync.audit_work_asset(
        project_name=test_project,
        domain="ui_design",
        source="CDO",
        target="UI Developer",
        asset_content=resolved_draft,
        spec_checklist=checklist,
        iteration=4
    )
    assert result_resolved["status"] == "APPROVED", "Failed to transition loop to APPROVED once checklist was satisfied!"
    assert not os.path.exists(result_resolved["feedback_path"] or ""), "Failed to delete resolved FEEDBACK.md card!"
    print("  [OK] Audit resolved. Gaps satisfied, loop approved, feedback card deleted.")
    
    print("\n[ALL TESTS PASSED] System verified and running smoothly!")

if __name__ == "__main__":
    run_tests()
