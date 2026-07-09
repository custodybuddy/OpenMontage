# Render Flow

This project uses a browser-to-Lambda render pipeline.

The browser does not render the final MP4.
The browser previews the Remotion composition, starts a Remotion Lambda render job, polls for progress, and then receives a downloadable MP4 URL.

## Main Flow

Browser
→ `GET /`
→ `app/root.tsx`
→ `app/routes.ts`
→ `app/home.tsx`
→ preview with `@remotion/player`
→ `app/remotion/components/Main.tsx`
→ user clicks **Render video**
→ `app/components/RenderControls.tsx`
→ `app/lib/use-rendering.ts`
→ `app/lib/api.ts`
→ `POST /api/lambda/render`
→ `app/render.tsx`
→ validate request with `app/remotion/schemata.ts`
→ `app/lib/render-video.server.ts`
→ Remotion Lambda
→ composition registered in `app/remotion/Root.tsx` and `app/remotion/index.ts`
→ render `app/remotion/components/Main.tsx`
→ encode frames to H.264 MP4
→ return `renderId` and `bucketName`
→ `use-rendering.ts` polls `/api/lambda/progress`
→ `app/progress.tsx` checks Lambda render status
→ returns `progress`, `done`, or `error`
→ when done, returns final MP4 URL and size
→ `RenderControls.tsx` switches to download state
→ `DownloadButton.tsx` renders the final MP4 link

## Important Rule

`home.tsx` previews the same `Main.tsx` composition that Remotion Lambda later renders.

The preview and final render must stay aligned by using the same:

* Remotion component
* `inputProps`
* schema from `app/remotion/schemata.ts`
* constants from `app/remotion/constants.mjs`

## Do Not Break This

Do not render the MP4 in the browser.

Do not replace the Lambda render path with local rendering for the UI button.

Do not bypass `schemata.ts`.

Do not duplicate composition settings across files.

Do not let the preview props and Lambda render props drift apart.

## Canonical Render Path

`home.tsx`
→ `RenderControls.tsx`
→ `use-rendering.ts`
→ `api.ts`
→ `render.tsx`
→ `render-video.server.ts`
→ Remotion Lambda
→ `progress.tsx`
→ `DownloadButton.tsx`

This is the source-of-truth render flow for the project.
