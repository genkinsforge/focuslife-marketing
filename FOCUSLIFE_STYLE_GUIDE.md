# FocusLife.ai Style Guide
*Comprehensive UI/UX Design System & Brand Guidelines*

---

## 🎨 Brand Identity

### **Logo & Name**
- **App Name**: FocusLife.ai
- **Tagline**: "AI-Powered Wellness Tracking & Insights"
- **Alternative**: "Multi-Condition Supplement Tracking Platform"

### **Brand Values**
- **Scientific**: Evidence-based approach to wellness
- **Accessible**: User-friendly design for all technical levels
- **Professional**: Healthcare-grade quality and security
- **Intelligent**: AI-driven insights and recommendations

---

## 🌈 Color System

### **Primary Brand Colors**
```css
--primary: #6366f1        /* Indigo-500 - Main brand color */
--primary-hover: #5558e3  /* Darker indigo for interactions */
--primary-light: #eef2ff  /* Light indigo for backgrounds */
--secondary: #8b5cf6      /* Purple-500 - Accent color */
--secondary-hover: #7c3aed /* Darker purple */
```

### **Status & Semantic Colors**
```css
/* Success States */
--success: #10b981        /* Emerald-500 */
--success-hover: #059669  /* Emerald-600 */
--success-light: #f0fdf4  /* Emerald-50 */
--success-border: #bbf7d0 /* Emerald-200 */

/* Warning States */
--warning: #f59e0b        /* Amber-500 */
--warning-hover: #e88306  /* Amber-600 */
--warning-light: #fef3c7  /* Amber-100 */
--warning-border: #fde68a /* Amber-200 */

/* Error States */
--error: #dc2626          /* Red-600 */
--error-hover: #b91c1c    /* Red-700 */
--error-light: #fef2f2    /* Red-50 */
--error-border: #fecaca   /* Red-200 */

/* Information States */
--info: #0ea5e9           /* Sky-500 */
--info-hover: #0284c7     /* Sky-600 */
--info-light: #f0f9ff     /* Sky-50 */
--info-border: #bae6fd    /* Sky-200 */
```

### **Neutral Color Scale**
```css
--gray-50: #f9fafb        /* Lightest backgrounds */
--gray-100: #f3f4f6       /* Card backgrounds */
--gray-200: #e5e7eb       /* Borders, dividers */
--gray-300: #d1d5db       /* Disabled borders */
--gray-400: #9ca3af       /* Placeholder text */
--gray-500: #6b7280       /* Secondary text */
--gray-600: #4b5563       /* Body text */
--gray-700: #374151       /* Headings */
--gray-800: #1f2937       /* Dark headings */
--gray-900: #111827       /* Darkest text */

--white: #ffffff          /* Pure white */
--black: #000000          /* Pure black */
```

### **Brand Gradients**
```css
/* Main Application Gradient */
--bg-gradient: linear-gradient(135deg, #6366f1, #a855f7, #ec4899)

/* Header Gradient */
--bg-header: linear-gradient(to right, #4f46e5, #7c3aed)

/* Dashboard Background */
--bg-dashboard: linear-gradient(135deg, #667eea 0%, #764ba2 100%)

/* Success Gradient */
--bg-success-gradient: linear-gradient(135deg, #10b981, #059669, #047857)

/* Subtle Section Background */
--bg-subtle: linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(139, 92, 246, 0.1))
```

---

## 🔤 Typography System

### **Font Family**
```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 
             'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
```

### **Type Scale**
```css
--text-xs: 0.75rem     /* 12px - Captions, badges */
--text-sm: 0.875rem    /* 14px - Body text, labels */
--text-base: 1rem      /* 16px - Default body */
--text-lg: 1.125rem    /* 18px - Large body */
--text-xl: 1.25rem     /* 20px - Small headings */
--text-2xl: 1.5rem     /* 24px - Headings */
--text-3xl: 1.875rem   /* 30px - Large headings */
```

### **Font Weights**
```css
--font-normal: 400     /* Body text */
--font-medium: 500     /* Labels, form elements */
--font-semibold: 600   /* Section headings */
--font-bold: 700       /* Important headings, metrics */
```

### **Text Colors**
```css
--text-primary: var(--gray-900)    /* Main content */
--text-secondary: var(--gray-700)  /* Supporting text */
--text-muted: var(--gray-500)      /* Placeholder text */
--text-light: var(--gray-400)      /* Disabled text */
--text-white: var(--white)         /* White text */
```

### **Typography Usage**
- **Page Titles**: `text-2xl` or `text-3xl`, `font-bold`, `text-primary`
- **Section Headings**: `text-xl`, `font-semibold`, `text-primary`
- **Body Text**: `text-sm` or `text-base`, `font-normal`, `text-secondary`
- **Labels**: `text-sm`, `font-medium`, `text-secondary`
- **Captions**: `text-xs`, `font-normal`, `text-muted`

---

## 🎛️ Component Library

### **Button System**

#### **Primary Button**
```css
.btn-primary {
  background-color: var(--primary);
  color: var(--text-white);
  padding: 0.75rem 1.5rem;        /* --space-3 --space-6 */
  border-radius: 0.5rem;          /* --radius-lg */
  border: none;
  font-weight: 500;
  font-size: var(--text-sm);
  cursor: pointer;
  transition: all 0.2s ease;      /* --transition-fast */
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;                    /* --space-2 */
}

.btn-primary:hover {
  background-color: var(--primary-hover);
  transform: translateY(-1px);
  box-shadow: var(--shadow-md);
}

.btn-primary:disabled {
  opacity: 0.6;
  cursor: not-allowed;
  transform: none;
}
```

#### **Button Variants**
- **Secondary**: Gray background, primary text
- **Outline**: Transparent background, primary border and text
- **Success**: Green theme for positive actions
- **Error**: Red theme for destructive actions
- **Ghost**: Transparent background, no border

#### **Button Sizes**
```css
.btn-sm { padding: 0.5rem 1rem; font-size: var(--text-xs); }     /* Small */
.btn-md { padding: 0.75rem 1.5rem; font-size: var(--text-sm); }  /* Default */
.btn-lg { padding: 1rem 2rem; font-size: var(--text-base); }     /* Large */
```

### **Form Elements**

#### **Input Fields**
```css
.form-input {
  width: 100%;
  padding: 0.75rem;               /* --space-3 */
  border: 1px solid var(--gray-300);
  border-radius: 0.375rem;        /* --radius-md */
  font-size: var(--text-sm);
  background-color: var(--white);
  color: var(--text-primary);
  transition: all 0.2s ease;
}

.form-input:focus {
  outline: none;
  border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
}

.form-input.error {
  border-color: var(--error);
  box-shadow: 0 0 0 3px rgba(220, 38, 38, 0.1);
}
```

#### **Select Dropdowns**
```css
.form-select {
  appearance: none;
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 20 20'%3e%3cpath stroke='%236b7280' stroke-linecap='round' stroke-linejoin='round' stroke-width='1.5' d='M6 8l4 4 4-4'/%3e%3c/svg%3e");
  background-position: right 12px center;
  background-repeat: no-repeat;
  background-size: 16px;
  padding-right: 40px;
  /* Inherits from .form-input */
}
```

#### **Form Labels**
```css
.form-label {
  display: block;
  font-size: var(--text-sm);
  font-weight: 500;
  color: var(--text-secondary);
  margin-bottom: 0.5rem;          /* --space-2 */
}
```

#### **Error Messages**
```css
.form-error {
  color: var(--error);
  font-size: var(--text-xs);
  margin-top: 0.25rem;            /* --space-1 */
}
```

### **Card Components**

#### **Base Card**
```css
.card {
  background-color: var(--white);
  border-radius: 0.75rem;         /* --radius-xl */
  box-shadow: var(--shadow-lg);
  border: 1px solid var(--gray-200);
  transition: all 0.2s ease;
  overflow: hidden;
}

.card:hover {
  box-shadow: var(--shadow-xl);
  transform: translateY(-2px);
}
```

#### **Card Variations**
- **Supplement Cards**: Special border states (default/active)
- **Analytics Cards**: Gradient backgrounds
- **Interactive Cards**: Hover effects and clickable states

### **Modal System**

#### **Modal Overlay**
```css
.modal-overlay {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 20px;
}
```

#### **Modal Content**
```css
.modal-content {
  background: white;
  border-radius: 16px;
  padding: 25px;
  max-width: 600px;
  width: 100%;
  max-height: 90vh;
  overflow: auto;
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
  animation: slideUp 0.3s ease-out;
}

@keyframes slideUp {
  from { 
    transform: translateY(50px); 
    opacity: 0; 
  }
  to { 
    transform: translateY(0); 
    opacity: 1; 
  }
}
```

### **Navigation Components**

#### **Tab Navigation**
```css
.tab-container {
  background: var(--gray-100);
  border-bottom: 2px solid var(--gray-200);
  display: flex;
  overflow-x: auto;
}

.tab-button {
  flex: 1;
  min-width: 120px;
  padding: 15px 10px;
  border: none;
  cursor: pointer;
  font-size: 0.95rem;
  font-weight: 500;
  color: var(--gray-500);
  background: transparent;
  transition: all 0.2s ease;
  white-space: nowrap;
}

.tab-button.active {
  background: white;
  color: var(--primary);
  border-bottom: 3px solid var(--primary);
  font-weight: 600;
}

.tab-button:hover:not(.active) {
  background: white;
  color: var(--gray-700);
}
```

---

## 📏 Spacing & Layout System

### **Spacing Scale**
```css
--space-1: 0.25rem     /* 4px */
--space-2: 0.5rem      /* 8px */
--space-3: 0.75rem     /* 12px */
--space-4: 1rem        /* 16px */
--space-5: 1.25rem     /* 20px */
--space-6: 1.5rem      /* 24px */
--space-8: 2rem        /* 32px */
--space-10: 2.5rem     /* 40px */
--space-12: 3rem       /* 48px */
--space-16: 4rem       /* 64px */
```

### **Border Radius System**
```css
--radius-sm: 0.25rem    /* 4px - Small elements */
--radius-md: 0.375rem   /* 6px - Form elements */
--radius-lg: 0.5rem     /* 8px - Buttons */
--radius-xl: 0.75rem    /* 12px - Cards */
--radius-2xl: 1rem      /* 16px - Large cards */
--radius-full: 50%      /* Circular elements */
```

### **Shadow System**
```css
--shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05)
--shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 
             0 2px 4px -1px rgba(0, 0, 0, 0.06)
--shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 
             0 4px 6px -2px rgba(0, 0, 0, 0.05)
--shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 
             0 10px 10px -5px rgba(0, 0, 0, 0.04)
--shadow-2xl: 0 25px 50px -12px rgba(0, 0, 0, 0.25)
```

### **Container Layouts**
```css
.container {
  width: 100%;
  max-width: 1200px;
  margin-left: auto;
  margin-right: auto;
  padding-left: var(--space-4);
  padding-right: var(--space-4);
}

.container-sm { max-width: 768px; }
.container-lg { max-width: 1440px; }
```

---

## 🎭 Interactive States

### **Hover Effects**
```css
/* Standard hover lift */
.hover-lift:hover {
  transform: translateY(-1px);
  box-shadow: var(--shadow-md);
  transition: all 0.2s ease;
}

/* Card hover */
.card-hover:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-xl);
}
```

### **Focus States**
```css
.focus-ring:focus {
  outline: none;
  box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
}

.focus-ring-error:focus {
  box-shadow: 0 0 0 3px rgba(220, 38, 38, 0.1);
}
```

### **Loading States**
```css
.spinner {
  width: 14px;
  height: 14px;
  border: 2px solid transparent;
  border-top: 2px solid currentColor;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
```

---

## 🏷️ Badge System

### **Status Badges**
```css
.badge {
  display: inline-flex;
  align-items: center;
  padding: var(--space-1) var(--space-2);
  border-radius: var(--radius-full);
  font-size: var(--text-xs);
  font-weight: 500;
  border: 1px solid;
}

.badge-success {
  background-color: var(--success-light);
  color: var(--success);
  border-color: var(--success-border);
}

.badge-warning {
  background-color: var(--warning-light);
  color: var(--warning);
  border-color: var(--warning-border);
}

.badge-error {
  background-color: var(--error-light);
  color: var(--error);
  border-color: var(--error-border);
}

.badge-info {
  background-color: var(--info-light);
  color: var(--info);
  border-color: var(--info-border);
}

.badge-gray {
  background-color: var(--gray-100);
  color: var(--gray-600);
  border-color: var(--gray-200);
}
```

---

## 🎯 Specialized Components

### **ADHD Metric Sliders**
```css
/* Custom range input */
.metric-slider {
  height: 8px;
  border-radius: 4px;
  appearance: none;
  cursor: pointer;
  outline: none;
}

.metric-slider::-webkit-slider-thumb {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: var(--primary);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
  border: 2px solid white;
  appearance: none;
  cursor: pointer;
}
```

### **Supplement Dose Cards**
```css
.supplement-card {
  border: 2px solid var(--gray-200);
  border-radius: 12px;
  padding: 15px;
  transition: all 0.3s ease;
  background: white;
  cursor: pointer;
}

.supplement-card.has-doses {
  border-color: var(--success);
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(5, 150, 105, 0.05));
}

.supplement-card:hover {
  box-shadow: var(--shadow-md);
  transform: translateY(-1px);
}
```

### **Focus Session Timer**
```css
.timer-display {
  font-family: 'Monaco', 'Menlo', monospace;
  font-size: var(--text-2xl);
  font-weight: var(--font-bold);
  color: var(--primary);
  text-align: center;
  background: var(--gray-50);
  padding: var(--space-4);
  border-radius: var(--radius-lg);
  border: 2px solid var(--gray-200);
}
```

### **Help Icons & Tooltips**
```css
.help-icon {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: var(--primary);
  color: white;
  font-size: 0.75rem;
  cursor: help;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-weight: var(--font-bold);
}
```

---

## 📱 Responsive Design

### **Breakpoints**
```css
/* Mobile first approach */
@media (min-width: 640px) { /* sm */ }
@media (min-width: 768px) { /* md */ }
@media (min-width: 1024px) { /* lg */ }
@media (min-width: 1280px) { /* xl */ }
@media (min-width: 1536px) { /* 2xl */ }
```

### **Responsive Patterns**
- **Navigation**: Horizontal scroll on mobile, full width on desktop
- **Cards**: Single column on mobile, grid layout on desktop
- **Modals**: Full-width padding on mobile, centered with max-width on desktop
- **Forms**: Single column on mobile, multi-column on desktop

---

## 🎨 Icon System

### **Icon Types**
- **Emoji Icons**: 📊, 💊, 📈, 📜, ⚙️ (Used in navigation)
- **Help Icons**: Circular "?" buttons
- **Status Indicators**: ✓, ✗, ⚠️, ▶️, ⏸️
- **UI Icons**: Arrows, chevrons, plus/minus signs

### **Icon Sizing**
```css
.icon-sm { font-size: 14px; }    /* Small icons */
.icon-md { font-size: 16px; }    /* Default icons */
.icon-lg { font-size: 20px; }    /* Large icons */
.icon-xl { font-size: 24px; }    /* Extra large icons */
```

---

## ⚡ Animation System

### **Transition Settings**
```css
--transition-fast: 0.2s ease      /* Quick interactions */
--transition-normal: 0.3s ease    /* Standard transitions */
--transition-slow: 0.5s ease      /* Slow, dramatic effects */
```

### **Common Animations**
```css
/* Fade in */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(5px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Slide up (modals) */
@keyframes slideUp {
  from { transform: translateY(50px); opacity: 0; }
  to { transform: translateY(0); opacity: 1; }
}

/* Bounce (success states) */
@keyframes bounce {
  0%, 20%, 53%, 80%, 100% { transform: translateY(0); }
  40%, 43% { transform: translateY(-15px); }
  70% { transform: translateY(-7px); }
  90% { transform: translateY(-2px); }
}
```

---

## 🔧 Development Guidelines

### **CSS Custom Properties Usage**
- Always use CSS variables for colors, spacing, and common values
- Maintain consistency with the design token system
- Use semantic color names (primary, success, error) over specific colors

### **Component Naming Convention**
```css
/* Block Element Modifier (BEM) style */
.component-name { }              /* Block */
.component-name__element { }     /* Element */  
.component-name--modifier { }    /* Modifier */

/* Examples */
.card { }
.card__header { }
.card__body { }
.card--elevated { }
```

### **State Classes**
```css
.is-active { }      /* Active state */
.is-disabled { }    /* Disabled state */
.is-loading { }     /* Loading state */
.is-hidden { }      /* Hidden state */
.has-error { }      /* Error state */
```

### **Utility Classes**
```css
/* Text utilities */
.text-center { text-align: center; }
.text-left { text-align: left; }
.text-right { text-align: right; }

/* Spacing utilities */
.m-0 { margin: 0; }
.mt-4 { margin-top: var(--space-4); }
.p-4 { padding: var(--space-4); }

/* Display utilities */
.flex { display: flex; }
.grid { display: grid; }
.hidden { display: none; }
.block { display: block; }
```

---

## 🎯 Accessibility Guidelines

### **Color Contrast**
- Ensure minimum 4.5:1 contrast ratio for normal text
- Ensure minimum 3:1 contrast ratio for large text
- Use color + other indicators (icons, text) for status

### **Focus Management**
- Visible focus indicators on all interactive elements
- Logical tab order through the interface
- Skip links for keyboard navigation

### **Screen Reader Support**
- Semantic HTML structure
- Proper heading hierarchy (h1, h2, h3, etc.)
- Alt text for images and meaningful icons
- ARIA labels for complex interactions

---

## 📋 Implementation Checklist

### **For New Components**
- [ ] Uses CSS custom properties for colors and spacing
- [ ] Follows responsive design patterns
- [ ] Includes hover, focus, and disabled states
- [ ] Implements proper accessibility features
- [ ] Consistent with existing component patterns
- [ ] Includes loading and error states where applicable

### **For New Features**
- [ ] Visual consistency with existing UI
- [ ] Proper semantic HTML structure
- [ ] Mobile-first responsive design
- [ ] Keyboard navigation support
- [ ] Screen reader compatibility
- [ ] Performance considerations (animations, images)

---

## 🚀 Future Enhancements

### **Planned Improvements**
- Dark mode color scheme
- Enhanced animation micro-interactions
- Advanced typography scale
- Component documentation with Storybook
- Design token automation
- Theme customization system

---

**Built with ❤️ by GenkinsForge | Transforming Wellness Through AI**

*This style guide represents the complete design system of FocusLife.ai as of September 2025, based on actual implemented components and styling patterns.*