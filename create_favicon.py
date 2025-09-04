#!/usr/bin/env python3
"""
Create favicon.ico from existing logo assets
"""

from PIL import Image
import os

def create_favicon():
    """Create favicon.ico from the best available logo"""
    
    # Try to use the existing logo files in order of preference
    logo_sources = [
        "focuslife-logo-nobg.png",  # PNG without background
        "focuslife-logo.png",       # Standard PNG
        "optimized/logo-small.jpg", # Optimized small logo
        "optimized/logo-large.jpg"  # Optimized large logo
    ]
    
    source_file = None
    for logo_file in logo_sources:
        if os.path.exists(logo_file):
            source_file = logo_file
            print(f"Using {logo_file} as source for favicon")
            break
    
    if not source_file:
        print("❌ No suitable logo file found for favicon creation")
        return False
    
    try:
        # Open the source image
        with Image.open(source_file) as img:
            # Convert to RGBA if not already
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            
            # Create multiple sizes for the ICO file
            # Standard favicon sizes: 16x16, 32x32, 48x48
            sizes = [(16, 16), (32, 32), (48, 48)]
            
            # Create a list to store the resized images
            favicon_images = []
            
            for size in sizes:
                # Resize the image to the target size with high-quality resampling
                resized = img.resize(size, Image.Resampling.LANCZOS)
                
                # Ensure we have a clean transparent background if it's a PNG
                if source_file.endswith('.png'):
                    # Keep transparency
                    favicon_images.append(resized)
                else:
                    # Convert to RGB for JPG sources and add white background
                    background = Image.new('RGB', size, (255, 255, 255))
                    if resized.mode == 'RGBA':
                        background.paste(resized, mask=resized.split()[-1])
                    else:
                        background.paste(resized)
                    favicon_images.append(background)
            
            # Save as favicon.ico
            favicon_images[0].save(
                'favicon.ico',
                format='ICO',
                sizes=[(img.width, img.height) for img in favicon_images],
                append_images=favicon_images[1:]
            )
            
            print("✅ Created favicon.ico with sizes: 16x16, 32x32, 48x48")
            
            # Also create individual PNG files for modern favicon usage
            for i, size in enumerate(sizes):
                png_filename = f"favicon-{size[0]}x{size[1]}.png"
                favicon_images[i].save(png_filename, format='PNG')
                print(f"✅ Created {png_filename}")
            
            # Create Apple Touch Icon (180x180)
            apple_touch_icon = img.resize((180, 180), Image.Resampling.LANCZOS)
            if source_file.endswith('.jpg'):
                # Add white background for JPG sources
                background = Image.new('RGB', (180, 180), (255, 255, 255))
                if apple_touch_icon.mode == 'RGBA':
                    background.paste(apple_touch_icon, mask=apple_touch_icon.split()[-1])
                else:
                    background.paste(apple_touch_icon)
                apple_touch_icon = background
            
            apple_touch_icon.save('apple-touch-icon.png', format='PNG')
            print("✅ Created apple-touch-icon.png (180x180)")
            
            return True
            
    except Exception as e:
        print(f"❌ Error creating favicon: {e}")
        return False

if __name__ == "__main__":
    print("🎨 Creating favicon from FocusLife.ai logo...")
    success = create_favicon()
    
    if success:
        print("\n🎉 Favicon creation completed!")
        print("Files created:")
        print("• favicon.ico (multi-size ICO file)")
        print("• favicon-16x16.png")
        print("• favicon-32x32.png") 
        print("• favicon-48x48.png")
        print("• apple-touch-icon.png")
        print("\nNext steps:")
        print("1. Add favicon links to HTML pages")
        print("2. Test favicon display in browsers")
    else:
        print("\n❌ Favicon creation failed!")