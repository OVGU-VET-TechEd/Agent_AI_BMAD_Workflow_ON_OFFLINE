# 🤖 Project Proposal Agent System - Command Guide

## Quick Start: How to Use Like @teaching-agent /help

This system works **exactly like your teaching workflow** but for project proposals!

---

## 🚀 Basic Pattern

Instead of: `@teaching-agent /create-outline`  
You use: `@proposal-agent /overseer` (or other commands)

**Each command activates a specialized agent that:**
1. Reads its task definition from `tasks/`
2. Loads templates from `templates/`
3. Reviews previous outputs from `docs/`
4. Produces new output following quality criteria

---

## 📋 Complete Command List

### System Commands

| Command | What It Does | When to Use |
|---------|-------------|-------------|
| `@proposal-agent /help` | Show all commands and workflow | Anytime you need guidance |
| `@proposal-agent /start` | Initialize new proposal project | Very first step |
| `@proposal-agent /status` | Check progress and next steps | See where you are |

### Agent Commands (Sequential Workflow)

| # | Command | Agent | Output | Time |
|---|---------|-------|--------|------|
| 1 | `@proposal-agent /overseer` | Overseer | Strategic analysis | ~15 min |
| 2 | `@proposal-agent /info-page` | Info Page | 1-page summary | ~10 min |
| 3 | `@proposal-agent /outline` | Outline | Full proposal (15-25 pages) | ~30 min |
| 4 | `@proposal-agent /work-packages` | Work Packages | Detailed WPs | ~25 min |
| 5 | `@proposal-agent /budget` | Budget | Budget calculation | ~20 min |
| 6 | `@proposal-agent /review` | Quality Review | Consistency check | ~15 min |

---

## 📖 Detailed Command Usage

### Command: @proposal-agent /help

**Purpose:** Get complete system overview

**You say:**
```
@proposal-agent /help
```

**System responds with:**
- List of all commands
- Workflow explanation
- Tips and best practices
- Quick start example

**When to use:** 
- First time using system
- Forgot what commands are available
- Need workflow reminder

---

### Command: @proposal-agent /start

**Purpose:** Initialize new proposal project

**You say:**
```
@proposal-agent /start
```

**System does:**
- Creates folder structure (if not already created)
- Checks for required directories
- Prepares for workflow
- Shows next steps

**Next step:** Upload your funding call PDF, then run `/overseer`

---

### Command: @proposal-agent /status

**Purpose:** Check current progress

**You say:**
```
@proposal-agent /status
```

**System shows:**
- Which stages completed
- Current stage
- Files generated
- Next recommended command
- Estimated completion

**Example output:**
```
✓ Stage 1: Strategic Analysis (COMPLETE)
✓ Stage 2: Project Summary (COMPLETE)
→ Stage 3: Full Proposal (IN PROGRESS)
  Next: Run @proposal-agent /outline
```

---

### Command: @proposal-agent /overseer

**Agent:** Overseer Agent (Strategic Coordinator)

**Purpose:** Analyze funding call and create strategic framework

**Prerequisites:**
- Funding call document uploaded to `call/` directory

**You say:**
```
I have a [Erasmus+ KA2 / Horizon Europe / National Grant] call.
Topic: [brief description]
Budget: €[amount]
Duration: [months]
Partners: [number]

@proposal-agent /overseer
```

**Full example:**
```
I have an Erasmus+ KA2 call for digital transformation in vocational education.
Topic: Developing AI-powered training tools for SMEs
Budget limit: €400,000
Duration: 30 months
Required partners: 5-7 from different EU countries

@proposal-agent /overseer
```

**Agent embodies this role:**
```
You are the OVERSEER AGENT - strategic project design expert.

You have deep expertise in:
- EU/research funding mechanisms
- Proposal strategy and positioning
- Consortium design
- Competitive analysis

Your task: Read tasks/overseer-analysis.md and execute it.
```

**Agent reads:**
- `tasks/overseer-analysis.md` (detailed instructions)
- `call/[your-call-document].pdf` (the actual call)
- `templates/project-outline-template.yaml` (structure)

**Agent produces:**
- `docs/overseer-analysis.md` - Strategic analysis document
- `docs/project-strategy.md` - High-level project framework

**What's in the output:**
- Call requirements extraction
- Strategic opportunities
- Proposed project concept
- Consortium recommendations
- Budget framework
- Risk assessment
- Handoff brief for next agent

**Duration:** ~15-20 minutes of AI work

**Next command:** `@proposal-agent /info-page`

---

### Command: @proposal-agent /info-page

**Agent:** Info Page Agent (Concise Communicator)

**Purpose:** Create 1-page project summary (max 600 words)

**Prerequisites:**
- Overseer analysis complete (`docs/overseer-analysis.md` exists)

**You say:**
```
@proposal-agent /info-page
```

**Or with guidance:**
```
Create the info page. 
Focus on: [specific emphasis, e.g., "industrial partnerships" or "policy impact"]
Tone: [academic / persuasive / technical]

@proposal-agent /info-page
```

**Agent embodies this role:**
```
You are the INFO PAGE AGENT - expert at distilling complex concepts.

You excel at:
- Compelling one-pagers
- Value proposition clarity
- Stakeholder communication
- Concise, powerful writing

Your task: Read tasks/create-info-page.md and execute it.
```

**Agent reads:**
- `tasks/create-info-page.md`
- `templates/project-info-page-template.yaml`
- `docs/overseer-analysis.md` (previous output)
- `docs/project-strategy.md` (previous output)

**Agent produces:**
- `docs/project-info-page.md` (1 page A4)

**Sections created:**
- Project title & acronym
- Short description (60 words)
- Main objective (80 words)
- Specific objectives (3-5 SMART)
- Key outputs (bullet list)
- Expected outcomes (bullet list)
- Project partners (with roles)
- Duration & budget (1 line)

**Quality check:** Fits on 1 page A4, compelling, clear, aligned with call

**Duration:** ~10 minutes

**Next command:** `@proposal-agent /outline`

---

### Command: @proposal-agent /outline

**Agent:** Outline Agent (Comprehensive Proposal Writer)

**Purpose:** Develop full project proposal (15-25 pages)

**Prerequisites:**
- Info page complete (`docs/project-info-page.md` exists)
- Call document available

**You say:**
```
@proposal-agent /outline
```

**With specific instructions:**
```
Create the full outline.
Emphasize: [innovation / impact / methodology / consortium strength]
Special sections needed: [e.g., "sustainability plan" / "gender equality"]
Page limit: [if different from 15-25]

@proposal-agent /outline
```

**Agent embodies this role:**
```
You are the OUTLINE AGENT - expert proposal writer.

You have mastered:
- Research proposal structure
- Evaluation criteria mapping
- Compelling narrative flow
- Academic and professional writing

Your task: Read tasks/create-outline.md and execute it.
```

**Agent reads:**
- `tasks/create-outline.md`
- `templates/project-outline-template.yaml`
- `docs/project-info-page.md` (expands on this)
- `call/[call-document].pdf` (ensures compliance)

**Agent produces:**
- `docs/project-outline.md` (15-25 pages)

**Sections created:**
1. Executive Summary
2. Context and Challenge (Background, Problem, Relevance)
3. Objectives and Approach (Goals, Methodology, Innovation)
4. Impact and Dissemination
5. Consortium and Resources
6. Work Plan (high-level)
7. Budget Overview
8. Risks and Quality Assurance
9. Ethics and Data Management

**Quality check:** Complete coverage, compelling narrative, evaluation criteria addressed

**Duration:** ~30-40 minutes

**Next command:** `@proposal-agent /work-packages`

---

### Command: @proposal-agent /work-packages

**Agent:** Work Package Agent (Project Management Expert)

**Purpose:** Define detailed work packages with tasks, deliverables, milestones

**Prerequisites:**
- Outline complete (`docs/project-outline.md` exists)

**You say:**
```
@proposal-agent /work-packages
```

**With specifications:**
```
Create detailed work packages.
Number of WPs: [e.g., 6]
Structure: [traditional / agile / other]
Special WP: [e.g., "Include dedicated WP for ethics"]

@proposal-agent /work-packages
```

**Agent embodies this role:**
```
You are the WORK PACKAGE AGENT - project management expert.

You excel at:
- Work breakdown structure
- Task sequencing and dependencies
- Deliverable definition
- Timeline planning
- Resource allocation

Your task: Read tasks/create-work-packages.md and execute it.
```

**Agent reads:**
- `tasks/create-work-packages.md`
- `templates/work-packages-template.yaml`
- `docs/project-outline.md` (work plan to detail)
- `docs/project-info-page.md` (objectives to map)

**Agent produces:**
- `docs/work-packages.md` (10-20 pages)

**For each WP, creates:**
- WP overview (lead, duration, person-months)
- Objectives (2-4 specific)
- Description of work (1-2 pages)
- Tasks (with leads, durations, dependencies)
- Deliverables (with types, dates, dissemination level)
- Milestones (with verification means)
- Risk analysis

**Also includes:**
- WP overview table (all WPs summary)
- Person-month allocation table (by partner, by WP)

**Quality check:** Logical structure, realistic timeline, clear dependencies

**Duration:** ~25-30 minutes

**Next command:** `@proposal-agent /budget`

---

### Command: @proposal-agent /budget

**Agent:** Budget Agent (Financial Planning Expert)

**Purpose:** Calculate comprehensive project budget

**Prerequisites:**
- Work packages complete (`docs/work-packages.md` exists with PM allocations)
- Call document with budget rules available

**You say:**
```
@proposal-agent /budget
```

**With cost parameters:**
```
Calculate the budget using:
- Professor rate: €[X]/hour
- Researcher rate: €[X]/hour  
- PhD rate: €[X]/hour
- Overhead: [X]%
- Special costs: [describe]

@proposal-agent /budget
```

**Agent embodies this role:**
```
You are the BUDGET AGENT - financial planning specialist.

You master:
- Research cost calculation
- Funding rules compliance
- Budget justification
- Cost-effectiveness analysis

Your task: Read tasks/create-budget.md and execute it.
```

**Agent reads:**
- `tasks/create-budget.md`
- `templates/budget-calculation-template.yaml`
- `docs/work-packages.md` (PM allocations to cost)
- `call/[call-document].pdf` (budget rules)

**Agent produces:**
- `docs/budget-calculation.md` (8-12 pages)

**Calculates:**
- **Personnel costs** (by staff category, by partner, by WP)
- **Travel costs** (consortium meetings, conferences, research visits)
- **Equipment** (with justification, >€1000 typically)
- **Other direct costs** (consumables, subcontracting, publications)
- **Indirect costs** (overhead, typically 25%)

**Provides:**
- Budget summary tables
- Detailed calculations per partner
- Cost justification narrative
- Compliance checklist

**Quality check:** Accurate math, realistic costs, well-justified, compliant

**Duration:** ~20-25 minutes

**Next command:** `@proposal-agent /review`

---

### Command: @proposal-agent /review

**Agent:** Quality Review Agent

**Purpose:** Final consistency and compliance check

**Prerequisites:**
- All main documents complete (overseer, info-page, outline, work-packages, budget)

**You say:**
```
@proposal-agent /review
```

**Agent checks:**
- Consistency across all documents
- Alignment with call requirements
- Budget matches work packages
- Timeline coherence
- Partner roles consistent
- Compliance issues
- Quality standards met

**Agent produces:**
- `docs/quality-review.md` (review report)

**Report includes:**
- Consistency findings
- Compliance checklist
- Issues to address
- Recommendations
- Final approval or required revisions

**Duration:** ~15 minutes

**Next command:** `@proposal-agent /export` (if all looks good)

---

## 🎯 Complete Workflow Example

Here's a realistic conversation flow:

```
=== Session Start ===

USER: [Uploads Erasmus_Plus_KA2_2026_Digital_Skills.pdf to call/ directory]

USER: @proposal-agent /help

CLAUDE: [Shows complete help with all commands]

USER: Great! Let me start.
      @proposal-agent /start

CLAUDE: ✓ Project proposal workflow initialized!
        
        Directory structure ready:
        - call/ (place funding call documents here) ✓
        - docs/ (outputs will go here)
        - templates/ (agent templates)
        - tasks/ (agent instructions)
        
        📋 Next step: Run @proposal-agent /overseer to analyze your call
        
        I see you've uploaded: Erasmus_Plus_KA2_2026_Digital_Skills.pdf
        Ready when you are!

USER: Perfect. This is for an Erasmus+ KA2 call about digital skills in 
      vocational training. Budget €350K, 30 months, need 5-6 partners.
      
      @proposal-agent /overseer

CLAUDE: # 🤖 Activating: Overseer Agent
        
        I am now the OVERSEER AGENT - your strategic project design expert.
        
        [Reads tasks/overseer-analysis.md]
        [Reads call/Erasmus_Plus_KA2_2026_Digital_Skills.pdf]
        [Analyzes requirements]
        
        === STRATEGIC ANALYSIS ===
        
        **Call Analysis:**
        - Priority: Digital transformation in VET
        - Key objectives: Skills development, innovation in pedagogy...
        [detailed analysis continues...]
        
        **Proposed Project Concept:**
        Title: "DigiTrain VET" - Digital Training Transformation...
        [complete strategy...]
        
        ✓ Saved to: docs/overseer-analysis.md
        ✓ Saved to: docs/project-strategy.md
        
        📋 Next: Run @proposal-agent /info-page

USER: Excellent analysis! Let's create the info page.
      Focus on innovation and industry partnerships.
      
      @proposal-agent /info-page

CLAUDE: # 🤖 Activating: Info Page Agent
        
        I am now the INFO PAGE AGENT - expert at concise, compelling summaries.
        
        [Reads task and templates]
        [Reviews overseer analysis]
        [Creates 1-page summary emphasizing innovation and partnerships]
        
        === PROJECT INFORMATION PAGE ===
        
        **Project Title:** DigiTrain VET: Digital Training Transformation...
        
        **Short Description:**
        DigiTrain VET revolutionizes vocational education by...
        [complete 1-pager follows...]
        
        ✓ Saved to: docs/project-info-page.md
        ✓ Length: 580 words (perfect fit for 1 page A4)
        
        📋 Next: Run @proposal-agent /outline

USER: @proposal-agent /status

CLAUDE: # 📊 Proposal Development Status
        
        ✅ Stage 1: Strategic Analysis (COMPLETE)
        ✅ Stage 2: Project Summary (COMPLETE)
        ⏳ Stage 3: Full Proposal (READY TO START)
        ⬜ Stage 4: Work Packages (PENDING)
        ⬜ Stage 5: Budget (PENDING)
        ⬜ Stage 6: Quality Review (PENDING)
        
        **Files Generated:**
        - docs/overseer-analysis.md (3,200 words)
        - docs/project-strategy.md (1,800 words)
        - docs/project-info-page.md (580 words)
        
        **Progress:** 33% complete
        **Next Command:** @proposal-agent /outline
        **Estimated Time to Completion:** ~90 minutes

USER: Great progress! Let's continue.
      @proposal-agent /outline

CLAUDE: # 🤖 Activating: Outline Agent
        
        I am now the OUTLINE AGENT - comprehensive proposal writer.
        
        [Detailed outline creation process...]
        [15-25 page proposal developed...]
        
        ✓ Saved to: docs/project-outline.md (18,500 words, ~23 pages)
        
        📋 Next: Run @proposal-agent /work-packages

[... workflow continues through all agents ...]

USER: @proposal-agent /review

CLAUDE: # 🤖 Activating: Quality Review Agent
        
        [Comprehensive review of all documents]
        
        === QUALITY REVIEW REPORT ===
        
        ✅ Consistency: Excellent - all documents aligned
        ✅ Budget-WP Match: Perfect - 98 PM allocated and costed
        ⚠️  Minor issue: Partner 3 role description slightly different
              in outline vs info page
        ✅ Call Compliance: 100% - all requirements addressed
        
        **Recommendation:** Address minor consistency issue, then ready
        
        ✓ Saved to: docs/quality-review.md

USER: Fix the Partner 3 description issue.

CLAUDE: ✓ Fixed! Partner 3 role now consistent across all documents.
        
        Your proposal is ready for export! 🎉
        
        Run @proposal-agent /export to generate final PDFs

=== Session Complete ===
```

---

## 💡 Pro Tips

### Iterating on Outputs

**You can re-run any agent to refine:**
```
USER: The info page is too technical. Make it more accessible.
      @proposal-agent /info-page

CLAUDE: [Recreates info page with simpler language]
```

### Providing Additional Context

**Give agents more to work with:**
```
USER: For the budget calculation, use these rates:
      - Professor: €72/hour (certified rate)
      - Researcher: €48/hour
      - PhD: €28/hour
      Also include €15K for external evaluation service.
      
      @proposal-agent /budget
```

### Asking for Variations

**Get alternatives:**
```
USER: Create two versions of the work package structure:
      1. Traditional (7 WPs with WP1=Management, WP7=Dissemination)
      2. Agile (4 WPs based on sprints)
      
      @proposal-agent /work-packages
```

### Quality Feedback

**If output isn't quite right:**
```
USER: The outline is good but Section 3 (Impact) needs strengthening.
      Add more on societal impact and long-term sustainability.
      
      Re-run @proposal-agent /outline focusing on Section 3
```

---

## ⚙️ Advanced Usage

### Custom Templates

**Point agent to modified template:**
```
USER: Use my custom template: templates/custom-outline-extended.yaml
      @proposal-agent /outline
```

### Multi-Call Comparison

**Analyze multiple calls:**
```
USER: Compare these two calls and recommend which to pursue:
      - call/Erasmus-KA2-2026.pdf
      - call/Horizon-WIDERA-2026.pdf
      
      @proposal-agent /overseer
```

### Partner-Specific Sections

**Focus on one partner:**
```
USER: Create detailed description for Partner 2 (Technical University Munich)
      Include: facilities, expertise, track record, specific role
      
      @proposal-agent /outline (Partner 2 section only)
```

---

## 🔄 Workflow Variations

### Quick Mode (Skip Some Steps)

**If you already have parts:**
```
Start at: @proposal-agent /work-packages
(if you already have outline from previous proposal)
```

### Deep Mode (Extra Iterations)

**Multiple refinement passes:**
```
1. @proposal-agent /outline (first draft)
2. Review and provide feedback
3. @proposal-agent /outline (revised version)
4. @proposal-agent /review (check consistency)
5. @proposal-agent /outline (final polish)
```

---

## 📞 Getting Help

### If Stuck

```
@proposal-agent /help
@proposal-agent /status
```

### If Agent Produces Wrong Output

```
USER: That wasn't right. Let me clarify:
      [provide specific instructions]
      
      Re-run: @proposal-agent /[command]
```

### If Need to Go Back

```
USER: Actually, let's revise the strategy first.
      @proposal-agent /overseer
      
      [Then continue forward from there]
```

---

## 🎓 Learning from Examples

**All skeleton files show realistic outputs:**
- `skeletons/example-project-info-page.md` - Perfect 1-pager
- `skeletons/example-work-package.md` - Complete WP2 with all elements
- `skeletons/example-budget-excerpt.md` - Detailed Partner 2 budget

**Study these before running agents to understand expected quality!**

---

## Summary: Command Quick Reference

| Purpose | Command |
|---------|---------|
| Get help | `@proposal-agent /help` |
| Initialize | `@proposal-agent /start` |
| Check progress | `@proposal-agent /status` |
| Analyze call | `@proposal-agent /overseer` |
| Create 1-pager | `@proposal-agent /info-page` |
| Full proposal | `@proposal-agent /outline` |
| Work packages | `@proposal-agent /work-packages` |
| Calculate budget | `@proposal-agent /budget` |
| Quality check | `@proposal-agent /review` |
| Export final | `@proposal-agent /export` |

---

**That's it! You're ready to write world-class proposals! 🚀**

Start with: `@proposal-agent /start`
