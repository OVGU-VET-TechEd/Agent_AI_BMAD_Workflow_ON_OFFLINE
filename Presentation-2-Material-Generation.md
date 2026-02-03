<!--
author:   BMAD Workshop Team
email:    workshop@bmad-method.com
version:  1.0.0 - Final
language: en
narrator: English Female
comment:  Presentation 2 of 4: Material Generation - Practical Workshop
logo:     https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/ChatGPT_logo.svg/120px-ChatGPT_logo.svg.png

@style
.info-box {
    background-color: rgba(70, 130, 220, 0.1);
    border: 2px solid rgba(70, 130, 220, 0.4);
    border-radius: 10px;
    padding: 20px;
    margin: 15px 0;
}
.success-box {
    background-color: rgba(76, 175, 80, 0.1);
    border: 2px solid rgba(76, 175, 80, 0.4);
    border-radius: 10px;
    padding: 20px;
    margin: 15px 0;
}
.warning-box {
    background-color: rgba(255, 160, 60, 0.1);
    border: 2px solid rgba(255, 160, 60, 0.4);
    border-radius: 10px;
    padding: 20px;
    margin: 15px 0;
}
@end
-->

# 📝 Presentation 2: Material Generation

> **Course:** BMAD Method - Automated Course Creation with AI  
> **Presentation:** 2 of 4  
> **Duration:** 1 hour 15 minutes  
> **Format:** Hands-on Workshop - Follow Along!

---

## 📚 Complete Course Overview

| # | Presentation | Duration | What You'll Learn |
|---|--------------|----------|-------------------|
| ✅ 1 | Fundamentals & Setup | 1h 15m | BMAD basics, VS Code, GitHub, Copilot |
| **→ 2** | **Material Generation** | **1h 15m** | **Folder structure, prompts, megaprompt** |
| 3 | Customization & Publishing | 1h 15m | Better prompts, GitHub Desktop, LiaScript |
| 4 | Local AI (Offline) | 1h 15m | Python, Ollama, offline generation |

**Total Course:** 5 hours of hands-on learning

---

## 👋 Welcome Back!

**Prerequisites:** You completed Presentation 1 and have:
- ✅ VS Code installed
- ✅ GitHub account connected
- ✅ GitHub Copilot working
- ✅ Repository `my-first-bmad-course` created

---

## What We'll Do (1 hour 15 minutes)

1. Set up the BMAD folder structure (15 min)
2. Create course outline with AI (15 min)
3. Create session content with AI (25 min)
4. Learn the Megaprompt method (15 min)
5. Generate a complete mini-course (5 min)

**⚡ Rule:** Create everything with the presenter!

---

# Part A: Project Structure (15 minutes)

---

## The BMAD Folder Structure

**Every BMAD project uses the same folders:**

```
📁 my-course/
├── 📁 docs/           ← Planning documents
├── 📁 materials/      ← Final course content
├── 📁 skeletons/      ← Draft sessions
├── 📁 templates/      ← Reusable formats
└── 📄 README.md       ← Project info
```

This keeps your course organized!

---

## Create the Folders

      {{0}}
**👉 DO THIS NOW:**

1. Open VS Code with your `my-first-bmad-course` repository
2. In the left sidebar, right-click → **New Folder**
3. Create these folders one by one:
   - `docs`
   - `materials`
   - `skeletons`
   - `templates`

---

## Check Your Structure

      {{0}}
Your project should now look like this:

```
📁 my-first-bmad-course/
├── 📁 docs/
├── 📁 materials/
├── 📁 skeletons/
├── 📁 templates/
├── 📄 README.md
└── 📄 course-outline.md  (from Presentation 1)
```

<div class="success-box">

**✅ Checkpoint:** Do you see all 4 folders?

If yes, your structure is ready!

</div>

---

## What Goes Where?

| Folder | Purpose | Example Files |
|--------|---------|---------------|
| `docs/` | Planning documents | outline.md, agenda.md |
| `materials/` | Final course content | session-01.md, session-02.md |
| `skeletons/` | Work-in-progress drafts | draft-session-01.md |
| `templates/` | Reusable formats | megaprompt.md, quiz-template.md |

---

# Part B: Creating Course Outline (15 minutes)

---

## Define Our Mini-Course

      {{0}}
**For this workshop, we'll create:**

<div class="info-box">

**Course:** Introduction to Time Management

- **Duration:** 1 hour total
- **Audience:** University students
- **Sessions:** 3 sessions (20 min each)
  1. Why Time Management Matters
  2. The Main Techniques
  3. Creating Your Plan

</div>

---

## Generate the Outline

      {{0}}
**👉 DO THIS NOW:**

1. Open Copilot Chat (**Ctrl+Shift+I**)
2. Type this prompt:

```
Create a course outline for "Introduction to Time Management" 
for university students. 

The course is 1 hour total with 3 sessions:
- Session 1: Why Time Management Matters (20 min)
- Session 2: The Main Techniques (20 min)  
- Session 3: Creating Your Plan (20 min)

For each session, list 3-4 key topics to cover.
Format as markdown.
```

3. Press **Enter**

---

## Save the Outline

      {{0}}
**👉 DO THIS NOW:**

1. Select all the AI-generated content
2. Create new file: **File → New File**
3. Paste the content
4. Save as: `docs/outline.md`

<div class="success-box">

**✅ Checkpoint:** Is `outline.md` inside the `docs` folder?

</div>

---

## Generate the Agenda

      {{0}}
**👉 DO THIS NOW:**

In Copilot Chat, type:

```
Based on the outline you just created, make a detailed 
agenda table with exact time allocations for each topic.

Format as a markdown table with columns:
| Time | Duration | Topic | Activity |
```

Save as: `docs/agenda.md`

---

# Part C: Creating Session Content (25 minutes)

---

## Creating Session 1

      {{0}}
**👉 DO THIS NOW:**

In Copilot Chat, type:

```
Create the full content for Session 1: "Why Time Management Matters"

Requirements:
- Duration: 20 minutes
- Audience: University students with no background
- Include: Introduction, 3 main points with examples, summary
- Tone: Friendly, practical, relatable to student life
- Add 2 discussion questions at the end

Format as markdown with clear headings.
```

Press **Enter** and wait for AI to generate.

---

## Save Session 1

      {{0}}
**👉 DO THIS NOW:**

1. Copy the AI-generated content
2. Create new file: **File → New File**
3. Paste the content
4. Save as: `materials/session-01-why-time-management.md`

<div class="success-box">

**✅ Session 1 created!** Keep going...

</div>

---

## Creating Session 2

      {{0}}
**👉 DO THIS NOW:**

In Copilot Chat, type:

```
Create Session 2: "The Main Time Management Techniques"

Requirements:
- Duration: 20 minutes
- Cover these 3 techniques: Pomodoro, Time Blocking, 2-Minute Rule
- For each technique include:
  * What it is (1-2 sentences)
  * How to do it (step by step)
  * When to use it
  * A student example
- Tone: Practical, actionable

Format as markdown.
```

Save as: `materials/session-02-techniques.md`

---

## Creating Session 3

      {{0}}
**👉 DO THIS NOW:**

In Copilot Chat, type:

```
Create Session 3: "Creating Your Personal Time Plan"

Requirements:
- Duration: 20 minutes
- This is a hands-on session
- Include a step-by-step exercise students do during class
- They should create a weekly schedule template
- End with 3 action items for after class

Format as markdown.
```

Save as: `materials/session-03-your-plan.md`

---

## Check Your Progress

      {{0}}
Your project should now have:

```
📁 my-first-bmad-course/
├── 📁 docs/
│   ├── 📄 outline.md
│   └── 📄 agenda.md
├── 📁 materials/
│   ├── 📄 session-01-why-time-management.md
│   ├── 📄 session-02-techniques.md
│   └── 📄 session-03-your-plan.md
├── 📁 skeletons/
├── 📁 templates/
└── 📄 README.md
```

<div class="success-box">

**🎉 Amazing!** You just created 3 complete sessions in ~25 minutes!

</div>

---

# Part D: The Megaprompt Method (15 minutes)

---

## What is a Megaprompt?

**Megaprompt = One big prompt that creates an entire course**

**Without Megaprompt:**
- Prompt 1 → Outline
- Prompt 2 → Agenda  
- Prompt 3 → Session 1
- Prompt 4 → Session 2
- ... (many prompts)

**With Megaprompt:**
- One detailed prompt → Complete course package!

---

## Megaprompt Structure

```
[ROLE]       → Who the AI should be
[COURSE]     → Title, duration, audience
[CONTENT]    → Topics to cover
[STYLE]      → Tone, format, examples
[OUTPUT]     → What files to generate
```

---

## The Megaprompt Template

      {{0}}
**👉 DO THIS NOW:**

1. Create new file: `templates/megaprompt-template.md`
2. Copy this entire template:

```markdown
# Course Creation Megaprompt

## Your Role
You are an expert course designer. Create a complete, 
ready-to-teach course based on these specifications.

## Course Information
- **Title:** [Course Name]
- **Duration:** [Total Hours]
- **Audience:** [Who is this for - be specific]
- **Prerequisites:** [What they should know]
- **Goal:** By the end, students will be able to [outcome]

## Content Requirements
Create [Number] sessions covering:
1. [Session 1 title] - [X minutes]
2. [Session 2 title] - [X minutes]
3. [Session 3 title] - [X minutes]

## Style Requirements
- Tone: [Formal/Casual/Friendly]
- Include: [Examples, exercises, discussions]
- Avoid: [Jargon, complex terms, etc.]

## Output Format
Generate each session as a separate markdown file with:
- Clear headings
- Bullet points for key concepts
- At least one practical example per topic
- A summary at the end of each session
```

3. Save the file.

---

## Fill In Your Own Megaprompt

      {{0}}
**👉 DO THIS NOW:**

1. Create new file: `templates/my-megaprompt.md`
2. Copy the template
3. Fill it in for a course YOU want to create:
   - Pick a topic you know well
   - Keep it short (30-60 minutes)
   - Define 2-3 sessions

**Example topics:**
- Introduction to [Your Field]
- Basics of [A Skill You Know]
- How to [Something You Can Teach]

---

## Use Your Megaprompt

      {{0}}
**👉 DO THIS NOW:**

1. Copy your filled-in megaprompt
2. Open Copilot Chat
3. Paste the entire megaprompt
4. Press **Enter**
5. Watch AI generate your complete course!

<div class="info-box">

**💡 Tip:** If the output is too long, ask Copilot:

"Generate Session 1 first, then I'll ask for the rest."

</div>

---

# Part E: Save and Commit (5 minutes)

---

## Commit All Your Work

      {{0}}
**👉 DO THIS NOW:**

1. Click **Source Control** icon (left sidebar)
2. You'll see all your new files listed
3. Click **+** to stage all changes
4. Type message: `Added complete time management course`
5. Click the **checkmark** (Commit)
6. Click **"Sync Changes"**

---

## Verify on GitHub

      {{0}}
**👉 DO THIS NOW:**

1. Go to **github.com**
2. Open your `my-first-bmad-course` repository
3. You should see all your folders and files!

<div class="success-box">

**✅ Your course is now backed up to the cloud!**

</div>

---

# ✅ Presentation 2 Complete!

## What You Accomplished

- ✅ Set up BMAD folder structure
- ✅ Generated course outline and agenda
- ✅ Created 3 complete session materials
- ✅ Learned the Megaprompt method
- ✅ Created your own megaprompt template
- ✅ Organized everything in proper folders
- ✅ Pushed to GitHub

---

## What's Next?

| Next | Presentation 3: Customization & Publishing |
|------|---------------------------------------------|
| **You'll learn:** | Better prompts, GitHub Desktop, LiaScript |
| **You'll do:** | Publish your course online for free |
| **Duration:** | 1 hour 15 minutes |

---

## Quick Reference Card

**BMAD Folders:**
- `docs/` → Planning (outline, agenda)
- `materials/` → Final content (sessions)
- `skeletons/` → Drafts
- `templates/` → Reusable formats

**Megaprompt Formula:**
```
ROLE + COURSE + CONTENT + STYLE + OUTPUT
```

---

**☕ Take a 10-minute break before Presentation 3!**

---

**End of Presentation 2**

