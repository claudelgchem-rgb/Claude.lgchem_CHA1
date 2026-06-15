# Review Queue — USRE49026E1 (extraction)

- Status: **partial** (all 36 claims captured; reissue markings unverified)
- Source used: https://www.freepatentsonline.com/RE49026.html (FPO)
- Retrieved: 2026-06-15

## Why flagged
1. **Reissue typographic conventions missing.** A US reissue patent (RE) prints amended
   claims with **bracketed [deleted matter]** and *italicized added matter*. The FPO text
   was returned as plain text with neither convention preserved. Therefore the precise
   scope of any reissue-amended claims (added vs. deleted words) is **UNVERIFIED** from
   this source. Claims 1-13 mirror the original US9605027B2 grant; claims 14-36 are
   reissue-added subject matter — these especially need confirmation of exact wording.
2. **Suspected OCR artifact, claim 20:** reads **`SEO ID NO: 175`** — almost certainly
   `SEQ ID NO: 175`. Preserved verbatim, flagged here.
3. Minor grammatical oddity claim 17 ("A method of identifying **a polypeptides** that...")
   preserved verbatim (may be original text, not OCR).

## Recommended action
Re-collect from USPTO PPUBS image/full-text (which renders reissue brackets/italics) and
compare with scripts/claim_diff.py. Confirm whether any of claims 1-36 carry reissue
add/delete markings that FPO stripped.
