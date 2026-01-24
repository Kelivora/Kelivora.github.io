---
name: dev-sop
description: |
  Standard Operating Procedures for web development workflows. Use when user wants to:
  - Build/optimize frontend UI (pages, components, tools)
  - Plan and implement multi-step features
  - Start dev server / deploy to port 2527
  - Deploy to GitHub Pages
  - Review code / fix bugs
  - Create new skills or features

  Automatically selects the appropriate workflow based on context.
---

# 开发标准操作流程 (Dev SOP)

## 快速调用

| 需求 | 快捷指令 |
|------|----------|
| 优化/新建页面UI | `优化首页` / `新建页面 xxx` |
| 复杂功能开发 | `开发功能 xxx` (自动创建计划并执行) |
| 启动开发服务器 | `启动服务器` / `部署到2527` |
| 代码审查/修复bug | `审查代码` / `修复bug` |
| 创建新技能 | `创建技能 xxx` |
| 部署到 GitHub Pages | `部署到 GH Pages` / `发布到线上` |

---

## 常用工作流

### 1. 前端开发 (frontend-design)

当用户说"优化"、"新建页面"、"设计UI"时自动触发：

```
invoke Skill(frontend-design, { "--mode": "code" })
```

**自动执行：**
1. 读取现有文件结构
2. 应用 Modern Editorial 设计风格（Noto Serif SC + Outfit，琥珀金配色）
3. 优化CSS动画和交互
4. 保持设计一致性

### 2. 复杂功能开发 (subagent-driven-development)

当用户说"开发功能"、"实现需求"时：

```
invoke Skill(superpowers:subagent-driven-development)
```

**自动执行：**
1. 使用 writing-plans 创建实施计划
2. 分任务逐步执行
3. 每次提交代码
4. 完成后审查

### 3. 启动服务器

```bash
# 使用内置脚本
python3 scripts/start_server.py 2527
./scripts/start_server.sh 2527

# 或手动
python3 -m http.server 2527
```

**快捷方式：** 直接说 `启动服务器` 或 `部署到2527`

### 4. 代码审查

当用户说"审查代码"、"检查bug"时：

```
invoke Skill(superpowers:requesting-code-review)
```

或

```
invoke Skill(superpowers:systematic-debugging)
```

### 5. 创建新技能

当用户说"创建技能"时：

```
invoke Skill(skill-creator)
```

### 6. 上传代码到 GitHub

当用户说"上传到 github"、"提交代码"、"push"时：

```
git add .
git commit -m "feat: description"
git push origin main
```

**自动执行：**
1. 检查 git status 和 diff
2. 添加所有更改
3. 提交（使用语义化前缀：feat/fix/docs/style/refactor/test/chore）
4. 推送到 main 分支

**快捷方式：** 直接说 `上传到 github` 或 `提交代码`

### 7. 部署到 GitHub Pages

当用户说"部署到 github pages"、"发布到线上"、"gh-pages"时：

#### 完整部署流程

```bash
# 步骤1: 提交代码到 main 分支
git add .
git commit -m "feat: description"
git push origin main

# 步骤2: 同步并推送 gh-pages 分支
git checkout gh-pages
git merge main --no-edit
git push origin gh-pages
git checkout main
```

#### 首次部署（无 gh-pages 分支）

```bash
# 如果 gh-pages 分支不存在
git checkout -b gh-pages
git push -u origin gh-pages
git checkout main
```

#### 访问地址

项目部署后访问地址格式：
- 仓库 `username.github.io` → `https://username.github.io/`
- 项目页面 `username.github.io/repo` → `https://username.github.io/repo/projects/xxx.html`

本项目地址：`https://kelivora.github.io/projects/`

**自动执行：**
1. 检查 git status 和 diff
2. 提交所有更改到 main 分支
3. 同步更新 gh-pages 分支
4. 推送到远程触发 Pages 部署
5. 返回部署后的访问地址

**快捷方式：** 直接说 `部署到 GH Pages` 或 `发布到线上`

**触发词：** "github pages"、"gh-pages"、"部署"、"发布"、"线上"、"deploy"

---

## 快捷命令速查

```
优化UI → frontend-design skill
新功能 → subagent-driven-development + writing-plans
启动服务 → python3 -m http.server 2527
代码审查 → requesting-code-review
修复bug → systematic-debugging
创建技能 → skill-creator
上传github → git add + commit + push
部署GH Pages → git checkout gh-pages && git merge main && git push
```

---

## 详细参考

- **触发词列表**: See [triggers.md](triggers.md) for all trigger phrases
- **常用命令**: See [commands.md](commands.md) for server, git, npm commands
- **设计规范**: See [design.md](design.md) for complete CSS variables and patterns

---

## 典型对话模式

| 用户意图 | 自动触发 |
|---------|----------|
| "优化整个项目" | frontend-design |
| "开发一个计算器" | writing-plans + subagent-driven-development |
| "服务器起不来" | systematic-debugging |
| "看一下代码有没有问题" | requesting-code-review |
| "把这个做成一个技能" | skill-creator |

## 注意事项

1. **优先使用现有文件** - 不创建重复代码
2. **保持一致性** - 所有页面使用相同的设计语言
3. **提交代码** - 每次完成都提交，保持版本清晰
4. **验证后再说完成** - 确保功能正常才结束
