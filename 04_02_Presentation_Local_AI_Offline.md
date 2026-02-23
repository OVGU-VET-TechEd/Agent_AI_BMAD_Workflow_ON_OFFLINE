<!--
author:   Sabbir Rifat
email:    a.rifat@ovgu.de
version:  2.0.0
language: en
narrator: English Female
comment:  Session 3: BMAD with Local AI (Offline) - Georgian University Workshop
logo:     https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/ChatGPT_logo.svg/120px-ChatGPT_logo.svg.png

@style
.info-box {
    background-color: rgba(70, 130, 220, 0.1);
    border: 2px solid rgba(70, 130, 220, 0.4);
    border-radius: 12px;
    padding: 25px;
    margin: 20px 0;
    transition: all 0.3s ease;
}

.info-box:hover {
    transform: translateY(-8px);
    box-shadow: 0 8px 20px rgba(70, 130, 220, 0.3);
    background-color: rgba(70, 130, 220, 0.15);
}

.success-box {
    background-color: rgba(76, 175, 80, 0.1);
    border: 2px solid rgba(76, 175, 80, 0.4);
    border-radius: 12px;
    padding: 25px;
    margin: 20px 0;
    transition: all 0.3s ease;
}

.success-box:hover {
    transform: translateY(-8px);
    box-shadow: 0 8px 20px rgba(76, 175, 80, 0.3);
    background-color: rgba(76, 175, 80, 0.15);
}

.warning-box {
    background-color: rgba(255, 160, 60, 0.1);
    border: 2px solid rgba(255, 160, 60, 0.4);
    border-radius: 12px;
    padding: 25px;
    margin: 20px 0;
    transition: all 0.3s ease;
}

.warning-box:hover {
    transform: translateY(-8px);
    box-shadow: 0 8px 20px rgba(255, 160, 60, 0.3);
    background-color: rgba(255, 160, 60, 0.15);
}

.comparison-table {
    background-color: rgba(156, 39, 176, 0.1);
    border: 2px solid rgba(156, 39, 176, 0.4);
    border-radius: 12px;
    padding: 25px;
    margin: 20px 0;
}

.step-container {
    display: grid;
    grid-template-columns: 1fr;
    gap: 20px;
    margin: 25px 0;
}

.step-box {
    background-color: rgba(156, 39, 176, 0.1);
    border-left: 5px solid rgba(156, 39, 176, 0.6);
    border-radius: 8px;
    padding: 20px;
    transition: all 0.3s ease;
}

.step-box:hover {
    transform: translateX(10px);
    box-shadow: 0 6px 15px rgba(156, 39, 176, 0.2);
    background-color: rgba(156, 39, 176, 0.15);
}

.step-box h4 {
    font-size: 20px;
    color: #7b1fa2;
    margin-bottom: 12px;
    font-weight: bold;
}

@end
-->

# Session 3: BMAD with Local AI (Offline)

> **Duration**: 1 hour 40 minutes  
> **Format**: 🎓 Hands-On Workshop  
> **Target Audience**: Georgian University Academic Staff  
> **Prerequisites**: Sessions 1 & 2 completed

Welcome to the final session! Today you'll learn to run AI **completely offline** on your own computer - no internet, no cloud, no monthly costs, and complete privacy!

**🎯 What We'll Do Together:**

* 🌐 **Part 1 - 10 min**: Why Local AI? (Cloud vs. Offline Comparison)
* 💻 **Part 2 - 20 min**: Install Ollama + DeepSeek Model / llama3.1:8b
* 🔧 **Part 3 - 15 min**: Configure VS Code Continue Extension
* 🎨 **Part 4 - 30 min**: Create a Course Offline (Everyone Together)
* 🔄 **Part 5 - 15 min**: Compare Cloud vs. Local Results
* ✅ **Part 6 - 10 min**: Best Practices & Workshop Wrap-up

---

## Quick Recap: The Complete Workshop Journey (3 minutes)

Let's review what we've accomplished over the past 5 hours!

### Session 1: Foundations (1h 40min)

<div class="info-box">

**✅ What You Learned:**

- Understanding Agentic AI vs. Traditional AI
- Setting up VS Code, GitHub, and Copilot
- BMAD Method: 7-stage workflow
- File structure and templates
- How templates, tasks, and agents work together

**✅ What You Installed:**

- VS Code
- GitHub account + Copilot with Claude Sonnet 4.5
- Understanding of the BMAD ecosystem

</div>

---

### Session 2: Cloud Implementation (1h 40min)


<div class="success-box">

**✅ What You Built:**

- GitHub repository: `AI-in-TVET-Course`
- Complete 2-hour course using megaprompt
- 7 files, 6,000+ words, professional materials
- Dual output: Desktop + GitHub cloud
- Prof. Dr. Elena Hoffmann persona
- Interactive LiaScript lecture

**✅ What You Mastered:**

- GitHub-first workflow
- BMAD megaprompt technique
- Git version control basics
- Cloud collaboration and sharing

</div>

---

### Session 3: Local AI (Today - 1h 40min)

<div class="warning-box">

**🎯 Today's Goal:**

Run the **same BMAD workflow** but completely **offline** using your own computer!

**Why?**

- ✅ **Privacy:** Data never leaves your machine
- ✅ **Cost:** 100% FREE forever (no subscriptions)
- ✅ **Independence:** Works without internet
- ✅ **Learning:** Understand how AI actually runs
- ✅ **Flexibility:** Customize models for your needs

</div>

---

## Part 1: Why Local AI? (10 minutes)

### Cloud AI vs. Local AI: The Complete Picture


<div class="comparison-table">

| Aspect | Cloud AI (Copilot + Claude) | Local AI (Ollama + DeepSeek/ llama3.1:8b) |
|--------|----------------------------|------------------------------|
| **Cost** | $10-20/month subscription | FREE forever |
| **Privacy** | Data sent to cloud servers | Data never leaves computer |
| **Internet** | Required always | Not required |
| **Speed** | ⚡ Very fast (2-10 seconds) | 🐢 Slower (25-120 seconds) |
| **Quality** | ⭐⭐⭐⭐⭐ Excellent | ⭐⭐⭐⭐ Good |
| **Context** | 200K+ tokens | 32K-128K tokens |
| **Setup** | Easy (5 minutes) | Moderate (35-50 minutes) |
| **Updates** | Automatic | Manual download |
| **Power** | Any computer | Needs decent specs |

</div>

---

### When to Use Which?

{{1}}
<div class="info-box">

**☁️ Use Cloud AI (Copilot + Claude) When:**

- You need highest quality output
- Speed is critical (tight deadlines)
- Working on complex, multi-document projects
- Creating courses for publication
- You have stable internet connection
- Budget allows subscription ($10-20/month)

**Examples:**
- Final course materials for students
- Professional development content
- Collaborative projects
- Public-facing materials

</div>

{{2}}
<div class="success-box">

**💻 Use Local AI (Ollama + DeepSeek/ llama3.1:8b) When:**

- Privacy is paramount (sensitive data)
- No internet available (travel, remote locations)
- Budget constraints (completely free)
- Learning and experimentation
- Initial drafts and brainstorming
- Personal notes and outlines
- Quick iterations

**Examples:**
- Course planning and outlines
- First drafts of materials
- Experimenting with ideas
- Personal study notes
- Confidential university data

</div>

---

### Real-World Scenario

<div class="warning-box">

**📚 Practical Workflow:**

**Step 1:** Create course outline with **Local AI** (free, private)

↓

**Step 2:** Review and refine outline

↓

**Step 3:** Generate full materials with **Cloud AI** (high quality)

↓

**Step 4:** Store final version on GitHub

**Result: Best of both worlds - privacy + quality + cost savings!**

</div>

---


### System Requirements for Local AI

<div class="success-box">

**Minimum Requirements:**

- **OS:** Windows 10/11, macOS, or Linux
- **RAM:** 8 GB minimum, 16 GB or more recommended
- **Storage:** 10 GB free space
- **Processor:** Modern CPU (any Intel/AMD from 2015+)
- **GPU:** Optional but helpful (NVIDIA/AMD Radeon)

**Note:** DeepSeek R1:7b / llama3.1:8b model is **4.5- 4.9 GB** - one-time download!

</div>


---

## Part 2: Install Ollama (20 minutes)

Ollama is a free, open-source application that lets you run AI models on your computer.

### Step 1: Download Ollama

**👉 EVERYONE DO THIS NOW:**

<div class="step-container">

<div class="step-box">
<h4>🌐 Go to Ollama Website</h4>

1. Open browser
2. Go to: **`ollama.com`**
3. You'll see the homepage with download button

</div>

<div class="step-box">
<h4>💾 Download for Your OS</h4>

**Windows Users:**
- Click **"Download for Windows"**
- File: `OllamaSetup.exe` 

**Mac Users:**
- Click **"Download for Mac"**
- File: `Ollama-darwin.zip`

**Linux Users:**
- Copy install command shown
- Open terminal and paste

</div>

</div>

---

### Step 2: Install Ollama

**👉 INSTALL NOW:**

<div class="step-container">

<div class="step-box">
<h4>🪟 Windows Installation</h4>

1. Run `OllamaSetup.exe`
2. Click **"Install"**
3. Wait for installation (2-3 minutes)
4. Ollama icon appears in system tray (bottom-right)
5. Click **"Finish"**

</div>

<div class="step-box">
<h4>🍎 Mac Installation</h4>

1. Open downloaded `.zip` file
2. Drag **Ollama.app** to Applications folder
3. Open Ollama from Applications
4. Allow permissions if prompted
5. Ollama icon appears in menu bar (top-right)

</div>

<div class="step-box">
<h4>🐧 Linux Installation</h4>

Run the command from ollama.com:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Wait for installation to complete.

</div>

</div>

---

### Step 3: Verify Ollama Installation

**👉 TEST OLLAMA:**

<div class="step-box">
<h4>✅ Verification Steps</h4>

1. Open **Terminal** (Windows: PowerShell, Mac: Terminal, Linux: Terminal)

2. Type:
```bash
ollama --version
```

3. Press Enter

4. You should see version number:
```
ollama version 0.x.x
```

</div>


<div class="success-box">

**✋ CHECKPOINT:** Can everyone see Ollama version number?

**✅ If yes → Ollama is installed correctly!**

**❌ If no → Try:**
- Restart computer
- Check system tray/menu bar for Ollama icon
- Re-run installer

</div>

---

### Step 4: Download DeepSeek R1:7b Model/ llama3.1:8b

Now let's download the AI model we'll use!


**👉 DOWNLOAD MODEL:**

<div class="step-box">
<h4>📥 Download DeepSeek </h4>

In your terminal/PowerShell, type:

```bash
ollama pull deepseek-r1:7b
```
```bash
ollama pull llama3.1:8b
```

Press Enter and wait...

</div>


<div class="warning-box">

**⚠️ IMPORTANT:**

- This downloads **4.9 GB** - takes 5-15 minutes depending on internet speed
- You only do this ONCE
- Model is stored permanently on your computer
- You can use it offline forever after download

**Expected Output:**

```
pulling manifest
pulling 8c17e007d6c0... 100% ▕████████████▏ 4.9 GB
pulling 966de95ca8a6... 100% ▕████████████▏ 1.4 KB
pulling fcc5a6bec9da... 100% ▕████████████▏ 7.7 KB
pulling a70ff7e570d9... 100% ▕████████████▏ 6.0 KB
pulling 56bb8bd477a5... 100% ▕████████████▏   96 B
pulling 34bb5ab01051... 100% ▕████████████▏  561 B
verifying sha256 digest
writing manifest
success
```

</div>

---

### Step 5: Test DeepSeek Model / llama 3.1


**👉 TEST THE MODEL:**

<div class="step-box">
<h4>🧪 Quick Test</h4>

In terminal, type:

```bash
ollama run deepseek-r1:7b / llama3.1:8b
```

Then ask a question:

```
Hello! Can you explain what you are in one sentence?
```

Press Enter and wait for response (15-30 seconds).

</div>


<div class="success-box">

**Expected Response:**

```
I am DeepSeek R1 /llama3.1:8b , an AI language model designed to 
assist with text-based tasks such as answering 
questions, generating content, and providing information.
```

**To exit:** Type `/bye` and press Enter

**✅ If you got a response → DeepSeek / llama3.1:8b is working!**

</div>

---

## Part 3: Install VS Code Continue Extension (15 minutes)

Continue is a VS Code extension that lets you use local AI models like Copilot, but completely free and offline!

### Step 1: Install Continue Extension


**👉 IN VS CODE:**

<div class="step-container">

<div class="step-box">
<h4>🔌 Install Extension</h4>

1. Open **VS Code**
2. Click **Extensions** icon (📦) in sidebar
3. Search: **`Continue`**
4. Find **"Continue - Codestral, Claude, and more"** by Continue
5. Click **"Install"**
6. Wait for installation (30 seconds)

</div>

</div>

---

### Step 2: Configure Continue for Local AI


**👉 CONFIGURE CONTINUE:**

<div class="step-box">
<h4>⚙️ Setup Local Model</h4>

1. After Continue installs, you'll see a new icon in left sidebar (looks like ">_<")
2. Click the Continue icon
3. Continue chat panel opens
4. Look for **gear icon** ⚙️ in top-right of Continue panel
5. Click gear icon → Opens `config.json` file

</div>

---

### Step 3: Edit Continue Configuration

**👉 REPLACE CONFIG:**

<div class="step-box">
<h4>📝 Update config.json</h4>

**Delete everything** in the file and replace with this:

```yaml
{
  "name": "local-offline-ollama",
  "version": "0.0.1",
  "models": [
    {
      "name": "deepseek-local",
      "provider": "ollama",
      "model": "deepseek-r1:7b",
      "apiBase": "http://127.0.0.1:11434",
      "contextLength": 8192,
      "roles": [
        "chat",
        "edit",
        "autocomplete"
      ]
    }
  ]
}
```

**OR**

```yaml
{
    - name: llama-agent
    provider: ollama
    model: llama3.1:8b
    apiBase: http://127.0.0.1:11434
    contextLength: 128000
    capabilities: [tool_use]
    roles:
      - chat
      - edit
      - autocomplete
      ]
    }
  ]
}
```


**Save** the file (Ctrl+S)

</div>

---

### Step 4: Restart VS Code


**👉 RESTART:**

<div class="step-box">
<h4>🔄 Apply Configuration</h4>

1. Close VS Code completely
2. Reopen VS Code
3. Open your `AI-in-TVET-Course` folder again
4. Click Continue icon in sidebar

</div>

---

### Step 5: Test Continue with DeepSeek / llama3.1:8b


**👉 TEST LOCAL AI:**

<div class="step-box">
<h4>🧪 Verify Setup</h4>

1. In Continue panel, look for model dropdown at top
2. Should show: **"DeepSeek R1 7B (Local) / llama3.1:8b"**
3. Choolse the agent mode
4. Type in Continue chat:

```
Hello! Please confirm you are DeepSeek/ llama 3.1 running locally 
on my computer. What are your capabilities?
```

4. Press Enter
5. Wait 15-90 seconds for response

</div>


<div class="success-box">

**Expected Response:**

```
Yes, I am DeepSeek R1/ llama 3.1 running locally on your computer 
through Ollama. I can help with:
- Code generation and explanation
- Writing and editing text
- Answering questions
- Creating educational content
- And more...

Since I'm running locally, your data never leaves your 
machine, and you can use me without internet connection.
```

**✅ If you got response → Continue is working with local AI!**

</div>

---

## Part 4: Create a Course Offline (30 minutes)

Now let's create a complete course using your local AI - completely offline!

### Our Second Course: "Data Literacy for Business Students"


<div class="info-box">

**📚 Course Specifications:**

- **Title:** Data Literacy for Business Students
- **Target Audience:** Undergraduate Business majors
- **Duration:** 90 minutes (1.5-hour session)
- **Format:** Interactive lecture with case studies
- **Topics:** Understanding data, basic statistics, data-driven decision making, common pitfalls

</div>

---

### Step 1: Create New Repository Folder

**👉 CREATE LOCAL FOLDER:**

<div class="step-box">
<h4>📁 Setup New Course Folder</h4>

1. Open File Explorer → Go to Desktop
2. Create new folder: **`Data-Literacy-Course`**
3. Copy the BMAD template files from your previous course:

   - Copy ALL folders from `AI-in-TVET-Course` EXCEPT files in `docs/`, `materials/`, and `skeletons/`
   - Paste into `Data-Literacy-Course` folder

You should have:

```
📁 Data-Literacy-Course/
 ├── 📁 checklists/
 ├── 📁 data/
 ├── 📁 docs/ (empty)
 ├── 📁 materials/ (empty)
 ├── 📁 skeletons/ (empty)
 ├── 📁 tasks/
 ├── 📁 templates/
 └── 📄 copilot-instructions.md
```

</div>

---

### Step 2: Open in VS Code

**👉 OPEN FOLDER:**

<div class="step-box">
<h4>📂 Open in VS Code</h4>

1. In VS Code: **File** → **Open Folder**
2. Select `Data-Literacy-Course` from Desktop
3. Click **"Select Folder"**
4. Trust the folder if prompted

</div>

---

### Step 3: Prepare Local AI Megaprompt


**👉 LOCAL AI MEGAPROMPT:**

<div class="warning-box">

**⚠️ Important Differences for Local AI:**

Local AI (DeepSeek/ llama 3.1) has limitations compared to Claude:
- Smaller context window (processes less at once)
- Slower processing (15-120 seconds per stage)
- Sometimes needs more specific instructions

**Strategy:** Break megaprompt into smaller, sequential commands

</div>

---

### Step 4: Create Outline with Local AI


**👉 START WITH OUTLINE:**

{{0}}
<div class="step-box">
<h4>📋 Stage 1: Outline</h4>

In Continue panel, type:

```
@folder I need to create a university course outline using 
the BMAD Method templates.

COURSE DETAILS:
- Title: Data Literacy for Business Students
- Target Audience: Undergraduate Business majors (2nd-3rd year)
- Duration: 90 minutes (single session)
- Prerequisites: Basic math, no statistics background

LEARNING OBJECTIVES:
1. Understand fundamental data concepts and terminology
2. Interpret basic statistical measures (mean, median, mode, variance)
3. Evaluate data quality and identify common biases
4. Apply data-driven thinking to business decisions
5. Recognize when data can mislead or be misused

Please read the template at templates/lecture-outline-template.yaml 
and create docs/lecture-outline.md following that structure.

Include:
- Clear course description
- All 5 learning objectives
- Target audience details
- Time commitment (90 minutes)
- An engaging abstract for business students

Save the file to docs/lecture-outline.md
```

Press Enter and **wait 2-4 minutes**

**You'll see:** Text appearing gradually as DeepSeek /llama 3.1 generates content

</div>

{{1}}
<div class="success-box">

**✋ CHECKPOINT (after 2-4 minutes):**

Check if `docs/lecture-outline.md` was created!

1. Open the file in VS Code
2. Verify it contains all 5 learning objectives
3. Check that course description is present

**✅ If created → Stage 1 complete!**

**⚠️ If incomplete:** Ask Continue to continue writing the outline.

</div>

---

### Step 5: Create Didactics (Teaching Style)


**👉 STAGE 2: DIDACTICS:**

<div class="step-box">
<h4>🎭 Define Teaching Approach</h4>

In Continue panel, type:

```
@folder Now create the didactics document using 
templates/lecture-didactics-template.yaml

TEACHING STYLE:
Professor Persona: Prof. Michael Zhang
- Expertise: Business Analytics, Data Science for Business
- Background: Former data analyst at consulting firm
- Personality: Practical, uses real business examples
- Style: "Here's how this works in the real world..."
- Approach: Case-study driven, emphasizes critical thinking

Difficulty Level: Beginner-friendly
- Assumes: Basic math (algebra), Excel familiarity
- No prior statistics knowledge needed
- Avoids: Complex formulas, heavy mathematics
- Focus: Intuition and practical application

Course Type: Application-oriented introduction
- Real business cases (marketing, finance, operations)
- Interactive examples
- Common mistakes and pitfalls
- Hands-on practice with data interpretation

Please create docs/lecture-didactics.md with:
- Complete Prof. Zhang persona
- Teaching style guidelines
- Difficulty level specifications
- Pedagogical approach details

Save to docs/lecture-didactics.md
```

Press Enter and **wait 30-60 seconds**

</div>

---

### Step 6: Create Agenda (Session Structure)


**👉 STAGE 3: AGENDA:**

<div class="step-box">
<h4>📅 Plan Session Structure</h4>

In Continue panel, type:

```
@folder Read docs/lecture-outline.md and 
docs/lecture-didactics.md, then create the agenda.

SESSION BREAKDOWN (90 minutes total):

Part 1 (15 min): What is Data Literacy?
- Why data matters in business
- Real examples of data-driven success
- Common data mistakes that cost companies money

Part 2 (20 min): Understanding Your Data
- Types of data (quantitative, qualitative, categorical)
- Descriptive statistics basics (mean, median, mode)
- What these numbers actually tell you

Part 3 (20 min): Data Quality & Biases
- How to spot bad data
- Common biases (selection, confirmation, survivorship)
- Real cases: when data misled businesses

Part 4 (25 min): Making Data-Driven Decisions
- CRISP-DM framework simplified
- Case study: Marketing campaign analysis
- Practice: Interpreting a business dataset

Part 5 (10 min): Wrap-up & Resources
- Key takeaways
- Tools for business students
- Next steps in data literacy

Use templates/lecture-agenda-template.yaml and create 
docs/lecture-agenda.md with:
- Each section with timing
- Learning objectives per section
- Transition logic
- Connection to overall course goals

Save to docs/lecture-agenda.md
```

Press Enter and **wait 30-60 seconds**

</div>

---

### Step 7: Create Session Skeleton

{{0}}
**👉 STAGE 4: SKELETON:**

<div class="step-box">
<h4>🗂️ Build Session Structure</h4>

In Continue panel, type:

```
@folder Read docs/lecture-agenda.md and create a 
detailed session skeleton.

Create skeletons/01-lecture.md following the structure:

# Data Literacy for Business Students

## Summary
[Brief session overview]

## Content Structure

### Part 1: What is Data Literacy? (15 min)
- Placeholder for opening hook
- Placeholder for business examples
- Placeholder for common mistakes

### Part 2: Understanding Your Data (20 min)
- Placeholder for data types explanation
- Placeholder for descriptive statistics
- Placeholder for practical examples

### Part 3: Data Quality & Biases (20 min)
- Placeholder for quality indicators
- Placeholder for bias examples
- Placeholder for real business cases

### Part 4: Making Data-Driven Decisions (25 min)
- Placeholder for decision framework
- Placeholder for case study
- Placeholder for practice activity

### Part 5: Wrap-up (10 min)
- Placeholder for summary
- Placeholder for resources
- Placeholder for next steps

## Interactive Elements
- Quiz 1: [Placeholder]
- Quiz 2: [Placeholder]
- Case Study: [Placeholder]
- Practice Activity: [Placeholder]

## References & Sources
- [Placeholder for academic sources]
- [Placeholder for business examples]

Save to skeletons/01-lecture.md
```

Press Enter and **wait 30-60 seconds**

</div>

{{1}}
<div class="info-box">

**⏸️ PAUSE HERE FOR GROUP CHECK (2 minutes)**

Let's make sure everyone has completed Stages 1-4 before moving to the longest stage (full materials generation).

**✋ CHECKPOINT:** 

Can everyone see these 4 files created?
1. docs/lecture-outline.md ✅
2. docs/lecture-didactics.md ✅
3. docs/lecture-agenda.md ✅
4. skeletons/01-lecture.md ✅

**If missing any:** Ask for help now!

</div>

---

### Step 8: Generate Full Interactive Materials


**👉 STAGE 5: FULL MATERIALS (This takes longest!):**

{{0}}
<div class="warning-box">

**⚠️ IMPORTANT:**

This stage generates 4,000-5,000 words of content. With local AI:
- **Processing time:** 2-4 minutes (much slower than cloud!)
- **Be patient!** DeepSeek / llama 3.1 is working hard
- **Don't interrupt** or close Continue panel
- Watch for progress as text appears

</div>

{{1}}
<div class="step-box">
<h4>📝 Generate Complete Lecture</h4>

In Continue panel, type:

```
@folder Now promote the skeleton to full interactive materials.

Read:
- docs/lecture-outline.md
- docs/lecture-didactics.md  
- docs/lecture-agenda.md
- skeletons/01-lecture.md
- data/liascript-cheat-sheet.md

Create materials/01-lecture.md as a complete 90-minute 
interactive lecture in LiaScript format.

REQUIREMENTS:

1. VOICE: Write entirely in Prof. Michael Zhang's voice
   - Practical, business-focused
   - Uses real company examples
   - Conversational but professional
   - "Let me show you how this works..."

2. CONTENT (4,000-5,000 words):
   - Part 1: Engaging introduction with business impact
   - Part 2: Clear explanations with Excel-level examples
   - Part 3: Real bias cases (Uber surge pricing, Netflix)
   - Part 4: Complete marketing case study walkthrough
   - Part 5: Actionable next steps

3. INTERACTIVE ELEMENTS:
   - 4+ quizzes in LiaScript format
   - 2+ Mermaid diagrams (data workflow, decision framework)
   - Progressive revelation using {{0}}, {{1}}, {{2}}
   - Discussion prompts
   - Practice activities

4. LIASCRIPT FORMAT:
   - Proper slide separators (---)
   - Quiz syntax: [( )] and [(X)]
   - Mermaid blocks: ```mermaid
   - Speaker notes where helpful
   - Section headers with timing

5. BUSINESS EXAMPLES:
   - E-commerce conversion rates
   - Marketing A/B test results
   - Sales pipeline data
   - Customer satisfaction scores
   - Financial forecasting

Create polished, ready-to-teach materials.

Save to materials/01-lecture.md
```

Press Enter and wait a couple of minutes

</div>

{{2}}
<div class="success-box">

**✋ CHECKPOINT (after 2-4 minutes):**

Check if `materials/01-lecture.md` was created and is 4,000+ words!

1. Open the file in VS Code
2. Look at bottom-right corner → Should show word count
3. Scroll through → Should see complete lecture structure

**✅ If created and substantial → Stage 5 complete!**

**⚠️ If incomplete:** Local AI might need multiple attempts. You can:
- Ask Continue to continue writing
- Or break into smaller sections

</div>

---

### Step 9: Quick Validation

**👉 STAGE 6: VALIDATE:**

<div class="step-box">
<h4>✅ Quality Check</h4>

In Continue panel, type:

```
@folder Please validate the course materials.

Check:
1. Are all 5 learning objectives covered in materials/01-lecture.md?
2. Does total timing match 90 minutes?
3. Is LiaScript syntax correct?
4. Is Prof. Zhang's voice consistent?
5. Are there interactive elements (quizzes, diagrams)?
6. Are business examples included?

Create docs/validation-report.md with:
- List of checks (✅ PASSED or ❌ FAILED)
- Any issues found
- Recommendations for improvement
- File structure summary

Save to docs/validation-report.md
```

Press Enter and **wait 30 seconds**

</div>

---

### Step 10: Create README

**👉 STAGE 7: DOCUMENTATION:**

{{0}}
<div class="step-box">
<h4>📄 Course Documentation</h4>

In Continue panel, type:

```
@folder Create a comprehensive README.md for this course.

Include:
- Course title and description
- Learning objectives
- Target audience
- Duration and structure
- How to use the materials
- Prof. Michael Zhang introduction
- File structure guide
- How to view in LiaScript
- Credits and license

Make it professional and welcoming for other instructors.

Save to README.md
```

Press Enter and **wait 30 seconds**

</div>

{{1}}
<div class="success-box">

**🎉 COURSE COMPLETE!**

You've created a complete course using **100% LOCAL AI**!

**What you built:**

```
✅ docs/lecture-outline.md
✅ docs/lecture-didactics.md
✅ docs/lecture-agenda.md
✅ skeletons/01-lecture.md
✅ materials/01-lecture.md (4,000-5,000 words!)
✅ docs/validation-report.md
✅ README.md

Total: 7 files, completely offline!
```

**Time:** ~15 minutes (vs. 45 min with cloud AI, vs. 20+ hours manually!)

</div>

---

## Part 5: Compare Cloud vs. Local Results (15 minutes)

Let's compare your two courses side-by-side!

### Comparison Activity

**👉 EVERYONE COMPARE:**

<div class="step-container">

<div class="step-box">
<h4>📊 Your Two Courses</h4>

**Course 1: AI in TVET**
- Created with: Cloud AI (Copilot + Claude Sonnet 4.5)
- Time: 5-7 minutes
- Quality: Professional, polished

**Course 2: Data Literacy**
- Created with: Local AI (Ollama + DeepSeek R1:7b / llama3.1:8b)
- Time: 15-35 minutes
- Quality: Good, functional

</div>

</div>

---

### Side-by-Side Analysis

<div class="comparison-table">

**Open both files and compare:**

| Aspect | Cloud AI (AI in TVET) | Local AI (Data Literacy) |
|--------|-----------------------|--------------------------|
| **Structure** | ✅ Clear, well-organized | ✅ Clear, well-organized |
| **Completeness** | ⭐⭐⭐⭐⭐ All sections complete | ⭐⭐⭐⭐ Mostly complete |
| **Writing Quality** | ⭐⭐⭐⭐⭐ Polished, eloquent | ⭐⭐⭐⭐ Good, functional |
| **Professor Voice** | ⭐⭐⭐⭐⭐ Consistent, natural | ⭐⭐⭐⭐ Consistent, good |
| **Examples** | ⭐⭐⭐⭐⭐ Rich, detailed | ⭐⭐⭐⭐ Present, relevant |
| **Interactive Elements** | ⭐⭐⭐⭐⭐ 7+ quizzes, diagrams | ⭐⭐⭐⭐ 4-5 quizzes, diagrams |
| **LiaScript Syntax** | ⭐⭐⭐⭐⭐ Perfect | ⭐⭐⭐⭐ Mostly correct |
| **Length** | 6,000-7,000 words | 4,000-5,000 words |
| **Generation Time** | 5-7 minutes | 20-50 minutes |

</div>

---

### Discussion: Which is Better?


<div class="info-box">

**Group Discussion (5 minutes):**

**Questions to consider:**

1. **Quality:** Is the cloud version significantly better? Or is local "good enough"?

2. **Speed:** Is the extra 10-25 minutes with local AI acceptable?

3. **Use Cases:** When would you choose each approach?

4. **Cost-Benefit:** Is cloud AI worth $10-20/month?

5. **Privacy:** How important is keeping data on your computer?

6. **Practicality:** Could you use local AI for course drafts, then cloud AI for final polish?

</div>

---

### Hybrid Workflow Strategy

<div class="success-box">

**🎯 RECOMMENDED APPROACH:**

**Phase 1: Planning with Local AI (FREE)**

```
✅ Brainstorm course ideas → DeepSeek / llama 3.1
✅ Create outlines → DeepSeek / llama 3.1
✅ Draft learning objectives → DeepSeek / llama 3.1
✅ Plan session structure → DeepSeek / llama 3.1
✅ Generate skeletons → DeepSeek / llama 3.1

Time: 10-35 minutes
Cost: $0
Privacy: 100%
```

**Phase 2: Production with Cloud AI (QUALITY)**

```
✅ Generate final materials → Claude
✅ Polish content → Claude
✅ Add rich examples → Claude
✅ Refine interactivity → Claude
✅ Validate thoroughly → Claude

Time: 5-10 minutes
Cost: Part of subscription
Quality: Maximum
```

**Result:** Best of both worlds - privacy + speed + quality!

</div>

---

## Part 6: Best Practices & Workshop Wrap-up (10 minutes)

Let's consolidate everything you've learned today!


### Complete Workshop Summary

<div class="warning-box">

**🎓 5-Hour Workshop: What You Accomplished**

**SESSION 1 (1h 40min): Foundations**

```
✅ Understood Agentic AI vs. Traditional AI
✅ Installed VS Code, GitHub, Copilot
✅ Learned BMAD Method (7 stages)
✅ Explored templates, tasks, agent config
✅ Grasped file structure and workflow
```

**SESSION 2 (1h 40min): Cloud Implementation**

```
✅ Created GitHub repository
✅ Built complete "AI in TVET" course
✅ Mastered megaprompt technique
✅ Generated 7 files, 6,000+ words
✅ Saved to Desktop + GitHub cloud
✅ Learned Git version control
```

**SESSION 3 (1h 40min): Local AI**

```
✅ Installed Ollama + DeepSeek model / llama 3.1
✅ Configured Continue extension
✅ Created "Data Literacy" course offline
✅ Compared cloud vs. local results
✅ Designed hybrid workflow strategy
✅ Gained complete BMAD independence
```

**TOTAL:** 3 complete courses, 2 AI systems, infinite possibilities!

</div>

---

### Your Toolkit: What You Can Now Do

<div class="success-box">

**🛠️ YOU NOW HAVE:**

**Technology Stack:**

- ✅ VS Code (development environment)
- ✅ GitHub (version control + cloud storage)
- ✅ GitHub Copilot + Claude (cloud AI, high quality)
- ✅ Ollama + DeepSeek / llama 3.1 (local AI, free + private)
- ✅ Continue extension (local AI interface)
- ✅ LiaScript (interactive presentation format)

**BMAD Template System:**

- ✅ 7-stage workflow
- ✅ Reusable templates (YAML)
- ✅ Task definitions (step-by-step guides)
- ✅ Agent instructions (AI personality)
- ✅ Quality checklists

**Skills:**

- ✅ Megaprompt technique (rapid development)
- ✅ Sequential prompting (local AI)
- ✅ Git version control
- ✅ GitHub collaboration
- ✅ LiaScript authoring
- ✅ Professor persona creation
- ✅ Course validation

</div>

---



### Real-World Application Scenarios


<div class="info-box">

**Scenario 1: New Course Development**

**Timeline: 1 Week**

**Day 1: Planning (Local AI)**
- Create 3-4 course outlines
- Experiment with different approaches
- Draft learning objectives
- Plan session structures
- **Time:** 1 hour, **Cost:** $0

**Day 2-3: Review & Refine**
- Discuss with colleagues
- Select best approach
- Refine objectives
- **Time:** 2 hours, **Cost:** $0

**Day 4: Production (Cloud AI)**
- Generate all materials with megaprompt
- Full interactive content
- Professional quality
- **Time:** 30 minutes, **Cost:** $0 (within subscription)

**Day 5-7: Polish & Test**
- Manual refinement
- Test with pilot group
- Final adjustments
- **Time:** 2-3 hours

**Total:** 5-6 hours vs. 40+ hours traditional method!

</div>

---


<div class="success-box">

**Scenario 2: Rapid Content Update**

**Situation:** Government changes curriculum requirements, need to update 5 courses

**With BMAD:**

**Week 1: Assessment**
- Review requirements with local AI
- Generate updated outlines
- Identify what needs changing
- **Time:** 2 hours, **Cost:** $0

**Week 2: Implementation**
- Use cloud AI megaprompt for each course
- Generate updated materials
- Validate against requirements
- **Time:** 1 hour (5 x 12 min), **Cost:** $0 (within subscription)

**Week 3: Review**
- Internal review
- Stakeholder approval
- Final refinements
- **Time:** 3-4 hours

**Total:** 6-7 hours for 5 complete course updates vs. 200+ hours traditional!

</div>

---


### Troubleshooting Guide

<div class="warning-box">

**Common Issues & Solutions:**

**Problem: DeepSeek / llama 3.1 is too slow**
✅ Solutions:
- Use for outlines only, cloud AI for materials
- Upgrade RAM (16GB recommended)
- Try smaller prompts
- Consider GPU if available

**Problem: Continue doesn't connect to Ollama**
✅ Solutions:
- Verify Ollama is running (check system tray)
- Restart Ollama: `ollama serve`
- Check config.json uses `http://localhost:11434`
- Restart VS Code

**Problem: Local AI output is incomplete**
✅ Solutions:
- Break into smaller prompts
- Ask AI to continue writing
- Increase specificity in prompts
- Use cloud AI for complex sections

**Problem: GitHub sync issues**
✅ Solutions:
- Use GitHub Desktop (easier than CLI)
- Check internet connection
- Verify GitHub credentials
- Use personal access token

**Problem: LiaScript syntax errors**
✅ Solutions:
- Use LiaScript Live Editor for testing
- Reference cheat sheet in data/ folder
- Ask AI to fix specific errors
- Validate with /validate-lecture command

</div>

---

### Resources & Support


<div class="info-box">

**📚 DOCUMENTATION:**

**BMAD Method:**

- Template Repository: https://github.com/SabbirRifat-uni/AI-Agent-BMAD-Whole-Course-Setup-Demo
- Example Courses: Browse public GitHub repos
- This Workshop Materials: Provided folders

**Tools:**

- **Ollama:** https://ollama.com/library (model library)
- **DeepSeek:** https://ollama.com/library/deepseek-r1
- **llama 3.1:** https://ollama.com/library/llama3.1
- **Continue:** https://continue.dev/docs
- **LiaScript:** https://liascript.github.io
- **GitHub:** https://docs.github.com

**Learning:**

- **Git Tutorial:** https://git-scm.com/book
- **Markdown Guide:** https://www.markdownguide.org
- **Prompt Engineering:** https://www.promptingguide.ai

</div>

---



## 🎉 Workshop Complete!

<div class="success-box">

**CONGRATULATIONS! 🎊**

You've completed the **5-hour BMAD Method Workshop**!

**What You Can Now Do:**

```
✅ Create complete university courses in 10-30 minutes
✅ Use both cloud and local AI effectively
✅ Work online OR offline with BMAD
✅ Maintain version control with Git/GitHub
✅ Create interactive LiaScript presentations
✅ Design custom professor personas
✅ Generate 5,000-7,000 word lectures
✅ Validate quality automatically
✅ Share courses with global community
✅ Train colleagues on the method
✅ Scale to entire curriculum
```

**You've Built:**

```
🏆 2 Complete Courses:
   1. AI in TVET (cloud AI) - 6,000+ words
   2. Data Literacy (local AI) - 4,000+ words

🛠️ 2 AI Systems:
   1. GitHub Copilot + Claude Sonnet 4.5
   2. Ollama + DeepSeek R1:7b / llama3.1:8b

📁 2 GitHub Repositories:
   1. AI-in-TVET-Course
   2. Data-Literacy-Course (can be pushed)

💡 Complete BMAD Toolkit:
   - Templates, tasks, checklists
   - Both cloud and local workflows
   - Professional portfolio foundation
```

</div>

---



## 🙏 Thank You!

{{0}}
<div class="success-box">

**THANK YOU FOR PARTICIPATING!**

You've been incredible students and active participants!

**Workshop instructor:**

- Hannes Tegelbeckers (hannes.tegelbeckers@ovgu.de)

**Institution:**
- ITVET, Otto-von-Guericke University Magdeburg, Germany


**Date:** January 12, 2026

</div>

---

{{1}}
<div class="info-box">

**STAY IN TOUCH:**

We'd love to hear about:
- Courses you create
- Challenges you face
- Successes you achieve
- Ideas for improvement

**Email us!** We're here to support your journey.

**Follow-up:**
- We'll send workshop materials summary
- Access to template repository
- Additional resources and guides
- Invitation to future workshops

</div>

---



## 🌟 You Are Now a BMAD Expert!

<div class="success-box">

**GO CREATE AMAZING COURSES!**

Remember:
- Start small, scale up
- Experiment freely
- Share your work
- Help others learn
- Keep improving

**You have the power to transform education!**

**Good luck and happy course creating! 🚀**

</div>

---





