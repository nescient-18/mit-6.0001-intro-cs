# Reflection — Problem Set #1
**Course:** 6.0001 – Introduction to Computer Science  
**Date Completed:** 2025-10-25

---

## 1. Objective
Construct a basic input-math-output program, remaining aware of problematic cases.

---

## 2. Freeform Summary 
As mentioned in [the parent file](https://github.com/nescient-18/mit-6.0001-intro-cs/blob/main/AI_DISCLOSURE.md), I had done this assignment before several years ago. It was elementary at this point. My intention going back to this assignment was to make my approach robust and professional. I'm presently unfamiliar with more rigorous programming and software development, so I wanted to approach this with the mindset of getting out as much as possible from a basic assignment.

Initially, I had an input check within the main body of the program that was very similar to `get_float()`. (Side Note: I should be more incremental with my commits and pushes so my progress appears as a genuine learning process.) After sending that code to GPT, it recommended to make a function to take care of that. Duh.

It recommended to have a more general key function check -- something I could put in a `lambda` function, say -- but I didn't feel it necessary for this assignment since it was a simple binary conditon: positive or not. As such, the `get_float()` function isn't very generalizable for other uses.

I was uncertain about whether to have a `break` statement within the loop and then `return` outside of it, but GPT recommended to have it within it since it's straightforward (which I knew it was, but there are customs I'm unfamiliar with). Similar ambivalence for `while True:`.

Probably the most interesting bit from this was the flow of control within the getter function. I originally had the positivity check within the `try` block. Even typing this now, I see how silly that is. The `try` check should be solely for error catching. We can worry about positivity condition iff it's a valid input to begin with. 

Once the inputs are guaranteed valid from the function, we can safely perform the math needed without worry about type errors.

---

## 2. Process & Reasoning


I wanted to approach the assignment more robustly and safeguard against improper input. My reasoning in this otherwise simple assignment allowed me to establish the importance of a clear flow of control. I could have had the input checks within the main body, but that would be too messy.

---

## 3. Key Insights
- Clear flow of control
- Validate early, fail clearly; prevent downstream code from needing to check anything
- Isolate input-handling from computation

---

## 4. Challenges & Debugging
Just uncertainties about best strategies and using GPT to guide me through them after attempting it myself.



