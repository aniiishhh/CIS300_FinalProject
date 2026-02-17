import hashlib

filenames = [
    "Steamed_rice_in_bowl_01.jpg",
    "Jeera_Rice_India.jpg",
    "Veg-Biryani.jpg",
    "Vegetable_Biryani.JPG",
    "Roti_or_chappati.jpg",
    "Dal_Makhani.jpg",
    "Paneer_Tikka_Masala.jpg",
    "Jeera_aloo.jpg",
    "Chana_masala.jpg",
    "Dal_Fry_(15295329183).jpg",
    "Mixed_salad_(Kosambri_or_Kachumber).jpg",
    "Cucumber_Mint_Raita.jpg",
    "Dry_Gobi_Manchurians.JPG",
    "Idli_Sambar-Noida-UP-SP004.jpg",
    "Masala_dosa_01.jpg"
]

base_url = "https://upload.wikimedia.org/wikipedia/commons"

print("Generated URLs:")
for filename in filenames:
    # Wikimedia uses spaces replaced by underscores in filenames for the URL generation usually, 
    # but the MD5 is calculated on the filename with underscores.
    # Actually, the filename in the URL uses underscores.
    clean_filename = filename.replace(" ", "_")
    
    # Calculate MD5
    m = hashlib.md5()
    m.update(clean_filename.encode('utf-8'))
    md5_hash = m.hexdigest()
    
    a = md5_hash[0]
    ab = md5_hash[0:2]
    
    # Standard full resolution URL
    full_url = f"{base_url}/{a}/{ab}/{clean_filename}"
    
    # Thumbnail URL (using 640px width)
    thumb_url = f"{base_url}/thumb/{a}/{ab}/{clean_filename}/640px-{clean_filename}"
    
    print(f"{filename}: {thumb_url}")
