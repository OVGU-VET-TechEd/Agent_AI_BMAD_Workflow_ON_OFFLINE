# System Initialization Prompt for Claude/ChatGPT Sessions

## Copy-Paste This at Start of New Session

```
I'm using the Project Proposal Agent System to develop a funding proposal.

SYSTEM OVERVIEW:
- 5 specialized agents work sequentially
- Each agent reads tasks/ and templates/ directories
- Agents build on previous outputs in docs/
- Commands: @proposal-agent /[command-name]

AGENT ROLES:
1. Overseer Agent → Strategic analysis of funding call
2. Info Page Agent → 1-page project summary  
3. Outline Agent → Full proposal (15-25 pages)
4. Work Package Agent → Detailed WPs, tasks, deliverables
5. Budget Agent → Comprehensive budget calculation

WORKFLOW SEQUENCE:
@proposal-agent /start → /overseer → /info-page → /outline → /work-packages → /budget → /review

PROJECT DIRECTORY: project-proposal-workflow/

When I use @proposal-agent /[command], please:
1. Read the corresponding task file from tasks/[command].md
2. Load the template from templates/
3. Review any previous outputs from docs/
4. Fully embody that agent's role and expertise
5. Produce the specified output following quality criteria

Ready to begin!
```

---

## Alternative: Minimal Version

If you prefer minimal setup:

```
I'm using the Project Proposal Agent System.

Commands work like: @proposal-agent /overseer, @proposal-agent /info-page, etc.

When I invoke an agent, read its task file and embody that role completely.

Project directory: project-proposal-workflow/

Ready!
```

---

## For First-Time Use

**Complete initialization with workflow explanation:**

```
Hi! I'm using the Project Proposal Agent System to write a funding proposal.

This is a multi-agent workflow where each agent specializes in one part:

**Available Commands:**
- @proposal-agent /help → Show all commands
- @proposal-agent /start → Initialize project
- @proposal-agent /overseer → Analyze funding call (Agent 1)
- @proposal-agent /info-page → Create 1-page summary (Agent 2)
- @proposal-agent /outline → Full proposal (Agent 3)
- @proposal-agent /work-packages → Detailed WPs (Agent 4)
- @proposal-agent /budget → Budget calculation (Agent 5)
- @proposal-agent /review → Quality check (Agent 6)
- @proposal-agent /status → Check progress

**How It Works:**
When I say "@proposal-agent /overseer", you should:
1. Announce: "🤖 Activating: Overseer Agent"
2. Read: tasks/overseer-analysis.md (your instructions)
3. Review: templates/ and previous docs/ outputs
4. Embody: That agent's expertise and role completely
5. Execute: The task and produce specified output
6. Save: Output to docs/ directory
7. Handoff: Brief next agent on what to do

**My Funding Call:**
[Describe your call: program, topic, budget, duration, partners]

Let's start with: @proposal-agent /start
```

---

## Usage Example

**Session Start:**
```
USER: [Paste system initialization prompt above]

CLAUDE: Got it! The Project Proposal Agent System is activated.

I understand:
✓ 5 specialized agents working sequentially  
✓ Each reads tasks/, templates/, and docs/
✓ Commands use @proposal-agent /[command] format
✓ I embody each agent's full role when invoked

Project directory: project-proposal-workflow/

Ready to help you develop your funding proposal!

What's your first command?

USER: @proposal-agent /help

CLAUDE: # 🤖 Project Proposal Agent System - Help
[Shows complete help documentation]

USER: @proposal-agent /start

CLAUDE: ✓ Project initialized! 
Next: Upload your funding call document, then run @proposal-agent /overseer

USER: [Uploads Erasmus_Plus_KA2_Call.pdf]
      
      This is for digital skills in construction sector.
      Budget: €400K, 30 months, 6 partners.
      
      @proposal-agent /overseer

CLAUDE: # 🤖 Activating: Overseer Agent

I am now the OVERSEER AGENT - strategic project design expert with deep 
expertise in EU funding mechanisms and proposal development.

[Proceeds to read call, analyze, and produce strategic framework...]
```

---

## Tips for Best Results

### 1. Upload Workflow Package First
Before pasting system prompt, upload the project-proposal-workflow ZIP so Claude can access:
- Task files (tasks/*.md)
- Templates (templates/*.yaml)
- Examples (skeletons/*.md)

### 2. Be Specific About Your Call
When initializing, provide:
- Funding program name (Erasmus+, Horizon Europe, etc.)
- Topic/priority area
- Budget range
- Duration
- Partner requirements

### 3. Use Commands Consistently
Always use the @proposal-agent /[command] format so Claude knows to switch agent modes

### 4. Provide Context Between Commands
Between agent invocations, you can:
- Give feedback on outputs
- Provide additional requirements
- Ask clarifying questions
- Request revisions

### 5. Iterate Freely
Re-run any agent command if output needs refinement. Each run overwrites previous output in docs/

---

## What Claude Will Do

When properly initialized, Claude will:

**On @proposal-agent /help:**
- Display complete command reference
- Show workflow steps
- Provide usage tips

**On @proposal-agent /start:**
- Confirm directory structure
- Check for uploaded documents
- Suggest next command

**On @proposal-agent /[agent-command]:**
- Announce agent activation
- Read relevant task file
- Load templates
- Review previous outputs
- Embody agent role completely
- Execute task professionally
- Produce high-quality output
- Save to docs/ directory
- Suggest next step

**On @proposal-agent /status:**
- Show completed stages
- Indicate current progress
- Recommend next action
- List generated files

---

## Troubleshooting

**If Claude doesn't recognize commands:**
→ Re-paste the initialization prompt
→ Make sure workflow files are uploaded

**If output quality is low:**
→ Check that Claude has access to task files
→ Provide more specific requirements
→ Ask Claude to read the example skeleton files first

**If agents don't hand off properly:**
→ Run @proposal-agent /status to check what's complete
→ Ensure previous stages finished before moving forward
→ Verify outputs exist in docs/ directory

**If confused about workflow:**
→ Run @proposal-agent /help anytime
→ Refer to AGENT_COMMANDS_GUIDE.md for examples
→ Ask: "What should I do next?"

---

## Advanced: Custom Agent Behaviors

You can modify agent behavior by adding to initialization:

```
Additional instructions for all agents:
- Writing style: [academic/conversational/persuasive]
- Emphasis areas: [innovation/impact/methodology/partnerships]
- Special requirements: [open science/gender equality/sustainability]
- Institution context: [describe your university/organization]
- Constraints: [budget limits/partner restrictions/timeline]
```

**Example with customization:**
```
I'm using the Project Proposal Agent System.

[Standard initialization prompt]

CUSTOM INSTRUCTIONS:
- Writing style: Academic but accessible
- Emphasize: Strong industry partnerships and commercialization potential
- Required sections: Open Science practices, Gender Equality Plan
- Institution: Technical University of Munich, Engineering Faculty
- Constraints: Max 4 partners (Germany + 3 EU), €350K budget limit

My call: Horizon Europe Cluster 4, Digital Technologies for Manufacturing
Budget: Up to €3M (but we're requesting €350K for our scope)

@proposal-agent /start
```

---

## Ready to Start?

**3-Step Quick Start:**

1. **Upload workflow ZIP** to Claude
2. **Paste initialization prompt** (use Complete or Minimal version above)
3. **Run first command:** `@proposal-agent /start`

Then follow the sequential workflow through all agents! 🚀

---

**Good luck with your proposal! May the funding be with you! 💰📝**
