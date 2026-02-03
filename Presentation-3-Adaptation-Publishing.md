<!--
author:   BMAD Workshop Team
email:    workshop@bmad-method.com
version:  1.0.0 - Final
language: en
narrator: English Female
comment:  Presentation 3 of 4: Customization & Publishing - Practical Workshop
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

# 🌐 Presentation 3: Customization & Publishing

> **Course:** BMAD Method - Automated Course Creation with AI  
> **Presentation:** 3 of 4  
> **Duration:** 1 hour 15 minutes  
> **Format:** Hands-on Workshop - Follow Along!

---

## 📚 Complete Course Overview

| # | Presentation | Duration | What You'll Learn |
|---|--------------|----------|-------------------|
| ✅ 1 | Fundamentals & Setup | 1h 15m | BMAD basics, VS Code, GitHub, Copilot |
| ✅ 2 | Material Generation | 1h 15m | Folder structure, prompts, megaprompt |
| **→ 3** | **Customization & Publishing** | **1h 15m** | **Better prompts, GitHub Desktop, LiaScript** |
| 4 | Local AI (Offline) | 1h 15m | Python, Ollama, offline generation |

**Total Course:** 5 hours of hands-on learning

---

## 👋 Welcome Back!

**Prerequisites:** You completed Presentations 1 & 2 and have:
- ✅ VS Code + GitHub + Copilot working
- ✅ Repository with folder structure
- ✅ A 3-session course created
- ✅ Megaprompt template saved

---

## What We'll Do (1 hour 15 minutes)

1. Write better prompts (15 min)
2. Customize AI output (15 min)
3. Install GitHub Desktop (10 min)
4. Publish with LiaScript (20 min)
5. Create your own course from scratch (15 min)

**⚡ Rule:** By the end, you'll have a LIVE published course!

---

# Part A: Better Prompts = Better Output (15 minutes)

---

## Why Some Prompts Work Better

**❌ Bad prompt:**
```
Make a course about Excel
```

**✅ Good prompt:**
```
Create a 1-hour course on Excel basics for office 
workers who have never used spreadsheets. Cover: 
navigation, data entry, simple formulas (SUM, AVERAGE). 
Use workplace examples like expense tracking.
```

**The difference:** Specific details → Targeted content

---

## The 5 Elements of a Good Prompt

<div class="info-box">

| Element | Question | Example |
|---------|----------|---------|
| **WHAT** | What do you want? | "Create a session..." |
| **WHO** | Who is the audience? | "...for beginners with no background" |
| **HOW LONG** | Duration/length? | "...20 minutes long" |
| **STYLE** | Tone and format? | "...friendly tone, with examples" |
| **OUTPUT** | How should it look? | "...as markdown with headings" |

</div>

---

## Practice: Improve a Prompt

      {{0}}
**👉 DO THIS NOW:**

**Original prompt:**
```
Create content about presentation skills
```

**In Copilot Chat, type this improved version:**
```
Create a 20-minute session on "Overcoming Presentation Anxiety"

Audience: Graduate students preparing for thesis defense
Include:
- 3 practical techniques they can use immediately
- A real example of someone who overcame their fear
- A 2-minute breathing exercise with step-by-step instructions

Tone: Supportive and encouraging
Format: Markdown with clear headings
```

**See how much better the output is!**

---

## Quick Prompt Improvements

| Instead of... | Say... |
|--------------|--------|
| "Make it good" | "Include 3 real-world examples" |
| "For students" | "For first-year MBA students with no finance background" |
| "Add exercises" | "Add 2 hands-on exercises they complete during class" |
| "Make it interesting" | "Start with a surprising statistic, use storytelling" |

---

# Part B: Customizing AI Output (15 minutes)

---

## You Don't Have to Accept First Output!

      {{0}}
**👉 TRY THIS NOW:**

After AI generates content, type:

```
Make these changes:
1. Add a story at the beginning about a famous person
2. Make the language simpler - avoid jargon
3. Add a summary box at the end with 3 key takeaways
```

AI will revise the content!

---

## Changing the Tone

      {{0}}
**👉 TRY THIS NOW:**

```
Rewrite the introduction to be more conversational. 
Use "you" and "we" language. 
Add a question that makes students think.
```

---

## Adding Specific Elements

      {{0}}
**👉 TRY THIS NOW:**

```
Add to this session:
- A diagram showing the 4-step process (describe in text)
- A real-world example from a tech company
- A "Common Mistakes" section with 3 things to avoid
```

---

## Converting Formats

      {{0}}
**For presentation slides:**
```
Convert this session into slides. Each slide should have:
- A clear title
- Maximum 5 bullet points
- Speaker notes underneath
```

**For handouts:**
```
Create a 1-page summary handout students can take home.
Include key points and action items only.
```

<div class="success-box">

**💡 Key Insight:** AI is your collaborator. Ask for changes until it's right!

</div>

---

# Part C: GitHub Desktop (10 minutes)

---

## Why GitHub Desktop?

**Command line (complicated):**
```
git add .
git commit -m "message"
git push origin main
```

**GitHub Desktop (easy):** Just click buttons!

---

## Install GitHub Desktop

      {{0}}
**👉 DO THIS NOW:**

1. Go to: **desktop.github.com**
2. Click **"Download for Windows"** (or Mac)
3. Run the installer (click through)
4. Open GitHub Desktop
5. Click **"Sign in to GitHub.com"**
6. Authorize in your browser

---

## Connect Your Repository

      {{0}}
**👉 DO THIS NOW:**

1. In GitHub Desktop, click **"Add"** (top left)
2. Click **"Clone Repository"**
3. Find `my-first-bmad-course` in the list
4. Choose where to save it (Desktop is fine)
5. Click **"Clone"**

<div class="success-box">

**✅ Your repository is now in GitHub Desktop!**

</div>

---

## The Simple Daily Workflow

      {{0}}
**From now on:**

```
1. Make changes in VS Code
2. Open GitHub Desktop
3. See your changes listed automatically
4. Type a short description
5. Click "Commit to main"
6. Click "Push origin"
```

**That's it!** Your work is backed up online.

---

# Part D: Publish with LiaScript (20 minutes)

---

## What is LiaScript?

**LiaScript turns your markdown into an interactive course:**

- ✅ Runs in any browser
- ✅ No installation needed
- ✅ Free to use forever
- ✅ Supports quizzes, animations, multimedia
- ✅ Works with your GitHub files

---

## Make Your Content LiaScript-Ready

      {{0}}
**👉 DO THIS NOW:**

1. Open one of your session files (e.g., `session-01-why-time-management.md`)
2. Add this header at the VERY TOP:

```markdown
<!--
author:   Your Name
version:  1.0.0
language: en
narrator: English Female
-->

# Your Session Title

(rest of your content below...)
```

3. Save the file

---

## Commit and Push

      {{0}}
**👉 DO THIS NOW:**

1. Open **GitHub Desktop**
2. You'll see your changed file
3. Type message: `Added LiaScript header`
4. Click **"Commit to main"**
5. Click **"Push origin"**

---

## Get the LiaScript URL

      {{0}}
**👉 DO THIS NOW:**

1. Go to **github.com** 
2. Open your `my-first-bmad-course` repository
3. Navigate to `materials/session-01-why-time-management.md`
4. Click the **"Raw"** button (top right of file content)
5. **Copy the URL** from your browser address bar

It will look like:
```
https://raw.githubusercontent.com/USERNAME/my-first-bmad-course/main/materials/session-01-why-time-management.md
```

---

## View Your Live Course!

      {{0}}
**👉 DO THIS NOW:**

1. Go to: **liascript.github.io**
2. In the input box, paste your Raw URL
3. Click **"Load Course"**

<div class="success-box">

**🎉 YOUR COURSE IS NOW LIVE!**

Anyone with this URL can view your interactive course!

</div>

---

## Share Your Course

      {{0}}
**The shareable URL format:**

```
https://liascript.github.io/course/?YOUR_RAW_URL
```

**Example:**
```
https://liascript.github.io/course/?https://raw.githubusercontent.com/username/my-first-bmad-course/main/materials/session-01-why-time-management.md
```

**Share this URL with:**
- Students
- Colleagues
- On social media
- In emails

---

## Make It Look Better (Optional)

      {{0}}
**Add custom styling to your LiaScript header:**

```markdown
<!--
author:   Your Name
version:  1.0.0
language: en
narrator: English Female
comment:  A short description of your course

@style
.highlight {
    background-color: #fff3cd;
    padding: 15px;
    border-radius: 5px;
    margin: 10px 0;
}
@end
-->
```

**Use it in your content:**
```markdown
<div class="highlight">

**Key Point:** This is important information!

</div>
```

---

# Part E: Create Your Own Course (15 minutes)

---

## Your Final Exercise

      {{0}}
**👉 DO THIS NOW - Create a real course!**

**Step 1:** Choose YOUR topic
- Something you know well
- Keep it short (30-60 minutes)
- 2-3 sessions maximum

**Ideas:**
- Introduction to [Your Research Area]
- How to [A Skill You Have]
- Basics of [Something You Teach]

---

## Use Your Megaprompt

      {{0}}
**👉 DO THIS NOW:**

1. Open your `templates/megaprompt-template.md`
2. Fill it in for your chosen topic
3. Paste into Copilot Chat
4. Generate your course
5. Save files to `materials/` folder
6. Add LiaScript headers
7. Commit + Push with GitHub Desktop
8. Generate your live URL!

---

## Checklist Before Finishing

      {{0}}
**Make sure you have:**

- [ ] Topic chosen
- [ ] Megaprompt filled and used
- [ ] 2-3 sessions generated
- [ ] Files saved in `materials/`
- [ ] LiaScript headers added
- [ ] Committed and pushed to GitHub
- [ ] Live LiaScript URL working

<div class="success-box">

**🎉 You now have a PUBLISHED course!**

</div>

---

# ✅ Presentation 3 Complete!

## What You Accomplished

- ✅ Learned to write better prompts
- ✅ Customized AI output
- ✅ Installed GitHub Desktop
- ✅ Published course with LiaScript
- ✅ Created your own course from scratch
- ✅ Have a live URL to share!

---

## What's Next?

| Next | Presentation 4: Local AI (Offline) |
|------|-------------------------------------|
| **You'll learn:** | Python, Ollama, DeepSeek model |
| **You'll do:** | Generate courses WITHOUT internet |
| **Duration:** | 1 hour 15 minutes |

<div class="info-box">

**Why learn offline?**
- Works without internet
- Completely free (no subscription)
- Full data privacy
- No API limits

</div>

---

## Quick Reference Card

**Daily Workflow:**
```
1. Open VS Code → Edit files
2. Open GitHub Desktop → Commit + Push
3. Share LiaScript URL
```

**LiaScript URL Formula:**
```
https://liascript.github.io/course/?
https://raw.githubusercontent.com/USER/REPO/main/FILE.md
```

**Good Prompt = WHAT + WHO + HOW LONG + STYLE + OUTPUT**

---

## Resources

- **VS Code:** code.visualstudio.com
- **GitHub:** github.com
- **GitHub Desktop:** desktop.github.com
- **GitHub Copilot:** github.com/features/copilot
- **LiaScript:** liascript.github.io

---

**☕ Take a 10-minute break before Presentation 4!**

---

**End of Presentation 3**

