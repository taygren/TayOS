import os
import json
from typing import Dict, List, Any, Optional
from dotenv import load_dotenv

load_dotenv()

# The 30 Laws of UX grouped by domain
LAWS_OF_UX = {
    "1. Cognitive Load & Decision-Making": {
        "Hick's Law": "Decision time increases with the number and complexity of choices. Minimize choices at every decision point; break complex tasks into smaller sequential steps; highlight recommended options; use progressive onboarding.",
        "Miller's Law": "The average person holds 7 (±2) items in working memory. Chunk content into groups of 5-9 items maximum; organize navigation/menus into logical categories.",
        "Cognitive Load": "The amount of mental resources required to understand and use an interface must be minimized. Eliminate unnecessary elements; use familiar patterns; reduce extraneous cognitive load; use progressive disclosure.",
        "Chunking": "Information grouped into meaningful units is easier to process and remember. Group related content visually; apply to forms, navigation, and data; use white space as a chunking tool.",
        "Choice Overload": "Too many options leads to paralysis, poor decisions, and decision fatigue. Cap option sets; surface defaults and recommendations prominently; reduce visible options at entry points.",
        "Occam's Razor": "The simplest solution that works is correct. Remove everything that doesn't serve the user; prefer simple interaction patterns; audit for decorative complexity."
    },
    "2. Visual Perception & Gestalt": {
        "Law of Proximity": "Objects near each other are perceived as related. Place related elements close together; separate unrelated elements with clear space.",
        "Law of Common Region": "Elements within a defined boundary are perceived as belonging together. Use cards, containers, borders, and background fills; common region is stronger than proximity.",
        "Law of Similarity": "Similar-looking elements are perceived as related. Apply consistent visual treatment (color, shape, size, style) to same-category elements.",
        "Law of Uniform Connectedness": "Visually connected elements are perceived as more related than elements with no connection. Use lines, arrows, or shared visual properties for tightest relationships.",
        "Law of Prägnanz": "People perceive complex or ambiguous images in the simplest form possible. Design for interpretation requiring least effort; keep structures clean and explicit."
    },
    "3. Memory & Learning": {
        "Working Memory": "Working memory temporarily holds and manipulates information needed to complete tasks. Never require users to remember info from step to step; display info persistently.",
        "Serial Position Effect": "Users best remember the first and last items in a list or sequence. Place most important nav items/actions first or last; repeat critical items if needed.",
        "Zeigarnik Effect": "People remember incomplete or interrupted tasks better than completed ones. Use progress indicators, completion percentages, and onboarding completeness triggers.",
        "Goal-Gradient Effect": "Users accelerate effort as they approach a goal. Show progress clearly; design indicators that make progress feel meaningful even in early stages.",
        "Mental Model": "Users approach your interface with a pre-existing model of how it should work. Align with user expectations/metaphors; explain deviations explicitly."
    },
    "4. Interaction & Performance": {
        "Fitts's Law": "The time to reach a target is determined by its size and distance. Make interactive targets large enough (~44px); place targets close to cursor; edge/corner targets are fastest.",
        "Doherty Threshold": "Productivity peaks when system response time stays under 400ms. Show immediate feedback, spinners, skeletons, or progress bars for slow operations.",
        "Postel's Law": "Be liberal in what you accept; be conservative in what you send. Accept flexible user input; normalize differences; keep system output standardized and predictable.",
        "Parkinson's Law": "Tasks expand to fill the available time. Set clear deadlines/limits; keep forms and workflows short."
    },
    "5. Experience & Emotion": {
        "Aesthetic-Usability Effect": "Aesthetically pleasing designs are perceived as more usable. Invest in visual polish to build patience; test usability separately from visual appeal.",
        "Peak-End Rule": "Users judge an experience by its peak emotional moment and its final moment. Design delight/achievement peaks and success states with care; minimize pain points.",
        "Flow": "Optimal experience occurs when challenge and skill are in balance. Remove distractions; provide immediate feedback; calibrate task difficulty.",
        "Paradox of the Active User": "Users never read documentation. They start using the product immediately. Design interfaces that teach themselves; use tooltips/hints.",
        "Pareto Principle": "80% of effects come from 20% of causes. Identify and optimize the 20% of features that deliver 80% of value; surface them prominently."
    },
    "6. Information Architecture & Navigation": {
        "Jakob's Law": "Users spend most of their time on other products and expect yours to work like theirs. Default to established design conventions; allow gradual transition paths.",
        "Von Restorff Effect": "When similar items are present, the one that differs is most likely to be remembered. Use visual differentiation for the single most important action; do not overuse.",
        "Tesler's Law": "Every system has an irreducible complexity. Shift complexity from user to the system where possible, but do not over-simplify.",
        "Selective Attention": "Users focus only on information relating to their current goal. Align layout with user goals; use visual hierarchy/motion to guide attention.",
        "Cognitive Bias": "Systematic errors in thinking influence perception. Leverage anchoring, confirmation bias, status quo bias, social proof, and loss aversion ethically."
    }
}

class UXLawReviewer:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY") or os.environ.get("OPENAI_API_KEY")

    def run_review(self, design_data: str, context: Dict[str, Any]) -> str:
        """
        Runs design data (text description, code, wireframe spec) against the 30 laws.
        """
        platform = context.get("platform", "Web")
        user_type = context.get("user_type", "Mixed")
        task_type = context.get("task_type", "General")
        stage = context.get("stage", "Concept")
        
        prompt = f"""You are the UX Law Reviewer. Your role is to evaluate UI designs, wireframes, user flows, or code against the 30 Laws of UX.
        
### System Context:
- Platform: {platform}
- User Type: {user_type}
- Task Type: {task_type}
- Design Stage: {stage}

### Input Design:
{design_data}

### The 30 Laws of UX Reference:
{json.dumps(LAWS_OF_UX, indent=2)}

### Review Objectives:
1. Evaluate the design against each of the six domains.
2. For each law, check status: ✅ Satisfied / ⚠️ Partially satisfied / ❌ Violated / — Not applicable.
3. For any ⚠️ or ❌ finding, produce:
   [SEVERITY] [Law Name] — [Short finding title]
   - What's wrong: Concrete description of the violation.
   - Why it matters: User behavior/outcome it causes.
   - Fix: Specific, actionable change.
4. Ratings: 🔴 Critical / 🟠 High / 🟡 Medium / 🟢 Low / Polish.
5. Create a "Priority Summary Table" and list "Top 3 Priority Fixes" based on impact-to-effort ratio.

Provide a comprehensive, beautiful markdown report. If no API key is provided, perform a standard structural audit.
"""
        # Call LLM if API Key is available, otherwise perform a deterministic mock review for execution safety.
        if self.api_key:
            try:
                import litellm
                # Ensure we handle litellm calling correctly.
                model_name = os.environ.get("AGENT_LLM_MODEL", "gemini/gemini-2.5-flash")
                response = litellm.completion(
                    model=model_name,
                    messages=[{"role": "user", "content": prompt}],
                    api_key=self.api_key
                )
                return response.choices[0].message.content
            except Exception as e:
                return f"## UX Law Reviewer (API Error)\nAn error occurred while calling the LLM: {str(e)}\n\nFallback local analysis:\n- Hick's Law: Ensure choices are minimized.\n- Miller's Law: Keep grouped items under 7.\n- Doherty Threshold: Add skeleton loader check."
        else:
            return self._generate_heuristic_review(design_data, platform)

    def run_checklist(self, context: Dict[str, Any]) -> str:
        """
        Produces a customized design checklist organized by the six domains.
        """
        checklist = [
            "# Pre-Design Checklist: 30 Laws of UX Compliance\n",
            f"**Platform**: {context.get('platform', 'Web')} | **Target Users**: {context.get('user_type', 'Mixed')}\n",
            "Use this checklist during wireframing and component styling to ensure compliance.\n"
        ]
        
        for domain, laws in LAWS_OF_UX.items():
            checklist.append(f"## {domain}")
            for law, description in laws.items():
                checklist.append(f"- [ ] **{law}**: {description}")
                checklist.append(f"  *Design Prompt*: How does the layout implement {law}?")
            checklist.append("")
            
        return "\n".join(checklist)

    def _generate_heuristic_review(self, design_data: str, platform: str) -> str:
        """Heuristic rule-based fallback when API key is missing."""
        report = []
        report.append("# UX Law Review (Local Heuristic Mode)")
        report.append(f"Platform context: {platform}\n")
        report.append("## Executive Summary")
        report.append("This is a structural baseline audit based on keyword mapping of design descriptions. For high-fidelity semantic auditing, please configure the `GEMINI_API_KEY`.\n")
        
        # Simple heuristics
        violations = []
        if "loading" not in design_data.lower() and "wait" not in design_data.lower():
            violations.append((
                "Doherty Threshold", "[High]", 
                "No loading states defined.", 
                "Slow processes might make the UI look broken.", 
                "Add a skeleton loader or progress indicator for actions taking >400ms."
            ))
        if len(design_data.split('\n')) > 15 or "30 options" in design_data.lower() or "overwhelm" in design_data.lower():
            violations.append((
                "Miller's Law", "[Medium]",
                "High density of details.",
                "Users may feel overwhelmed with too many options presented at once.",
                "Group features into cards or tab systems to limit working memory load to 5-9 items."
            ))
        if "standard" not in design_data.lower() and "convention" not in design_data.lower():
            violations.append((
                "Jakob's Law", "[Low / Polish]",
                "Potential custom interaction pattern.",
                "Users might need to relearn the navigation layout.",
                "Ensure navigation and interaction cues map to common platform paradigms (e.g. standard headers)."
            ))
            
        report.append("## Findings Domain Scan")
        for law, severity, wrong, why, fix in violations:
            report.append(f"### {severity} | {law}")
            report.append(f"- **What's wrong**: {wrong}")
            report.append(f"- **Why it matters**: {why}")
            report.append(f"- **Fix**: {fix}\n")
            
        report.append("## Priority Summary Table")
        report.append("| Finding | Law | Severity | Fix Effort |")
        report.append("| :--- | :--- | :--- | :--- |")
        for law, severity, _, _, _ in violations:
            report.append(f"| {law} review | {law} | {severity} | Low |")
            
        return "\n".join(report)

if __name__ == "__main__":
    # Test layout
    sample_design = "A landing page showing a table of 25 pricing plan features side-by-side with no highlights or filters. When clicked, the payment processing takes 3 seconds with a frozen submit button."
    reviewer = UXLawReviewer()
    print(reviewer.run_review(sample_design, {"platform": "Mobile Web"}))
