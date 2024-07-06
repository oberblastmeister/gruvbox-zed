import json

def lenient_load_str(s):
    json.loads(s)
    
with open("./gruvbox-material-dark-template.json", "r") as template_file:
    with open("./palette.json", "r") as palette_file:
        template = template_file.read()
        palette: dict[str, str] = json.load(palette_file)
        
        items = []
        for color_name, color in palette.items():
            items.append((color_name, color))
        items.sort(reverse=True)
        for color_name, color in items:
            template = template.replace(f"${color_name}", color)
        with open("themes/gruvbox-material-dark.json", "w") as theme_file:
            theme_file.write(f"// Generated file! DO NOT EDIT!\n{template}")
