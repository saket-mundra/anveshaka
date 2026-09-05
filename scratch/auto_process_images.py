import os
from PIL import Image, ImageOps

SOURCE_DIR = r"c:\Anveshaka\Website Images"
TARGET_DIR = r"c:\Anveshaka\static\images"

os.makedirs(TARGET_DIR, exist_ok=True)

processed_count = 0
for filename in os.listdir(SOURCE_DIR):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
        src_path = os.path.join(SOURCE_DIR, filename)
        clean_name = os.path.splitext(filename)[0].lower().replace(" ", "-")
        
        try:
            with Image.open(src_path) as img:
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")
                
                # 1. Create Card Thumbnail (800x533, 3:2 ratio)
                card_img = ImageOps.fit(img, (800, 533), Image.Resampling.LANCZOS)
                card_path = os.path.join(TARGET_DIR, f"{clean_name}-card.jpg")
                card_img.save(card_path, "JPEG", quality=85, optimize=True)
                
                # 2. Create Banner Cover (1600x900, 16:9 ratio)
                banner_img = ImageOps.fit(img, (1600, 900), Image.Resampling.LANCZOS)
                banner_path = os.path.join(TARGET_DIR, f"{clean_name}-banner.jpg")
                banner_img.save(banner_path, "JPEG", quality=85, optimize=True)
                
                processed_count += 1
        except Exception as e:
            print(f"Error processing {filename}: {e}")

print(f"Image processing complete! Successfully generated responsive web assets for {processed_count} images.")
