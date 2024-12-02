# Compression Chronicles: A Successfully Failed Experiment

Welcome to my wild ride through the fundamentals of data compression! This project started as a way to learn about how compression algorithms work—turns out, I learned way more than I bargained for. Buckle up, because things got interesting.
What Happened?

## The Initial Goal

The idea was simple: take a PNG image, apply a custom compression algorithm, and reconstruct it back to its original state. The aim? To understand how compression works, from encoding to reconstruction, and maybe even achieve something close to lossless compression.
The Plot Twist

When I encoded the PNG using my algorithm, the resulting file was a whopping 8 times the size of the original. Yup, you read that right—eight times! 😅 Turns out, text-based representations of integers (like the ones I was using) are incredibly inefficient. Who knew storing 255 as text instead of binary would be such a disaster? (Spoiler: Everyone who knows compression fundamentals knew.)
Reconstruction: Sort of a Success?

#### Original Image (11.2 MB)
<img src="example7.png" alt="Original Image" width=400px>

#### Reconstructed Image (3.5 MB)
<img src="reconstructed-example7.png" alt="Original Image" width=400px>

When I decoded the file and reconstructed the image, something...unexpected happened. The new image was about 1/3 the size of the original, which sounds great, but here’s the catch:

  1) The reconstructed image was not grayscale as intended.
  2) Some pixel values got generalized into pure black and white, leading to noticeable changes.
  3) The overall exposure of the image was higher, giving it a strange, washed-out vibe.

I wouldn’t call it “lossless” compression—it’s more like “oops-my-bad-but-let’s-pretend-this-is-art.”

## Lessons Learned

  1) Text ≠ Efficient Storage: Representing data as text is ridiculously inefficient for most formats, especially for high-frequency data like pixel values. Binary storage is king. 👑
  2) Lossy vs Lossless: My attempt wasn’t purely lossless because my algorithm simplified pixel values, which introduced artifacts (aka mistakes).
  3) Metadata Matters: Exposure changes are technically a form of data loss, but I’m now tinkering with the idea of encoding the original exposure as metadata. That way, I can apply a correction during reconstruction. Fingers crossed this works! 🤞


## Why I’m Calling This a Success (Kinda)

Even though the results weren’t what I expected, this experiment taught me the nitty-gritty of compression, encoding, and reconstruction. It’s a successfully failed project that pushed me out of my comfort zone and into the strange world of “artistic data corruption.”

Thanks for checking out my project!
