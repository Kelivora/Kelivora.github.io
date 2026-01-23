# 常用命令速查

## 服务启动

```bash
# 快速启动（默认2527端口）
python3 -m http.server 2527

# 指定端口
python3 -m http.server 8080

# 指定目录
python3 -m http.server 2527 --directory /data/vibecoding

# 后台运行
nohup python3 -m http.server 2527 > /dev/null 2>&1 &
```

## 查看端口占用

```bash
# 查看2527端口
lsof -i:2527

# 杀掉占用端口的进程
kill $(lsof -ti:2527)
```

## Git 操作

```bash
# 提交所有更改
git add . && git commit -m "feat: description"

# 查看状态
git status

# 查看差异
git diff
```

## Node.js

```bash
# 安装依赖
npm install

# 启动开发服务器
npm run dev

# 构建
npm run build
```

## 技能相关

```bash
# 初始化新技能
python3 scripts/init_skill.py <skill-name>

# 打包技能
python3 scripts/package_skill.py <skill-folder>
```
