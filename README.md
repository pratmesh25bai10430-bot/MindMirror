# MindMirror
A CLI-based “cognitive mirror” that analyzes how you describe your focus and turns it into a layered reflection.  Instead of scoring attention, it tries to detect patterns like internal conflict, distraction, and motivation using simple rule-based logic inspired by psychology

This is a command-line based Cognitive Reflection System.

Instead of giving you scores like “low focus” or “high distraction”, it tries to:

* read what you write
* detect patterns (like conflict, distraction, motivation)
* and give back a slightly philosophical reflection

It also uses a very small Naive Bayes model to detect emotional tone (positive/negative).

## Requirements
* Python 3.x

## How To Setup And Run
If using git:
git clone 
cd 

Or just download zip and extract it

Then just run hybrid_analyzer.py

## How It Works

1. Rule-Based AI
  Detects patterns like:
  * “want but can’t” → conflict
  * “always/never” → cognitive distortion
  * “instagram/scrolling” → distraction

2. Naive Bayes (Machine Learning)
  * Trained on small text samples
  * Classifies your input as Positive or Negative

3. Reflection Engine
  * Combines everything
  * Generates a human-like interpretation

## Inspiration
Conventional Psychology or online tests are MCQ based and limited, this tool allows the discreteness of MCQ and the freedom of text based answer to do a good psychological analysis.
