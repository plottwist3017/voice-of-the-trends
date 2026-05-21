from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import pandas as pd
import numpy as np

# ------------------------------------------------
# Power BI dataset
# ------------------------------------------------
df = dataset

# ------------------------------------------------
# 1. Clean + aggregate hashtags
# ------------------------------------------------
df = df.groupby('hashtag', as_index=False)['mentions'].sum()

# remove weak/noisy hashtags
df = df[df['mentions'] > 2]

# keep top hashtags
df = df.sort_values('mentions', ascending=False).head(1500)

# convert to dictionary
freq = dict(zip(df['hashtag'], df['mentions']))

# ------------------------------------------------
# 2. Load mask image
# ------------------------------------------------
mask = Image.open(
    r"C:\Users\kavya\OneDrive\Desktop\Projects\the-voice-of-twitter-2025\brain.png"
).convert("L")

mask = np.array(mask)

# cleaner mask edges
mask = np.where(mask > 128, 255, 0).astype(np.uint8)

# ------------------------------------------------
# 3. Generate word cloud
# ------------------------------------------------
wc = WordCloud(
    background_color="white",

    mask=mask,

    # word settings
    max_words=2000,
    min_font_size=10,
    max_font_size=220,

    # layout
    relative_scaling=0.5,
    prefer_horizontal=0.9,
    collocations=False,
    margin=1,

    # sharper rendering
    width=2400,
    height=1800,
    scale=4,

    # outline
    contour_width=2,
    contour_color="#E5E7EB",

    # DARK vibrant colors
    colormap="tab20b",

    # consistency
    random_state=42
).generate_from_frequencies(freq)

# ------------------------------------------------
# 4. Display
# ------------------------------------------------
plt.figure(figsize=(16, 12))

# nearest = sharp text
plt.imshow(wc, interpolation="nearest")

plt.axis("off")
plt.tight_layout(pad=0)

plt.show()