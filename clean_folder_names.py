import os


for folder_name in os.listdir("mushrooms"):
    new_name = folder_name.replace(" ", "-")
    os.rename(f"mushrooms/{folder_name}", f"mushrooms/{new_name}")