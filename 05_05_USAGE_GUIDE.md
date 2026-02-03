# Project Proposal Workflow System - Quick Reference Guide

## Overview

This workflow system transforms your teaching material generator into a comprehensive **Project Proposal Development System** with 5 specialized AI agents that work together to create complete funding proposals.

## System Architecture

### 🎯 Five Specialized Agents

1. **Overseer Agent** (Coordinator)
   - Analyzes funding calls
   - Creates project strategy
   - Ensures alignment with requirements
   - Guides all other agents

2. **Info Page Agent** (Summary Writer)
   - Creates 1-page project summary
   - Formats: Description, Objectives, Outputs, Outcomes, Partners
   - Maximum: 1 page A4 (~500-600 words)

3. **Outline Agent** (Proposal Writer)
   - Develops full project proposal (15-25 pages)
   - Sections: Context, Objectives, Impact, Consortium, Work Plan
   - Adapts to specific call requirements

4. **Work Package Agent** (Project Manager)
   - Defines detailed work packages (4-8 WPs)
   - Creates tasks, deliverables, milestones
   - Establishes timelines and dependencies

5. **Budget Agent** (Financial Planner)
   - Calculates staff costs by person-months
   - Computes travel, equipment, other costs
   - Applies overhead rates
   - Creates justification narratives

## Directory Structure

```
project-proposal-workflow/
├── README.md                          # Main documentation
├── call/                              # 📁 Place funding call documents here
│   └── README.md                      # Instructions for call documents
├── docs/                              # 📁 Generated proposal documents
│   ├── overseer-analysis.md          # Strategic analysis (Agent 1)
│   ├── project-info-page.md          # 1-page summary (Agent 2)
│   ├── project-outline.md            # Full proposal (Agent 3)
│   ├── work-packages.md              # WP descriptions (Agent 4)
│   └── budget-calculation.md         # Budget details (Agent 5)
├── templates/                         # 📋 YAML templates for each component
│   ├── project-info-page-template.yaml
│   ├── project-outline-template.yaml
│   ├── work-packages-template.yaml
│   └── budget-calculation-template.yaml
├── tasks/                            # 📝 Task definitions for each agent
│   ├── overseer-analysis.md
│   ├── create-info-page.md
│   ├── create-outline.md
│   ├── create-work-packages.md
│   └── create-budget.md
├── skeletons/                        # 📄 Example outputs (proof of concept)
│   ├── example-project-info-page.md
│   ├── example-work-package.md
│   └── example-budget-excerpt.md
└── assets/                           # Additional resources
    ├── templates/
    └── images/
```

## Workflow Sequence

### Step 1: Preparation
```
1. Unzip the workflow package
2. Place your funding call document in call/ directory
   Example: call/Erasmus-Plus-KA2-2026.pdf
3. Read call/README.md for guidance
```

### Step 2: Overseer Analysis (Agent 1)
```
Task: /overseer-analysis
Input: call/[your-call-document].pdf
Output: docs/overseer-analysis.md
        docs/project-strategy.md

Actions:
- Analyzes call requirements
- Extracts priorities and criteria
- Proposes project concept
- Recommends consortium
- Creates strategic framework
```

### Step 3: Info Page Creation (Agent 2)
```
Task: /create-info-page
Input: docs/overseer-analysis.md
Output: docs/project-info-page.md (1 page A4)

Sections:
✓ Project Title & Acronym
✓ Short Description (60 words)
✓ Main Objective (80 words)
✓ Specific Objectives (3-5 SMART)
✓ Key Outputs (bullet list)
✓ Expected Outcomes (bullet list)
✓ Project Partners (with roles)
✓ Duration & Budget (1 line)
```

### Step 4: Outline Development (Agent 3)
```
Task: /create-outline
Input: docs/project-info-page.md
       call/[call-document].pdf
Output: docs/project-outline.md (15-25 pages)

Sections:
1. Executive Summary
2. Context and Challenge
3. Objectives and Approach
4. Impact and Dissemination
5. Consortium and Resources
6. Work Plan (high-level)
7. Budget Overview
8. Risks and Quality
9. Ethics and Data Management
```

### Step 5: Work Packages Definition (Agent 4)
```
Task: /create-work-packages
Input: docs/project-outline.md
Output: docs/work-packages.md (10-20 pages)

For each WP:
✓ Objectives
✓ Description of work
✓ Tasks (with leads, duration, dependencies)
✓ Deliverables (with types and dates)
✓ Milestones (with verification)
✓ Person-months per partner
```

### Step 6: Budget Calculation (Agent 5)
```
Task: /create-budget
Input: docs/work-packages.md (PM allocations)
       call/[call-document].pdf (budget rules)
Output: docs/budget-calculation.md (8-12 pages)

Components:
✓ Staff costs (by category and PM)
✓ Travel costs (meetings, conferences)
✓ Equipment (with justification)
✓ Other costs (consumables, subcontracting)
✓ Indirect costs (overhead %)
✓ Budget justification narrative
```

## Key Features

### 1. Call-Specific Adaptation
The **Overseer Agent** reads your specific call document and:
- Extracts requirements automatically
- Maps your strengths to call priorities
- Ensures compliance throughout
- Adapts templates to call structure

### 2. Agent Handoffs
Each agent builds on previous work:
```
Overseer → Info Page:    Strategic direction, core concept
Info Page → Outline:     Objectives, positioning
Outline → Work Packages: Structure, deliverables framework
WP → Budget:            Resource requirements, PM allocations
```

### 3. Built-in Examples
Three skeleton files demonstrate outputs:
- `example-project-info-page.md`: DigiConstruct project (EU training)
- `example-work-package.md`: WP2 with full task breakdown
- `example-budget-excerpt.md`: Partner 2 budget detail

### 4. Template-Driven
YAML templates ensure consistency:
- Standardized sections
- Word count limits
- Required elements
- Quality criteria

## Customization Options

### Modify Templates
Edit YAML files in `templates/` to:
- Add custom sections
- Change word limits
- Adjust formatting
- Include institution-specific elements

### Adapt Tasks
Edit markdown files in `tasks/` to:
- Change agent instructions
- Add quality checkpoints
- Include specific requirements
- Adjust workflow steps

### Add Call-Specific Elements
In `call/` directory:
- Create subdirectories for different calls
- Add supplementary guidelines
- Include eligibility checklists

## Budget Calculation Details

### Standard Assumptions (Customizable)
```
Person-Month (PM): 140 productive hours
Working year: 1,720 hours (220 days × 8 hours - 10% buffer)
Overhead rate: 25% (standard EU, check your call)

Staff Categories (Example - adjust to your rates):
- Professor: €65-75/hour
- Researcher: €45-55/hour  
- PhD Student: €25-35/hour
- Technician: €35-45/hour
- Admin: €30-40/hour
```

### Cost Categories
1. **Personnel**: Staff salaries (typically 60-70% of budget)
2. **Travel**: Consortium meetings, conferences, research visits
3. **Equipment**: Items >€1,000 (check call threshold)
4. **Other Direct**: Consumables, subcontracting, publications
5. **Indirect**: Overhead (building, admin, infrastructure)

## Common Funding Programs

The system adapts to various programs:

### Erasmus+ (Education)
- Focus: Training, education, mobility
- Typical budget: €200K-€500K
- Duration: 24-36 months
- Funding rate: 80-100%

### Horizon Europe (Research)
- Focus: Research, innovation, technology
- Typical budget: €2M-€10M+
- Duration: 36-48 months
- Funding rate: 100% (RIA) or 70% (IA)

### National Programs
- Varies by country
- Specific templates often required
- Budget rules differ

## Quality Assurance

Each agent includes quality criteria:

**Overseer**: Comprehensive analysis, strategic insight
**Info Page**: One-page limit, compelling narrative
**Outline**: Full coverage, evaluation criteria alignment
**Work Packages**: Logical structure, realistic timeline
**Budget**: Accurate calculations, compliance

## Tips for Success

### 1. Start Early
Run the Overseer Agent as soon as call opens to:
- Identify gaps in expertise
- Plan consortium formation
- Assess competitiveness

### 2. Iterate
Use multiple passes:
- Draft → Review → Refine
- Get partner feedback at each stage
- Validate with industry/stakeholders

### 3. Maintain Consistency
Ensure alignment across all documents:
- Same objectives throughout
- Consistent partner roles
- Budget matches work plan
- Timeline coherence

### 4. Use Examples
Study the skeleton files to understand:
- Level of detail expected
- Writing style and tone
- Structure and formatting
- Quality standards

### 5. Customize Heavily
Adapt everything to your:
- Institutional context
- Consortium composition
- Call requirements
- Subject domain

## Integration with AI Agents

### Recommended AI Setup
When using with Claude, ChatGPT, or other LLMs:

**System Prompt**:
```
You are the [Agent Name] for project proposal development.
Read the task definition in tasks/[agent-task].md
Follow the template in templates/[template].yaml
Use previous outputs from docs/ as context
Produce output according to quality criteria
```

**Context Files**:
1. Relevant task definition
2. Applicable template
3. Previous agent outputs
4. Funding call excerpt

### Workflow Automation
You can automate the sequence:
```python
agents = [
    'overseer-analysis',
    'create-info-page', 
    'create-outline',
    'create-work-packages',
    'create-budget'
]

for agent_task in agents:
    # Load task definition
    # Load previous outputs
    # Run AI agent
    # Save output
    # Validate quality
```

## File Formats

### Input Formats Accepted
- **Call documents**: PDF, DOCX, TXT
- **Templates**: YAML
- **Tasks**: Markdown
- **Examples**: Markdown

### Output Formats Generated
- **Primary**: Markdown (.md)
- **Optional**: DOCX (convert from MD)
- **Optional**: PDF (export from MD/DOCX)
- **Optional**: Excel (for budgets)

## Version Control

The included `.gitignore` file protects:
- Confidential call materials
- Draft documents
- Partner internal notes
- API keys
- Large media files

Recommended Git workflow:
```bash
git init
git add .
git commit -m "Initial proposal setup"
git branch develop
# Work on develop branch
# Merge to main when ready
```

## Troubleshooting

### Issue: Agent produces wrong format
**Solution**: Check template YAML, ensure AI has access to it

### Issue: Budget doesn't match work packages
**Solution**: Re-run Budget Agent with updated WP person-months

### Issue: Outline too long/short
**Solution**: Adjust template page limits, review call requirements

### Issue: Call requirements unclear
**Solution**: Run Overseer Agent again with additional call documents

## Next Steps After Generation

1. **Review all outputs** for consistency
2. **Get partner input** at each stage
3. **Validate with stakeholders** (especially industry partners)
4. **Check compliance** against call requirements
5. **Professional editing** before submission
6. **Create final PDFs** following call formatting rules
7. **Submit on time** through official portal

## Advanced Features

### Multi-Call Management
Create call-specific subdirectories:
```
call/
├── erasmus-2026/
│   ├── main-call.pdf
│   └── guide.pdf
├── horizon-2027/
│   ├── work-programme.pdf
│   └── template.xlsx
```

### Partner Management
Add partner info files:
```
partners/
├── partner-1-profile.md
├── partner-2-cv.pdf
├── partner-3-facilities.md
```

### Template Library
Build your own templates:
```
assets/templates/
├── executive-summary-v2.yaml
├── impact-section-extended.yaml
├── custom-wp-structure.yaml
```

## Support and Updates

This is a **proof-of-concept system**. You can:
- Extend agents with new capabilities
- Add quality validation scripts  
- Create output formatters (MD → DOCX)
- Build web interface
- Integrate with project management tools

---

## Quick Command Reference

```bash
# Generate workflow system
python Project_Proposal_Workflow_Generator.py

# Navigate to workflow
cd project-proposal-workflow

# Add your call
cp ~/Downloads/call.pdf call/

# View structure
tree -L 2

# Edit templates
nano templates/project-info-page-template.yaml

# Check outputs
ls -lh docs/

# Create archive
zip -r proposal-backup.zip .
```

---

**Remember**: This is a framework and accelerator. The quality of your proposal still depends on:
- Strong project concept
- Excellent consortium
- Compelling narrative
- Realistic planning
- Competitive positioning

The agents help structure and organize - the strategic thinking is yours!

**Happy Proposal Writing! 🚀**
