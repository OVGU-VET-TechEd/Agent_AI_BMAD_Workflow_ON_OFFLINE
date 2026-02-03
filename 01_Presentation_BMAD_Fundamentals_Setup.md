<!--
author:   BMAD Workshop Team
email:    workshop@bmad-method.com
version:  1.0.0 - Final
language: en
narrator: English Female
comment:  Presentation 1 of 4: BMAD Fundamentals & Setup - Practical Workshop
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

# 🚀 Presentation 1: BMAD Fundamentals & Setup

> **Course:** BMAD Method - Automated Course Creation with AI  
> **Presentation:** 1 of 4  
> **Duration:** 1 hour 15 minutes  
> **Format:** Hands-on Workshop - Follow Along!

---

## 📚 Complete Course Overview

| # | Presentation | Duration | What You'll Learn |
|---|--------------|----------|-------------------|
| **→ 1** | **Fundamentals & Setup** | **1h 15m** | **BMAD basics, VS Code, GitHub, Copilot** |
| 2 | Material Generation | 1h 15m | Folder structure, prompts, megaprompt |
| 3 | Customization & Publishing | 1h 15m | Better prompts, GitHub Desktop, LiaScript |
| 4 | Local AI (Offline) | 1h 15m | Python, Ollama, offline generation |

**Total Course:** 5 hours of hands-on learning

---

## 👋 Welcome!

**What we'll do in the next 1 hour 15 minutes:**

1. Understand what BMAD does (10 min)
2. Set up VS Code + GitHub (25 min)
3. Install GitHub Copilot (15 min)
4. Create your first repository (15 min)
5. Run your first AI command (10 min)

**⚡ Rule:** Do everything WITH the presenter. Don't just watch!

---

# Part A: What is BMAD? (10 minutes)

---


## BMAD = AI Creates Your Course

**BMAD stands for:** Build → Material → Automate → Delivery

**How it works:**

```
You: "Create a course on Machine Learning for beginners"
     ↓
AI: Generates outline → agenda → sessions → materials
     ↓
You: Review, adjust, publish
```

**That's it!** You guide, AI creates.

---

## The 8 Steps (Simple Version)

```
Step 1: Create Outline      → What topics to cover
Step 2: Create Didactics    → How to teach it
Step 3: Create Agenda       → Time breakdown
Step 4: Create Sessions     → Basic structure
Step 5: Fill Sessions       → Full content
Step 6: Refine Content      → Make it better
Step 7: Check Quality       → Fix problems
Step 8: Bundle Everything   → Ready to publish
```

**You don't need to memorize this.** The AI guides you through each step!

---

## The Problem We're Solving

**Creating a course takes too long:**

| Traditional Way | BMAD Way |
|----------------|----------|
| 20-40 hours | 1-2 hours |
| Manual writing | AI generates |
| Inconsistent format | Professional template |
| Easy to forget steps | Guided pipeline |

---


## Two Ways to Use BMAD

<div class="info-box">

| Method | Internet | Cost | Best For |
|--------|----------|------|----------|
| **Online** (Copilot) | Required | free/paid | Speed, quality |
| **Offline** (Ollama) | Not needed | Free | Privacy, no internet |

**Today:** We set up the Online method (Presentations 1-3)

**Presentation 4:** We add the Offline method

</div>

---

# Part B: Installing VS Code (25 minutes)

---

## What is VS Code?

**VS Code = Your course creation workspace**

- Free code editor from Microsoft
- Works on Windows, Mac, Linux
- Where you'll write and organize courses
- Connects to GitHub and AI tools

---

## Step 1: Download VS Code

      {{0}}
**👉 DO THIS NOW:**

1. Open your browser
2. Go to: **code.visualstudio.com**
3. Click the big **"Download"** button
4. Wait for download to complete

---

## Step 2: Install VS Code

      {{0}}
**👉 DO THIS NOW:**

**Windows:**
1. Double-click the downloaded file
2. Accept the license → Click **Next**
3. ✅ Check **"Add to PATH"**
4. ✅ Check **"Add Open with Code"**
5. Click **Install** → **Finish**

**Mac:**
1. Open the downloaded `.zip`
2. Drag **Visual Studio Code** to **Applications**
3. Open from Applications

---

## Step 3: Open VS Code

      {{0}}
**👉 DO THIS NOW:**

1. Open VS Code
2. You should see the Welcome tab
3. Close the Welcome tab (we don't need it)

<div class="success-box">

**✅ Checkpoint:** Is VS Code open on your screen?

If yes, you're ready to continue!

</div>

---

## Step 4: Create GitHub Account

      {{0}}
**👉 DO THIS NOW (if you don't have an account):**

1. Go to: **github.com**
2. Click **"Sign up"**
3. Enter your email
4. Create a password
5. Choose a username
6. Complete verification
7. Select **Free** plan

**Already have an account?** Just sign in at github.com

---

## Step 5: Install Git

      {{0}}
**👉 DO THIS NOW:**

**Windows:**
1. Go to: **git-scm.com**
2. Download for Windows
3. Run installer → Click **Next** through all screens
4. Click **Install** → **Finish**

**Mac:**
1. Open Terminal (Cmd + Space, type "Terminal")
2. Type: `git --version`
3. If prompted, click **Install** for Xcode tools

---

## Step 6: Connect VS Code to GitHub

      {{0}}
**👉 DO THIS NOW:**

1. In VS Code, click the **person icon** (bottom left)
2. Click **"Sign in to Sync Settings"**
3. Choose **"Sign in with GitHub"**
4. Browser opens → Click **Authorize**
5. Return to VS Code

<div class="success-box">

**✅ Checkpoint:** Is VS Code connected to GitHub?

You should see your GitHub username in VS Code.

</div>

---

# Part C: Installing GitHub Copilot (15 minutes)

---

## What is GitHub Copilot?

**GitHub Copilot = AI assistant inside VS Code**

- It reads your files
- It understands your project
- It generates content when you ask
- It's the "brain" that creates your course

---

## Step 1: Get Copilot Access

      {{0}}
**👉 DO THIS NOW:**

1. Go to: **github.com/features/copilot**
2. Click **"Start free trial"** (or use your plan)
3. Complete the signup

<div class="info-box">

**💡 Students & Teachers:** Get FREE access!

Go to: **education.github.com**

Verify your academic email for free Copilot access.

</div>

---

## Step 2: Install Copilot Extension

      {{0}}
**👉 DO THIS NOW:**

1. In VS Code, press **Ctrl+Shift+X** (Extensions)
2. Search: **"GitHub Copilot"**
3. Click **Install** on "GitHub Copilot"
4. Also install **"GitHub Copilot Chat"**
5. Restart VS Code if prompted

---

## Step 3: Verify Copilot Works

      {{0}}
**👉 DO THIS NOW:**

1. Look at bottom-right of VS Code
2. You should see the **Copilot icon** (two sparkles)
3. Click it → It should say "Ready"

**If it asks to sign in:** Follow the prompts.

<div class="success-box">

**✅ Checkpoint:** Do you see the Copilot icon?

If yes, AI is ready to help you!

</div>

---

# Part D: Create Your First Repository (15 minutes)

---

## What is a Repository?

**Repository = Folder for your course project**

- Stores all your files
- Tracks all changes
- Backs up to the cloud (GitHub)
- Can be shared with others

---

## Step 1: Create Repository on GitHub

      {{0}}
**👉 DO THIS NOW:**

1. Go to **github.com**
2. Click the **+** icon (top right)
3. Click **"New repository"**
4. Fill in:
   - **Name:** `my-first-bmad-course`
   - **Description:** `Testing BMAD method`
   - ✅ **Public**
   - ✅ **Add README file**
5. Click **"Create repository"**

---

## Step 2: Clone to Your Computer

      {{0}}
**👉 DO THIS NOW:**

1. On your new repository page, click **"Code"** (green button)
2. Copy the HTTPS URL
3. In VS Code, press **Ctrl+Shift+P**
4. Type: **"Git Clone"** → Select it
5. Paste the URL → Press Enter
6. Choose **Desktop** as save location
7. Click **"Open"** when asked

---

## Step 3: Explore Your Project

      {{0}}
**👉 DO THIS NOW:**

Look at VS Code's left sidebar. You should see:

```
📁 my-first-bmad-course
   📄 README.md
```

<div class="success-box">

**✅ Checkpoint:** Do you see your repository in VS Code?

This is your course project! Everything you create goes here.

</div>

---

# Part E: Your First AI Command (10 minutes)

---

## Open Copilot Chat

      {{0}}
**👉 DO THIS NOW:**

1. Press **Ctrl+Shift+I** (or click Chat icon in sidebar)
2. Copilot Chat panel opens on the right
3. You'll see a text input at the bottom

---

## Try a Simple Command

      {{0}}
**👉 DO THIS NOW:**

In the Copilot Chat, type this EXACTLY:

```
Create a simple course outline for a 2-hour introduction 
to Microsoft Excel for complete beginners. Include 4 main 
topics with time allocations.
```

Press **Enter** and watch AI generate content!

---

## Understanding the Response

      {{0}}
Copilot will generate something like:

```markdown
# Introduction to Microsoft Excel (2 hours)

## Topic 1: Getting Started (30 min)
- Opening Excel
- Understanding the interface
- Basic navigation

## Topic 2: Entering Data (30 min)
- Typing in cells
- Selecting ranges
- Basic formatting
...
```

**This is AI-generated course content!**

---

## Save Your Work

      {{0}}
**👉 DO THIS NOW:**

1. Click **File → New File** (or Ctrl+N)
2. Copy and paste the AI-generated outline
3. Click **File → Save As**
4. Name it: `course-outline.md`
5. Save inside your `my-first-bmad-course` folder

---

## Push to GitHub

      {{0}}
**👉 DO THIS NOW:**

1. Click **Source Control** icon (left sidebar - looks like branches)
2. You'll see `course-outline.md` listed
3. Click the **+** next to the file (stage it)
4. Type message: `Added course outline`
5. Click the **checkmark** (Commit)
6. Click **"Sync Changes"**

**Now check github.com** - your file is there!

<div class="success-box">

**🎉 Congratulations!** 

You just created content with AI and saved it to the cloud!

</div>

---

# ✅ Presentation 1 Complete!

## What You Accomplished

- ✅ Understand what BMAD does
- ✅ Installed VS Code
- ✅ Connected to GitHub
- ✅ Installed GitHub Copilot
- ✅ Created your first repository
- ✅ Generated content with AI
- ✅ Pushed to the cloud

---

## What's Next?

| Next | Presentation 2: Material Generation |
|------|-------------------------------------|
| **You'll learn:** | Folder structure, session creation, megaprompt |
| **You'll create:** | A complete 3-session mini-course |
| **Duration:** | 1 hour 15 minutes |

---

## Quick Reference Card

**Keyboard Shortcuts:**
- `Ctrl+Shift+I` → Open Copilot Chat
- `Ctrl+Shift+X` → Extensions
- `Ctrl+Shift+P` → Command Palette
- `Ctrl+S` → Save file

**Websites:**
- VS Code: code.visualstudio.com
- GitHub: github.com
- Copilot: github.com/features/copilot

---

**☕ Take a 10-minute break before Presentation 2!**

---

**End of Presentation 1**

