# CustodyBuddy Animated Explainer Workflow

Use this self-contained example workflow to create calm, legally cautious CustodyBuddy animated explainers for separated or divorced parents. It demonstrates a reusable 45-60 second vertical structure without depending on generated project artifacts.

## Purpose

Create a short vertical animated explainer that teaches one co-parenting, documentation, or family-court-adjacent concept in plain language without giving legal advice or promising outcomes.

The output should feel calm, organized, secure, and premium. It should help parents understand a practical idea, not inflame conflict.

## Required Inputs

- `topic`: The specific explainer topic.
- `audience`: The intended parent audience, such as separated parents, divorced parents, high-conflict co-parents, or self-represented parents.
- `jurisdiction`: Default to Ontario unless the user specifies otherwise.
- `goal`: The practical lesson the viewer should understand.
- `key_message`: The one sentence the viewer should remember.
- `legal_safety_boundary`: What the explainer must not claim, promise, or advise.
- `cta_destination`: The CustodyBuddy action or destination, such as organize records, download checklist, join waitlist, or learn more.
- `source_links`: Official or credible sources to anchor the explainer.
- `brand_assets`: Optional logo, wordmark, icon set, or approved visual components.

## Fixed Format

- Pipeline: `animated-explainer`
- Orientation: Vertical 9:16
- Duration: 45-60 seconds
- Recommended target: 55 seconds
- Scene count: 8 scenes
- Voiceover length: 105-140 words
- Captions: Large, high-contrast, timed `Caption[]` JSON rendered as native text layers
- Music: Low-volume ambient piano, soft documentary bed, or warm minimal pulse
- Disclaimer: Required on final frame and, when appropriate, in the voiceover

## Brand System

Use the CustodyBuddy Modern Academic visual system:

- Deep Midnight: `#01012B`
- Background Dark: `#05070A`
- Goldenrod: `#DDAA13`
- Soft Gold: `#F5C542`
- White cards: `#FFFFFF`
- Surface: `#F9FAFB`
- Borders: `#E5E7EB`
- Trust Blue: `#046BD2`

Typography:

- Headings: Playfair Display
- Body and captions: Open Sans
- CTAs and button-style labels: Raleway

Accessibility rules:

- Use Goldenrod text only on Deep Midnight or dark backgrounds.
- Do not use Goldenrod text on white.
- Do not use white text on Goldenrod.
- Render all exact text as native text layers, not generated images.
- Keep captions large enough for mobile viewing.

## Tone Rules

Use a calm, factual, protective, and non-inflammatory tone.

Allowed:

- "may"
- "can help"
- "often"
- "in many cases"
- "ask a lawyer or legal professional"
- "educational information only"
- "child-focused"
- "organized records"

Avoid:

- "will win"
- "prove your case"
- "guaranteed"
- "the court wants"
- "use this against the other parent"
- inflammatory labels for the other parent
- scary courtroom imagery
- legal advice framed as instructions

## Research Anchor Section

Every CustodyBuddy explainer must include a research anchor section before scripting.

Template:

```markdown
## Research Anchors

- Source 1: [Official source name and URL]
  - Relevant point: [Plain-language summary]
- Source 2: [Official source name and URL]
  - Relevant point: [Plain-language summary]
- Source 3: [Optional credible source and URL]
  - Relevant point: [Plain-language summary]

Practical implication:

[Explain what the sources support for this explainer, without overstating the law.]
```

Preferred sources:

- Ontario Family Law Rules: https://www.ontario.ca/laws/regulation/990114
- Divorce Act, Best Interests of the Child: https://laws-lois.justice.gc.ca/eng/acts/d-3.4/page-3.html
- Ontario court, Legal Aid Ontario, Department of Justice Canada, or other official public legal information sources

Research guardrails:

- Prefer official legal-information sources over law-firm blog posts.
- Do not quote or summarize beyond what is needed for a short explainer.
- If the topic is jurisdiction-specific, confirm the jurisdiction before drafting.
- If the source does not support a claim, remove or soften the claim.

## Output Structure

Produce the following sections for every workflow run:

1. Short hook
2. Full voiceover script
3. Scene-by-scene storyboard
4. Visual direction for each scene
5. Caption text for each scene
6. Timed caption JSON
7. Suggested music mood
8. Final CTA
9. Legal-safety disclaimer
10. Research anchors
11. Rendering notes

## Script Template

Use this structure and adapt it to the topic:

```markdown
## 1. Short Hook

[One or two short sentences. Under 18 words if possible.]

## 2. Full Voiceover Script

[Hook.]

[Explain why the issue matters in plain language.]

[Clarify the legal-safe principle without legal advice.]

[Give the practical framework: dates, context, pattern, child impact, communication, records, safety, or next step.]

[Reframe away from conflict and toward organization, clarity, and support.]

[CustodyBuddy CTA.]

Educational information only. Not legal advice.

Approximate word count: [number]
```

Voiceover timing:

- 45 seconds: 105-115 words
- 50 seconds: 115-125 words
- 55 seconds: 125-135 words
- 60 seconds: 135-145 words

## 8-Scene Storyboard Template

| Scene | Time | Purpose | Visual Direction | Caption Text |
|---|---:|---|---|---|
| 1 | 0-5s | Hook | Deep Midnight hero card. One simple gold icon tied to the topic. Slow fade or soft scale. | [Short hook caption] |
| 2 | 5-10s | Reframe | Show what is missing, misunderstood, or incomplete. Use placeholders, not hostile message text. | [Reframe caption] |
| 3 | 10-17s | Legal-safe principle | Abstract civic, document, calendar, or family-support visual. No gavels, judges, police, or fear imagery. | [Legal-safe principle] |
| 4 | 17-25s | Framework | Reveal four white cards with Goldenrod left bars one at a time; keep one card primary and no more than two readable at once. | [Framework caption] |
| 5 | 25-33s | Compare | Before-then-after view: show the incomplete approach briefly, then give the organized, child-focused approach visual priority. | [Comparison caption] |
| 6 | 33-41s | Protective guidance | Parent-centered, calm icon system. Emphasize clarity, support, and care. | [Guidance caption] |
| 7 | 41-50s | Practical checklist | Checklist appears line by line with soft tick animation. | [Practical action caption] |
| 8 | 50-55s | CTA and disclaimer | CustodyBuddy closing card. Deep Midnight background, Goldenrod headline, white disclaimer. | [CTA plus disclaimer] |

Timing rules:

- Keep scene 1 short and clear.
- Use scene 4 as the core framework moment.
- Use scene 7 as the most practical, actionable moment.
- Use scene 8 for the CTA and disclaimer.
- If targeting 60 seconds, extend scenes 4, 5, and 7 by 1-2 seconds each.

### 55-Second Remotion Timing Map

At 30 fps, use this frame map for the recommended cut. The `from` value is zero-based; `durationInFrames` is the number of frames in the scene.

| Scene | Start frame (`from`) | `durationInFrames` | End frame (exclusive) |
|---|---:|---:|---:|
| 1 | 0 | 150 | 150 |
| 2 | 150 | 150 | 300 |
| 3 | 300 | 210 | 510 |
| 4 | 510 | 240 | 750 |
| 5 | 750 | 240 | 990 |
| 6 | 990 | 240 | 1230 |
| 7 | 1230 | 270 | 1500 |
| 8 | 1500 | 150 | 1650 |

## Visual Direction Pattern

Use this reusable direction pattern:

- Scene 1: Premium title card with one gold outline icon and large Playfair Display headline.
- Scene 2: Expand the viewer's understanding by showing missing context or a wider timeline.
- Scene 3: State the legal-safe principle using abstract, non-threatening visuals.
- Scene 4: Reveal the core framework one card at a time, reserving the largest visual weight for the current card.
- Scene 5: Compare an incomplete approach briefly, then hold on the stronger organized approach.
- Scene 6: Reframe away from blame and toward child-focused clarity.
- Scene 7: Give a simple checklist or repeatable next step.
- Scene 8: Close with CustodyBuddy CTA and legal disclaimer.

Motion style:

- Soft fades
- Gentle upward card reveals
- Slow scale on hero icons
- Thin-line icon animations
- Subtle gold glow for emphasis
- No harsh shake, glitch, sirens, red-alert visuals, or dramatic courtroom effects

## Caption Rules

- Use one short primary caption per scene; treat the final legal disclaimer as a separate required text layer.
- Keep each display caption on screen for at least 2 seconds. If it needs longer, shorten it or split the idea across scenes instead of shrinking the type.
- Prefer sentence case.
- Avoid legal jargon unless immediately explained.
- Keep each caption under 14 words when possible.
- Use native text layers so captions render exactly.
- Derive the display timing from the approved narration, not from visual cuts alone. A caption may cross a scene boundary when the spoken phrase does.
- Store every caption in JSON using Remotion's `Caption` type. Keep the JSON with the composition data so wording and timing can be reviewed separately from the React layout.

Caption JSON contract:

```ts
import type { Caption } from "@remotion/captions";

const captions: Caption[] = [
  {
    text: "[Short spoken phrase]",
    startMs: 0,
    endMs: 1800,
    timestampMs: 0,
    confidence: 1,
  },
];
```

For manually approved captions, use `confidence: 1`; preserve transcription confidence when the data comes from a speech-to-text pass. `startMs` must be earlier than `endMs`. Captions that reproduce narration must match the approved voiceover exactly; CTA and disclaimer display copy must match the approved on-screen copy.

Caption pattern:

1. [Hook]
2. [Clarify the misconception]
3. [Legal-safe principle]
4. [Core framework]
5. [Comparison]
6. [Protective guidance]
7. [Practical checklist]
8. [CTA plus disclaimer]

## CTA Structure

Use this format:

```markdown
CustodyBuddy helps parents [organize / document / prepare / understand] [topic-specific records or next step] calmly, clearly, and securely.
```

Examples:

- CustodyBuddy helps parents organize co-parenting records calmly, clearly, and securely.
- CustodyBuddy helps parents keep child-focused documentation in one calm, organized place.
- CustodyBuddy helps you turn stressful co-parenting details into clear, organized records.

## Legal-Safety Disclaimer

Required final-frame disclaimer:

```text
Educational information only. Not legal advice.
```

Optional expanded disclaimer for captions or description:

```text
This video is general educational information for parents. It is not legal advice and does not predict any court outcome. For advice about your situation, speak with a qualified legal professional.
```

## Output Checklist

- The output includes a short hook.
- The voiceover is 105-140 words for a 45-60 second video.
- The voiceover uses plain language and avoids promises about court outcomes.
- The storyboard has exactly 8 scenes.
- Each scene has timing, purpose, visual direction, and caption text.
- Captions are short, large, accessible, rendered as text, and supplied as timed `Caption[]` JSON.
- The visual direction uses Deep Midnight, Goldenrod, Soft Gold, and white cards.
- The tone remains calm, factual, protective, and non-inflammatory.
- The final CTA names CustodyBuddy and focuses on organization or clarity.
- The legal disclaimer appears on the final frame.
- Research anchors cite official or credible sources.
- Rendering notes identify local limitations and fallback path.

## Validation Checklist

Content validation:

- No legal advice is presented as instruction.
- No outcome is promised or implied.
- No claim exceeds the cited research anchors.
- The script distinguishes practical information from legal conclusions.
- The video does not encourage attacking or shaming the other parent.
- The child impact framing is careful and not exploitative.

Brand validation:

- Goldenrod is not used as text on white.
- White is not used as text on Goldenrod.
- Deep Midnight is used for hero or full-dark scenes.
- Captions meet mobile readability standards.
- The visuals feel premium, calm, organized, and secure.

Storyboard validation:

- The first scene hooks within 5 seconds.
- Scene 4 contains the core framework.
- Scene 5 contains a clear comparison.
- Scene 7 contains a practical checklist.
- Scene 8 contains CTA and disclaimer.
- There are no scary courtroom visuals.
- There are no hostile message screenshots with readable accusations.

Technical validation:

- Duration is between 45 and 60 seconds.
- Aspect ratio is 9:16.
- Captions are exact text layers and each JSON entry has valid, ordered millisecond timings.
- Music is ducked below narration with a frame-driven volume curve.
- Final export is playable and readable on a phone.

## Remotion Implementation Contract

Use this contract when this workflow is implemented in Remotion:

- Register a vertical composition in `src/Root.tsx` at `1080 × 1920`, `30 fps`, and `1650` frames for the recommended 55-second cut. Adjust the frame count to match the approved voiceover duration.
- Put the shared background in an `AbsoluteFill`; place each storyboard scene in a `Sequence` with explicit `from` and `durationInFrames` values. Keep the final CTA/disclaimer sequence on screen long enough to read.
- Keep all meaningful text inside a mobile safe area: at least `80px` from the left and right edges and `100px` from the top and bottom edges. At 1080px wide, use roughly `84px` or more for the main headline, `44px` for important supporting copy, and `32px` for short labels.
- Build readable content with flex or grid layout, gaps, and reserved layout slots. Use absolute positioning only for backgrounds and decorative accents so captions and cards cannot collide.
- Drive motion with `useCurrentFrame()` and `interpolate()` with clamped ranges and an `Easing.bezier()` curve. Prefer individual `scale`, `translate`, and `rotate` style properties when practical.
- Do not use CSS transitions, CSS keyframe animations, or Tailwind animation classes; they do not render reliably on the Remotion timeline.
- Store approved logos, icons, music, and image assets in `public/`, reference them through `staticFile()`, and render images with Remotion's `Img` component. Keep captions and disclaimers as HTML text layers driven by the approved `Caption[]` data.
- Load Playfair Display, Open Sans, and Raleway with `@remotion/google-fonts`, specifying only the required weights and `latin` subset. Use only approved font fallbacks if a font cannot be bundled.
- Use `Audio` from `@remotion/media` for narration and music. Start the music bed around `0.08` to `0.15` volume beneath narration, and use an `interpolate()` volume callback to fade it in and out; the callback frame is relative to when that audio track starts.
- Render representative stills from the hook, framework, checklist, and final CTA at normal viewing size before approving the export. For example: `npx remotion still [composition-id] --scale=0.25 --frame=30`.

## Rendering Notes For Mac OS Catalina

This local Catalina environment has known rendering limitations:

- Use `python3`, not `python`, for project scripts.
- FFmpeg is the safest local rendering path for draft assembly and encoding.
- Remotion is preferred for high-quality component motion, captions, and exact text, but requires a supported Node setup and installed `remotion-composer` dependencies.
- HyperFrames should be treated as unavailable on macOS Catalina 10.15 and older because the modern Node/browser runtime is unsupported.
- Do not plan a HyperFrames-only workflow for Catalina.
- If Remotion dependencies are missing locally, either install them on a supported machine or use the cloud fallback below.

Local draft recommendation:

- Use FFmpeg for timing tests, audio muxing, and simple text-card drafts.
- Use native text overlays for captions and disclaimers.
- Avoid generated images for any text-heavy screen.

## Recommended Cloud Rendering Fallback

Recommended fallback: render the final motion version in a Linux cloud environment using Remotion.

Preferred options:

- Remotion Lambda on AWS for scalable Remotion rendering when the project is ready for production.
- A Linux CI runner, such as GitHub Actions, for deterministic renders when the project can run with checked-in dependencies and cached assets.
- A temporary Linux VM or cloud workstation with Node, FFmpeg, Chromium dependencies, and the Remotion project dependencies installed.

Why this is recommended:

- It avoids Catalina's browser/runtime limitations.
- It supports exact native text rendering for captions and legal disclaimers.
- It keeps the CustodyBuddy visual system consistent across scenes.
- It is a better fit than HyperFrames on Catalina for this workflow.

Cloud setup requirements:

- Node version supported by the Remotion project.
- FFmpeg available on PATH.
- Browser/Chromium dependencies available for Remotion rendering.
- Fonts installed or bundled: Playfair Display, Open Sans, Raleway.
- All assets stored in the project workspace or fetched from stable URLs.
- Final output exported as vertical 9:16 MP4.

Reference:

- Remotion Lambda documentation: https://www.remotion.dev/docs/lambda
- Remotion `renderMedia()` documentation: https://www.remotion.dev/docs/renderer/render-media

## Reusable Prompt

Use this prompt when starting a new CustodyBuddy explainer:

```text
Create a CustodyBuddy animated explainer pipeline output.

Topic:
[TOPIC]

Goal:
[GOAL]

Audience:
[AUDIENCE]

Jurisdiction:
[JURISDICTION]

Format:
Vertical 9:16 video, 45-60 seconds, 8 scenes.

Brand style:
CustodyBuddy Modern Academic. Use Deep Midnight, Goldenrod, Soft Gold, white cards, large accessible captions, simple icons, and soft motion.

Tone:
Calm, factual, protective, non-inflammatory, and legally cautious. Do not give legal advice. Avoid promises about court outcomes. Use plain language.

Required outputs:
1. Short hook
2. Full voiceover script
3. Scene-by-scene storyboard
4. Visual direction for each scene
5. Caption text for each scene
6. Timed caption JSON using Remotion's Caption type
7. Suggested music mood
8. Final CTA
9. Legal-safety disclaimer
10. Research anchors
11. Rendering notes
```
