# Reflection — Problem Set #2
**Course:** 6.0001 – Introduction to Computer Science  
**Date Completed:** 2025-11-03

---

## 1. Objective
Create a more comprehensive program with ongoing input, rules, and different possible outputs.

---

## 2. Freeform Summary 
This was the most fun assignment thus far. I completed all but the "hint" problem a few years ago. Doing it now, I sense I am getting a stronger idea of what programming actually is, although it still remains a bit nebulous to me. As of now, I'm seeing how modular everything is and the importance of giving each function a specific task whose domain is validated by prior code. At the moment, it feels much of what I learned from this assignment is implicit -- a deeper subconscious comfort with the material and preparation for more complex programs. Could it be programming is simply getting each piece to work and fitting them together, and that more complexity just means more pieces and relationships? I'll see.

I spent the most time on this relatively simple assignment figuring out how to reduce redundancy within `hangman()`. The warning handling was very messy originally, so I spent some time thinking how to streamline it into a single function. Maybe this wasn't perfect, but it cleaned it up to my amateur eyes.

I learned my lesson from the previous PS and ensured my loop condition was affected each iteration. I also continue to implement a clear flow of control, as seen within the input testing. The goal of that code fragment was simply to test the input -- it didn't need to handle the warnings or displaying progress. Those are separate processes that can be handled by a simple call to other functions. I also wrote and commented out basic code a beginner would probably do without fully utilizing Pythonic sets and comprehension.

I also spent too much time trying to be clever about `match_with_gaps()`. I had an idea that we could have a necessary and sufficient conditional check by: 1. checking if `revealed` was a subset of `set(other_word)`; 2. checking if the symmetric difference between the two was only `{"_"}`. If those two were true, I thought, we could return False (assuming equal length). It turned out this was a sufficient condition, but not a necessary one from the counterexample: `"ab_ _"` and `"axby"`. The former is a subset of the latter sans underscores, and the symmetric difference is only `"_"`, but clearly, the former is not a potential candidate. From this, I did a fairly simple positional check for each letter. Maybe my implementation was naive.

---

## 2. Key Insights
- Keep each "function" a function. If it's not your job, relegate it.
- Don't be afraid to return tuples (especially if it makes the code cleaner)
- Let each piece of the code do its job. Not everything can and should be handled in one place. Understand how each piece fits together. 

---

## 3. Challenges
Trying to be too clever without getting it to work first, and also not considering enough counterexamples. I should have thought of more examples myself before giving GPT a "proof" sketch.

## 4. GPT Insights

Zach’s strength in this assignment was his instinct for structure and abstraction. He moved beyond making the program “work” to reasoning about *how control flow, state, and modularity interact*. His refactoring of `hangman()` showed an emerging understanding of single-responsibility design: each helper should do one job cleanly and communicate through explicit return values.

A highlight of his thinking was the set-theoretic exploration of `match_with_gaps()`. Although that approach failed on positional cases, it revealed an important growth edge: learning to test conjectures systematically and distinguish **sufficient** from **necessary** conditions. That’s exactly how theoretical reasoning merges with programming practice.

Going forward, Zach should continue training that balance between elegance and evidence — experimenting boldly, but always stress-testing ideas with counterexamples and small traces. He’s also beginning to think in algorithmic asymptotics, and learning when theoretical O(n) analysis matters and when real-world constraints flatten it.

Overall, this problem set marks a clear shift from beginner’s pattern imitation toward true computational reasoning — the mindset that scales.
