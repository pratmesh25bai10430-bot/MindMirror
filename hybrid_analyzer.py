import string
from collections import defaultdict
import math

# PREPROCESS 
def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text.split()


# INPUT
def get_inputs():
    print("\n--- Reflection Session ---\n")
    
    exp = input("Describe your recent experience with studying or focus:\n> ")
    
    distract = input("\nWhat usually distracts or interrupts your focus?\n> ")
    
    print("\nAnswer briefly:")
    
    print("Do you feel your work is a choice?")
    print("a) No  b) Sometimes  c) Yes")
    choice = input("> ").lower()
    
    print("\nWhen you are focused, your mind feels:")
    print("a) Forced  b) Neutral  c) Natural")
    state = input("> ").lower()
    
    return exp, distract, choice, state


# NAIVE BAYES TRAINING DATA
train_data = [
    ("i feel happy and motivated", "Positive"),
    ("i am focused and productive", "Positive"),
    ("i feel calm and confident", "Positive"),
    
    ("i feel tired and distracted", "Negative"),
    ("i am stressed and anxious", "Negative"),
    ("i feel overwhelmed and exhausted", "Negative"),
]


# TRAIN NAIVE BAYES
def train_naive_bayes(data):
    word_counts = {
        "Positive": defaultdict(int),
        "Negative": defaultdict(int)
    }
    
    class_counts = {"Positive": 0, "Negative": 0}
    vocab = set()

    for text, label in data:
        words = preprocess(text)
        class_counts[label] += 1
        
        for word in words:
            word_counts[label][word] += 1
            vocab.add(word)

    return word_counts, class_counts, vocab


# PREDICT
def predict_naive_bayes(text, word_counts, class_counts, vocab):
    words = preprocess(text)
    total_docs = sum(class_counts.values())
    
    scores = {}
    
    for label in ["Positive", "Negative"]:
        score = math.log(class_counts[label] / total_docs)
        total_words = sum(word_counts[label].values())
        
        for word in words:
            word_freq = word_counts[label][word] + 1  # smoothing
            score += math.log(word_freq / (total_words + len(vocab)))
        
        scores[label] = score

    return "Positive" if scores["Positive"] > scores["Negative"] else "Negative"


# DETECTORS
def detect_conflict(words):
    if "but" in words and ("want" in words or "should" in words):
        return True
    return False


def detect_distortion(words):
    distortion_words = ["always", "never", "impossible", "can't", "fail"]
    return any(w in distortion_words for w in words)


def detect_distraction(words):
    distractions = ["instagram", "scrolling", "youtube", "phone", "doomscroll"]
    return any(w in distractions for w in words)


def detect_motivation(words):
    if "have" in words or "must" in words:
        return "external"
    if "want" in words or "like" in words:
        return "internal"
    return "unclear"


# PATTERN ANALYSIS
def analyze_patterns(exp, distract):
    words = preprocess(exp) + preprocess(distract)
    
    return {
        "conflict": detect_conflict(words),
        "distortion": detect_distortion(words),
        "distraction": detect_distraction(words),
        "motivation": detect_motivation(words)
    }


# REFLECTION ENGINE
def generate_reflection(patterns, choice, state, nb_sentiment):
    lines = []

    if patterns["conflict"]:
        lines.append("There seems to be a tension between what you intend and what you actually do.")

    if patterns["distortion"]:
        lines.append("Your language leans toward absolute terms, which can make challenges feel heavier than they are.")

    if patterns["distraction"]:
        lines.append("Your attention appears to be pulled outward, shaped by external stimuli rather than internal direction.")

    if patterns["motivation"] == "external":
        lines.append("Your engagement seems influenced more by obligation than genuine choice.")
    elif patterns["motivation"] == "internal":
        lines.append("There is a trace of intrinsic desire in how you approach your work.")

    if nb_sentiment == "Negative":
        lines.append("There is also an underlying negative emotional tone in how you describe your experience.")
    else:
        lines.append("Your expression carries a relatively positive emotional tone.")

  
    if choice == "a":
        lines.append("You perceive your actions as necessary rather than chosen.")
    elif choice == "c":
        lines.append("You experience your work as something you actively choose.")

    if state == "a":
        lines.append("Your focus feels forced, which often resists depth.")
    elif state == "c":
        lines.append("Your focus aligns naturally when it emerges.")

    lines.append(
        "Focus may not be something you force, but something that emerges when perception, intention, and state align."
    )

    return " ".join(lines)


# SUMMARY
def generate_summary(patterns):
    if patterns["conflict"]:
        return "Core Issue: Internal conflict between intention and action."
    elif patterns["distraction"]:
        return "Core Issue: External distractions dominating attention."
    else:
        return "Core State: Relatively balanced cognitive pattern."


# MAIN 
def main():
    print("=== Cognitive Reflection System ===")
    
    exp, distract, choice, state = get_inputs()
    
    # Train ML
    word_counts, class_counts, vocab = train_naive_bayes(train_data)
    
    # Pattern + ML
    patterns = analyze_patterns(exp, distract)
    nb_sentiment = predict_naive_bayes(exp + " " + distract, word_counts, class_counts, vocab)
    
    # Output
    reflection = generate_reflection(patterns, choice, state, nb_sentiment)
    summary = generate_summary(patterns)
    
    print("\n--- Reflection ---\n")
    print(reflection)
    
    print("\n--- Summary ---")
    print(summary)


if __name__ == "__main__":
    main()