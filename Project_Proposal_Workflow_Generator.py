#!/usr/bin/env python3
"""
Complete Project Proposal Workflow Generator
Creates all files (.yaml, .md, etc.) for the EU/Research Project Proposal workflow

Usage:
    python Project_Proposal_Workflow_Generator.py
    
This will create a 'project-proposal-workflow' directory with all necessary files.
"""

import os
import zipfile
from pathlib import Path
from datetime import datetime

def create_file_structure():
    """Create complete file structure with all templates and definitions"""
    
    base_dir = Path("project-proposal-workflow")
    
    # Define all files and their contents
    files = {
        # ===== README =====
        "README.md": """# Project Proposal Workflow System

This workflow system helps you develop comprehensive project proposals using AI agents.

## Overview

Five specialized agents work together to create a complete project proposal:

1. **Overseer Agent** - Coordinates the entire proposal development process
2. **Info Page Agent** - Creates concise 1-page project summary
3. **Outline Agent** - Develops full project proposal based on funding call
4. **Work Package Agent** - Defines detailed work packages and deliverables
5. **Budget Agent** - Calculates staff costs and project budget

## Directory Structure

```
project-proposal-workflow/
├── call/                    # Place your funding call documents here
│   └── [your-call].pdf
├── docs/                    # Generated proposal documents
│   ├── project-info-page.md
│   ├── project-outline.md
│   ├── work-packages.md
│   └── budget-calculation.md
├── templates/               # YAML templates for each component
├── tasks/                   # Task definitions for each agent
├── examples/                # Example outputs
└── skeletons/              # Skeleton/draft documents
```

## Workflow Steps

1. **Place call document** in `call/` directory
2. **Run overseer task**: Analyzes call and creates project strategy
3. **Run info-page task**: Creates 1-page project summary
4. **Run outline task**: Develops complete proposal outline
5. **Run work-packages task**: Defines WPs, tasks, and deliverables
6. **Run budget task**: Calculates costs and creates budget

## Getting Started

1. Add your funding call document to `call/` directory
2. Review templates in `templates/` for customization
3. Start with task: `/overseer-analysis`
4. Follow the sequential workflow through all agents

## Agent Handoffs

Each agent builds on previous outputs:
- Overseer → Info Page (strategic direction)
- Info Page → Outline (core objectives and scope)
- Outline → Work Packages (detailed structure)
- Work Packages → Budget (resource requirements)

Happy proposal writing! 📝
""",

        # ===== TEMPLATES =====
        "templates/project-info-page-template.yaml": """template:
  id: project-info-page-template
  name: "Project Info Page (1 Page A4)"
  version: 1.0
  output:
    format: markdown
    filename: docs/project-info-page.md
  title: "Project Information Page"
  max_length: "1 page A4 (approximately 500-600 words)"
  sections:
    - id: title
      title: Project Title
      template: "Official project title (concise and descriptive)"
      max_words: 15
    - id: acronym
      title: Project Acronym
      template: "Memorable acronym (if applicable)"
      max_words: 1
    - id: short-description
      title: Short Description
      template: >
        2-3 sentences capturing the essence of the project.
        What problem does it solve? What's innovative?
      max_words: 60
    - id: objective
      title: Main Objective
      template: >
        Primary goal of the project. What do you aim to achieve?
        Should align with call objectives.
      max_words: 80
    - id: specific-objectives
      title: Specific Objectives
      template: >
        3-5 concrete, measurable objectives.
        Use bullet points. Each should be SMART.
      format: bullet_list
    - id: outputs
      title: Key Outputs
      template: >
        Tangible deliverables and products.
        What will the project produce? (tools, methods, publications, etc.)
      format: bullet_list
    - id: outcomes
      title: Expected Outcomes
      template: >
        Impact and changes resulting from outputs.
        Benefits to stakeholders, society, science, industry.
      format: bullet_list
    - id: partners
      title: Project Partners
      template: >
        List of consortium partners with roles:
        - Lead Partner (Coordinator)
        - Partner 2: Role/expertise
        - Partner 3: Role/expertise
        Include country codes.
      format: structured_list
    - id: duration-budget
      title: Duration & Budget
      template: "Duration: XX months | Total Budget: €XXX,XXX"
      max_words: 20
""",

        "templates/project-outline-template.yaml": """template:
  id: project-outline-template
  name: "Complete Project Proposal Outline"
  version: 1.0
  output:
    format: markdown
    filename: docs/project-outline.md
  title: "Project Proposal Outline"
  inputs:
    - call/[funding-call-document]
    - docs/project-info-page.md
  sections:
    - id: executive-summary
      title: Executive Summary
      template: >
        Comprehensive overview (1-2 pages):
        - Context and challenge
        - Project approach and innovation
        - Expected impact
        - Consortium strength
    - id: context-challenge
      title: "1. Context and Challenge"
      subsections:
        - id: background
          title: "1.1 Background"
          template: "State of the art, current gaps, needs"
        - id: problem-statement
          title: "1.2 Problem Statement"
          template: "Clear articulation of the problem to be addressed"
        - id: relevance
          title: "1.3 Relevance to Call"
          template: "Direct alignment with call priorities and scope"
    - id: objectives-approach
      title: "2. Objectives and Approach"
      subsections:
        - id: overall-objective
          title: "2.1 Overall Objective"
          template: "Main goal aligned with call"
        - id: specific-objectives
          title: "2.2 Specific Objectives"
          template: "Detailed SMART objectives (usually 3-6)"
        - id: methodology
          title: "2.3 Methodology and Approach"
          template: "How will objectives be achieved? Methods, frameworks"
        - id: innovation
          title: "2.4 Innovation and Beyond State-of-Art"
          template: "What's novel? How does it advance the field?"
    - id: impact-dissemination
      title: "3. Impact and Dissemination"
      subsections:
        - id: expected-impact
          title: "3.1 Expected Impact"
          template: "Scientific, societal, economic impact"
        - id: target-groups
          title: "3.2 Target Groups and Stakeholders"
          template: "Who will benefit? How will they be engaged?"
        - id: dissemination
          title: "3.3 Dissemination and Exploitation"
          template: "Communication strategy, publications, IP management"
        - id: sustainability
          title: "3.4 Sustainability"
          template: "How will results be sustained after project end?"
    - id: consortium
      title: "4. Consortium and Resources"
      subsections:
        - id: partner-overview
          title: "4.1 Partner Overview"
          template: "Brief description of each partner and their role"
        - id: expertise-complementarity
          title: "4.2 Expertise and Complementarity"
          template: "How partners complement each other"
        - id: management-structure
          title: "4.3 Management Structure"
          template: "Project governance, decision-making, coordination"
    - id: work-plan
      title: "5. Work Plan (High-Level)"
      template: >
        Overview of work packages and timeline.
        Detailed WP descriptions follow in separate document.
    - id: budget-overview
      title: "6. Budget Overview"
      template: >
        High-level budget summary.
        Detailed calculations in separate budget document.
    - id: risks-quality
      title: "7. Risks and Quality Assurance"
      subsections:
        - id: risk-analysis
          title: "7.1 Risk Analysis"
          template: "Key risks and mitigation strategies"
        - id: quality-assurance
          title: "7.2 Quality Assurance"
          template: "Quality control measures and standards"
    - id: ethics-data
      title: "8. Ethics and Data Management"
      subsections:
        - id: ethical-considerations
          title: "8.1 Ethical Considerations"
          template: "Ethics issues and how they'll be addressed"
        - id: data-management
          title: "8.2 Data Management"
          template: "Data handling, FAIR principles, security"
""",

        "templates/work-packages-template.yaml": """template:
  id: work-packages-template
  name: "Work Packages Definition"
  version: 1.0
  output:
    format: markdown
    filename: docs/work-packages.md
  title: "Work Package Descriptions"
  inputs:
    - docs/project-outline.md
    - docs/project-info-page.md
  sections:
    - id: wp-overview
      title: Work Package Overview
      template: >
        Table summarizing all WPs:
        - WP number, title, lead partner
        - Start/end months
        - Person-months per partner
    - id: wp-detailed
      title: Detailed Work Package Descriptions
      template: >
        For each WP (typically 4-8 WPs):
        
        ## WP{{number}}: {{title}}
        
        **Lead Partner**: {{lead}}
        **Duration**: Month {{start}} - Month {{end}}
        **Total Person-Months**: {{pm}}
        
        ### Objectives
        - List specific WP objectives
        
        ### Description of Work
        Detailed description of activities and tasks
        
        ### Tasks
        - Task {{wp}}.1: {{task_title}}
          - Description
          - Lead: {{partner}}
          - Duration: M{{start}}-M{{end}}
        
        ### Deliverables
        - D{{wp}}.1: {{deliverable_title}} (M{{month}}, {{type}}, {{dissemination}})
        
        ### Milestones
        - MS{{number}}: {{milestone_description}} (M{{month}})
        
        ### Dependencies
        - Inputs from other WPs
        - Critical path elements
""",

        "templates/budget-calculation-template.yaml": """template:
  id: budget-calculation-template
  name: "Budget Calculation"
  version: 1.0
  output:
    format: markdown
    filename: docs/budget-calculation.md
  title: "Project Budget Calculation"
  inputs:
    - docs/work-packages.md
    - call/[funding-call-document]
  sections:
    - id: budget-summary
      title: Budget Summary Table
      template: >
        | Partner | Personnel | Travel | Equipment | Other | Indirect | Total |
        |---------|-----------|--------|-----------|-------|----------|-------|
    - id: personnel-costs
      title: "1. Personnel Costs"
      subsections:
        - id: staff-categories
          title: "1.1 Staff Categories and Rates"
          template: >
            Define staff categories per partner:
            - Senior Researcher: €XX/hour
            - Researcher: €XX/hour
            - PhD Student: €XX/hour
            - Technician: €XX/hour
        - id: person-months-breakdown
          title: "1.2 Person-Month Breakdown by WP"
          template: >
            Table showing PM allocation:
            - By partner
            - By WP
            - By staff category
        - id: personnel-calculation
          title: "1.3 Personnel Cost Calculation"
          template: >
            Calculation methodology:
            Person-months × hours/month × hourly rate
            Standard: 1 PM = 140 hours (or per call rules)
    - id: travel-costs
      title: "2. Travel and Subsistence"
      template: >
        - Project meetings: {{number}} meetings × {{participants}} × €{{cost}}
        - Conferences: {{number}} × €{{cost}}
        - Research visits: Details
        - Dissemination events: Details
    - id: equipment-costs
      title: "3. Equipment and Infrastructure"
      template: >
        List major equipment items:
        - Item description, justification, cost
        - Depreciation if applicable
        - Only items > €1,000 (or per call rules)
    - id: other-costs
      title: "4. Other Direct Costs"
      template: >
        - Consumables: €{{amount}}
        - Subcontracting: €{{amount}} (specify services)
        - Publishing costs: €{{amount}}
        - Other: Specify
    - id: indirect-costs
      title: "5. Indirect Costs (Overheads)"
      template: >
        Calculated as % of direct costs (typically 25%)
        Per partner based on call rules
    - id: budget-justification
      title: "6. Budget Justification"
      template: >
        Narrative explaining:
        - Why resources are necessary
        - How they relate to work plan
        - Cost-effectiveness considerations
""",

        # ===== TASKS =====
        "tasks/overseer-analysis.md": """# Task: overseer-analysis

## Purpose
**Overseer Agent** analyzes the funding call and creates an overarching project strategy.
This agent coordinates the entire proposal development process and ensures alignment with call requirements.

## Agent Role
You are the **Project Proposal Overseer Agent**. You have deep expertise in EU/research funding mechanisms,
proposal writing, and project design. You analyze funding calls strategically and guide the proposal
development process from start to finish.

## Inputs
- Funding call document from `call/` directory
- Call-specific requirements (eligibility, budget limits, duration, priorities)

## Output
- `docs/overseer-analysis.md` (Strategic analysis document)
- `docs/project-strategy.md` (High-level project strategy)

## Steps

### 1. Call Analysis
- Read and analyze the complete funding call document
- Extract key information:
  - Call objectives and priorities
  - Eligibility criteria
  - Budget limits and funding rates
  - Duration constraints
  - Required deliverables and milestones
  - Evaluation criteria and weightings
  - Submission deadlines

### 2. Strategic Assessment
- Identify strategic opportunities within the call
- Map institutional strengths to call priorities
- Highlight potential innovation angles
- Assess competitiveness factors

### 3. Project Framework Design
- Propose high-level project concept
- Suggest potential project title and acronym
- Outline main objectives (3-5)
- Identify required expertise areas
- Recommend consortium composition

### 4. Resource Planning
- Estimate overall budget envelope
- Suggest project duration
- Propose work package structure (4-8 WPs)
- Identify critical resources needed

### 5. Risk and Compliance Check
- Flag potential eligibility issues
- Identify compliance requirements
- Note ethical considerations
- Highlight critical success factors

### 6. Handoff Preparation
- Create strategic brief for Info Page Agent
- Define key messages and positioning
- Establish evaluation criteria alignment
- Set quality standards for proposal

## Output Format

Document should include:
- **Executive Brief**: One-paragraph call summary
- **Strategic Analysis**: Opportunities and competitive positioning
- **Project Concept**: High-level project idea
- **Consortium Recommendations**: Required expertise and potential partners
- **Resource Framework**: Budget and timeline guidance
- **Compliance Checklist**: Key requirements to address
- **Next Steps**: Clear instructions for Info Page Agent

## Quality Criteria
- Comprehensive call understanding
- Strategic insight and innovation
- Realistic resource assessment
- Clear guidance for subsequent agents
- Compliance awareness

## Handoff to Next Agent
Pass to **Info Page Agent** with:
- Strategic project concept
- Core objectives and innovation angles
- Budget and timeline constraints
- Key evaluation criteria to address
""",

        "tasks/create-info-page.md": """# Task: create-info-page

## Purpose
Creates the **Project Information Page** (1-page A4 format).
Concise summary including short description, objectives, outputs, outcomes, and partners.

## Agent Role
You are the **Info Page Agent**. You excel at distilling complex project concepts into clear,
compelling one-page summaries. You understand how to hook reviewers' interest immediately
and communicate value proposition effectively.

## Inputs
- Strategic analysis from `docs/overseer-analysis.md`
- Project concept from `docs/project-strategy.md`
- Funding call objectives and priorities

## Output
- `docs/project-info-page.md` (Markdown file, max 1 page A4)
- Structure based on `templates/project-info-page-template.yaml`

## Steps

### 1. Craft Project Title
- Create compelling, descriptive title
- Maximum 15 words
- Include key terms from call
- Consider: What would make reviewers interested?

### 2. Design Project Acronym
- Memorable and relevant acronym
- Relates to project theme
- Easy to pronounce
- Check: Not already used in similar contexts

### 3. Write Short Description (60 words)
- Hook: What's the problem/opportunity?
- Solution: Your innovative approach
- Value: What's unique/impactful?
- Use active voice, avoid jargon

### 4. Define Main Objective (80 words)
- Single overarching goal
- Align with call's main objective
- Measurable and achievable
- Clear benefit statement

### 5. Specify 3-5 Specific Objectives
- SMART objectives (Specific, Measurable, Achievable, Relevant, Time-bound)
- Each 1-2 sentences
- Numbered list
- Each addresses different aspect of main objective

### 6. List Key Outputs
- Tangible deliverables (tools, methods, guidelines, publications)
- 4-6 bullet points
- Concrete and specific
- Match call's expected outcomes

### 7. Describe Expected Outcomes
- Impact and changes from outputs
- Benefits to stakeholders
- Scientific/societal/economic value
- 4-6 bullet points

### 8. Define Consortium Partners
- List all partners with:
  - Organization name and country code
  - Role in project (Coordinator/Partner)
  - Key expertise contribution
- Demonstrate complementarity and coverage

### 9. Specify Duration and Budget
- Total project duration (months)
- Total budget (€)
- Funding rate if relevant
- One concise line

## Quality Criteria
- Fits on 1 page A4 (500-600 words)
- Clear and compelling language
- Perfect alignment with call
- No jargon or acronyms without explanation
- Professional formatting
- Error-free

## Handoff to Next Agent
Pass to **Outline Agent** with:
- Approved project info page
- Core messaging and positioning
- Objectives to expand in detail
- Consortium structure to elaborate
""",

        "tasks/create-outline.md": """# Task: create-outline

## Purpose
Creates the **Complete Project Proposal Outline**.
Develops full proposal structure based on funding call requirements.

## Agent Role
You are the **Outline Agent**. You are an expert proposal writer with deep knowledge of
research funding mechanisms. You create comprehensive, well-structured proposals that
address all evaluation criteria and tell a compelling story.

## Inputs
- Project info page from `docs/project-info-page.md`
- Funding call document from `call/`
- Strategic analysis from `docs/overseer-analysis.md`
- Call-specific proposal template/structure

## Output
- `docs/project-outline.md` (Complete proposal outline, 15-25 pages)
- Structure based on `templates/project-outline-template.yaml`
- Adapted to specific call requirements

## Steps

### 1. Call Structure Analysis
- Identify required proposal sections from call
- Note page limits per section
- Map evaluation criteria to sections
- Understand scoring/weighting

### 2. Executive Summary
- Comprehensive overview (1-2 pages)
- Cover: Context, approach, innovation, impact, consortium
- Can stand alone - reviewers may read only this
- Write LAST (after all other sections)

### 3. Section 1: Context and Challenge
**1.1 Background**
- State of the art in field
- Current approaches and limitations
- Market/policy context if relevant

**1.2 Problem Statement**
- Clear articulation of problem
- Why is it important? Who is affected?
- Quantify impact of problem if possible

**1.3 Relevance to Call**
- Direct mapping to call priorities
- Quote specific call objectives
- Show perfect fit

### 4. Section 2: Objectives and Approach
**2.1 Overall Objective**
- Single main goal
- Aligned with call's overall objective
- Ambitious yet achievable

**2.2 Specific Objectives**
- 3-6 SMART objectives
- Each linked to call priorities
- Logical progression

**2.3 Methodology and Approach**
- How will objectives be achieved?
- Methods, frameworks, standards
- Work flow and interdependencies
- Innovation in methodology

**2.4 Innovation and Beyond State-of-Art**
- What's novel in your approach?
- How does it advance beyond current practice?
- Breakthrough potential
- Risk and ambition

### 5. Section 3: Impact and Dissemination
**3.1 Expected Impact**
- Scientific impact: Publications, new knowledge
- Societal impact: Benefits to society
- Economic impact: Market potential, efficiency gains
- Map to call's expected impacts

**3.2 Target Groups and Stakeholders**
- Who will benefit?
- How will they be engaged?
- Letters of support if required

**3.3 Dissemination and Exploitation**
- Communication strategy
- Publication plan (Open Access)
- IP management and exploitation
- Sustainability after project

**3.4 Sustainability**
- How will results persist?
- Business model if relevant
- Scaling potential

### 6. Section 4: Consortium and Resources
**4.1 Partner Overview**
- 1-2 paragraphs per partner
- Expertise, track record, facilities
- Specific role in project

**4.2 Expertise and Complementarity**
- Coverage of all needed expertise
- No gaps or overlaps
- Synergies and added value

**4.3 Management Structure**
- Governance bodies (Steering Committee, etc.)
- Decision-making processes
- Coordination mechanisms
- Communication plan

### 7. Section 5: Work Plan (High-Level)
- Overview of work package structure
- Gantt chart or timeline
- Dependencies and critical path
- Note: Detailed WPs in separate document

### 8. Section 6: Budget Overview
- Total budget and breakdown by category
- Budget per partner
- Cost-effectiveness narrative
- Note: Detailed budget in separate document

### 9. Section 7: Risks and Quality
**7.1 Risk Analysis**
- Identify 5-8 key risks
- For each: description, probability, impact, mitigation
- Show proactive management

**7.2 Quality Assurance**
- Quality standards to be applied
- Review processes
- Validation methods

### 10. Section 8: Ethics and Data
**8.1 Ethical Considerations**
- Ethics self-assessment
- Issues identified and how addressed
- Ethics approvals needed

**8.2 Data Management**
- FAIR data principles
- Data Management Plan outline
- Security and privacy
- Open data commitments

## Quality Criteria
- Complete coverage of all call requirements
- Compelling narrative flow
- Clear alignment with evaluation criteria
- Professional, error-free writing
- Appropriate use of figures/tables
- Within page limits
- Consistent with info page

## Handoff to Next Agent
Pass to **Work Package Agent** with:
- Approved outline
- Work package structure (number and titles)
- Objectives to be distributed across WPs
- Deliverables and milestones framework
""",

        "tasks/create-work-packages.md": """# Task: create-work-packages

## Purpose
Creates **Detailed Work Package Descriptions** with tasks, deliverables, and milestones.
Transforms high-level outline into concrete, actionable work plan.

## Agent Role
You are the **Work Package Agent**. You are an expert project manager with deep experience
in structuring research and innovation projects. You design clear, logical work plans with
well-defined tasks, realistic timelines, and meaningful deliverables.

## Inputs
- Project outline from `docs/project-outline.md`
- Project info page from `docs/project-info-page.md`
- Call requirements for work packages
- Budget constraints from overseer analysis

## Output
- `docs/work-packages.md` (Detailed WP descriptions, 10-20 pages)
- Structure based on `templates/work-packages-template.yaml`

## Steps

### 1. Work Package Architecture
Typical structure includes:
- **WP1: Project Management** (always)
- **WP2-WPn: Core Technical/Research WPs** (4-6 WPs)
- **WP(n+1): Dissemination and Exploitation** (usually)

Each WP should:
- Have clear objective(s)
- Be assignable to one lead partner
- Be manageable in scope
- Have defined deliverables
- Align with project objectives

### 2. WP Overview Table
Create summary table:
```
| WP | Title | Lead | Start | End | Total PM |
|----|-------|------|-------|-----|----------|
| WP1 | Management | P1 | M1 | M36 | 18 |
| WP2 | ... | P2 | M1 | M24 | 45 |
```

Include person-months per partner per WP:
```
| WP | P1 | P2 | P3 | P4 | Total |
|----|----|----|----|----|-------|
| WP1 | 8 | 4 | 3 | 3 | 18 |
```

### 3. For Each Work Package

#### WP Header
- **WP Number and Title**: WP1: Project Management and Coordination
- **Lead Partner**: Partner name
- **Duration**: Month X - Month Y
- **Total Person-Months**: XX PM
- **Participating Partners**: List all

#### Objectives
List 2-4 specific WP objectives:
- What will this WP achieve?
- How does it contribute to project objectives?
- Use action verbs

#### Description of Work
Narrative description (1-2 pages):
- Context and approach
- Key activities
- Methods and tools
- Interdependencies with other WPs
- Innovation elements

#### Tasks Breakdown
For each task within WP:
- **Task X.1: [Task Title]**
  - Description (2-3 paragraphs)
  - Lead: Partner X
  - Contributing partners: Y, Z
  - Duration: MX-MY
  - Dependencies: Links to other tasks

Example:
```
**Task 2.1: Requirements Analysis and Specification**
Conduct comprehensive analysis of stakeholder needs and technical requirements.
Includes literature review, stakeholder interviews, and expert consultations.
Results will feed into design phase (Task 2.2).

- Lead: P2
- Contributing: P1, P3
- Duration: M1-M6
- Dependencies: Kickoff (MS1)
```

#### Deliverables
List all deliverables:
- **D[WP].[N]: [Deliverable Title]** (M[X], [Type], [Dissemination Level])
  - Brief description
  - Quality criteria

Types: Report (R), Demonstrator (DEM), Data set (DATA), Website (WEB), etc.
Dissemination: Public (PU), Confidential (CO), Restricted (RE)

Example:
```
- **D2.1: Requirements Specification Document** (M6, R, PU)
  - Comprehensive specification of user and technical requirements
  - Includes use cases and acceptance criteria
  - Quality: Reviewed by all partners and stakeholders
```

#### Milestones
Key checkpoints:
- **MS[N]: [Milestone Description]** (M[X])
  - Verification means (how you know it's achieved)

Example:
```
- **MS3: Requirements Validated** (M6)
  - Means of verification: D2.1 approved by all partners and 
    stakeholder validation workshop completed
```

#### Risk and Dependencies
- Dependencies on other WPs or external factors
- Risks specific to this WP
- Brief mitigation notes

### 4. Special Considerations

**WP1: Management**
- Typical tasks: Coordination, reporting, quality assurance, ethics, IPR
- Usually 5-8% of total PM
- Lead always coordinator

**Technical/Research WPs**
- Each should be substantive (not too fragmented)
- Balance across partners
- Clear progression and dependencies

**Dissemination/Exploitation WP**
- Communication activities
- Stakeholder engagement
- Exploitation planning
- Usually runs entire project duration

### 5. Internal Consistency Checks
- Sum of PM per WP matches budget
- All project objectives covered by WPs
- Timeline logical (no impossible dependencies)
- Deliverables sufficient for demonstrating progress
- Milestones at logical decision points
- Balanced workload across partners and time

## Quality Criteria
- Clear, logical WP structure
- Realistic and detailed task descriptions
- Meaningful deliverables (not just "reports")
- Achievable milestones
- Proper dependencies identified
- Consistent with budget and timeline
- Professional formatting

## Handoff to Next Agent
Pass to **Budget Agent** with:
- Person-month breakdown per partner per WP
- Equipment and resource needs identified in WP descriptions
- Travel requirements (meetings, conferences)
- Subcontracting needs if any
""",

        "tasks/create-budget.md": """# Task: create-budget

## Purpose
Creates **Detailed Budget Calculation** with staff costs, travel, equipment, and other costs.
Transforms person-month allocations into comprehensive financial plan.

## Agent Role
You are the **Budget Agent**. You are an expert in research project financial planning
and EU/research funding rules. You create accurate, justified, and compliant budgets
that optimize resource use while meeting all project needs.

## Inputs
- Work packages from `docs/work-packages.md` (PM allocations)
- Project outline from `docs/project-outline.md`
- Funding call budget rules and eligible costs
- Partner cost information (hourly rates, overhead rates)

## Output
- `docs/budget-calculation.md` (Detailed budget, 8-12 pages)
- Structure based on `templates/budget-calculation-template.yaml`
- Excel spreadsheet: `docs/budget-detailed.xlsx` (optional but recommended)

## Steps

### 1. Understand Funding Rules
From call document, extract:
- Eligible cost categories
- Funding rate (e.g., 100%, 70%, or other)
- Overhead calculation method (typically 25% of direct costs)
- Specific restrictions (max amounts, categories)
- Audit and compliance requirements

### 2. Budget Summary Table
Create overview:
```markdown
| Partner | Personnel | Travel | Equipment | Other | Subtotal | Indirect (25%) | Total | Funding |
|---------|-----------|--------|-----------|-------|----------|----------------|-------|---------|
| P1 (Lead) | €180,000 | €15,000 | €20,000 | €10,000 | €225,000 | €56,250 | €281,250 | €281,250 |
| P2 | €200,000 | €12,000 | €0 | €8,000 | €220,000 | €55,000 | €275,000 | €275,000 |
| ... | | | | | | | | |
| **Total** | €XXX | €XXX | €XXX | €XXX | €XXX | €XXX | €XXX | €XXX |
```

### 3. Personnel Costs

#### 3.1 Define Staff Categories per Partner
```markdown
**Partner 1: [Organization Name]**
- Professor/Senior Researcher: €75/hour
- Researcher (Postdoc): €55/hour
- PhD Student: €30/hour
- Project Manager: €65/hour
- Technician: €40/hour

[Basis: Institutional rates, national standards, or certified cost methodology]
```

#### 3.2 Person-Month Breakdown Table
```markdown
| WP | Role | P1 | P2 | P3 | Total PM |
|----|------|----|----|----|----- |
| WP1 | PM | 6 | 2 | - | 8 |
| WP1 | Admin | 2 | - | - | 2 |
| WP2 | Senior Res | 8 | 10 | 12 | 30 |
| WP2 | PhD | 6 | 12 | 18 | 36 |
| ... | | | | | |
```

#### 3.3 Personnel Cost Calculation
For each partner:
```markdown
**Partner 1 Personnel Costs:**

| Staff Category | PM | Hours/PM | Rate (€/h) | Total (€) |
|----------------|----|---------|-----------| ---------|
| Senior Researcher | 14 | 140 | 75 | 147,000 |
| Researcher | 8 | 140 | 55 | 61,600 |
| PhD Student | 18 | 140 | 30 | 75,600 |
| Project Manager | 8 | 140 | 65 | 72,800 |
| **Subtotal Personnel P1** | **48** | | | **€357,000** |

Calculation: PM × 140 hours/PM × hourly rate
(Note: Standard 1 PM = 140 productive hours, or as per call rules)
```

### 4. Travel and Subsistence

#### 4.1 Project Meetings
```markdown
**Consortium Meetings**
- Number of meetings: 6 (one every 6 months)
- Participants per meeting: Average 2 per partner × 5 partners = 10
- Cost per participant: €800 (€600 travel + €200 accommodation/meals)
- Total: 6 × 10 × €800 = €48,000

Breakdown by partner:
- P1: €9,600 (2 people × 6 meetings × €800)
- P2: €9,600
- ...
```

#### 4.2 Conferences and Dissemination
```markdown
**Conference Participation**
- Number of conferences: 8 (2 per year, different partners)
- Average cost: €1,500 per conference (registration €500 + travel/stay €1,000)
- Total: 8 × €1,500 = €12,000

- P1: €4,500 (3 conferences)
- P2: €4,500 (3 conferences)
- P3: €3,000 (2 conferences)
```

#### 4.3 Research Visits/Secondments
If applicable:
```markdown
**Research Visits**
- PhD exchange between P2 and P3: 1 month
- Cost: €2,500 (travel + subsistence)
```

**Total Travel Budget: €XX,XXX**

### 5. Equipment and Infrastructure

List major items (typically >€1,000):
```markdown
**Partner 1:**
- High-performance Computing Server: €15,000
  - Justification: Required for data processing in WP3
  - Specifications: [details]
  - Depreciation: If >€5,000, may need to calculate depreciation
  
- Specialized Software Licenses: €5,000
  - Justification: Analysis tools for WP4 and WP5

**Partner 2:**
- Laboratory Equipment: €25,000
  - Justification: Testing and validation in WP6
  - [Details]

**Total Equipment: €45,000**

Note: Only direct project use. General office equipment not eligible.
```

### 6. Other Direct Costs

#### 6.1 Consumables
```markdown
**Consumables and Supplies**
- Lab materials (P2): €8,000 over 36 months
- Office supplies (all partners): €3,000
- Printing and copying: €2,000
**Total Consumables: €13,000**
```

#### 6.2 Subcontracting
```markdown
**Subcontracting Services**
- User testing and validation (external company): €20,000
  - Justification: Specialized expertise not available in consortium
  - WP5, M18-M24
  
- Professional translation services: €5,000
  - Justification: Dissemination materials in 5 languages

**Total Subcontracting: €25,000**

Note: Subcontracting must be justified (expertise not in consortium) 
and should not exceed 25-30% of direct costs.
```

#### 6.3 Other Costs
```markdown
**Publication Costs**
- Open Access publications: €10,000 (5 articles × €2,000 average APC)
- Conference proceedings: €3,000

**Audit Costs** (if required):
- External audit (if total >€750k): €15,000

**Ethics and Legal**
- Ethics board reviews: €3,000
- Legal advice on IPR: €5,000

**Total Other Costs: €XX,XXX**
```

### 7. Indirect Costs (Overheads)

```markdown
**Indirect Costs Calculation**

Indirect costs cover:
- General administration
- Premises (heating, electricity, rent)
- IT infrastructure
- Libraries
- Human resources departments
- Finance and accounting

Calculation: 25% of direct eligible costs (standard EU rate)

| Partner | Direct Costs | Indirect (25%) | Total |
|---------|-------------|----------------|-------|
| P1 | €450,000 | €112,500 | €562,500 |
| P2 | €380,000 | €95,000 | €475,000 |
| ... | | | |
| **Total** | €X,XXX,XXX | €XXX,XXX | €X,XXX,XXX |

Note: Some funding schemes use different overhead rates or calculation methods.
Check call-specific rules.
```

### 8. Total Budget Summary

```markdown
## Final Budget Summary

| Cost Category | Amount (€) | % of Total |
|---------------|-----------|------------|
| Personnel | 1,200,000 | 65% |
| Travel | 65,000 | 4% |
| Equipment | 45,000 | 2% |
| Other Direct | 85,000 | 5% |
| **Subtotal Direct** | **1,395,000** | **76%** |
| Indirect (25%) | 348,750 | 24% |
| **TOTAL** | **1,743,750** | **100%** |

**Requested Funding**: €1,743,750 (100% funding rate)

Distribution by Partner:
- P1 (Coordinator): €562,500 (32%)
- P2: €475,000 (27%)
- P3: €380,000 (22%)
- P4: €326,250 (19%)
```

### 9. Budget Justification Narrative

For each major budget category, explain:
- **Why necessary**: How does it support project objectives?
- **Realism**: Are costs realistic and competitive?
- **Efficiency**: Are resources used optimally?
- **Compliance**: Do costs meet funding rules?

Example:
```markdown
## Budget Justification

### Personnel Costs (€1,200,000 - 69% of direct costs)
The personnel budget reflects the high intellectual input required for this research project.
The allocation of 112 person-months across 36 months ensures adequate expertise while maintaining
cost-efficiency. Senior researchers (30% of PM) provide scientific leadership and methodology
development, while PhD students (40% of PM) conduct core research activities. Project management
(8% of PM) ensures effective coordination. All rates are based on certified institutional cost models.

### Travel (€65,000)
Travel budget supports essential collaboration (semi-annual consortium meetings) and dissemination
(conference presentations of results). The project's international nature requires face-to-face
coordination to ensure quality. Conference presentations are crucial for scientific validation
and impact. Costs are calculated conservatively based on average EU travel expenses.

[Continue for each category...]
```

### 10. Cost-Effectiveness Analysis

```markdown
## Cost-Effectiveness

- **Cost per expected output**: €XXX,XXX per major deliverable
- **Benchmarking**: Compared to similar projects, budget is X% lower/comparable
- **Value for money**: Expected impact justifies investment
- **Efficiency measures**:
  - Use of existing infrastructure where possible
  - Shared resources across WPs
  - Leveraging partner in-kind contributions
  - Open-source tools to minimize licensing costs
```

### 11. Budget Compliance Checklist

```markdown
## Compliance with Funding Rules

- ✓ All costs are eligible per call guidelines
- ✓ Costs are necessary and reasonable
- ✓ Costs are actual (not estimated without basis)
- ✓ Costs are identifiable and verifiable
- ✓ No double funding with other grants
- ✓ Overhead rate compliant (25% or as specified)
- ✓ Subcontracting justified and within limits
- ✓ Equipment depreciation correctly calculated
- ✓ Personnel costs based on certified methodology
- ✓ Audit trail documentation available
```

## Quality Criteria
- Accurate calculations (no errors)
- Realistic cost estimates
- Complete justification
- Full compliance with funding rules
- Clear presentation
- Consistent with work packages
- Optimal resource allocation
- Professional formatting

## Final Deliverables
1. Budget narrative document (markdown)
2. Detailed budget tables
3. Optional: Excel spreadsheet with calculations
4. Budget justification integrated into proposal

## Integration Note
This budget must be perfectly aligned with:
- Work package person-month allocations
- Project timeline and activities
- Partnership agreements
- Call budget limits and rules
""",

        # ===== EXAMPLE SKELETONS =====
        "skeletons/example-project-info-page.md": """# Project Information Page

## Project Title
Innovative Digital Skills Training for Small and Medium Enterprises in the Construction Sector

## Project Acronym
DigiConstruct

## Short Description
DigiConstruct addresses the critical digital skills gap in the European construction sector by developing and piloting an innovative, AI-powered training platform specifically designed for SME employees. The project combines cutting-edge educational technology with industry-specific content to deliver personalized, workplace-integrated learning experiences that improve productivity, safety, and competitiveness in an increasingly digitalized construction industry.

## Main Objective
To develop, validate, and deploy a comprehensive digital skills training ecosystem that enables 5,000+ construction sector SME employees across five European countries to acquire essential digital competencies (BIM, IoT, data analytics, AR/VR) through personalized, AI-supported learning pathways, thereby increasing SME competitiveness and contributing to the digital transformation of the European construction industry.

## Specific Objectives
1. **Develop an AI-Powered Training Platform**: Create an adaptive learning management system that personalizes content delivery based on individual learner profiles, prior knowledge, and workplace context, achieving 80% learner satisfaction and 70% completion rates.

2. **Co-Create Industry-Specific Content**: Work with construction SMEs and educational institutions to develop 120+ hours of modular, practical training content covering BIM, IoT sensors, data analytics, and AR/VR applications, validated by at least 30 industry partners.

3. **Implement and Pilot in 5 Countries**: Deploy and test the platform with 250 pilot users across Germany, Spain, Poland, Netherlands, and Italy, collecting quantitative and qualitative data to demonstrate effectiveness and gather improvement insights.

4. **Establish Sustainable Business Model**: Develop and validate a financially sustainable exploitation strategy including certification pathways, licensing models, and partnership frameworks ensuring platform viability beyond project funding.

5. **Disseminate Best Practices**: Reach 10,000+ stakeholders through conferences, publications, workshops, and digital channels, creating a European-wide community of practice around digital skills in construction.

## Key Outputs
- **AI-Powered Learning Platform**: Open-source LMS with adaptive learning algorithms, available in 6 languages
- **Training Content Library**: 120+ hours of modular, workplace-oriented training materials covering 4 key digital technology areas
- **Assessment and Certification Framework**: Validated competency assessment tools and micro-credential certification system
- **Implementation Toolkit**: Guidelines, templates, and resources for SMEs to adopt and integrate the training platform
- **Policy Recommendations**: Evidence-based policy brief for EU and national stakeholders on digital skills development in construction
- **Research Publications**: Minimum 8 peer-reviewed publications on digital pedagogy, AI in vocational training, and construction sector innovation

## Expected Outcomes
- **Enhanced Digital Competencies**: 5,000+ construction sector workers gain measurable improvements in digital skills, with 70% achieving recognized micro-credentials
- **Increased SME Competitiveness**: Participating SMEs report 25% average improvement in project efficiency and 15% reduction in error rates through digital tool adoption
- **Industry-Education Collaboration**: Strengthened partnerships between 50+ SMEs and 15 educational institutions, creating sustainable pipeline for future skills development
- **Scalable Training Model**: Validated, replicable training approach transferable to other sectors and regions, with 10+ organizations expressing interest in adoption
- **Policy Impact**: Research findings integrated into 3+ national digital skills strategies and European construction sector policy discussions
- **Economic Impact**: Contribution to EU construction sector digitalization, supporting industry competitiveness and sustainability goals

## Project Partners
1. **Technical University of Berlin (Germany)** - Coordinator
   - Expertise: Engineering pedagogy, educational technology, AI in education
   - Role: Project coordination, platform development, research leadership

2. **Polytechnic University of Madrid (Spain)** - Partner
   - Expertise: Construction engineering, BIM, professional training
   - Role: Content development (BIM), Spanish pilot, validation

3. **National Association of Construction SMEs Poland** - Partner
   - Expertise: Industry needs assessment, SME networks, workforce development
   - Role: Industry liaison, Polish pilot, exploitation strategy

4. **TechEd Innovations B.V. (Netherlands)** - Partner
   - Expertise: EdTech development, LMS platforms, AI/machine learning
   - Role: Technical platform development, AI implementation

5. **Italian Construction Training Institute (Italy)** - Partner
   - Expertise: Vocational training, certification systems, adult education
   - Role: Content development (safety, AR/VR), Italian pilot, certification framework

6. **Digital Skills Europe Foundation (Belgium)** - Partner
   - Expertise: EU policy, digital skills frameworks, dissemination
   - Role: Policy engagement, dissemination, European network building

## Duration & Budget
**Duration**: 36 months (January 2026 - December 2028)  
**Total Budget**: €2,450,000  
**EU Contribution**: €2,450,000 (100% funding rate under Erasmus+ KA2)
""",

        "skeletons/example-work-package.md": """# Work Package 2: Learning Content Development

**Lead Partner**: P2 - Polytechnic University of Madrid  
**Duration**: Month 6 - Month 30  
**Total Person-Months**: 68 PM

## Participating Partners
- P1: Technical University of Berlin (18 PM)
- P2: Polytechnic University of Madrid - Lead (25 PM)
- P3: National Association Construction SMEs Poland (8 PM)
- P5: Italian Construction Training Institute (15 PM)
- P6: Digital Skills Europe Foundation (2 PM)

## Objectives
1. Develop comprehensive, modular training content covering 4 key digital technology areas relevant to construction SMEs
2. Ensure content is pedagogically sound, industry-validated, and adaptable to different learning contexts and prior knowledge levels
3. Create content in formats optimized for AI-powered personalization and adaptive learning pathways
4. Produce content in 6 European languages with cultural and regional adaptations

## Description of Work
WP2 focuses on creating the intellectual foundation of the DigiConstruct platform: high-quality, engaging learning content that addresses real construction sector needs while being optimized for AI-driven personalization. Content development follows a co-creation methodology involving educational experts, industry practitioners, and technology specialists.

The work is organized around four technology clusters: (1) Building Information Modeling (BIM), (2) Internet of Things (IoT) for construction monitoring, (3) Data analytics for project management, and (4) Augmented/Virtual Reality (AR/VR) for safety and training. Each cluster comprises 30+ hours of structured learning content including video lectures, interactive simulations, case studies, practical exercises, and assessments.

Content is designed following Universal Design for Learning (UDL) principles to accommodate diverse learner needs, backgrounds, and learning preferences. Metadata tagging enables the AI algorithms developed in WP3 to effectively map content to learner profiles and dynamically adjust learning paths.

## Tasks

### Task 2.1: Needs Analysis and Learning Objectives Definition
**Lead**: P2 | **Contributing**: P1, P3, P5  
**Duration**: M6-M12

Conduct comprehensive analysis of digital skills gaps in construction SMEs through:
- Literature review of construction sector digitalization trends
- Survey of 200+ SME employees on current competencies and training needs
- Focus groups with 6 SME clusters (2 per pilot country)
- Expert consultations with technology vendors and industry associations

Deliverables from this task feed into precise learning objective formulation for each technology cluster, ensuring content directly addresses industry-identified needs while aligning with European Digital Competence Framework (DigComp) standards.

**Dependencies**: Initial platform design from WP3 (to understand technical constraints)

### Task 2.2: Instructional Design Framework
**Lead**: P1 | **Contributing**: P2, P5  
**Duration**: M8-M14

Develop comprehensive instructional design framework including:
- Pedagogical model adapted for adult learners in workplace contexts
- Content structure templates for different content types
- Assessment design principles and item banks
- Multimedia production guidelines
- Accessibility and inclusion standards
- AI-readiness specifications (metadata schemas, granularity standards)

Framework reviewed by external advisory board including adult education experts and construction industry representatives.

**Dependencies**: Learning objectives from Task 2.1

### Task 2.3: BIM Content Development
**Lead**: P2 | **Contributing**: P5  
**Duration**: M12-M24

Create comprehensive BIM training content (30 hours) covering:
- BIM fundamentals and industry standards (ISO 19650)
- Software tools (Revit, ArchiCAD - tool-agnostic where possible)
- Collaborative workflows and coordination
- Quantity take-off and cost estimation from BIM
- 4D/5D BIM applications
- Mobile BIM and on-site usage

Content includes 15 video lectures, 20 interactive exercises, 8 case studies based on real projects, and 5 simulation-based challenges. All content produced in English, Spanish, and Italian with professional translation.

### Task 2.4: IoT and Sensor Technology Content
**Lead**: P1 | **Contributing**: P2  
**Duration**: M12-M24

Develop IoT training module (25 hours) addressing:
- Sensor types and applications in construction (temperature, humidity, vibration, progress monitoring)
- Data collection and wireless transmission protocols
- Real-time monitoring dashboards
- Predictive maintenance applications
- Integration with project management systems

Includes hands-on exercises with affordable IoT kits that SMEs can replicate, video demonstrations from real construction sites, and troubleshooting guides.

### Task 2.5: Data Analytics Content Creation
**Lead**: P1 | **Contributing**: P3  
**Duration**: M14-M26

Produce data analytics module (35 hours) covering:
- Construction data types and sources
- Data cleaning and preparation
- Descriptive analytics and visualization
- Introduction to predictive analytics for planning
- Key Performance Indicators (KPIs) for construction projects
- Excel and Power BI applications (accessible tools for SMEs)

Emphasis on practical, immediately applicable techniques. Includes 10 worked examples using anonymized real project data, step-by-step tutorials, and downloadable templates.

### Task 2.6: AR/VR for Safety and Training Content
**Lead**: P5 | **Contributing**: P2  
**Duration**: M14-M26

Create AR/VR training content (30 hours) including:
- Safety training scenarios (fall prevention, equipment operation, hazard identification)
- Virtual construction site walkthroughs
- Equipment operation simulations
- Collaborative virtual design reviews
- Mobile AR for on-site information overlay

Develop 5 VR scenarios and 8 AR applications optimized for affordable headsets (Meta Quest, smartphones). Include implementation guides for SMEs with limited tech infrastructure.

### Task 2.7: Assessment and Evaluation Development
**Lead**: P1 | **Contributing**: All partners  
**Duration**: M16-M28

Design comprehensive assessment system:
- Pre-assessment diagnostics (knowledge and skill level)
- Formative assessments embedded in learning content (100+ interactive questions/activities)
- Summative assessments for each technology cluster
- Practical competency demonstrations (portfolio-based)
- Peer and supervisor assessment templates

All assessments mapped to learning objectives and competency frameworks. Item banks created to enable adaptive testing.

### Task 2.8: Translation, Localization, and Cultural Adaptation
**Lead**: P6 | **Contributing**: All partners  
**Duration**: M20-M30

Translate all content into 6 languages (English, German, Spanish, Polish, Italian, Dutch) with:
- Professional translation by native speakers with construction sector knowledge
- Cultural adaptation of examples and case studies
- Regional regulatory context adjustments (e.g., safety standards, BIM protocols)
- Quality review by bilingual subject matter experts

Localization includes not just language but also units of measurement, currency, typical project types, and visual representations relevant to each context.

### Task 2.9: Content Integration and Quality Assurance
**Lead**: P2 | **Contributing**: All partners  
**Duration**: M24-M30

Final integration of all content into platform with:
- Technical quality checks (all media functional, links working)
- Pedagogical review (alignment with framework from Task 2.2)
- User acceptance testing with 50 pilot learners
- Accessibility compliance verification (WCAG 2.1 AA standard)
- Industry validation by partner SMEs

Iterative refinement based on feedback. Final sign-off by all content developers.

## Deliverables

- **D2.1: Needs Analysis Report** (M12, R, PU)
  - Comprehensive report on digital skills gaps, learning needs, and training priorities in construction SMEs
  - Quality: Validated through 200+ survey responses and 6 focus groups

- **D2.2: Instructional Design Framework** (M14, R, PU)
  - Complete framework document including templates, guidelines, and quality standards for all content
  - Quality: Reviewed and approved by external pedagogical experts

- **D2.3: BIM Training Content** (M24, DEM, PU)
  - 30 hours of BIM training content in 3 languages, fully integrated into platform
  - Quality: Tested with 20 users, industry validation by 5 BIM experts

- **D2.4: IoT and Sensor Technology Content** (M24, DEM, PU)
  - 25 hours of IoT training content with hands-on exercises
  - Quality: Technical review by 3 IoT specialists, pilot tested

- **D2.5: Data Analytics Training Content** (M26, DEM, PU)
  - 35 hours of data analytics content with real-world examples and templates
  - Quality: Validated with actual construction project data, user tested

- **D2.6: AR/VR Safety and Training Content** (M26, DEM, PU)
  - 30 hours of AR/VR content including 5 VR scenarios and 8 AR applications
  - Quality: Safety content reviewed by health & safety professionals, tech tested on target devices

- **D2.7: Assessment System** (M28, R+DEM, PU)
  - Complete assessment framework and item banks for all content areas
  - Quality: Psychometric validation, alignment check with learning objectives

- **D2.8: Multilingual Content Package** (M30, DEM, PU)
  - All content available in 6 languages with cultural adaptations
  - Quality: Native speaker review, cultural appropriateness check

- **D2.9: Content Quality Assurance Report** (M30, R, CO)
  - Comprehensive QA documentation including testing results, validation outcomes, and refinement log
  - Quality: Independent QA audit

## Milestones

- **MS4: Learning Objectives Defined and Validated** (M12)
  - Means of verification: D2.1 approved by consortium and 15+ industry partners confirm relevance

- **MS5: Instructional Design Framework Approved** (M14)
  - Means of verification: D2.2 reviewed by external experts and adopted by all content developers

- **MS6: Core Content Modules Completed (BIM + IoT)** (M24)
  - Means of verification: D2.3 and D2.4 delivered, pilot tested with positive feedback (>4/5 rating)

- **MS7: All Content Development Finalized** (M26)
  - Means of verification: All content modules (D2.3-2.6) delivered and integrated into platform

- **MS8: Multilingual Content Ready for Pilot** (M30)
  - Means of verification: D2.8 delivered, content accessible in all 6 languages on platform

## Risk Analysis and Mitigation

**Risk 1: Industry Involvement Below Target**
- *Probability*: Medium | *Impact*: High
- *Mitigation*: P3 (SME association) commits to mobilizing members; early engagement strategy; incentives for participation (free training, certificates)

**Risk 2: Content Development Delays**
- *Probability*: Medium | *Impact*: Medium
- *Mitigation*: Staggered development schedule; monthly progress reviews; buffer time built into timeline; contingency content from previous projects

**Risk 3: Translation Quality Issues**
- *Probability*: Low | *Impact*: Medium
- *Mitigation*: Professional translators with sector expertise; native speaker review; pilot testing in each language; iteration budget allocated

**Risk 4: Rapidly Changing Technology (esp. AI/AR/VR)**
- *Probability*: High | *Impact*: Medium
- *Mitigation*: Focus on principles rather than specific tools; modular structure allows updates; tool-agnostic where possible; final development late in project

## Dependencies

**From Other WPs:**
- WP3 (Platform Development): Technical specifications for content format and metadata
- WP1 (Management): Quality assurance framework and ethical clearance for industry data
- WP5 (Piloting): Feedback for content refinement

**To Other WPs:**
- WP3: Content specifications for platform design; assessment requirements for AI algorithms
- WP5: Content modules for pilot implementation
- WP6: Content samples for dissemination and promotional materials
""",

        "skeletons/example-budget-excerpt.md": """# Budget Calculation - Partner 2: Polytechnic University of Madrid

## Partner Overview
- **Country**: Spain
- **Role**: WP2 Lead (Content Development), WP5 Co-lead (Spanish Pilot)
- **Total Budget**: €478,750

## Personnel Costs

### Staff Categories and Rates
Based on certified institutional cost methodology (audited 2024):
- **Full Professor**: €72/hour
- **Associate Professor**: €58/hour
- **Research Fellow (Postdoc)**: €45/hour
- **PhD Researcher**: €28/hour
- **Instructional Designer**: €42/hour
- **Administrative Support**: €32/hour

### Person-Month Allocation by Work Package

| WP | Role | PM | Hours | Rate | Total |
|----|------|----|----- |------|-------|
| **WP1: Management** | | | | | |
| WP1 | Admin Support | 3 | 420 | €32 | €13,440 |
| **WP2: Content Development (LEAD)** | | | | | |
| WP2 | Full Professor | 8 | 1,120 | €72 | €80,640 |
| WP2 | Associate Professor | 12 | 1,680 | €58 | €97,440 |
| WP2 | Instructional Designer | 15 | 2,100 | €42 | €88,200 |
| WP2 | PhD Researcher | 22 | 3,080 | €28 | €86,240 |
| **WP3: Platform Development** | | | | | |
| WP3 | Associate Professor | 4 | 560 | €58 | €32,480 |
| WP3 | Research Fellow | 6 | 840 | €45 | €37,800 |
| **WP5: Piloting and Validation** | | | | | |
| WP5 | Associate Professor | 6 | 840 | €58 | €48,720 |
| WP5 | Research Fellow | 8 | 1,120 | €45 | €50,400 |
| WP5 | PhD Researcher | 10 | 1,400 | €28 | €39,200 |
| **WP6: Dissemination** | | | | | |
| WP6 | Full Professor | 2 | 280 | €72 | €20,160 |
| WP6 | Admin Support | 2 | 280 | €32 | €8,960 |
| | | | | | |
| **TOTAL PERSONNEL** | | **98 PM** | **13,720h** | | **€603,680** |

*Note: 1 Person-Month = 140 productive hours (excluding holidays, sick leave, administrative time)*
*Calculation basis: Spanish national standards for university research projects*

## Travel and Subsistence

### Consortium Meetings
- **Number of meetings**: 6 (semi-annual, months 6, 12, 18, 24, 30, 36)
- **Participants per meeting**: 2 (WP2 lead + management representative)
- **Average cost per trip**: €850
  - Flight/train: €450 (average within EU)
  - Hotel (2 nights): €280 (€140/night)
  - Per diem (3 days): €120 (€40/day - Spanish government rates)
- **Total consortium meetings**: 6 × 2 × €850 = **€10,200**

### Conferences and Dissemination Events
- **Academic conferences**: 4 participations over 3 years
  - Average cost: €1,400 (registration €500 + travel/stay €900)
  - Total: 4 × €1,400 = €5,600

- **Industry workshops**: 3 events (presenting project to construction sector)
  - Average cost: €600 (local/regional travel + materials)
  - Total: 3 × €600 = €1,800

### Research/Validation Visits
- **Pilot site visits in Spain**: 8 visits to partner SMEs for content validation
  - Average cost: €200/visit (local travel, meals)
  - Total: 8 × €200 = €1,600

- **Partner exchange visits**: 2 working visits to P1 (Berlin) for methodology alignment
  - Cost: €900 each × 2 = €1,800

**TOTAL TRAVEL**: €10,200 + €5,600 + €1,800 + €1,600 + €1,800 = **€21,000**

## Equipment and Infrastructure

### Computer Hardware
- **High-performance workstations for content creation**: 3 units
  - Specs: Video editing capable, 32GB RAM, dedicated GPU
  - Cost: €2,200 per unit
  - Total: 3 × €2,200 = €6,600
  - Justification: Required for AR/VR content development and video production (WP2)

### Software Licenses
- **Professional video production suite**: €3,500
  - Adobe Creative Cloud Team license (3 years)
  - For instructional video creation (WP2)

- **BIM software educational licenses**: €2,800
  - Autodesk Revit + ArchiCAD (3-year educational)
  - Essential for BIM content development (WP2, Task 2.3)

- **VR/AR development tools**: €1,500
  - Unity Pro licenses for VR scenario development
  - WP2, Task 2.6

### VR/AR Hardware for Testing
- **VR headsets**: 3 units × €450 = €1,350
  - Meta Quest 3 for testing VR content
  - Necessary to ensure content works on target consumer devices

- **AR-capable tablets**: 2 units × €800 = €1,600
  - iPad Pro for AR application testing
  - Ensures cross-platform compatibility

**TOTAL EQUIPMENT**: €6,600 + €3,500 + €2,800 + €1,500 + €1,350 + €1,600 = **€17,350**

*Note: Equipment >€1,000 follows institutional depreciation rules. Items used 100% for project; no depreciation split needed.*

## Other Direct Costs

### Consumables and Supplies
- **Office supplies and materials**: €1,200 (€400/year × 3 years)
- **Printing costs for validation materials**: €800
  - User guides, assessment forms, pilot materials
- **Cloud storage and backup**: €600 (€200/year × 3 years)
  - Additional storage for large multimedia files

**Subtotal consumables**: €2,600

### Subcontracting Services
- **Professional video production support**: €12,000
  - External production company for 6 high-quality instructional videos
  - Justification: Professional quality required; expertise not available in-house
  - WP2, months 15-24

- **Expert consultations - BIM specialists**: €4,000
  - Industry experts to review and validate BIM content
  - 8 consultations × €500
  - WP2, Task 2.3

- **Usability testing - professional UX firm**: €6,000
  - External firm to conduct structured usability testing of Spanish pilot
  - WP5, month 32

**Subtotal subcontracting**: €22,000

*Note: All subcontracting justified by absence of expertise in consortium; total subcontracting = €22,000 (3.4% of direct costs, well within 30% limit)*

### Dissemination and Publishing
- **Open Access publication charges**: €8,000
  - 4 journal articles × €2,000 average APC
  - Gold Open Access as per EU mandate

- **Conference registration fees**: Already included in Travel budget above

- **Project website hosting and maintenance**: €900 (€300/year × 3 years)
  - Spanish localized content portal

- **Promotional materials**: €1,500
  - Brochures, posters, roll-up banners for events
  - Spanish language dissemination materials

**Subtotal dissemination**: €10,400

### Other Costs
- **Ethics and data protection compliance**: €2,000
  - Legal review of pilot participant data handling
  - GDPR compliance audit

- **Translation and interpretation**: €3,000
  - Professional interpretation at 2 consortium meetings in Spain
  - Technical document translation (contract, reports)

**Subtotal other**: €5,000

**TOTAL OTHER DIRECT COSTS**: €2,600 + €22,000 + €10,400 + €5,000 = **€40,000**

## Indirect Costs (Overheads)

Calculated as **25%** of total eligible direct costs (standard EU rate):

**Direct costs eligible for overhead calculation:**
- Personnel: €603,680
- Travel: €21,000
- Equipment: €17,350
- Other direct: €40,000
- **Total direct costs**: €682,030

**Indirect costs (25%)**: €682,030 × 0.25 = **€170,507.50** → **€170,508**

Indirect costs cover:
- General administration and management
- Building costs (heating, electricity, maintenance, rent)
- IT infrastructure (network, central systems)
- Library and information resources
- Human resources and personnel administration
- Financial and accounting services
- Legal and procurement support

*Basis: Institutional overhead rate certified by Spanish Ministry of Science and Innovation, 2024*

## Total Partner Budget Summary

| Cost Category | Amount (€) | % of Partner Total |
|---------------|-----------|-------------------|
| Personnel | 603,680 | 69.6% |
| Travel & Subsistence | 21,000 | 2.4% |
| Equipment | 17,350 | 2.0% |
| Other Direct Costs | 40,000 | 4.6% |
| **Subtotal Direct** | **682,030** | **78.6%** |
| Indirect Costs (25%) | 170,508 | 19.7% |
| **TOTAL P2 BUDGET** | **852,538** | **100%** |

**Requested EU Funding**: €852,538 (100% funding rate, Erasmus+ KA2)

## Budget Justification - Partner 2

### Personnel (69.6% of total)
The personnel budget reflects the substantial intellectual effort required for developing 120+ hours of high-quality, industry-validated training content across four technology domains (BIM, IoT, Data Analytics, AR/VR). As WP2 lead, P2 coordinates content development with 25 PM allocated to this work package.

Senior academic staff (Full and Associate Professors, 20 PM total) provide scientific leadership, pedagogical expertise, and ensure academic rigor. Their involvement is essential for methodology development, industry expert coordination, and quality assurance.

Instructional designers (15 PM) bring specialized expertise in adult learning, multimedia design, and e-learning content creation - critical for producing engaging, pedagogically sound materials. PhD researchers (32 PM total across all WPs) conduct literature reviews, develop case studies, create exercises, and support piloting - cost-effective while ensuring quality.

Administrative support (5 PM) handles coordination tasks, documentation, and reporting, freeing senior staff for high-value activities.

All rates are based on institutional certified cost model, audited annually, and aligned with Spanish national standards for university research projects.

### Travel (2.4% of total)
Travel budget supports essential face-to-face collaboration in this multinational project. Semi-annual consortium meetings are necessary for complex decision-making, content alignment across partners, and relationship building. Two representatives per meeting ensure WP2 leadership presence and continuity.

Conference participation (4 over 3 years) is moderate and necessary for disseminating findings, networking with construction education community, and ensuring research impact. Selection focuses on high-quality venues with clear dissemination value.

Industry workshop participation connects project with Spanish construction sector, validates content relevance, and builds exploitation partnerships. Local/regional focus keeps costs minimal.

Research visits to pilot sites are essential for understanding real workplace contexts and validating content applicability. Exchange visits to P1 (coordinator) ensure methodological alignment and knowledge transfer.

All travel costs calculated conservatively using Spanish government per diem rates and average EU transport costs.

### Equipment (2.0% of total)
Equipment requests are limited to items essential for content development that aren't available through normal institutional infrastructure.

High-performance workstations are necessary for professional video editing and VR/AR content creation - standard university PCs lack required GPU and RAM. Content production demands are well beyond typical academic computing needs.

Software licenses cover industry-standard tools (Adobe suite, BIM platforms, Unity) necessary for professional-quality content. Educational licenses used where available to minimize cost.

VR headsets and AR tablets are critical for testing developed content on actual consumer devices that SMEs would use - cannot rely solely on high-end development equipment. Ensures content accessibility and functionality.

All equipment will be used 100% for project purposes during project lifetime, with institutional ownership afterward supporting continued educational innovation.

### Other Direct Costs (4.6% of total)
Subcontracting (€22,000, 3.2% of direct costs) is limited to areas where external expertise provides clear value and efficiency:
- Professional video production for flagship instructional content ensures broadcast quality
- BIM expert consultations bring current industry practice and validation
- Professional UX testing provides objective assessment of pilot

Consumables are modest - primarily materials for pilot implementation and cloud storage for large multimedia files.

Dissemination costs, particularly Open Access publication, ensure compliance with EU open science requirements and maximize project impact. Costs are competitive (average APC for education/engineering journals).

Ethics and translation support essential project functions not available in-house.

### Indirect Costs (19.7% of total)
Overhead at 25% is standard EU rate and reflects actual institutional costs of providing research infrastructure, administration, financial management, legal support, and facilities. Rate is certified by Spanish authorities and subject to audit.

### Cost-Effectiveness
- **Cost per training hour developed**: €852,538 ÷ 120 hours = €7,104/hour
  - Includes research, design, development, validation, and multilingual production
  - Comparable to industry e-learning development costs (€5,000-15,000/hour for high-quality content)
  
- **Cost per pilot user (Spanish pilot)**: €852,538 ÷ 100 users = €8,525/user
  - Includes content development benefiting all 5,000 final users
  - Actual cost per end user across project: €2,450,000 ÷ 5,000 = €490/user (highly cost-effective)

- **Value for money**: Partner brings critical mass of BIM and construction expertise, strong SME network in Spain, and experienced content development team. Budget enables leadership of project's core intellectual output.

Partner 2 budget represents excellent value, combining academic excellence with industry relevance, and delivering scalable content that will benefit European construction sector for years beyond project completion.
""",

        # ===== CALL FOLDER README =====
        "call/README.md": """# Funding Call Documents

Place your funding call documents in this directory.

## Recommended Files

1. **Main Call Document** (PDF)
   - Full call text with all requirements
   - Named clearly: `Call-Erasmus-KA2-2026.pdf` or `Horizon-Europe-CL4-2026.pdf`

2. **Work Programme** (PDF, if separate)
   - Detailed work programme showing topics and budgets

3. **Submission Templates** (if provided)
   - Partner description template
   - Budget template
   - Other administrative forms

4. **Eligibility Checklists** (if available)
   - Self-assessment tools from funding agency

## Usage in Workflow

The **Overseer Agent** will:
1. Read the call document from this directory
2. Extract key requirements:
   - Objectives and priorities
   - Eligibility criteria
   - Budget limits
   - Duration
   - Evaluation criteria
3. Generate strategic analysis
4. Guide subsequent agents based on call specifics

## Tips

- Use descriptive filenames
- Keep original filenames from funding agency
- If multiple calls, create subdirectories: `call/erasmus-2026/`, `call/horizon-2027/`
- Include any supplementary guides or FAQ documents
""",

        # ===== GITIGNORE =====
        ".gitignore": """# Sensitive information
call/CONFIDENTIAL_*
docs/*DRAFT*
*_internal_notes.md

# Environment
.env
.env.local

# Python
__pycache__/
*.py[cod]
venv/
env/

# OS files
.DS_Store
Thumbs.db
*.swp

# Temporary files
*.tmp
*.bak
~$*.docx
~$*.xlsx

# Build outputs
*.zip

# Large files
*.mp4
*.mov
call/*.mp4

# API keys and credentials
*_api_key.txt
credentials*.json
"""
    }
    
    # Create all files
    print("Creating project proposal workflow files...")
    print(f"Output directory: {base_dir.absolute()}\n")
    
    for file_path, content in files.items():
        full_path = base_dir / file_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Created: {file_path}")
    
    # Create empty directories
    empty_dirs = [
        "docs",
        "skeletons",
        "assets/templates",
        "assets/images"
    ]
    
    print("\nCreating empty directories...")
    for dir_path in empty_dirs:
        (base_dir / dir_path).mkdir(parents=True, exist_ok=True)
        print(f"✓ Created: {dir_path}/")
    
    return base_dir

def create_zip_archive(base_dir):
    """Create a zip file of all generated files"""
    zip_filename = f"project-proposal-workflow-{datetime.now().strftime('%Y%m%d')}.zip"
    
    print(f"\nCreating zip archive: {zip_filename}")
    
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(base_dir):
            dirs[:] = [d for d in dirs if d not in ['__pycache__', '.git', 'venv']]
            
            for file in files:
                file_path = Path(root) / file
                arcname = file_path.relative_to(base_dir.parent)
                zipf.write(file_path, arcname)
                
    print(f"✓ Zip archive created: {zip_filename}")
    return zip_filename

def main():
    """Main function to generate all files"""
    print("=" * 70)
    print("Project Proposal Workflow Generator")
    print("=" * 70)
    print()
    
    try:
        # Create file structure
        base_dir = create_file_structure()
        
        # Create zip archive
        zip_file = create_zip_archive(base_dir)
        
        # Success message
        print("\n" + "=" * 70)
        print("✓ SUCCESS! Project proposal workflow system generated")
        print("=" * 70)
        print(f"\nFiles created in: {base_dir.absolute()}")
        print(f"Zip archive: {zip_file}")
        print("\n📋 Next Steps:")
        print("1. Extract the zip file or navigate to the directory")
        print("2. Place your funding call document in call/ directory")
        print("3. Review templates/ for customization")
        print("4. Start with: /overseer-analysis")
        print("5. Follow workflow: Info Page → Outline → Work Packages → Budget")
        print("\n💡 Each agent builds on previous outputs")
        print("   Overseer guides the entire process")
        print("\nHappy proposal writing! 📝\n")
        
    except Exception as e:
        print(f"\n✗ Error occurred: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0

if __name__ == '__main__':
    exit(main())
