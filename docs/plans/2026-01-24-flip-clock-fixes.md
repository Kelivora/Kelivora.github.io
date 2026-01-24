# 翻页时钟修复计划

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development to implement this plan task-by-task.

**Goal:** 修复秒数被遮挡的bug，移除双击切换，添加实体按钮控制12/24小时制和秒数显示/隐藏

**Architecture:**
- 修复 flip-card 的 z-index 层级问题
- 底部添加实体按钮栏替代双击交互
- 按钮使用与项目一致的琥珀金配色风格

**Tech Stack:** 纯 HTML/CSS/JS，无需额外依赖

---

### Task 1: 修复 z-index 遮挡问题

**Files:**
- Modify: `projects/tools/flip-clock.html:78-106`

**Step 1: 分析问题并修复 z-index**

当前问题：秒数卡片可能被前一个分隔符遮挡，需要确保正确层级。

修改 `.card-upper` 和 `.card-lower` 的 z-index：
```css
.card-upper {
  z-index: 10;
}

.card-lower {
  z-index: 5;
}
```

**Step 2: 验证修复**

目视检查确保所有卡片正常显示不被遮挡。

**Step 3: Commit**

```bash
git add projects/tools/flip-clock.html
git commit -m "fix: 修复翻页时钟卡片z-index遮挡问题"
```

---

### Task 2: 添加实体按钮区域

**Files:**
- Modify: `projects/tools/flip-clock.html:225-235`
- Modify: `projects/tools/flip-clock.html:430-436`

**Step 1: 更新底部提示区域为按钮栏**

将 `<div class="info">` 改为按钮栏：
```html
<div class="controls">
  <button id="toggle-12" class="control-btn">12/24</button>
  <button id="toggle-sec" class="control-btn">秒数</button>
</div>
```

**Step 2: 添加按钮样式**

在 `<style>` 中添加：
```css
.controls {
  display: flex;
  gap: 20px;
  margin-top: 10px;
}

.control-btn {
  padding: 12px 24px;
  font-family: var(--font-body);
  font-size: 14px;
  font-weight: 500;
  color: var(--text-primary);
  background: var(--card-bg);
  border: 1px solid var(--accent-light);
  border-radius: var(--border-radius);
  cursor: pointer;
  transition: all 0.2s ease;
}

.control-btn:hover {
  background: var(--accent-light);
}

.control-btn.active {
  background: var(--accent);
  color: white;
  border-color: var(--accent);
}
```

**Step 3: Commit**

```bash
git add projects/tools/flip-clock.html
git commit -m "feat: 添加实体按钮控制区域"
```

---

### Task 3: 移除双击切换功能，更新按钮逻辑

**Files:**
- Modify: `projects/tools/flip-clock.html:575-598`

**Step 1: 移除双击事件监听器**

删除 `document.addEventListener('dblclick', ...)` 相关代码。

**Step 2: 更新按钮点击事件**

修改为：
```javascript
// 12/24小时切换
document.getElementById('toggle-12').addEventListener('click', function() {
  use12Hour = !use12Hour;
  this.classList.toggle('active', use12Hour);
  lastTime = {};
  updateClock();
  updateDate();
});

// 秒数显示切换
document.getElementById('toggle-sec').addEventListener('click', function() {
  showSeconds = !showSeconds;
  this.classList.toggle('active', showSeconds);
  const secCards = document.querySelectorAll('[data-unit^="seconds"]');
  secCards.forEach(card => {
    card.style.visibility = showSeconds ? 'visible' : 'hidden';
    card.style.opacity = showSeconds ? '1' : '0';
  });
});
```

**Step 3: 初始化按钮状态**

在 `init()` 函数末尾添加：
```javascript
// 初始化按钮状态
document.getElementById('toggle-12').classList.toggle('active', use12Hour);
document.getElementById('toggle-sec').classList.toggle('active', showSeconds);
```

**Step 4: Commit**

```bash
git add projects/tools/flip-clock.html
git commit -m "feat: 实现实体按钮功能，移除双击交互"
```

---

### Task 4: 部署到 GitHub Pages

**Files:**
- Modify: 无（仅部署）

**Step 1: 提交代码并推送到 main**

```bash
git add .
git commit -m "fix: 翻页时钟按钮交互优化
- 添加实体控制按钮
- 修复z-index遮挡问题
- 移除双击切换"
git push origin main
```

**Step 2: 同步 gh-pages 分支**

```bash
git checkout gh-pages
git merge main --no-edit
git push origin gh-pages
git checkout main
```

---

## Execution

**Plan complete and saved to `docs/plans/2026-01-24-flip-clock-fixes.md`. Two execution options:**

**1. Subagent-Driven (this session)** - I dispatch fresh subagent per task, review between tasks, fast iteration

**2. Parallel Session (separate)** - Open new session with executing-plans, batch execution with checkpoints

**Which approach?**
