<!--
author:   BMAD Workshop Team
email:    workshop@bmad-method.com
version:  1.0.0 - Final
language: en
narrator: English Female
comment:  Presentation 4 of 4: Local AI (Offline) - Practical Workshop
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

# 🖥️ Presentation 4-V1: Local AI (Offline)

> **Course:** BMAD Method - Automated Course Creation with AI  
> **Presentation:** 4 of 4 (Final)  
> **Duration:** 1 hour 15 minutes  
> **Format:** Hands-on Workshop - Follow Along!

---

## 📚 Complete Course Overview

| # | Presentation | Duration | What You'll Learn |
|---|--------------|----------|-------------------|
| ✅ 1 | Fundamentals & Setup | 1h 15m | BMAD basics, VS Code, GitHub, Copilot |
| ✅ 2 | Material Generation | 1h 15m | Folder structure, prompts, megaprompt |
| ✅ 3 | Customization & Publishing | 1h 15m | Better prompts, GitHub Desktop, LiaScript |
| **→ 4** | **Local AI (Offline)** | **1h 15m** | **Python, Ollama, offline generation** |

**Total Course:** 5 hours of hands-on learning

---

## 👋 Welcome to the Final Presentation!

**Why Offline AI?**

| Online (Copilot) | Offline (Ollama) |
|------------------|------------------|
| Needs internet | Works anywhere |
| Monthly fee ($19) | Completely free |
| Data goes to cloud | Data stays on your computer |
| API limits apply | No limits |

**Best of both:** Learn both methods, use what fits your situation!

---

## What We'll Do (1 hour 15 minutes)

1. Install Python (15 min)
2. Install Ollama (10 min)
3. Download AI model (10 min)
4. Create Python generator script (15 min)
5. Generate course offline (15 min)
6. Publish your offline-generated course (10 min)

**⚡ By the end:** You'll generate courses without internet!

---

# Part A: Install Python (15 minutes)

---

## What is Python?

**Python is a programming language that:**
- Is easy to learn
- Runs on any computer
- Can talk to AI models
- Is used by millions of people

**You don't need to become a programmer!**
We'll just run one script.

---

## Check If You Already Have Python

      {{0}}
**👉 DO THIS NOW:**

1. Open **VS Code**
2. Open the Terminal: **View → Terminal** (or press `` Ctrl+` ``)
3. Type this command and press Enter:

```bash
python --version
```

**If you see:** `Python 3.x.x` → You have Python! Skip to Part B.

**If you see:** Error or "not recognized" → Continue below.

---

## Download Python

      {{0}}
**👉 DO THIS NOW:**

1. Go to: **python.org**
2. Click **"Downloads"**
3. Click the big yellow **"Download Python 3.x.x"** button
4. Save the file to your Downloads folder

---

## Install Python (Windows)

      {{0}}
**👉 DO THIS NOW:**

1. Run the downloaded file
2. **⚠️ IMPORTANT:** Check the box that says **"Add Python to PATH"**
3. Click **"Install Now"**
4. Wait for installation to complete
5. Click "Close"

<div class="warning-box">

**⚠️ Don't forget step 2!** 
The "Add Python to PATH" checkbox is REQUIRED.

</div>

---

## Verify Python Works

      {{0}}
**👉 DO THIS NOW:**

1. **Close VS Code completely**
2. **Open VS Code again** (this refreshes the terminal)
3. Open Terminal: **View → Terminal**
4. Type:

```bash
python --version
```

**You should see:** `Python 3.x.x`

<div class="success-box">

**✅ Python is installed!**

</div>

---

## Install Required Library

      {{0}}
**👉 DO THIS NOW:**

In the terminal, type:

```bash
pip install requests
```

Wait for it to finish. You'll see "Successfully installed..."

<div class="info-box">

**What is `requests`?**  
A library that lets Python talk to Ollama. Think of it as a translator.

</div>

---

# Part B: Install Ollama (10 minutes)

---

## What is Ollama?

**Ollama is like a container that:**
- Runs AI models on YOUR computer
- Works completely offline
- Is free and open source
- Handles all the complicated AI stuff for you

**You tell Ollama what AI model to use, and it does the rest!**

---

## Download Ollama

      {{0}}
**👉 DO THIS NOW:**

1. Go to: **ollama.ai**
2. Click **"Download"**
3. Choose your system (Windows/Mac/Linux)
4. Save the installer

---

## Install Ollama

      {{0}}
**👉 DO THIS NOW:**

1. Run the downloaded installer
2. Click through the installation (all defaults are fine)
3. Wait for it to complete
4. Ollama runs in the background automatically

---

## Verify Ollama Works

      {{0}}
**👉 DO THIS NOW:**

Open a **new terminal** in VS Code and type:

```bash
ollama --version
```

**You should see:** `ollama version x.x.x`

<div class="success-box">

**✅ Ollama is installed!**

</div>

---

# Part C: Download AI Model (10 minutes)

---

## What AI Model Should We Use?

**DeepSeek Coder** is perfect for us:
- Very good at following instructions
- Produces well-formatted text
- Runs on most computers (6.7GB)
- Completely free

---

## Download DeepSeek Coder

      {{0}}
**👉 DO THIS NOW:**

In the terminal, type:

```bash
ollama pull deepseek-coder:6.7b
```

**This downloads 6.7GB.** Time depends on your internet:
- Fast internet: 5-10 minutes
- Slow internet: 15-30 minutes

**You'll see progress:** `pulling... 45% |████████░░░░░░░░|`

---

## While Downloading: Understand the Size

| Model | Size | Quality | Speed |
|-------|------|---------|-------|
| Small (1B) | ~1GB | Lower | Very fast |
| Medium (6.7B) | ~4GB | Good | Moderate |
| Large (13B+) | ~8GB+ | Excellent | Slower |

**We're using 6.7B** = Good balance of quality and speed.

---

## Test the Model Works

      {{0}}
**👉 DO THIS NOW (after download completes):**

```bash
ollama run deepseek-coder:6.7b
```

You're now chatting with local AI! Type:

```
Hello! Write a haiku about learning.
```

Press Enter. You should get a response!

**To exit:** Type `/bye` and press Enter.

<div class="success-box">

**✅ Your local AI is working!**

</div>

---

# Part D: Create Python Generator Script (15 minutes)

---

## What Will This Script Do?

```
Your Prompt → Python Script → Ollama → Course Content
```

The script:
1. Takes your prompt
2. Sends it to Ollama
3. Gets the response
4. Saves it to a file

---

## Create the Script

      {{0}}
**👉 DO THIS NOW:**

1. In VS Code, open your `my-first-bmad-course` folder
2. Create a new file: **File → New File**
3. Save it as: `generator.py` (in the root folder)

---

## The Generator Script

      {{0}}
**👉 COPY THIS ENTIRE SCRIPT into generator.py:**

```python
import requests
import json
import os
from datetime import datetime

def generate_content(prompt, model="deepseek-coder:6.7b"):
    """Send prompt to Ollama and get response."""
    url = "http://localhost:11434/api/generate"
    
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    
    print(f"🤖 Generating content with {model}...")
    print("⏳ This may take 1-3 minutes...")
    
    try:
        response = requests.post(url, json=data, timeout=300)
        response.raise_for_status()
        result = response.json()
        return result.get("response", "")
    except requests.exceptions.ConnectionError:
        print("❌ Error: Cannot connect to Ollama.")
        print("   Make sure Ollama is running!")
        return None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def save_to_file(content, filename):
    """Save content to a markdown file."""
    # Create materials folder if it doesn't exist
    os.makedirs("materials", exist_ok=True)
    
    filepath = os.path.join("materials", filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"✅ Saved to: {filepath}")
    return filepath

def main():
    print("=" * 50)
    print("🎓 BMAD Offline Course Generator")
    print("=" * 50)
    
    # The prompt - customize this!
    prompt = """
Create a 20-minute session for beginners on "Introduction to Time Management"

Include:
- Session title and learning objectives
- An engaging introduction with a relatable scenario
- 3-4 main teaching points with clear explanations
- 2 practical tips they can use immediately
- A brief summary

Format as clean Markdown with proper headings (# ## ###).
Use simple language suitable for beginners.
Make it engaging and practical.
"""
    
    print("\n📝 Your prompt:")
    print("-" * 40)
    print(prompt[:200] + "..." if len(prompt) > 200 else prompt)
    print("-" * 40)
    
    # Generate content
    content = generate_content(prompt)
    
    if content:
        # Create filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        filename = f"session-generated-{timestamp}.md"
        
        # Save the content
        save_to_file(content, filename)
        
        print("\n" + "=" * 50)
        print("🎉 DONE! Your content has been generated!")
        print("=" * 50)
        print(f"\n📄 Preview (first 500 characters):")
        print("-" * 40)
        print(content[:500])
        print("-" * 40)
    else:
        print("\n❌ Generation failed. Check that Ollama is running.")

if __name__ == "__main__":
    main()
```

4. **Save the file** (Ctrl+S)

---

## Understanding the Script

<div class="info-box">

**Key parts:**

| Part | What it does |
|------|--------------|
| `generate_content()` | Talks to Ollama |
| `save_to_file()` | Saves output to markdown |
| `prompt = """..."""` | Your instructions to AI |
| `main()` | Runs everything |

**You only need to change the `prompt` variable!**

</div>

---

# Part E: Generate Course Offline (15 minutes)

---

## Make Sure Ollama is Running

      {{0}}
**👉 DO THIS NOW:**

Open a **new terminal** and type:

```bash
ollama serve
```

You should see: `Listening on 127.0.0.1:11434`

**Keep this terminal open!**

<div class="warning-box">

**⚠️ Don't close the Ollama terminal!**
It needs to stay running while you generate content.

</div>

---

## Run the Generator

      {{0}}
**👉 DO THIS NOW:**

1. Open a **second terminal** in VS Code
2. Navigate to your project folder (if not already there)
3. Run:

```bash
python generator.py
```

**Wait 1-3 minutes.** You'll see progress messages.

---

## Success!

      {{0}}
**When it finishes, you'll see:**

```
🎉 DONE! Your content has been generated!
✅ Saved to: materials/session-generated-20250117-143052.md
```

**👉 DO THIS NOW:**

1. Open the `materials/` folder
2. Find your generated file
3. Open it and read the content!

<div class="success-box">

**🎉 You just generated course content COMPLETELY OFFLINE!**

</div>

---

## Customize the Prompt

      {{0}}
**👉 DO THIS NOW:**

1. Open `generator.py`
2. Find the `prompt = """` section
3. Replace it with YOUR topic:

```python
    prompt = """
Create a 20-minute session for [YOUR AUDIENCE] on "[YOUR TOPIC]"

Include:
- Session title and learning objectives
- An engaging introduction
- 3-4 main teaching points
- 2 practical exercises
- A summary

Format as clean Markdown with proper headings.
"""
```

4. Save and run again!

---

## Generate Multiple Sessions

      {{0}}
**👉 TRY THIS:**

Change the prompt to generate Session 2, then Session 3:

```python
    prompt = """
Create Session 2 of a Time Management course: "The Priority Matrix"

This is a follow-up to Session 1 (Introduction to Time Management).

Include:
- What is the Eisenhower Matrix
- How to categorize tasks
- A hands-on exercise for categorizing their own tasks
- Common mistakes to avoid

Duration: 20 minutes
Audience: Beginners
Format: Markdown
"""
```

---

# Part F: Publish Your Offline Course (10 minutes)

---

## Add LiaScript Header

      {{0}}
**👉 DO THIS NOW:**

1. Open your generated file in `materials/`
2. Add this header at the VERY TOP:

```markdown
<!--
author:   Your Name
version:  1.0.0
language: en
narrator: English Female
comment:  Generated offline using BMAD + Ollama
-->

(rest of generated content below...)
```

3. Save the file

---

## Push to GitHub

      {{0}}
**👉 DO THIS NOW:**

1. Open **GitHub Desktop**
2. See your new/changed files
3. Write message: `Added offline-generated session`
4. Click **"Commit to main"**
5. Click **"Push origin"**

---

## Get Your LiaScript URL

      {{0}}
**👉 DO THIS NOW:**

1. Go to **github.com** → your repository
2. Navigate to your generated file in `materials/`
3. Click **"Raw"**
4. Copy the URL
5. Go to **liascript.github.io**
6. Paste the Raw URL
7. View your course!

<div class="success-box">

**🎉 Your offline-generated course is now LIVE online!**

</div>

---

# 🎓 Course Complete!

---

## What You Learned in This Course

| Presentation | Skills Gained |
|--------------|---------------|
| **1. Fundamentals** | VS Code, GitHub, Copilot basics |
| **2. Generation** | Folder structure, megaprompt, AI content |
| **3. Publishing** | Better prompts, GitHub Desktop, LiaScript |
| **4. Offline** | Python, Ollama, local AI generation |

---

## Your BMAD Toolkit

<div class="success-box">

**Online Workflow:**
```
VS Code → Copilot → GitHub → LiaScript
```

**Offline Workflow:**
```
VS Code → Python → Ollama → GitHub → LiaScript
```

**Both produce the same result:** Professional course materials!

</div>

---

## Quick Reference: Common Commands

| Task | Command |
|------|---------|
| Check Python | `python --version` |
| Check Ollama | `ollama --version` |
| Start Ollama | `ollama serve` |
| Download model | `ollama pull deepseek-coder:6.7b` |
| Chat with AI | `ollama run deepseek-coder:6.7b` |
| Run generator | `python generator.py` |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "Python not found" | Reinstall Python, check "Add to PATH" |
| "Cannot connect to Ollama" | Run `ollama serve` in separate terminal |
| "Model not found" | Run `ollama pull deepseek-coder:6.7b` |
| Generation is very slow | Normal for first run; subsequent runs faster |
| Output quality is poor | Make your prompt more specific |

---


## 🎉 Congratulations!

<div class="success-box">

**You are now a BMAD practitioner!**

You can:
- ✅ Create professional courses with AI
- ✅ Work online OR offline
- ✅ Publish interactive content
- ✅ Share your knowledge with the world

**Go create something amazing!** 🚀

</div>

---


