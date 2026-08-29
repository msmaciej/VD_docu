# _VDAIA_Processes — Problems We Solve: catalogue, discovery assets & flow diagrams

This folder holds the expanded **Problems We Solve** taxonomy and the discovery-phase assets
that support it. It complements the AI-Automation PM framework in the repo root — it does not
replace any phase workbook or template. See **vd-process-integration-note** for how these wire
into the framework (the spine, the canonical taxonomy, pricing/boundary mappings, and the edits
to make in the master files).

## Canonical taxonomy
4 groups → 19 sub-processes (expands the original 10). This is the single source of truth;
the Fit-Check "6 areas" and Phase 1 Quick Diagnostic "10 types" are legacy views that roll up
into it.

## What's here and where it belongs

| File | What it is | Framework role | Fill in? |
|------|------------|----------------|----------|
| `vd-pattern-catalogue.docx` / `.pdf` | 4 groups, 19 sub-processes, every example, each with a Scope boundary | Fulfils the planned **Automation Category Reference** (Phase 1–2 + reference throughout) | No — reference |
| `vd-discovery-reference_v2.docx` / `.pdf` | The three layers, the primitive, dials & tiers, how to use in discovery | PM aid during the **Interview Script** (Phase 1) | No — reference |
| `vd-scoping-worksheet_v2.docx` / `.pdf` | Fill-anywhere form: dials per candidate process | Per-process capture → **Quick Diagnostic** + **Pricing Calculator** adders | Yes — one per process |
| `vortexdeep-flows.pdf` | All 29 flow diagrams, one per page, labelled | Design reference (**Workflows Library** companion, Phase 3) + discovery visual | No — reference |
| `g*.svg` / `g*.png`, `add*.svg` / `add*.png` | Individual flow diagrams (SVG for web/site, PNG for docs) | Site content + diagram source | No — assets |
| `problems_we_solve_taxonomy_reconciliation.svg` / `.png` | Taxonomy map | Phase 0 reference — **finalise to the 19** | No — reference |

## Tier ↔ package (pricing)
- Base → **Basic**  ·  Base + triage → **Pro**  ·  Multi-branch → **Pro / Managed**  ·  (autonomous → Agentic, mostly out-of-shape)

## Dials ↔ complexity adders
- Trigger/channels → *Extra data sources/triggers* · Draft/act → *AI generation steps* · Systems → *CRM integration* ·
  Human gates → *Approval workflow* · Reporting → *Reporting layer* · Sensitivity → *Sensitive data multiplier*

## Scope boundary ↔ Automation Boundary
Each pattern's Scope boundary is the **default** for Phase 2's per-client **Automation Boundary** matrix.

## Housekeeping (safe to delete)
- `~$-discovery-reference_v2.docx` — Word lock/temp file
- `vortexdeep-flows copy.pdf`, `vortexdeep-flows_temp.pdf` — duplicate/temp renders
- `vd-discovery-reference_v1.*` — superseded by v2 (keep only if you want the history)
- `_LI-Never-ASK--*.png` — appears unrelated to this folder

## Versioning
Filenames carry `_v2` where a newer version exists. Keep one canonical version per asset; move
older ones to an `/_archive` subfolder rather than leaving duplicates in place.
