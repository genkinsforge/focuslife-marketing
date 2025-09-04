#!/usr/bin/env python3
"""
Crops the empty space from SVG logos by adjusting the viewBox
to fit the actual content bounds.
"""

def create_cropped_logos():
    """Create cropped versions of all logo SVGs"""
    
    # Cropped vector version - adjusted viewBox to fit the magnifying glass
    vector_cropped = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="15 15 140 140" width="140" height="140">
  <title>FocusLife.ai Logo</title>
  <desc>AI-Powered Wellness Tracking - Magnifying Glass with Leaf</desc>
  
  <defs>
    <!-- Green gradient for leaf -->
    <linearGradient id="leafGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#10b981"/>
      <stop offset="100%" style="stop-color:#047857"/>
    </linearGradient>
    
    <!-- Gray gradient for handle -->
    <linearGradient id="handleGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#4b5563"/>
      <stop offset="100%" style="stop-color:#1f2937"/>
    </linearGradient>
  </defs>

  <!-- Magnifying glass rim -->
  <circle cx="75" cy="75" r="45" 
          fill="white" 
          stroke="#1f2937" 
          stroke-width="6"/>

  <!-- Leaf shape inside the magnifying glass -->
  <path d="M 55 60 
           Q 65 45 85 55
           Q 100 65 95 85
           Q 90 100 75 95
           Q 60 90 55 85
           Q 50 75 55 60 Z" 
        fill="url(#leafGradient)" 
        stroke="#047857" 
        stroke-width="1"/>
  
  <!-- Leaf central vein -->
  <path d="M 65 70 Q 75 65 85 75" 
        fill="none" 
        stroke="#065f46" 
        stroke-width="2" 
        stroke-linecap="round"/>

  <!-- Magnifying glass handle -->
  <rect x="108" y="108" 
        width="12" 
        height="42" 
        rx="6" 
        ry="6" 
        fill="url(#handleGradient)" 
        stroke="#111827" 
        stroke-width="2" 
        transform="rotate(45 114 129)"/>

  <!-- Handle connector -->
  <circle cx="108" cy="108" r="6" 
          fill="#1f2937" 
          stroke="#111827" 
          stroke-width="1"/>
</svg>'''

    # Cropped brand version
    brand_cropped = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="15 15 140 140" width="140" height="140">
  <title>FocusLife.ai Logo - Brand Colors</title>
  <desc>AI-Powered Wellness Tracking - Brand Color Version</desc>
  
  <defs>
    <!-- Brand gradient -->
    <linearGradient id="brandGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#6366f1"/>
      <stop offset="50%" style="stop-color:#8b5cf6"/>
      <stop offset="100%" style="stop-color:#a855f7"/>
    </linearGradient>
    
    <!-- Green gradient for leaf -->
    <linearGradient id="leafGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#10b981"/>
      <stop offset="100%" style="stop-color:#047857"/>
    </linearGradient>
  </defs>

  <!-- Magnifying glass rim with brand colors -->
  <circle cx="75" cy="75" r="45" 
          fill="white" 
          stroke="url(#brandGradient)" 
          stroke-width="6"/>

  <!-- Leaf shape inside the magnifying glass -->
  <path d="M 55 60 
           Q 65 45 85 55
           Q 100 65 95 85
           Q 90 100 75 95
           Q 60 90 55 85
           Q 50 75 55 60 Z" 
        fill="url(#leafGradient)" 
        stroke="#047857" 
        stroke-width="1"/>
  
  <!-- Leaf central vein -->
  <path d="M 65 70 Q 75 65 85 75" 
        fill="none" 
        stroke="#065f46" 
        stroke-width="2" 
        stroke-linecap="round"/>

  <!-- Magnifying glass handle with brand colors -->
  <rect x="108" y="108" 
        width="12" 
        height="42" 
        rx="6" 
        ry="6" 
        fill="url(#brandGradient)" 
        stroke="#4f46e5" 
        stroke-width="2" 
        transform="rotate(45 114 129)"/>

  <!-- Handle connector -->
  <circle cx="108" cy="108" r="6" 
          fill="url(#brandGradient)" 
          stroke="#4f46e5" 
          stroke-width="1"/>
</svg>'''

    # Cropped monochrome version
    mono_cropped = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="15 15 140 140" width="140" height="140">
  <title>FocusLife.ai Logo - Monochrome</title>
  <desc>AI-Powered Wellness Tracking - Single Color Version</desc>

  <!-- Magnifying glass rim -->
  <circle cx="75" cy="75" r="45" 
          fill="white" 
          stroke="#1f2937" 
          stroke-width="6"/>

  <!-- Leaf shape inside the magnifying glass -->
  <path d="M 55 60 
           Q 65 45 85 55
           Q 100 65 95 85
           Q 90 100 75 95
           Q 60 90 55 85
           Q 50 75 55 60 Z" 
        fill="#1f2937" 
        stroke="#1f2937" 
        stroke-width="1"/>
  
  <!-- Leaf central vein -->
  <path d="M 65 70 Q 75 65 85 75" 
        fill="none" 
        stroke="white" 
        stroke-width="2" 
        stroke-linecap="round"/>

  <!-- Magnifying glass handle -->
  <rect x="108" y="108" 
        width="12" 
        height="42" 
        rx="6" 
        ry="6" 
        fill="#1f2937" 
        stroke="#111827" 
        stroke-width="2" 
        transform="rotate(45 114 129)"/>

  <!-- Handle connector -->
  <circle cx="108" cy="108" r="6" 
          fill="#1f2937" 
          stroke="#111827" 
          stroke-width="1"/>
</svg>'''

    return [
        ("focuslife-logo-vector-cropped.svg", vector_cropped),
        ("focuslife-logo-brand-cropped.svg", brand_cropped), 
        ("focuslife-logo-mono-cropped.svg", mono_cropped)
    ]

def crop_embedded_svg():
    """Create cropped version of the embedded PNG SVG"""
    
    # First get the base64 data from the existing embedded SVG
    with open("focuslife-logo-embedded.svg", "r") as f:
        content = f.read()
        
    # Extract the base64 data
    start = content.find("data:image/png;base64,") + len("data:image/png;base64,")
    end = content.find('"', start)
    base64_data = content[start:end]
    
    # Create cropped embedded version
    embedded_cropped = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" 
     width="400" height="400" viewBox="100 100 600 600">
  <title>FocusLife.ai Logo - High Quality</title>
  <desc>AI-Powered Wellness Tracking Platform Logo - Original Quality Cropped</desc>
  
  <!-- Embedded PNG as data URI - cropped viewBox -->
  <image x="0" y="0" width="800" height="800" 
         xlink:href="data:image/png;base64,{base64_data}"
         preserveAspectRatio="xMidYMid meet"/>
</svg>'''

    return embedded_cropped

if __name__ == "__main__":
    # Create cropped versions
    cropped_versions = create_cropped_logos()
    
    # Write the vector versions
    for filename, content in cropped_versions:
        with open(filename, 'w') as f:
            f.write(content)
        print(f"✅ Created {filename}")
    
    # Create cropped embedded version
    try:
        embedded_content = crop_embedded_svg()
        with open("focuslife-logo-embedded-cropped.svg", 'w') as f:
            f.write(embedded_content)
        print("✅ Created focuslife-logo-embedded-cropped.svg")
    except Exception as e:
        print(f"⚠️  Could not create cropped embedded version: {e}")
    
    print("\n🎨 Cropped logo versions created:")
    print("• All logos now have tight bounds with no empty space")
    print("• ViewBox adjusted to fit actual content (15 15 140 140)")
    print("• Embedded version cropped to focus on main logo area")
    print("• Perfect for web use - no wasted space!")