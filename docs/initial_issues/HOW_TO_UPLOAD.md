# How to Upload Initial Issues and Discussions

This guide shows you how to create the initial issues and discussions for your GitHub repository.

## Part 1: Create Issues

### Issue #1: Phase 4 Roadmap

1. Go to https://github.com/GenAICPA/SkillsforAudit/issues
2. Click the green **"New issue"** button
3. Choose **"Feature Request"** template (or blank if templates aren't showing)
4. Copy the content from `ISSUE_01_phase4_roadmap.md`
5. Fill in:
   - **Title**: `🗺️ Roadmap: Phase 4 - Cross-Reference Engine`
   - **Body**: Paste the content from the file
   - **Labels**: Click gear icon next to "Labels", add: `enhancement`, `help wanted`, `phase-4`
   - **Projects**: Skip for now
   - **Milestone**: Skip for now
6. Click **"Submit new issue"**
7. After creation, click "Pin issue" (right sidebar) to keep it at the top

### Issue #2: Phase 5 Prototype

1. Click **"New issue"** again
2. Copy content from `ISSUE_02_phase5_prototype.md`
3. Fill in:
   - **Title**: `🗺️ Roadmap: Phase 5 - Integrated Prototype`
   - **Labels**: `enhancement`, `help wanted`, `phase-5`
4. Submit and **pin** this issue too

### Issue #3: XBRL Examples Wanted

1. Click **"New issue"**
2. Copy content from `ISSUE_03_xbrl_examples.md`
3. Fill in:
   - **Title**: `📚 Wanted: Real-World XBRL Examples from SEC EDGAR`
   - **Labels**: `help wanted`, `data`, `xbrl`, `good first contribution`
4. Submit and **pin** this issue

## Part 2: Create Welcome Discussion

### First: Enable Discussions

1. Go to https://github.com/GenAICPA/SkillsforAudit/settings
2. Scroll down to **"Features"** section
3. Check the box for **"Discussions"**
4. Click **"Set up discussions"** button

### Configure Discussion Categories

GitHub will create default categories. Let's customize:

1. Go to https://github.com/GenAICPA/SkillsforAudit/discussions/categories
2. Keep or edit these categories:
   - **📢 Announcements** (for project updates)
   - **💡 Ideas** (feature suggestions)
   - **❓ Q&A** (technical questions)
   - **🎓 Show and Tell** (share implementations)
3. Add a new category:
   - Click **"New category"**
   - Name: `Teaching Experiences`
   - Description: `Share classroom stories, student projects, and pedagogical insights`
   - Format: `Discussion`

### Create Welcome Discussion

1. Go to https://github.com/GenAICPA/SkillsforAudit/discussions
2. Click **"New discussion"**
3. Copy content from `ISSUE_04_welcome_discussion.md`
4. Fill in:
   - **Title**: `👋 Welcome to Skills for Audit! Introduce Yourself`
   - **Category**: Select "Announcements"
   - **Body**: Paste the content
5. Click **"Start discussion"**
6. After creation, **pin** the discussion (click ⋯ menu → "Pin discussion")

## Part 3: Add Labels to Repository

Make sure these labels exist (Settings → Labels):

1. Go to https://github.com/GenAICPA/SkillsforAudit/labels
2. Create these labels if they don't exist:

| Label | Color | Description |
|-------|-------|-------------|
| `phase-1` | `#0052CC` | Phase 1: Foundations |
| `phase-2` | `#0052CC` | Phase 2: Structured Data |
| `phase-3` | `#0052CC` | Phase 3: XBRL |
| `phase-4` | `#0052CC` | Phase 4: Cross-Reference |
| `phase-5` | `#0052CC` | Phase 5: Prototype |
| `xbrl` | `#1D76DB` | XBRL-related |
| `data` | `#FEF2C0` | Data files, samples |
| `education` | `#BFD4F2` | Educational content |
| `help wanted` | `#008672` | Looking for contributors |
| `good first contribution` | `#7057FF` | Good for newcomers |

GitHub will have some default labels (bug, enhancement, documentation) - keep those too.

## Part 4: Verify Everything

After creating issues and discussions:

### Check Issues Tab
- [ ] 3 issues visible
- [ ] All 3 issues are pinned at the top
- [ ] Labels are correctly applied
- [ ] Issues display properly formatted markdown

### Check Discussions Tab
- [ ] Welcome discussion is visible
- [ ] Welcome discussion is pinned
- [ ] Categories are set up correctly
- [ ] Discussion displays properly

### Test Issue Templates
- [ ] Try creating a new issue
- [ ] Verify templates appear (Bug Report, Feature Request, Educational Content)
- [ ] Cancel without submitting

## Part 5: Optional - Add Milestones

For better project tracking:

1. Go to https://github.com/GenAICPA/SkillsforAudit/milestones
2. Click **"New milestone"**
3. Create:
   - **Milestone**: `Phase 4 - Cross-Reference Engine`
   - **Due date**: (optional, maybe 3 months out)
   - **Description**: Implementation of cross-reference engine
4. Create another:
   - **Milestone**: `Phase 5 - Integrated Prototype`
   - **Due date**: (optional)
5. Go back to Issues #1 and #2, assign to respective milestones

## Quick Checklist

After following all steps above:

- [ ] 3 issues created and pinned
- [ ] Discussions enabled and configured
- [ ] 1 welcome discussion created and pinned
- [ ] All labels properly applied
- [ ] Issues display correctly with formatting
- [ ] Discussion displays correctly
- [ ] (Optional) Milestones created

## Screenshots for Reference

### Creating an Issue:
1. Click "New issue"
2. Fill in title and body
3. Add labels from right sidebar
4. Click "Submit new issue"
5. Click "Pin issue" from right sidebar

### Creating a Discussion:
1. Enable Discussions in Settings first
2. Go to Discussions tab
3. Click "New discussion"
4. Select category
5. Fill in title and body
6. Click "Start discussion"
7. Pin using ⋯ menu

## Troubleshooting

**Issue templates not showing?**
- Wait a few minutes after pushing `.github/ISSUE_TEMPLATE/` files
- Try hard refresh (Ctrl+Shift+R)
- Templates appear at bottom of "New issue" page

**Can't pin issues/discussions?**
- You must be the repository owner or have admin access
- Pin option is in right sidebar for issues
- Pin option is in ⋯ menu for discussions

**Markdown not rendering correctly?**
- Check that you copied the entire content
- Ensure no extra backticks or formatting errors
- Preview before submitting

## Next Steps

After creating these initial issues/discussions:

1. **Star your own repository** (if you haven't already)
2. **Watch the repository** (to get notifications)
3. **Share the repository** with your initial network
4. **Respond to comments** as people start engaging

Good luck! 🚀
