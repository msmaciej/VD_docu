# VortexDeep — Framework Update Changelog

Consolidated record of every file created or edited while integrating the expanded
**Problems We Solve** catalogue (4 groups / 19 sub-processes) into the AI-Automation PM
framework. All edits to existing master workbooks are **additive** and saved as **new
versions** — originals untouched. Every edited/new Office file was verified by converting
to PDF (no repair error); every Word file also passed OOXML schema validation.

Note on figures: pricing numbers are **indicative**, computed from the calculator's own
published package bases and complexity adders. The Quote Calculator remains authoritative.

---

## 1. New assets (reference + discovery + pricing)

| File | What it is | Framework role |
|------|------------|----------------|
| `vd-pattern-catalogue.docx/.pdf` | 4 groups / 19 sub-processes, every example, each with a **Scope boundary** | Fulfils the planned *Automation Category Reference*; Phase 1–2 + reference |
| `vd-master-overview.docx/.pdf` | The **build-up ladder** (L0 Capture → L4 Agentic): where to start, how to climb | Organising spine; Phase 2 start-rung, Phase 6 climb |
| `vd-discovery-reference.docx/.pdf` | Three layers, the primitive, dials & tiers, discovery use | PM aid during the Interview Script (Phase 1) |
| `vd-scoping-worksheet.docx/.pdf` | Fill-anywhere form; per-process dials | Phase 1 capture → Quick Diagnostic + pricing adders |
| `vd-process-integration-note.docx/.pdf` | Spine, taxonomy reconciliation, asset map, change-list | Index/reference |
| `AI_Automation_PM_Helper_Priced_Examples_v1.xlsx` | All 29 examples → package + dials → indicative range; mgredshift v4.0/v4.1/v4.2 | Pricing reference (Phase 1–2); calculator engine untouched |
| `ladder.svg/.png` | The build-up ladder diagram | Master Overview visual |
| `taxonomy19.svg/.png` | Canonical 4×19 taxonomy | Replaces the older 6-area reconciliation diagram |
| `vortexdeep-flows.pdf` + `g*/add*` SVG/PNG | 29 process-flow diagrams | Design reference (Phase 3) + discovery visual + site content |
| `README_VDAIA_Processes.md` | Documents every file in `_VDAIA_Processes` + housekeeping | Folder index |

## 2. Edited master workbooks (additive, new versions)

| File | From → To | Change | Verified |
|------|-----------|--------|----------|
| Phase 0 Master Overview Index | v4 → **v5** | File Index: corrected stale versions (Phase1 v5→v6, Phase2 v2→v3, Pricing v6→v10); flipped *Automation Category Reference* **To Build → In Use** (= the catalogue) | Converts clean |
| Phase 1 Discovery MASTER | v6 → **v7** | Quick Diagnostic **Q0 list extended 10 → 19** (one text cell; no formulas/dropdowns touched) | Converts clean |
| Pricing Calculator | v10 → **v11** | *Example Quotes*: anchored existing MG Red Shift row as **v4.0**; added **v4.1** (template reply) and **v4.2 + v4.1** (dual intake) — three independent-build rows | Converts clean; ordering v4.1 < v4.0 < v4.2 |

## 3. Key reconciliations recorded

- **Taxonomy:** one canonical map = 4 groups / 19 sub-processes. The Fit-Check "6 areas" and Quick-Diagnostic "10 types" are legacy views that roll up into it.
- **Tiers ↔ packages:** base → Basic Intake · base+triage → Basic+ AI Triage · multi-branch → Pro Multi-Channel · monitoring → Managed Operations · autonomous → Agentic (mostly out-of-shape).
- **Dials ↔ complexity adders:** trigger/channels → data sources/triggers · draft/act → AI-generation steps · systems → CRM · human gates → approval workflow · reporting → reporting layer · sensitivity → ×1.3–1.7 multiplier. **No formula changes needed.**
- **Scope boundary ↔ Phase 2 Automation Boundary:** the catalogue's per-pattern boundary is the default that seeds the per-client Phase 2 matrix.
- **Independent builds vs expansion:** three clients wanting similar-but-different solutions = three independent builds, each priced on its own dials (mgredshift trio). Expansion of one live system is the only case needing a change/rework convention.

## 4. Open items (recommended next, in order)

1. **Phase 0 File Index — paste 5 asset rows** (rows 26–30) and extend the count ranges `5:25` → `5:30`. (Auto-insert skipped: merged divider + fixed-range formulas → safer to paste by hand. Rows provided in the Integration Note.)
2. **Point Phase 0 File Index** Pricing row to **v11** (now that the trio is added).
3. **Calculator wording:** count AI-generation as an explicit adder rather than burying the first draft in "draft support," so template-vs-AI always differentiates (the modelling note behind the mgredshift ordering).
4. **Fit-Check / reconciliation diagram:** swap the 6-area image for `taxonomy19` (4×19).
5. **Site + disclaimer:** publish the expanded 19; add the client-friendly "human in control / what we automate vs what stays with you" note.
6. **Housekeeping:** remove `_VDAIA_Processes` temp/junk (`~$…` lock, `…copy.pdf`, `…_temp.pdf`); archive `_v1` assets superseded by `_v2`.

## 5. Not changed (deliberately)

- Pricing Calculator **formula engine** — no formulas altered; only reference rows added.
- Phase 1 **Automation Methods** — catalogues methods, not categories; the 19 reuse the same methods.
- Phases 2–7 workbooks and the Word deliverable templates — unchanged this round.
