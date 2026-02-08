from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox

# ---------- UTILIDADES ----------

def select_file():
    return filedialog.askopenfilename(
        filetypes=[("Images", "*.png *.jpg *.jpeg *.tga *.bmp")]
    )

def select_output_path():
    return filedialog.asksaveasfilename(
        title="Guardar textura ORM",
        defaultextension=".png",
        filetypes=[("PNG Image", "*.png")]
    )

def black_image(size):
    return Image.new("L", size, 0)


def load_or_black(path, size):
    if path:
        return Image.open(path).convert("L")
    return black_image(size)


# ---------- CORE ORM ----------

def create_orm(ao_path, rough_path, metal_path, alpha_path, output_path):
    # Determinar tamaño base
    base_img = None
    for p in [ao_path, rough_path, metal_path, alpha_path]:
        if p:
            base_img = Image.open(p).convert("L")
            break

    if base_img is None:
        raise ValueError("Debes seleccionar al menos una textura")

    size = base_img.size

    ao = load_or_black(ao_path, size)
    rough = load_or_black(rough_path, size)
    metal = load_or_black(metal_path, size)
    alpha = load_or_black(alpha_path, size)

    # Validar tamaños
    for img in [ao, rough, metal]:
        if img.size != size:
            raise ValueError("Todas las imágenes deben tener la misma resolución")

    result = Image.new("RGB", size)
    width, height = size

    for y in range(height):
        for x in range(width):
            result.putpixel(
                (x, y),
                (
                    ao.getpixel((x, y)),      # R
                    rough.getpixel((x, y)),   # G
                    metal.getpixel((x, y)),   # B
                    alpha.getpixel((x, y))    # A
                )
            )

    result.save(output_path)
