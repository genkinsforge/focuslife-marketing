# Repository Guidelines

## Project Structure & Module Organization
- Root: planning docs like `MARKETING_FEATURES_2025.md`.
- `src/`: application code (pages, components, utilities).
- `public/`: static assets served as-is (images, icons, robots.txt).
- `tests/`: unit/integration tests mirroring `src/` paths.
- `scripts/`: local tooling (build, data transforms, one-offs).
- `docs/`: specs, ADRs, and non-marketing documentation.

Example: `src/components/Hero.tsx`, `tests/components/Hero.test.tsx`.

## Build, Test, and Development Commands
- `npm install`: install dependencies (use `pnpm`/`yarn` if preferred).
- `npm run dev`: start local development server with hot reload.
- `npm test`: run unit tests in watch/CI modes.
- `npm run build`: create an optimized production build.
- `npm run lint` / `npm run format`: check and auto-format code.

If this repo is static-only today, keep commands in place for future app code.

## Coding Style & Naming Conventions
- Indentation: 2 spaces for JS/TS; 2 or 4 for config as needed.
- Filenames: `kebab-case` for general files, `PascalCase` for React components.
- Variables/functions: `camelCase`; constants: `ALL_CAPS_SNAKE_CASE`.
- Linting/formatting: ESLint + Prettier; run before commits.

## Testing Guidelines
- Framework: Jest or Vitest for unit tests; Playwright for e2e (optional).
- Location: alongside source or under `tests/` using the same path.
- Naming: `*.test.ts[x]` or `*.spec.ts[x]`.
- Coverage: target ≥80% lines; enforce in CI when added.

## Commit & Pull Request Guidelines
- Commits: use Conventional Commits (e.g., `feat: add hero section`).
- PRs: include clear description, linked issue, and screenshots for UI.
- Size: prefer small, focused PRs; include test updates and docs.
- Checks: ensure build, lint, and tests pass before requesting review.

## Security & Configuration Tips
- Never commit secrets; use `.env.local` and add `.env.example`.
- Review third-party scripts/assets added to `public/`.
- Keep dependencies updated; address `npm audit` findings promptly.

