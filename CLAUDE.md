# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the FocusLife.ai project repository - an AI-Powered Wellness Tracking & Insights platform that focuses on multi-condition health tracking including ADHD/Focus Management, Weight Loss, Sleep Optimization, and Energy Management. The platform provides comprehensive supplement management with AI-driven effectiveness analysis and drug interaction screening.

## Current Project Status

This appears to be a **branding and design assets repository** rather than an active codebase. The repository contains:
- Brand documentation and style guides
- Logo assets and visual materials
- Marketing feature specifications
- Planning documents

**No active codebase exists yet** - there are no package.json, source files, or build configuration present.

## Key Project Documents

### Brand & Design System
- **FOCUSLIFE_STYLE_GUIDE.md**: Comprehensive UI/UX design system with brand identity, color system, typography, components, and responsive design patterns
- **MARKETING_FEATURES_2025.md**: Complete feature specifications and marketing materials for the platform
- **AGENTS.md**: Repository guidelines and development standards

### Brand Assets
- Various FocusLife logo versions in multiple formats (.svg, .png)
- Cropped and optimized logo variants (brand, mono, vector versions)
- Marketing images and hero graphics

### Brand Color System
- Primary: Indigo (#6366f1) with purple accent (#8b5cf6)
- Semantic colors for success, warning, error, and info states
- Comprehensive neutral gray scale
- Brand gradients for backgrounds and UI elements

## Asset Management Commands

Since this is currently an asset repository, use these Python commands:

### Logo Processing
```bash
python crop_svg_logos.py  # Creates cropped versions of all logo SVGs
```

The script generates:
- `focuslife-logo-vector-cropped.svg`
- `focuslife-logo-brand-cropped.svg`
- `focuslife-logo-mono-cropped.svg`
- `focuslife-logo-embedded-cropped.svg`

## Future Development Setup

When transitioning to an active codebase, the expected structure based on AGENTS.md will be:

```
src/                 # Application code (pages, components, utilities)
public/              # Static assets (currently contains brand/ folder)
tests/               # Unit/integration tests
scripts/             # Build and data transformation tools
docs/                # Technical documentation
```

### Expected Development Commands
- `npm install` - Install dependencies
- `npm run dev` - Start development server with hot reload
- `npm test` - Run unit tests
- `npm run build` - Create production build
- `npm run lint` / `npm run format` - Code quality checks

## Design System Implementation

When implementing the UI, follow the comprehensive style guide in FOCUSLIFE_STYLE_GUIDE.md:

- **Component naming**: Use BEM methodology (.component-name__element--modifier)
- **CSS variables**: Always use design tokens for colors, spacing, typography
- **Responsive design**: Mobile-first approach with defined breakpoints
- **Accessibility**: Ensure WCAG compliance with proper contrast and focus management

## Key Features to Implement

Based on MARKETING_FEATURES_2025.md, the platform should include:

1. **Multi-Condition Health Tracking** (ADHD, Weight Loss, Sleep, Energy)
2. **AI-Powered Analytics Engine** with effectiveness correlation
3. **Comprehensive Supplement Management** (5 substance categories)
4. **Drug Interaction Screening** with real-time safety checks
5. **Focus Session Intelligence** (6 session types with timer system)
6. **Healthcare Professional Integration** with enterprise security

## Brand Guidelines

- **App Name**: FocusLife.ai
- **Tagline**: "AI-Powered Wellness Tracking & Insights"
- **Brand Values**: Scientific, Accessible, Professional, Intelligent
- **Visual Identity**: Modern, clean interface with indigo/purple gradient scheme
- **Target Users**: ADHD adults, wellness enthusiasts, health-conscious professionals

## Current Repository Usage

This repository serves as the brand assets and planning hub for FocusLife.ai. When starting development:

1. Use existing brand assets from the root directory and `public/brand/`
2. Follow the comprehensive style guide for all UI implementation
3. Reference the feature specifications in MARKETING_FEATURES_2025.md
4. Implement the development structure outlined in AGENTS.md