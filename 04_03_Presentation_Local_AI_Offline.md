<!--
author:   Sabbir Rifat
email:    a.rifat@ovgu.de
version:  3.0.0
language: en
narrator: English Female
comment:  Session 3: BMAD with Local AI (Offline) via VS Code Chat - No Python Required
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

.highlight-box {
    background-color: rgba(0, 150, 136, 0.1);
    border: 2px solid rgba(0, 150, 136, 0.4);
    border-radius: 12px;
    padding: 25px;
    margin: 20px 0;
    transition: all 0.3s ease;
}

.highlight-box:hover {
    transform: translateY(-8px);
    box-shadow: 0 8px 20px rgba(0, 150, 136, 0.3);
    background-color: rgba(0, 150, 136, 0.15);
}

@end
-->

# Presentation 4-V3: Local AI via VS Code Chat (No Python Required!)

> **Duration**: 1 hour 40 minutes
> **Format**: Hands-On Workshop
> **Target Audience**: Georgian University Academic Staff
> **Prerequisites**: Sessions 1 & 2 completed

Welcome to the final session! Today you'll learn to run AI **completely offline** on your own computer — directly through the **VS Code Chat panel** you already know, with **no Python, no extra extensions, no scripting**.

**The Key Idea:** VS Code's Chat panel has a **model dropdown menu** (see screenshot below). We'll add local Ollama models to that same dropdown — so switching between cloud AI and local AI is as simple as selecting a different model from the list!


---

**What We'll Do Together:**

* **Part 1 - 10 min**: Why Local AI? (Cloud vs. Offline Comparison)
* **Part 2 - 20 min**: Install Ollama + Download DeepSeek / Llama 3.1 Model
* **Part 3 - 20 min**: Add Ollama Models to VS Code Chat Dropdown (The New Way!)
* **Part 4 - 30 min**: Run the Full BMAD Method via Chat (Everyone Together)
* **Part 5 - 10 min**: Compare Cloud vs. Local Results

---

## Quick Recap: The Complete Workshop Journey (3 minutes)

Let's review what we've accomplished over the past sessions!

### Session 1: Foundations (1h 40min)

<div class="info-box">

**What You Learned:**

- Understanding Agentic AI vs. Traditional AI
- Setting up VS Code, GitHub, and Copilot
- BMAD Method: 7-stage workflow
- File structure and templates
- How templates, tasks, and agents work together

**What You Installed:**

- VS Code
- GitHub account + Copilot with Claude Sonnet 4.5
- Understanding of the BMAD ecosystem

</div>

---

### Session 2: Cloud Implementation (1h 40min)

<div class="success-box">

**What You Built:**

- GitHub repository: `AI-in-TVET-Course`
- Complete 2-hour course using megaprompt
- 7 files, 6,000+ words, professional materials
- Dual output: Desktop + GitHub cloud
- Prof. Dr. Elena Hoffmann persona
- Interactive LiaScript lecture

**What You Mastered:**

- GitHub-first workflow
- BMAD megaprompt technique
- Git version control basics
- Cloud collaboration and sharing

</div>

---

### Session 3: Local AI — Today's Approach (1h 40min)

<div class="highlight-box">

**What's Different in This Version (V3)?**

In the previous version (V2), we used:

- The **Continue extension** as a separate chat panel
- **Python scripts** to interact with Ollama
- A **different interface** than what you learned in Sessions 1 & 2

**Today's approach is simpler:**

- **No Python installation needed**
- **No Continue extension needed**
- **No extra tools or scripts**
- We use the **same VS Code Chat panel** you already know from Copilot
- Local models appear in the **same dropdown menu** as Claude / GPT-4o
- Switch between cloud and local AI with **one click**

**This makes the Python setup completely obsolete!**

</div>

---

## Part 1: Why Local AI? (10 minutes)

### Cloud AI vs. Local AI: The Complete Picture

<div class="comparison-table">

| Aspect | Cloud AI (Copilot + Claude) | Local AI (Ollama + DeepSeek / Llama 3.1) |
|--------|----------------------------|------------------------------|
| **Cost** | $10-20/month subscription | FREE forever |
| **Privacy** | Data sent to cloud servers | Data never leaves computer |
| **Internet** | Required always | Not required |
| **Speed** | Very fast (2-10 seconds) | Slower (25-120 seconds) |
| **Quality** | Excellent | Good |
| **Context** | 200K+ tokens | 32K-128K tokens |
| **Setup** | Easy (5 minutes) | Moderate (30-40 minutes) |
| **Updates** | Automatic | Manual download |
| **Power** | Any computer | Needs decent specs |

</div>

---

### When to Use Which?

{{1}}
<div class="info-box">

**Use Cloud AI (Copilot + Claude) When:**

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

**Use Local AI (Ollama + DeepSeek / Llama 3.1) When:**

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

### The Big Advantage of V3: One Interface, Two AI Systems

<div class="highlight-box">

**The Problem Before (V2):**

```
Cloud AI  →  VS Code Copilot Chat panel     (one interface)
Local AI  →  Continue extension panel        (different interface)
            + Python scripts                 (yet another tool)
```

You had to learn multiple tools and switch between different panels.

**The Solution Now (V3):**

```
Cloud AI  →  VS Code Chat panel  →  Select "Claude Sonnet 4.5" from dropdown
Local AI  →  VS Code Chat panel  →  Select "DeepSeek R1:7b" from dropdown
```

**Same panel. Same workflow. Same prompts. Just pick a different model!**

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

**Note:** DeepSeek R1:7b / Llama 3.1:8b model is **4.5–4.9 GB** — one-time download!

</div>

---

## Part 2: Install Ollama + Download Model (20 minutes)

Ollama is a free, open-source application that lets you run AI models on your computer. It runs in the background and serves models through a local API — which VS Code can connect to directly.

### Step 1: Download Ollama

**EVERYONE DO THIS NOW:**

<div class="step-container">

<div class="step-box">
<h4>Go to Ollama Website</h4>

1. Open browser
2. Go to: **`ollama.com`**
3. You'll see the homepage with download button

</div>

<div class="step-box">
<h4>Download for Your OS</h4>

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

**INSTALL NOW:**

<div class="step-container">

<div class="step-box">
<h4>Windows Installation</h4>

1. Run `OllamaSetup.exe`
2. Click **"Install"**
3. Wait for installation (2-3 minutes)
4. Ollama icon appears in system tray (bottom-right)
5. Click **"Finish"**

</div>

<div class="step-box">
<h4>Mac Installation</h4>

1. Open downloaded `.zip` file
2. Drag **Ollama.app** to Applications folder
3. Open Ollama from Applications
4. Allow permissions if prompted
5. Ollama icon appears in menu bar (top-right)

</div>

<div class="step-box">
<h4>Linux Installation</h4>

Run the command from ollama.com:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Wait for installation to complete.

</div>

</div>

---

### Step 3: Verify Ollama Installation

**TEST OLLAMA:**

<div class="step-box">
<h4>Verification Steps</h4>

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

**CHECKPOINT:** Can everyone see Ollama version number?

**If yes** → Ollama is installed correctly!

**If no** → Try:
- Restart computer
- Check system tray/menu bar for Ollama icon
- Re-run installer

</div>

---

### Step 4: Download AI Model(s)

Now let's download the AI model(s) we'll use!

**DOWNLOAD MODEL:**

<div class="step-box">
<h4>Download DeepSeek R1:7b</h4>

In your terminal/PowerShell, type:

```bash
ollama pull deepseek-r1:7b
```

Press Enter and wait...

</div>

<div class="step-box">
<h4>(Optional) Also download Llama 3.1:8b</h4>

```bash
ollama pull llama3.1:8b
```

</div>

<div class="warning-box">

**IMPORTANT:**

- This downloads **~4.9 GB** — takes 5-15 minutes depending on internet speed
- You only do this **ONCE**
- Model is stored permanently on your computer
- You can use it offline forever after download

**Expected Output:**

```
pulling manifest
pulling 8c17e007d6c0... 100% |================| 4.9 GB
pulling 966de95ca8a6... 100% |================| 1.4 KB
pulling fcc5a6bec9da... 100% |================| 7.7 KB
pulling a70ff7e570d9... 100% |================| 6.0 KB
pulling 56bb8bd477a5... 100% |================|   96 B
pulling 34bb5ab01051... 100% |================|  561 B
verifying sha256 digest
writing manifest
success
```

</div>

---

### Step 5: Quick Test in Terminal

**TEST THE MODEL:**

<div class="step-box">
<h4>Quick Test</h4>

In terminal, type:

```bash
ollama run deepseek-r1:7b
```

Then ask a question:

```
Hello! Can you explain what you are in one sentence?
```

Press Enter and wait for response (15-30 seconds).

</div>

<div class="success-box">

**Expected Response (similar to):**

```
I am DeepSeek R1, an AI language model designed to
assist with text-based tasks such as answering
questions, generating content, and providing information.
```

**To exit:** Type `/bye` and press Enter

**If you got a response** → DeepSeek is working! Now let's add it to VS Code Chat.

</div>

---

## Part 3: Add Ollama Models to VS Code Chat Dropdown (20 minutes)

This is the **key part** that makes everything simpler! Instead of installing extra extensions or writing Python scripts, we add our local Ollama models directly to the **same Chat dropdown** you've been using with Copilot.

### How It Works — The Concept

<div class="highlight-box">

**What the screenshot shows:**

The VS Code Chat panel has a **model dropdown** at the top. Right now it lists cloud models like:

- Claude Sonnet 4.5
- GPT-4o
- Gemini

**What we're about to do:**

Add your **local Ollama models** to that same list:

- Claude Sonnet 4.5 (cloud)
- GPT-4o (cloud)
- **DeepSeek R1:7b (LOCAL — offline!)**
- **Llama 3.1:8b (LOCAL — offline!)**

**After setup, switching between cloud and local AI = one click in the dropdown!**

</div>

---

### Step 1: Open VS Code Settings

**DO THIS NOW:**

<div class="step-box">
<h4>Open Settings (JSON)</h4>

1. Open **VS Code**
2. Press **`Ctrl + Shift + P`** (Windows/Linux) or **`Cmd + Shift + P`** (Mac)
3. Type: **`Preferences: Open User Settings (JSON)`**
4. Press Enter
5. The `settings.json` file opens in the editor

</div>

---

### Step 2: Add Ollama as a Chat Model Provider

**ADD THIS CONFIGURATION:**

<div class="step-box">
<h4>Configure Ollama Provider</h4>

In your `settings.json` file, add the following block inside the main `{}` braces. If there are already other settings, add a comma after the last one, then paste this:

```json
"chat.models.providers": [
    {
        "id": "ollama",
        "name": "Ollama (Local)",
        "type": "openai-compatible",
        "baseUrl": "http://localhost:11434/v1",
        "models": [
            {
                "id": "deepseek-r1:7b",
                "name": "DeepSeek R1 7B (Local/Offline)"
            },
            {
                "id": "llama3.1:8b",
                "name": "Llama 3.1 8B (Local/Offline)"
            }
        ]
    }
]
```

**Save** the file (`Ctrl + S`)

</div>

<div class="warning-box">

**Important Notes:**

- Ollama exposes an **OpenAI-compatible API** at `http://localhost:11434/v1` — that's how VS Code connects to it
- The `id` values (`deepseek-r1:7b`, `llama3.1:8b`) must match exactly what you pulled with `ollama pull`
- You can add more models later by pulling them with Ollama and adding entries here
- If you only pulled one model, only include that one in the `"models"` array

</div>

---

### Alternative: Add Models via the Chat Dropdown UI

If you prefer using the graphical interface instead of editing JSON:

<div class="step-box">
<h4>Add via Dropdown (Alternative Method)</h4>

1. Open the **Chat panel** in VS Code (`Ctrl + Shift + I`)
2. Click the **model dropdown** at the top of the Chat panel (where it shows the current model name)
3. Scroll to the bottom and click **"Manage Models..."** or **"Configure Chat Models..."**
4. Click **"Add Model..."**
5. Select **"Ollama"** from the provider list
6. VS Code auto-detects your running Ollama models
7. Check the models you want to add (e.g., `deepseek-r1:7b`)
8. Click **"Add"**

The models now appear in your dropdown!

</div>

<div class="info-box">

**Which method to choose?**

- **JSON method** → More control, can copy-paste exact config, reproducible
- **UI method** → Easier, guided, no typing — but requires Ollama to be running

**Both achieve the same result!** Use whichever feels more comfortable.

</div>

---

### Step 3: Verify — Check the Dropdown

**CHECK NOW:**

<div class="step-box">
<h4>Verify Models Appear in Chat</h4>

1. Make sure Ollama is running (check system tray / menu bar)
2. Open **VS Code Chat panel** (`Ctrl + Shift + I`)
3. Click the **model dropdown** at the top
4. You should now see your local models listed:

```
  Claude Sonnet 4.5          (cloud)
  GPT-4o                     (cloud)
  ─────────────────────────
  DeepSeek R1 7B (Local)     ← NEW!
  Llama 3.1 8B (Local)       ← NEW!
```

5. Select **"DeepSeek R1 7B (Local/Offline)"**

</div>

<div class="success-box">

**CHECKPOINT:** Can you see the local model(s) in the dropdown?

**If yes** → Excellent! You're ready to use local AI through the Chat panel!

**If no** → Try these fixes:
- Make sure Ollama is running: open terminal, type `ollama serve`
- Restart VS Code after saving `settings.json`
- Check that the `baseUrl` is correct: `http://localhost:11434/v1`
- Verify your model name matches: `ollama list` in terminal shows installed models

</div>

---

### Step 4: Test Local AI in VS Code Chat

**TEST NOW:**

<div class="step-box">
<h4>Send a Test Message</h4>

1. In the Chat panel, make sure a **local model** is selected from the dropdown
2. Type:

```
Hello! Please confirm you are running locally on my computer.
What model are you, and what are your capabilities?
```

3. Press Enter
4. Wait **15-90 seconds** for response (local models are slower than cloud)

</div>

<div class="success-box">

**Expected Response (similar to):**

```
I am DeepSeek R1, a large language model running locally
on your computer through Ollama. I can help with:
- Text generation and editing
- Answering questions
- Creating educational content
- Code generation
- And more...

Since I'm running locally, your data never leaves your
machine, and you can use me without an internet connection.
```

**If you got a response → Local AI is working in VS Code Chat!**

</div>

---

### Why This Makes Python Obsolete

<div class="highlight-box">

**What we eliminated by using the Chat dropdown approach:**

| Previously Required (V1/V2) | Now Required (V3) |
|------------------------------|--------------------|
| Python installation | **Not needed** |
| `pip install requests` | **Not needed** |
| Python generator script | **Not needed** |
| Continue extension | **Not needed** |
| `config.json` for Continue | **Not needed** |
| Learning a new interface | **Not needed** |
| Separate chat panel | **Not needed** |

**What you need:**

1. Ollama (to run models locally)
2. One setting in VS Code (to connect to Ollama)

**That's it!** Everything else uses the same Chat panel and workflow from Sessions 1 & 2.

**The BMAD method works identically** — you write the same prompts, reference the same templates, get the same type of output. The only difference is which model processes it.

</div>

---

## Part 4: Run the Full BMAD Method via VS Code Chat (30 minutes)

Now let's create a complete course using your local AI through the VS Code Chat — the **exact same workflow** as Session 2, but completely offline!

### Our Course: "Data Literacy for Business Students"

<div class="info-box">

**Course Specifications:**

- **Title:** Data Literacy for Business Students
- **Target Audience:** Undergraduate Business majors
- **Duration:** 90 minutes (1.5-hour session)
- **Format:** Interactive lecture with case studies
- **Topics:** Understanding data, basic statistics, data-driven decision making, common pitfalls

</div>

---

### Step 1: Select Your Local Model in the Dropdown

**DO THIS FIRST:**

<div class="step-box">
<h4>Switch to Local AI</h4>

1. Open your course folder in VS Code (e.g., the `AI-in-TVET-Course` folder or create a new `Data-Literacy-Course` folder)
2. Open **Chat panel** (`Ctrl + Shift + I`)
3. Click the **model dropdown** at the top
4. Select **"DeepSeek R1 7B (Local/Offline)"** (or whichever local model you installed)
5. The dropdown now shows your local model as active

**That's the only change from Session 2's workflow!** Everything else is the same.

</div>

---

### Step 2: Create Course Folder Structure

**CREATE FOLDERS:**

<div class="step-box">
<h4>Setup New Course Folder</h4>

1. Open File Explorer → Go to Desktop
2. Create new folder: **`Data-Literacy-Course`**
3. Inside it, create these subfolders:

```
Data-Literacy-Course/
 ├── docs/        (empty — planning documents go here)
 ├── materials/   (empty — final content goes here)
 ├── skeletons/   (empty — drafts go here)
 └── templates/   (copy templates from your previous course)
```

4. In VS Code: **File** → **Open Folder** → select `Data-Literacy-Course`

</div>

---

### Step 3: Stage 1 — Create Outline

**IN VS CODE CHAT (with local model selected):**

<div class="step-box">
<h4>Stage 1: Outline</h4>

Type in the Chat panel:

```
I need to create a university course outline using the BMAD Method.

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

Please create a detailed course outline with:
- Clear course description
- All 5 learning objectives with explanations
- Target audience details
- Time commitment (90 minutes)
- An engaging abstract for business students

Format as markdown. I will save this as docs/lecture-outline.md
```

Press Enter and **wait 1-4 minutes** (local model is slower than cloud).

Copy the output and save it as `docs/lecture-outline.md`.

</div>

<div class="success-box">

**CHECKPOINT (after 1-4 minutes):**

Is `docs/lecture-outline.md` created with all 5 learning objectives?

**If yes** → Stage 1 complete!

**If output seems cut off:** Ask in Chat: "Please continue where you left off."

</div>

---

### Step 4: Stage 2 — Create Didactics

**CONTINUE IN CHAT:**

<div class="step-box">
<h4>Stage 2: Didactics (Teaching Style)</h4>

Type in the Chat panel:

```
Now create the didactics document — the teaching approach for this course.

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

Please create a comprehensive didactics document with:
- Complete Prof. Zhang persona description
- Teaching style guidelines
- Difficulty level specifications
- Pedagogical approach details
- How to handle different skill levels in the room

Format as markdown. I will save this as docs/lecture-didactics.md
```

Press Enter and **wait 30-120 seconds**.

Copy the output and save it as `docs/lecture-didactics.md`.

</div>

---

### Step 5: Stage 3 — Create Agenda

**CONTINUE IN CHAT:**

<div class="step-box">
<h4>Stage 3: Agenda</h4>

Type in the Chat panel:

```
Based on the outline and didactics we just created,
now create a detailed session agenda.

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

Create the agenda with:
- Each section with precise timing
- Learning objectives per section
- Transition logic between sections
- Connection to overall course goals

Format as a markdown table and structured document.
I will save this as docs/lecture-agenda.md
```

Press Enter and **wait 30-120 seconds**.

Copy the output and save it as `docs/lecture-agenda.md`.

</div>

---

### Step 6: Stage 4 — Create Session Skeleton

**CONTINUE IN CHAT:**

<div class="step-box">
<h4>Stage 4: Skeleton</h4>

Type in the Chat panel:

```
Now create a detailed session skeleton — the structural
framework that will be filled with full content.

Create a skeleton for the 90-minute Data Literacy lecture
with this structure:

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

Format as markdown. I will save this as skeletons/01-lecture.md
```

Press Enter and **wait 30-60 seconds**.

Copy the output and save as `skeletons/01-lecture.md`.

</div>

{{1}}
<div class="info-box">

**PAUSE HERE FOR GROUP CHECK (2 minutes)**

Everyone should have these 4 files created:

1. `docs/lecture-outline.md`
2. `docs/lecture-didactics.md`
3. `docs/lecture-agenda.md`
4. `skeletons/01-lecture.md`

**If missing any:** Ask for help now before we move to the full materials stage!

</div>

---

### Step 7: Stage 5 — Generate Full Interactive Materials

**THIS IS THE LONGEST STAGE:**

<div class="warning-box">

**IMPORTANT:**

This stage generates 4,000-5,000 words of content. With local AI:

- **Processing time:** 2-5 minutes (much slower than cloud!)
- **Be patient!** The model is working hard on your machine
- **Don't close** the Chat panel while it's generating
- Watch for text appearing gradually

</div>

<div class="step-box">
<h4>Stage 5: Full Materials</h4>

Type in the Chat panel:

```
Now create the COMPLETE interactive lecture materials.

Based on everything we've created (outline, didactics,
agenda, skeleton), generate a full 90-minute interactive
lecture in LiaScript format.

REQUIREMENTS:

1. VOICE: Write entirely in Prof. Michael Zhang's voice
   - Practical, business-focused
   - Uses real company examples
   - Conversational but professional
   - "Let me show you how this works..."

2. CONTENT (4,000-5,000 words):
   - Part 1: Engaging introduction with business impact
   - Part 2: Clear explanations with Excel-level examples
   - Part 3: Real bias cases (e.g., Uber surge pricing, Netflix)
   - Part 4: Complete marketing case study walkthrough
   - Part 5: Actionable next steps

3. INTERACTIVE ELEMENTS:
   - 4+ quizzes in LiaScript format
   - 2+ diagrams described in text
   - Discussion prompts
   - Practice activities

4. LIASCRIPT FORMAT:
   - Proper slide separators (---)
   - Quiz syntax: [( )] for wrong, [(X)] for correct
   - Section headers with timing
   - Speaker notes where helpful

5. BUSINESS EXAMPLES:
   - E-commerce conversion rates
   - Marketing A/B test results
   - Sales pipeline data
   - Customer satisfaction scores

Create polished, ready-to-teach materials.
I will save this as materials/01-lecture.md
```

Press Enter and **wait 2-5 minutes**.

Copy the output and save it as `materials/01-lecture.md`.

</div>

<div class="success-box">

**CHECKPOINT (after 2-5 minutes):**

Check if `materials/01-lecture.md` was created and is substantial!

1. Open the file in VS Code
2. Check bottom status bar for word count
3. Scroll through — should see complete lecture structure

**If created and substantial** → Stage 5 complete!

**If output was cut off:** Type in Chat: "Please continue the lecture from where you stopped." Then append the continuation to the file.

</div>

---

### Step 8: Stage 6 — Validation

**VALIDATE:**

<div class="step-box">
<h4>Stage 6: Quality Check</h4>

Type in the Chat panel:

```
Please validate the course materials I just created.

Check:
1. Are all 5 learning objectives covered?
2. Does total timing match 90 minutes?
3. Is LiaScript syntax correct?
4. Is Prof. Zhang's voice consistent throughout?
5. Are there interactive elements (quizzes, diagrams)?
6. Are business examples included?

Create a validation report with:
- List of checks (PASSED or FAILED for each)
- Any issues found
- Recommendations for improvement
- File structure summary

Format as markdown. I will save this as docs/validation-report.md
```

Press Enter and **wait 30-60 seconds**.

Copy the output and save as `docs/validation-report.md`.

</div>

---

### Step 9: Stage 7 — Create README

<div class="step-box">
<h4>Stage 7: Documentation</h4>

Type in the Chat panel:

```
Create a professional README.md for this course repository.

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

Make it professional and welcoming for other instructors
who might want to use or adapt this course.
```

Press Enter and **wait 30-60 seconds**.

Copy the output and save as `README.md`.

</div>

<div class="success-box">

**COURSE COMPLETE!**

You've created a complete course using **100% Local AI** through the **VS Code Chat panel**!

**What you built:**

```
 docs/lecture-outline.md
 docs/lecture-didactics.md
 docs/lecture-agenda.md
 skeletons/01-lecture.md
 materials/01-lecture.md (4,000-5,000 words!)
 docs/validation-report.md
 README.md

Total: 7 files, completely offline, no Python needed!
```

</div>

---

## Part 5: Compare Cloud vs. Local Results (10 minutes)

Let's compare your two courses side-by-side!

### Comparison Activity

**EVERYONE COMPARE:**

<div class="step-container">

<div class="step-box">
<h4>Your Two Courses</h4>

**Course 1: AI in TVET**
- Created with: Cloud AI (Copilot + Claude Sonnet 4.5)
- Time: 5-7 minutes
- Quality: Professional, polished

**Course 2: Data Literacy**
- Created with: Local AI (Ollama + DeepSeek R1:7b via VS Code Chat)
- Time: 15-35 minutes
- Quality: Good, functional

</div>

</div>

---

### Side-by-Side Analysis

<div class="comparison-table">

**Open both courses and compare:**

| Aspect | Cloud AI (AI in TVET) | Local AI (Data Literacy) |
|--------|-----------------------|--------------------------|
| **Structure** | Clear, well-organized | Clear, well-organized |
| **Completeness** | All sections complete | Mostly complete |
| **Writing Quality** | Polished, eloquent | Good, functional |
| **Professor Voice** | Consistent, natural | Consistent, good |
| **Examples** | Rich, detailed | Present, relevant |
| **Interactive Elements** | 7+ quizzes, diagrams | 4-5 quizzes, diagrams |
| **LiaScript Syntax** | Perfect | Mostly correct |
| **Length** | 6,000-7,000 words | 4,000-5,000 words |
| **Generation Time** | 5-7 minutes | 15-35 minutes |
| **Setup Required** | Copilot subscription | Ollama only |
| **Python Required** | No | **No** (same as cloud!) |

</div>

---

### The V3 Advantage: Seamless Switching

<div class="highlight-box">

**The real power of this approach:**

You can switch between cloud and local AI **mid-conversation**!

**Example workflow:**

1. Start drafting outline with **local model** (free, private)
2. Switch to **Claude Sonnet 4.5** in the dropdown for polishing (high quality)
3. Switch back to **local model** for experimentation
4. Final pass with **cloud** for publication quality

**How:** Just click the dropdown and select a different model. Your chat context stays!

This was not possible with the Python/Continue approach in V2.

</div>

---

### Hybrid Workflow Strategy

<div class="success-box">

**RECOMMENDED APPROACH:**

**Phase 1: Planning with Local AI (FREE)**

```
 Brainstorm course ideas → Local model (dropdown)
 Create outlines → Local model (dropdown)
 Draft learning objectives → Local model (dropdown)
 Plan session structure → Local model (dropdown)
 Generate skeletons → Local model (dropdown)

Time: 10-35 minutes
Cost: $0
Privacy: 100%
```

**Phase 2: Production with Cloud AI (QUALITY)**

```
 Generate final materials → Claude (dropdown)
 Polish content → Claude (dropdown)
 Add rich examples → Claude (dropdown)
 Refine interactivity → Claude (dropdown)
 Validate thoroughly → Claude (dropdown)

Time: 5-10 minutes
Cost: Part of subscription
Quality: Maximum
```

**Result:** Best of both worlds — privacy + quality + cost savings!

</div>

---

