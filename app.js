// Agent Citadel Dashboard Logic Controller

// Mock data database for agents, files, and simulation logs
const AGENT_DATABASE = {
  cso: {
    name: "Chief Strategy Officer (CSO)",
    code: "L1-ORC | Layer 1 Orchestrate",
    desc: "Responsible for framing Tay's raw concept. Evaluates strategic alignment, competitive advantages, ROI, and designs the overarching master verification checklist.",
    rules: "1. Must frame the strategy before manager decomposition. 2. Highlight value propositions and project bottlenecks early. 3. Output a structured planning verification block."
  },
  cto: {
    name: "Chief Technology Officer (CTO)",
    code: "L1-ENG | Layer 1 Engineering",
    desc: "Architects the target system layout. Selects programming runtimes, defines data architecture, choose dependencies, and checks for systemic structural design patterns.",
    rules: "1. Standardize on clean, typed modules (e.g., Python Type Hints, TypeScript). 2. Avoid complex framework assumptions unless explicitly specified. 3. Enforce strict modular patterns."
  },
  vp_qa: {
    name: "VP of Quality Assurance",
    code: "L1-QA | Layer 1 QA & Testing",
    desc: "Establishes project coverage limits, unit testing schemas, testing tools, and validates integration gate parameters.",
    rules: "1. Target minimum 80% coverage limits for core system layers. 2. Standardize on reliable mock frameworks. 3. Reject any draft lacking unit testing models."
  },
  ciso: {
    name: "Chief Information Security Officer (CISO)",
    code: "L1-SEC | Layer 1 Security",
    desc: "Formulates systemic security metrics, InfoSec compliance models, access credentials guidelines, and runs sandbox verification requirements.",
    rules: "1. Zero hardcoded tokens or secret variables. 2. Verify input normalization boundaries on all integrations. 3. Design strict sandbox runtime definitions."
  },
  cdo: {
    name: "Chief Design Officer (CDO)",
    code: "L1-UI | Layer 1 UI & Design",
    desc: "Owns styling systems, colors, and layout aesthetics. Runs the **UX Law Reviewer** (Review Mode / Checklist Mode) auditing UI layouts against the 30 Laws of UX.",
    rules: "1. Every design must satisfy Hick's Law, Miller's Law, and the Doherty Threshold (<400ms). 2. Force WCAG AAA contrast scales. 3. Enforce glassmorphic HSL visual grids."
  },
  vp_rel: {
    name: "VP of Release Operations",
    code: "L1-REL | Layer 1 Release",
    desc: "Coordinates version gates, deployment schedules, semantic tagging patterns, and designs active rollback procedures.",
    rules: "1. Prepare full automated rollback scripts before major releases. 2. Require C-Suite operational approvals before promoting code."
  },
  pm: {
    name: "Project Manager (PM)",
    code: "L2-ORC | Layer 2 Orchestrate",
    desc: "Translates CSO master plan checklist into milestone tasks (task.md), coordinates timelines, and manages grid handoffs.",
    rules: "1. Generate clean task checklist trackers. 2. Enforce prompt handoffs between Engineering, QA, and Security."
  },
  lead_eng: {
    name: "Lead Engineer",
    code: "L2-ENG | Layer 2 Engineering",
    desc: "Translates CTO blueprints into class files structure, designs database schemas, and executes rigorous code reviews of Software Engineer drafts.",
    rules: "1. Review software engineer outputs before QA handoff. 2. Ensure clear inline docstring explanations for all major routines."
  },
  qa_lead: {
    name: "QA Lead",
    code: "L2-QA | Layer 2 QA & Testing",
    desc: "Designs rigorous test scenarios, writes integration test guidelines, and monitors unit test runs outcomes.",
    rules: "1. Construct complete integration specs. 2. Verify all mock targets are fully updated and accurate."
  },
  sec_lead: {
    name: "Security Lead",
    code: "L2-SEC | Layer 2 Security",
    desc: "Identifies threat vulnerabilities vectors, conducts SAST review audits, and reviews third-party dependencies libraries.",
    rules: "1. Run dependency vulnerability scanners. 2. Identify potential injection patterns early."
  },
  ui_mgr: {
    name: "UI/UX Manager",
    code: "L2-UI | Layer 2 UI & Design",
    desc: "Builds responsive interface mockups, establishes modular components templates, and audits accessibility contrast controls.",
    rules: "1. Ensure touch targets are at least 44px (Fitts's Law). 2. Group interactive states using Cards region elements."
  },
  rel_mgr: {
    name: "Release Manager",
    code: "L2-REL | Layer 2 Release",
    desc: "Automates CI/CD run parameters, compiles tag updates, and maintains changelogs records.",
    rules: "1. Automate version increases. 2. Verify release builds compile properly before deployment."
  },
  ops: {
    name: "Operations Analyst",
    code: "L3-ORC | Layer 3 Orchestrate",
    desc: "Drafts fine-grained task items, collects agent runtimes, and writes logs files.",
    rules: "1. Track active backlogs accurately. 2. Collect running operational statistics logs."
  },
  swe: {
    name: "Software Engineer",
    code: "L3-ENG | Layer 3 Engineering",
    desc: "Writes the core functional code files, builds logic loops, and refactors helper scripts.",
    rules: "1. No placeholder implementations or '# TODO'. 2. Complete typing details on all class scopes."
  },
  qa_eng: {
    name: "QA Engineer",
    code: "L3-QA | Layer 3 QA & Testing",
    desc: "Writes unit tests files, implements mock classes, runs automated tests suites, and records bug logs.",
    rules: "1. Utilize pytest structure. 2. Document reproducing parameters for all failed tests."
  },
  sec_ops: {
    name: "SecOps Analyst",
    code: "L3-SEC | Layer 3 Security",
    desc: "Performs scanning sweeps, runs secrets scan checks, and verifies sandbox limits.",
    rules: "1. Execute dependency scanners during build runs. 2. Run automated static checks."
  },
  ui_dev: {
    name: "UI Developer",
    code: "L3-UI | Layer 3 UI & Design",
    desc: "Develops CSS stylesheets animations, writes semantic HTML components, and refactors frontend assets.",
    rules: "1. Leverage pure, modern CSS structures. 2. Guarantee smooth micro-animations transition details."
  },
  devops: {
    name: "DevOps Analyst",
    code: "L3-REL | Layer 3 Release",
    desc: "Triggers compilation builds, pushes container registries, and checks live health ports.",
    rules: "1. Double-check deployment health endpoints. 2. Log performance metrics parameters."
  }
};

const FILE_DATABASE = {
  global_rules: {
    title: "global_rules.md",
    meta: "Path: /global_rules.md | Size: 1.2KB",
    content: `<h1>Tay's Global Agent System Rules</h1>
<p>These rules govern the operational standards, behavior, and design constraints for all agents in the grid.</p>
<h2>Core Directives</h2>
<ul>
  <li><strong>First-Principles Thinking</strong>: Analyze problems from the ground up. State constraints, components, and data flows first.</li>
  <li><strong>No Placeholders</strong>: All code, mock outputs, and plans must be 100% complete and operational.</li>
  <li><strong>Memory Loop Integration</strong>: Every agent check runs, logs, and elevates learning through recursive MEMORY.md updates.</li>
</ul>`
  },
  global_memory: {
    title: "MEMORY.md",
    meta: "Path: /MEMORY.md | Size: 920B",
    content: `<h1>System Learning Ledger (MEMORY.md)</h1>
<p>This ledger retains system-wide learnings, rules calibration, and experiences across projects.</p>
<h2>Active Learnings</h2>
<ul>
  <li><strong>UX Law Integration</strong>: All front-end assets must pass the CDO's 30 Laws of UX review script first.</li>
  <li><strong>Python Runtimes</strong>: Emphasize typed Python 3.11 structures for orchestrator core logic functions.</li>
</ul>`
  },
  workstation_orc: {
    title: "orchestration/workstation_rules.md",
    meta: "Path: /orchestration/workstation_rules.md | Size: 780B",
    content: `<h1>Strategic Orchestration Workstation Rules</h1>
<h2>Roles & Checks</h2>
<ul>
  <li><strong>CSO (Chief Strategy Officer)</strong>: Generates the master checklists and ROI guidelines.</li>
  <li><strong>Project Manager</strong>: Breaks goals into task.md lists.</li>
  <li><strong>Operations Analyst</strong>: Formulates backlog items.</li>
</ul>`
  },
  workstation_eng: {
    title: "engineering/workstation_rules.md",
    meta: "Path: /engineering/workstation_rules.md | Size: 840B",
    content: `<h1>Technical Engineering Workstation Rules</h1>
<h2>Directives</h2>
<ul>
  <li>Always write comprehensive Docstrings for all classes and files.</li>
  <li>Complete type hint structures are mandatory to enforce typing safety.</li>
  <li>No structural shortcut blocks are permitted.</li>
</ul>`
  },
  workstation_ui: {
    title: "ui_design/workstation_rules.md",
    meta: "Path: /ui_design/workstation_rules.md | Size: 960B",
    content: `<h1>Frontend, UI, & Design Workstation Rules</h1>
<h2>UX Law Auditing</h2>
<ul>
  <li><strong>Hick's Law</strong>: Keep navigation and form choices minimized.</li>
  <li><strong>Doherty Threshold</strong>: Add progress skeleton indicators for actions taking &gt;400ms.</li>
  <li><strong>Fitts's Law</strong>: Minimum touch target size must scale to 44px.</li>
</ul>`
  },
  workstation_qa: {
    title: "qa/workstation_rules.md",
    meta: "Path: /qa/workstation_rules.md | Size: 680B",
    content: `<h1>QA & Testing Workstation Rules</h1>
<h2>Directives</h2>
<ul>
  <li>Pytest framework standard for automated test suites.</li>
  <li>Maintain a minimum code coverage baseline of 80% on logic.</li>
  <li>Mock integrations must represent actual operational boundaries.</li>
</ul>`
  },
  project_billing_rules: {
    title: "projects/billing_app/rules.md",
    meta: "Path: /projects/billing_app/project_rules.md | Size: 1.1KB",
    content: `<h1>Billing App Project-Specific Rules</h1>
<p>Tailored rules card calibrated specifically for Tay's billing app project.</p>
<h2>Behavioral Calibrations (Extracted from billing_sample.py)</h2>
<ul>
  <li>Uses dark space theme grids with refined, tailored HSL color values.</li>
  <li>Applies glassmorphism blur layers for cards region grouping.</li>
  <li>Prefers structured checklist-first validation designs.</li>
</ul>`
  },
  project_billing_memory: {
    title: "projects/billing_app/MEMORY.md",
    meta: "Path: /projects/billing_app/MEMORY.md | Size: 880B",
    content: `<h1>Billing App Learnings Ledger</h1>
<h2>Logged Learnings</h2>
<ul>
  <li><strong>[BUG] (ui_design)</strong>: Forms submit button was too small on mobile. Adjusted target to 48px to satisfy Fitts's Law.</li>
  <li><strong>[MILESTONE] (engineering)</strong>: Core payment API class was refactored with typed signatures.</li>
</ul>`
  }
};

// --- Tab Switching Logic ---
const tabs = document.querySelectorAll('.nav-tab');
const sections = document.querySelectorAll('.view-section');

tabs.forEach(tab => {
  tab.addEventListener('click', () => {
    tabs.forEach(t => t.classList.remove('active'));
    sections.forEach(s => s.classList.remove('active'));
    
    tab.classList.add('active');
    const target = tab.getAttribute('data-target');
    document.getElementById(target).classList.add('active');
  });
});

// --- Agent Details Modal Logic ---
const agentCards = document.querySelectorAll('.agent-card');
const modal = document.getElementById('agent-modal');
const modalClose = document.getElementById('modal-close-btn');

agentCards.forEach(card => {
  card.addEventListener('click', () => {
    const agentKey = card.getAttribute('data-agent');
    const agentData = AGENT_DATABASE[agentKey];
    
    if (agentData) {
      document.getElementById('modal-agent-name').textContent = agentData.name;
      document.getElementById('modal-agent-code').textContent = agentData.code;
      document.getElementById('modal-agent-desc').textContent = agentData.desc;
      document.getElementById('modal-agent-rules').textContent = agentData.rules;
      
      modal.classList.add('active');
    }
  });
});

modalClose.addEventListener('click', () => {
  modal.classList.remove('active');
});

// --- Settings Modal Logic ---
const btnSettings = document.getElementById('btn-settings');
const settingsModal = document.getElementById('settings-modal');
const settingsCloseBtn = document.getElementById('settings-close-btn');
const btnSaveSettings = document.getElementById('btn-save-settings');

const inputGemini = document.getElementById('settings-gemini-key');
const inputOpenAI = document.getElementById('settings-openai-key');
const inputAnthropic = document.getElementById('settings-anthropic-key');
const selectDefaultModel = document.getElementById('settings-default-model');

function loadStoredSettings() {
  inputGemini.value = localStorage.getItem('gemini_api_key') || '';
  inputOpenAI.value = localStorage.getItem('openai_api_key') || '';
  inputAnthropic.value = localStorage.getItem('anthropic_api_key') || '';
  selectDefaultModel.value = localStorage.getItem('default_browser_model') || 'gemini-2.5-flash';
}

// Load keys silently on boot so inputs are ready
loadStoredSettings();

btnSettings.addEventListener('click', () => {
  loadStoredSettings();
  settingsModal.classList.add('active');
});

settingsCloseBtn.addEventListener('click', () => {
  settingsModal.classList.remove('active');
});

btnSaveSettings.addEventListener('click', () => {
  localStorage.setItem('gemini_api_key', inputGemini.value.trim());
  localStorage.setItem('openai_api_key', inputOpenAI.value.trim());
  localStorage.setItem('anthropic_api_key', inputAnthropic.value.trim());
  localStorage.setItem('default_browser_model', selectDefaultModel.value);
  
  settingsModal.classList.remove('active');
  alert('Settings saved successfully!');
});

// Click outside modal to close
window.addEventListener('click', (e) => {
  if (e.target === modal) {
    modal.classList.remove('active');
  }
  if (e.target === settingsModal) {
    settingsModal.classList.remove('active');
  }
});

// --- Memory Palace Explorer Logic ---
const treeNodes = document.querySelectorAll('.tree-node');
const fileTitle = document.getElementById('viewer-file-title');
const fileMeta = document.getElementById('viewer-file-meta');
const fileContent = document.getElementById('viewer-content');

function loadFile(fileKey) {
  const fileData = FILE_DATABASE[fileKey];
  if (fileData) {
    fileTitle.textContent = fileData.title;
    fileMeta.textContent = fileData.meta;
    fileContent.innerHTML = fileData.content;
  }
}

// Initial Load
loadFile('global_rules');

treeNodes.forEach(node => {
  node.addEventListener('click', () => {
    const fileKey = node.getAttribute('data-file');
    if (fileKey) {
      treeNodes.forEach(n => n.classList.remove('active'));
      node.classList.add('active');
      loadFile(fileKey);
    }
  });
});

// --- Dynamic Pipeline Simulator Sandbox Logic ---
const btnLaunch = document.getElementById('btn-launch');
const inputProject = document.getElementById('input-project');
const inputPlatform = document.getElementById('input-platform');
const inputIdea = document.getElementById('input-idea');
const checkUX = document.getElementById('check-ux-review');
const logConsole = document.getElementById('log-console');
const monitorTitle = document.getElementById('monitor-project-title');
const monitorStatus = document.getElementById('monitor-status');

// Status dots in Home Grid
const allStatusDots = document.querySelectorAll('.agent-status-dot');

function logConsoleLine(text, type = 'system') {
  const line = document.createElement('div');
  line.className = `console-line ${type}`;
  line.textContent = text;
  logConsole.appendChild(line);
  logConsole.scrollTop = logConsole.scrollHeight;
}

btnLaunch.addEventListener('click', () => {
  const projectName = inputProject.value.trim() || "unnamed_project";
  const platform = inputPlatform.value;
  const ideaText = inputIdea.value.trim();
  
  if (!ideaText) {
    alert("Please enter a concept or idea to orchestrator!");
    return;
  }
  
  // Disable button during execution
  btnLaunch.disabled = true;
  monitorTitle.textContent = `project: ${projectName}`;
  monitorStatus.textContent = "active";
  monitorStatus.className = "monitor-status-badge active";
  
  // Clear logs
  logConsole.innerHTML = "";
  logConsoleLine(`[SYSTEM] Starting execution engine pipeline for project: ${projectName}...`, 'system');
  
  // Reset all Home grid dots
  allStatusDots.forEach(dot => {
    dot.className = "agent-status-dot idle";
  });
  
  // Steps definitions
  const steps = [
    {
      id: "orc",
      dots: ["cso", "pm", "ops"],
      title: "Strategic Orchestration",
      logs: [
        `[CSO] Frame - Analyzing strategic concept for '${projectName}'...`,
        `[CSO] Plan - Generating master planning verification checklist...`,
        `[PM] Breakdown - Translating master plan into task.md milestones...`,
        `[OPS] Backlog - Formulating 8 user-story task logs.`,
        `[SUCCESS] Orchestration baseline validated. Local MEMORY.md synced.`
      ]
    },
    {
      id: "eng",
      dots: ["cto", "lead_eng", "swe"],
      title: "Technical Engineering",
      logs: [
        `[CTO] Architect - Defining modular Python structures & files tree...`,
        `[Lead Eng] Specs - Writing class blueprints and type details definitions...`,
        `[SWE] Code - Drafting main module logic. Complete signatures compiled.`,
        `[SUCCESS] Base system logic compiled. Rules card verified.`
      ]
    },
    {
      id: "qa",
      dots: ["vp_qa", "qa_lead", "qa_eng"],
      title: "QA & Testing",
      logs: [
        `[VP QA] Standards - Checking coverage requirements (Target: 80%)...`,
        `[QA Lead] Scenarios - Generating 14 automated unit test scenarios...`,
        `[QA Eng] Tests - Writing pytest mock testing classes...`,
        `[QA Eng] Running pytest suite... 14 passed. Coverage reached 86.4%.`
      ]
    },
    {
      id: "sec",
      dots: ["ciso", "sec_lead", "sec_ops"],
      title: "Security & Protection",
      logs: [
        `[CISO] Policy - Initiating dependency safety scan guidelines...`,
        `[Sec Lead] Scan - Inspecting packages boundaries... Zero threat vectors found.`,
        `[SecOps] Sweep - Checking sandbox rules and token exclusions... OK.`,
        `[SUCCESS] Infosec gate clearance approved.`
      ]
    },
    {
      id: "ui",
      dots: ["cdo", "ui_mgr", "ui_dev"],
      title: "Frontend, UI, & Design",
      logs: [
        `[CDO] UX Reviewer - Initiating 30 Laws of UX review in Audit Mode...`,
        `[CDO] Checking Hick's Law and Miller's Law option density...`,
        `[WARNING] Miller's Law violation: Too many dashboard items concurrent.`,
        `[CDO] GAP IDENTIFIED! Generated FEEDBACK.md card. State: RESOLVING.`,
        `[SYSTEM] Re-routing vertical optimization loop to UI Developer...`,
        `[UI Developer] Refactoring code... Chunked menu options into grouped cards.`,
        `[CDO] Re-auditing work asset... Gaps satisfied! State: APPROVED.`,
        `[UI Manager] Layout - Designing card regional elements...`,
        `[UI Developer] Assets - Generating premium HSL glassmorphic style panels.`,
        `[SUCCESS] Premium front-end assets validated against UX standards.`
      ]
    },
    {
      id: "rel",
      dots: ["vp_rel", "rel_mgr", "devops"],
      title: "Release Management",
      logs: [
        `[VP Release] Gates - Checking all L1/L2 checklist parameters... Passed.`,
        `[Release Manager] Build - Compiling Git release tag (v1.0.0)...`,
        `[DevOps] Deploy - Deploying containers build logic... Health check OK.`,
        `[SUCCESS] System successfully running. Global and project memories written.`
      ]
    }
  ];
  
  // Dynamic step transition loop
  let currentStepIndex = 0;
  
  async function runLiveAIAudit(ideaText, platform, node, connector, dots, step) {
    const key = localStorage.getItem('gemini_api_key');
    const model = localStorage.getItem('default_browser_model') || 'gemini-2.5-flash';
    const targetModel = model.startsWith('gemini') ? model : 'gemini-2.5-flash';
    
    logConsoleLine("[CDO] UX Reviewer - Initiating 30 Laws of UX review in LIVE AI Mode...", "highlight");
    logConsoleLine("[SYSTEM] Connecting to Gemini API for real-time semantic analysis...", "system");
    
    try {
      const url = `https://generativelanguage.googleapis.com/v1beta/models/${targetModel}:generateContent?key=${key}`;
      const response = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          contents: [{
            parts: [{
              text: `You are the CDO (Chief Design Officer) and UX Law Reviewer of TayOS.
Perform a professional UX law review of the following concept/idea against the 30 Laws of UX:
Concept: "${ideaText}"
Platform: ${platform}

Structure your response into 3 short sections:
1. ✅ Satisfied UX Laws (e.g. Miller's Law, Fitts's Law)
2. ❌ Gaps / Violations Identified (e.g. Doherty Threshold concerns, Hick's Law)
3. Actionable Design Changes

Keep it punchy, professional, under 15 lines total, using bullet points and clear indicators.`
            }]
          }]
        })
      });
      
      if (!response.ok) {
        throw new Error(`API returned status ${response.status}`);
      }
      
      const data = await response.json();
      const aiText = data.candidates[0].content.parts[0].text;
      
      logConsoleLine("[SUCCESS] Connection established. Processing real-time CDO audit:", "success");
      
      const lines = aiText.split('\n');
      let lIndex = 0;
      
      function printAILine() {
        if (lIndex >= lines.length) {
          // Complete step
          node.classList.remove('active');
          node.classList.add('completed');
          if (connector) connector.classList.add('completed');
          
          dots.forEach(d => {
            const dot = document.getElementById(`status-${d}`);
            if (dot) dot.className = "agent-status-dot completed";
          });
          
          currentStepIndex++;
          setTimeout(executeStep, 1000);
          return;
        }
        
        const lineText = lines[lIndex].trim();
        if (lineText) {
          let logType = 'system';
          if (lineText.includes('✅') || lineText.startsWith('1.') || lineText.startsWith('##') || lineText.startsWith('**1.')) logType = 'success';
          if (lineText.includes('❌') || lineText.includes('⚠️') || lineText.startsWith('2.') || lineText.startsWith('**2.')) logType = 'warning';
          if (lineText.includes('CDO') || lineText.startsWith('3.') || lineText.startsWith('**3.')) logType = 'highlight';
          logConsoleLine(lineText, logType);
        }
        lIndex++;
        setTimeout(printAILine, 200);
      }
      
      printAILine();
      
    } catch (err) {
      logConsoleLine(`[WARNING] Gemini Live API call failed: ${err.message}. Falling back to simulated heuristics...`, "warning");
      // Fallback to static logging
      runHeuristicFallback(node, connector, dots, step);
    }
  }

  function runHeuristicFallback(node, connector, dots, step) {
    let logIndex = 0;
    function printNextLog() {
      if (logIndex >= step.logs.length) {
        node.classList.remove('active');
        node.classList.add('completed');
        if (connector) connector.classList.add('completed');
        dots.forEach(d => {
          const dot = document.getElementById(`status-${d}`);
          if (dot) dot.className = "agent-status-dot completed";
        });
        currentStepIndex++;
        setTimeout(executeStep, 800);
        return;
      }
      const logText = step.logs[logIndex];
      let logType = 'system';
      if (logText.includes('[SUCCESS]')) logType = 'success';
      if (logText.includes('[WARNING]')) logType = 'warning';
      if (logText.includes('[CDO]') || logText.includes('[CSO]') || logText.includes('[CTO]')) logType = 'highlight';
      
      // Inject closed-loop dynamic DOM animations
      if (logText.includes('GAP IDENTIFIED')) {
        const uiDevCard = document.querySelector('[data-agent="ui_dev"]');
        if (uiDevCard && !document.getElementById('iter-badge-ui-dev')) {
          const badge = document.createElement('span');
          badge.className = 'iteration-badge';
          badge.style.position = 'absolute';
          badge.style.top = '8px';
          badge.style.right = '28px';
          badge.style.background = 'var(--alert-amber)';
          badge.style.color = 'black';
          badge.style.fontWeight = 'bold';
          badge.style.fontSize = '0.65rem';
          badge.style.padding = '1px 5px';
          badge.style.borderRadius = '3px';
          badge.style.fontFamily = 'var(--font-mono)';
          badge.textContent = 'Iter 2';
          badge.id = 'iter-badge-ui-dev';
          uiDevCard.appendChild(badge);
        }
        const uiDevDot = document.getElementById('status-ui_dev');
        if (uiDevDot) uiDevDot.className = 'agent-status-dot reviewing';
      }
      if (logText.includes('Gaps satisfied')) {
        const badgeEl = document.getElementById('iter-badge-ui-dev');
        if (badgeEl) badgeEl.remove();
        const uiDevDot = document.getElementById('status-ui_dev');
        if (uiDevDot) uiDevDot.className = 'agent-status-dot completed';
      }
      
      logConsoleLine(logText, logType);
      logIndex++;
      setTimeout(printNextLog, 450);
    }
    printNextLog();
  }

  function executeStep() {
    if (currentStepIndex >= steps.length) {
      // Done pipeline
      btnLaunch.disabled = false;
      monitorStatus.textContent = "completed";
      monitorStatus.className = "monitor-status-badge";
      logConsoleLine("[SYSTEM] Pipeline successfully completed!", 'success');
      
      // Select UI design tree node to show updated project memory as visual detail
      loadFile('project_billing_memory');
      return;
    }
    
    const step = steps[currentStepIndex];
    
    // Highlight visual nodes
    const node = document.getElementById(`stage-${step.id}`);
    const connector = document.getElementById(`conn-${step.id}`);
    
    node.classList.add('active');
    logConsoleLine(`[SYSTEM] Triggers: ${step.title}...`, 'highlight');
    
    // Animate Home Grid status dots
    step.dots.forEach(d => {
      const dot = document.getElementById(`status-${d}`);
      if (dot) dot.className = "agent-status-dot executing";
    });
    
    // Check if we can intercept UI step with real Gemini API call
    if (step.id === "ui" && checkUX.checked && localStorage.getItem('gemini_api_key')) {
      runLiveAIAudit(ideaText, platform, node, connector, step.dots, step);
    } else {
      runHeuristicFallback(node, connector, step.dots, step);
    }
  }
  
  // Clear visual stages on start
  document.querySelectorAll('.stage-node').forEach(n => n.className = "stage-node");
  document.querySelectorAll('.stage-connector').forEach(c => c.className = "stage-connector");
  
  // Run
  executeStep();
});
