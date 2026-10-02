# 📊 Progress Dashboard

> Auto-aggregated from the six block READMEs. Refresh anytime with:
> `python3 tools/progress.py`

**Overall: 1/100 days complete**

```
block1-memory-safe-mastery       [#...................]  1/20
block2-the-low-level             [...............]  0/15
block3-ai-native-development     [....................]  0/20
block4-security-and-pqc          [....................]  0/20
block5-edge-and-future-systems   [...............]  0/15
block6-integration-and-mastery   [..........]  0/10
```

## How this stays honest

Each block README carries a `**Progress: N/M**` marker. `tools/progress.py`
counts the actual `- [x]` checkboxes per block and compares them against the
marker on every run — a marker that drifts from reality fails the script
(exit 1). Update checkboxes and markers together; the script keeps you from
claiming days you did not do.

## Commands

| Command | What it does |
|---|---|
| `python3 tools/progress.py` | print dashboard + verify marker sync (exit 1 on drift) |
| `python3 tools/progress.py --quiet` | same, without the closing pep talk |