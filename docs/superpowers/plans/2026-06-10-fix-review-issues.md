# Fix Review Summary Issues Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix a typo in views, remove duplicate URL patterns, and add missing trailing blank lines in HTML templates.

**Architecture:** Surgical fixes to existing files to align with the review feedback and project structure.

**Tech Stack:** Django (Python), HTML.

---

### Task 1: Fix typo in `taxi/views.py`

**Files:**
- Modify: `taxi/views.py`

- [ ] **Step 1: Correct the import from Manufacture to Manufacturer**

```python
<<<<
from taxi.models import Driver, Manufacture, Car
====
from taxi.models import Driver, Manufacturer, Car
>>>>
```

- [ ] **Step 2: Commit**

```bash
git add taxi/views.py
git commit -m "fix: correct typo in Manufacturer import"
```

### Task 2: Remove duplicate URL pattern in `taxi_service/urls.py`

**Files:**
- Modify: `taxi_service/urls.py`

- [ ] **Step 1: Remove the redundant `include('taxi.urls')` pattern**

Since `taxi/urls.py` does not exist and the root path is already handled by the `index` view in the next line, the `include` is both a duplicate and broken.

```python
<<<<
    path('', include('taxi.urls', namespace='taxi')),
    path('', index, name='index'),
====
    path('', index, name='index'),
>>>>
```

- [ ] **Step 2: Commit**

```bash
git add taxi_service/urls.py
git commit -m "fix: remove duplicate and broken URL pattern"
```

### Task 3: Add trailing blank lines to HTML templates

**Files:**
- Modify: `templates/base.html`
- Modify: `templates/includes/sidebar.html`
- Modify: `templates/taxi/index.html`

- [ ] **Step 1: Add trailing blank line to `templates/base.html`**
- [ ] **Step 2: Add trailing blank line to `templates/includes/sidebar.html`**
- [ ] **Step 3: Add trailing blank line to `templates/taxi/index.html`**

- [ ] **Step 4: Commit**

```bash
git add templates/base.html templates/includes/sidebar.html templates/taxi/index.html
git commit -m "style: add trailing blank lines to templates"
```

### Task 4: Final Verification

- [ ] **Step 1: Check code visually and run available tests (if any)**
- [ ] **Step 2: Run `python manage.py check` (if environment allows)**
