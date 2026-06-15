# Review Queue — WO2016011208A1 (extraction)

- Status: **partial** (all 54 claims captured; final claim = 54)
- Primary source attempted: WIPO Patentscope — **HTTP 403 Forbidden** (blocked).
- Source used (fallback): https://www.freepatentsonline.com/WO2016011208A1.html (FPO)
- Retrieved: 2026-06-15

## Why flagged
FPO's text for this PCT publication is OCR of a scanned WIPO PDF and carries **pervasive**
OCR artifacts. All preserved **verbatim** in 02_extracted (the ONE RULE: do not fix), but
the document needs independent re-collection from a clean source before verification.

### Artifact patterns observed (non-exhaustive)
- Position labels split by a space: **`XI 0`**=X10, **`XI I`/`XI 1`**=X11, `XI 2`=X12,
  `XI 3`=X13, `XI 4`=X14, `XI 5`=X15, `XI 6`=X16, `XI 7`=X17, `XI 8`=X18, `XI 9`=X19,
  `Xl`/`XI`=X1, `Xl l`=X11 (header of claim 1).
- Residue OCR: **`Ache`**=Achc; **`He`**=Ile; **`Gin`**=Gln; **`Tie`**=Tle.
- Beta-homo / beta-Ala residues mangled: `phPhe`,`phTyr`,`phTrp`,`phAla`,`phLeu`,`phVal`,
  `phNal`,`pAla`,`PAla`,`PhAla`,`PhLeu`,`PhVal` (for βhPhe/βhTyr/βhTrp/βhAla/βhLeu/βhVal/
  βhNal/βAla).
- Mojibake fragments: **`β!ιΡ1ιε(4-Ρ)`** (claim 28, for βhPhe(4-F)), **`βΙιΑΚ`**,
  **`βηΑΚ`**, **`βϋευ`**, **`βΑ1&`** (claims 28).
- `(D)Qln` (claim 16, for (D)Gln); `claiml` (claim 3 preamble, for "claim 1").
- **Truncated C-termini** in sequence lists of claims 11, 16, 41 where OCR dropped
  characters, e.g. `-E -NH2`, `-EN -NH2`, `-K G-NH2`, `-Q -NH2`, `[Aib]- -NH2`. The intended
  trailing residues are not recoverable from this source.

### Non-text figure
- **Claim 35** recites "the peptide inhibitor comprises the structure of **Formula I:**"
  followed by a **chemical-structure drawing (R1-X-R2)** that FPO did NOT render as text.
  In the extraction the figure location is marked `[NON-TEXT CHEMICAL STRUCTURE FIGURE — not
  captured by source]`; only the surrounding R1/X/R2 definitional text was captured verbatim.

## Recommended action
Re-collect from WIPO Patentscope (retry; was 403) or the original PCT PDF / Espacenet, then
run scripts/claim_diff.py. Treat current sequence strings and the Formula I figure as
NON-authoritative. Claim count (54), dependency structure, and prose method claims (47-54)
appear reliable.
