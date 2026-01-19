# 🔍 Axiom - AI-Powered Repository Analysis Tool

**Axiom** analyzes your codebase and recommends the best deployment platforms, regions, and configurations - powered by AI.

## 🚀 Features (Current)

- ✅ **Multi-language Detection** - Python, JavaScript, TypeScript, Go, Rust, and more
- ✅ **Framework Recognition** - Django, FastAPI, React, Next.js, Express, and 20+ frameworks
- ✅ **File Analysis** - Comprehensive repository structure analysis
- ✅ **CLI Interface** - Easy-to-use command-line tool
- 🚧 **Dependency Analysis** - Coming soon
- 🚧 **Database Detection** - Coming soon
- 🚧 **AI Recommendations** - Coming soon

## 📦 Installation

### Development Mode

```bash
cd backend/agents/repo_analyzer
pip install -e .
```

This installs the `axiom` command globally on your system.

## 🎯 Usage

### Basic Analysis

```bash
axiom analyze /path/to/your/repo
```

### Export to JSON

```bash
axiom analyze /path/to/repo --output results.json
```

### JSON Output (for piping)

```bash
axiom analyze /path/to/repo --json
```



## 💬 Contact

Created by Mangesh - [https://github.com/MangeshBhalerao]

---

**Note**: This project is under active development. Features and APIs may change.
