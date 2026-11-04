# Hebrew presentation mode (optional)

This is the **optional Hebrew-language extension** of the portfolio presentation theme. Apply it **whenever Hebrew is chosen for a presentation**. Do not apply it to English-only presentations. Preserve the portfolio's colors, typography hierarchy, illustrations and layout system.

## Required presentation settings

1. **File and encoding.** Use a standard editable `.pptx` Office Open XML package. Preserve Unicode Hebrew, Latin letters, numbers, punctuation and mathematical symbols. Do not reinterpret the file as a plain-text encoding or attempt a separate "UTF-8 slide setting".
2. **Paragraph direction.** Set Hebrew paragraphs to **right-to-left (RTL)** at the paragraph level, not merely right-align their text. For DrawingML-based PowerPoint files, check the effective paragraph direction in the slide XML and its inherited styles.
3. **Text alignment.** Independently align Hebrew body paragraphs to the right. Center only when the composition calls for centered text. Text alignment and text direction are separate properties.
4. **Mixed scripts.** Preserve English terms, variable names, mathematical expressions, numbers and equations in logical **left-to-right (LTR)** order within RTL paragraphs. Use appropriate script/language runs and, when needed, directional isolation. Avoid manually reversing strings or inserting arbitrary invisible marks as a substitute for proper paragraph direction.
5. **Punctuation.** Render Hebrew question marks, periods, commas, parentheses, colons, comparison signs and equals signs in their intended visual and grammatical positions. Check the displayed result, especially around adjacent Hebrew and English runs. For bilingual company-name pairs, use a clearly spaced equality sign such as `אינטל = INTEL`.
6. **Fonts.** Use Hebrew-capable Unicode fonts with adequate Latin, digit and symbol coverage. Retain the portfolio typography hierarchy. The portfolio's Hebrew fallbacks are **Noto Serif Hebrew** for serif roles and **Noto Sans Hebrew** for sans-serif roles, or compatible fonts available in the target renderer. Do not assume that a font available in one environment exists in PowerPoint or Google Slides.
7. **Editable content.** Keep text as native editable presentation text. Do not rasterize it or replace it with images to hide bidirectional or font problems. Preserve all original characters and wording.
8. **Layout preservation.** Maintain slide dimensions, element geometry, colors, shapes, spacing and content unless the requested change specifically requires otherwise. For a narrowly scoped edit, change only the intended object or property. Never rebuild unrelated slides to insert punctuation.
9. **Verification before release.** Inspect **every slide** for correct Hebrew reading order, punctuation, mixed-script order, font glyph coverage, clipping, alignment, element ordering and unchanged content. Inspect the PPTX structure and extracted text, render all slides, and visually compare with the pre-edit version. When the destination is Google Slides or mobile PowerPoint, also check that target renderer when available. If not checked, state the limitation rather than claiming cross-renderer verification.

## Implementation and acceptance checks

- Set **paragraph direction first**, then paragraph alignment, then run-level language/script behavior. A right-aligned LTR paragraph is **not** a correctly configured Hebrew paragraph.
- Do not mistake **slide object order** for **text direction**. Arrange flow diagrams in RTL reading order independently of paragraph settings.
- Keep equations and code tokens in logical order. Do not reverse Unicode characters to force visual positioning.
- Check text at the beginning and end of each line, especially question marks, parentheses and punctuation beside Latin words.
- Detect missing-glyph squares, replacement characters, accidental text-to-image conversion and text that has been mirrored or reordered.
- Compare slide count, slide order, object counts, geometry, text and visual renderings against the approved baseline. For minimal changes, verify that every unrelated object is unchanged.
- Release only after the intended change and the absence of unintended changes have been established. If a rendering defect remains, do not label the file as verified.

This document is a language-specific **extension**, not a replacement for `theme/portfolio/README.md`. It is enabled by choosing Hebrew for the presentation.
