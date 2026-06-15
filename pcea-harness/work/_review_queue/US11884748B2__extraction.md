# Review Queue — US11884748B2 (extraction)

- Status: **partial** (all 21 claims captured, but source OCR unreliable)
- Source used: https://www.freepatentsonline.com/11884748.html (FPO)
- WIPO/Google not applicable (US grant); Google Patents expected 503 per run policy.
- Retrieved: 2026-06-15

## Why flagged
FreePatentsOnline returned the full claim set, but the OCR of the peptide sequences in
**claim 1** (and a few dependents) contains corruptions that change/garble residue tokens.
These were preserved **verbatim** (the ONE RULE: do not fix), but they are almost certainly
not the true grant text and must be re-collected from an authoritative source.

## Specific suspect strings (preserved verbatim in 02_extracted)
- Claim 1, SEQ ID NO 702/704/861/911/912/915: leading residue rendered **`[Abta]`**.
  Strongly suspected OCR corruption of **`[Abu]`** because:
  (a) every claim recites cyclization "via a thioether bond between **Abu** and C";
  (b) sibling patent US10941183B2 lists the identical SEQ ID NOs 702 and 704 with `[Abu]`.
- Claim 1, SEQ ID NO 877: **`-AiN-`** (suspected `[Aib]`).
- Claim 1, SEQ ID NO 880: **`[AibMLys(Ac)]`** (suspected `[Aib]-[Lys(Ac)]`).
- Claim 1, SEQ ID NO 782 / claim 4: **`[Phe[4-(2-aminoethoxy)]-W-`** (bracket balance / residue W vs 2-Nal uncertain).
- Claim 1, SEQ ID NO 984 / claim 17: **`[alphα-methyl-L-Leucine]`** (mixed Latin/Greek 'alphα').
- Claim 12: **`-8 2-Nal]`** (stray '8 ' before 2-Nal; bracket dropped).
- Claims 15/20/21: **`acbc]` / `acpc]` / `achc]`** with leading bracket dropped.

## Recommended action
Re-collect claims from USPTO Patent Public Search (PPUBS) full-text/image or the official
PDF, then run scripts/claim_diff.py against the current extraction. Until then, do NOT treat
the sequence strings as authoritative. The non-sequence claim scaffolding (preamble,
"cyclized via a thioether bond between Abu and C", dependency structure) appears reliable.
