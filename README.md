# 100-Day Curriculum · Polyglot Security AI Expert

**1 hour every day · 100 days · Rust, TypeScript, C, C++, Zig, Dart**

---

## 🎯 Purpose

This repository is a **self-study curriculum** to grow into a polyglot software
engineer with a focus on **security, AI-native development, and low-level
systems**. Over 100 days — committing at least one hour per day — it takes you
from Rust fundamentals all the way to post-quantum cryptography, edge systems,
and a published open-source capstone.

The curriculum is deliberately **polyglot**: instead of mastering one language,
you learn how memory, types, concurrency, and interoperability work across
six languages and ecosystems. Each day pairs **theory** (a guided write-up with
verified sources) with **practice** (a coding task you must complete and
commit).

It is both a **learning plan** and a **public progress record**: your GitHub
commit graph is the proof that you did the work.

📊 **Live progress:** [docs/PROGRESS.md](docs/PROGRESS.md) — aggregated by
`python3 tools/progress.py`, which also verifies the per-block markers.

---

## 🗂️ Project Structure

```
.
├── README.md                      ← you are here (curriculum overview)
├── docs/                          ← daily lesson guides (theory + tasks)
│   ├── PROGRESS.md                ← aggregated progress dashboard
│   ├── block1-memory-safe-mastery/
│   │   ├── README.md              ← block overview + progress checklist
│   │   ├── Day001.md … Day020.md  ← one file per day
│   ├── block2-the-low-level/
│   ├── block3-ai-native-development/
│   ├── block4-security-and-pqc/
│   ├── block5-edge-and-future-systems/
│   └── block6-integration-and-mastery/
├── tools/                         ← helper scripts (progress aggregation)
└── days/                          ← your hands-on code per day
    ├── day1/                      ← Rust crate (Cargo project)
    └── day2/
```

- **`docs/`** holds the **curriculum content**: each `DayNNN.md` explains the
  theory for that day, states a concrete coding task, gives **hints** that point
  at the right APIs and concepts (but **no solution code**), lists a "Definition
  of Done" checklist, and links to primary sources. Read this _before_ you code.
  The docs intentionally **do not contain the code you must build** — copying a
  ready-made answer would remove the learning. The hints guide you; the
  implementation is yours to write in `days/`.
- **`days/`** holds **your solutions**: one folder per day where you write and
  build the code that fulfills the day's task. Each day is a standalone
  project (e.g. a Rust crate with its own `Cargo.toml`).

---

## 📋 Block Overview

| #   | Block                 | Days   | Focus                                               | Outcome                                     | README                                                  |
| --- | --------------------- | ------ | --------------------------------------------------- | ------------------------------------------- | ------------------------------------------------------- |
| 1   | Memory-Safe Mastery   | 1–20   | Rust Ownership, TS Advanced, WASM, Tauri, FFI       | Fullstack memory-safe app deployed          | [README](docs/block1-memory-safe-mastery/README.md)     |
| 2   | The Low Level         | 21–35  | C Memory, C++ Modern, Zig, Allocator Design         | Polyglot memory pool + benchmarks           | [README](docs/block2-the-low-level/README.md)           |
| 3   | AI-Native Development | 36–55  | Agents, LangGraph, K8s, vLLM, ML Engineering, MLOps | AI dev tool with GitHub integration         | [README](docs/block3-ai-native-development/README.md)   |
| 4   | Security & PQC        | 56–75  | Crypto, TLS, PQC, Supply Chain, Formal Verification | PQC migration CLI tool                      | [README](docs/block4-security-and-pqc/README.md)        |
| 5   | Edge & Future Systems | 76–90  | TinyML, RISC-V, MLIR/TVM, io_uring, Polyglot Arch   | Edge-to-cloud pipeline + language benchmark | [README](docs/block5-edge-and-future-systems/README.md) |
| 6   | Integration & Mastery | 91–100 | Capstone, Open Source, Brand, Interview, Roadmap    | Published capstone + 5-year plan            | [README](docs/block6-integration-and-mastery/README.md) |

---

## 🚀 How to Use This Curriculum

### Daily workflow (repeat for each day)

1. **Read the lesson.** Open `docs/blockN/DayNNN.md` for the current day and
   work through the theory section. Follow the linked primary sources for
   depth.
2. **Check the task.** Every day file ends with a practical task and a
   **Definition of Done (DoD)** checklist. That checklist is your acceptance
   criteria — don't mark the day complete until every box is ticked.
3. **Write the code.** Create (or continue) the matching folder under `days/`
   — e.g. `days/day1/` for Day 001. Implement the task there.
4. **Build & verify.** For Rust days that means `cargo run` (and
   `cargo build 2>&1 | grep warning` should be empty). Other languages use
   their equivalent toolchain.
5. **Commit.** Commit with a clear message, e.g.
   `git commit -m "day1: ownership & borrowing without clone"`. This is your
   progress proof — see the rules below.
6. **Update the block checklist.** In the block's `docs/blockN/README.md`,
   tick the day's checkbox (`[ ]` → `[x]`). The progress counter at the top of
   that file is updated automatically by the pre-commit hook on each commit.

### Example: Day 1

```bash
# 1. read the lesson
$ cat docs/block1-memory-safe-mastery/Day001.md

# 2. work in the matching days folder (already scaffolded as a Rust crate)
$ cd days/day1
$ cargo run
   Compiling day1 v0.1.0 ...
hello this is a testpushed value

# 3. commit your work
$ git add days/day1 docs/block1-memory-safe-mastery/README.md
$ git commit -m "day1: ownership & borrowing without clone"
```

### Tooling notes

- **Rust days** are individual Cargo crates under `days/dayN/`. Run
  `cargo run` / `cargo test` from inside the day's folder.
- Other languages (TypeScript, C/C++, Zig, Dart) are introduced in later
  blocks; each day's lesson file specifies how to set up and run that day's
  project.
- Build artifacts (`target/`, etc.) are gitignored — only source is committed.

---

## ⚡ Key Rules

1. **At least 1 hour every day.** More is allowed, less is not.
2. **Code beats theory.** Each day has a practical task that you must complete —
   the docs give you the task and hints, **not** the solution. You write the code.
3. **Commit every day to GitHub.** Your public commit graph is your proof of
   progress.
4. **If you miss a day, make it up on the weekend.**

---
