#!/usr/bin/env python3
"""
Optimize images for web use by resizing and compressing them
"""

from PIL import Image
import os

def optimize_image(input_path, output_path, max_width=1200, quality=85):
    """
    Optimize an image by resizing and compressing it
    """
    try:
        with Image.open(input_path) as img:
            # Convert to RGB if necessary (removes alpha channel for JPEG)
            if img.mode in ('RGBA', 'LA', 'P'):
                # Create white background
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                img = background
            elif img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Calculate new dimensions
            width, height = img.size
            if width > max_width:
                ratio = max_width / width
                new_width = max_width
                new_height = int(height * ratio)
                img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            # Save optimized image
            img.save(output_path, 'JPEG', quality=quality, optimize=True)
            return True
    except Exception as e:
        print(f"Error optimizing {input_path}: {e}")
        return False

def create_optimized_images():
    """Create optimized versions of all images"""
    
    # Create optimized directory
    os.makedirs('optimized', exist_ok=True)
    
    # List of images to optimize with their target sizes
    images_to_optimize = [
        # Screenshots - resize to reasonable web sizes
        ('Screenshot 2025-09-04 125011.png', 'optimized/dashboard-screenshot.jpg', 800),
        ('Screenshot 2025-09-04 125053.png', 'optimized/add-supplement-screenshot.jpg', 800),
        ('Screenshot 2025-09-04 125125.png', 'optimized/focus-session-screenshot.jpg', 800),
        
        # Hero/marketing images - keep larger but optimize
        ('focuslife-supplement-management-hero.png', 'optimized/supplement-management-hero.jpg', 1200),
        ('focuslife-active-lifestyle.png', 'optimized/active-lifestyle-hero.jpg', 1200),
        ('focuslife-healthcare-consultation.png', 'optimized/healthcare-consultation-hero.jpg', 1200),
        ('focuslife-social-interaction.png', 'optimized/social-interaction-hero.jpg', 1200),
        
        # Logo - smaller version for favicon/small use
        ('focuslife-logo-nobg.png', 'optimized/logo-small.jpg', 400),
        ('focuslife-logo.png', 'optimized/logo-large.jpg', 800),
    ]
    
    optimized_count = 0
    for input_file, output_file, max_width in images_to_optimize:
        if os.path.exists(input_file):
            if optimize_image(input_file, output_file, max_width):
                print(f"✅ Optimized: {input_file} → {output_file}")
                optimized_count += 1
            else:
                print(f"❌ Failed: {input_file}")
        else:
            print(f"⚠️  Not found: {input_file}")
    
    print(f"\n🎨 Optimized {optimized_count} images for web use")
    print("• Reduced file sizes for faster loading")
    print("• Converted to JPEG format for better compression") 
    print("• Resized to appropriate web dimensions")

if __name__ == "__main__":
    create_optimized_images()