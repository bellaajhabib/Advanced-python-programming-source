from io import BytesIO
from pathlib import Path
from reportlab.pdfgen import canvas

OUTPUT_DIR = Path("pdf-tests")
OUTPUT_DIR.mkdir(exist_ok=True)

SIZES_MB = [
    0.5,
    1,
    2,
    5,
    8,
    10,
    15,
    19,
    19.9,
    20,
    20.1,
    21,
    25,
]

def generate_pdf(size_mb):
    target = int(size_mb * 1024 * 1024)

    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)
    pdf.drawString(100, 750, f"PDF test - {size_mb} Mo")
    pdf.save()

    content = buffer.getvalue()

    # Padding après EOF : pratique pour tester la taille,
    # mais à éviter pour tester des validateurs PDF stricts.
    padding = target - len(content)

    if padding < 0:
        raise ValueError("Target size too small")

    filename = OUTPUT_DIR / f"test-{size_mb}MB.pdf"

    with open(filename, "wb") as f:
        f.write(content)
        f.write(b" " * padding)

    print(f"Created: {filename} ({size_mb} MB)")


for size in SIZES_MB:
    generate_pdf(size)