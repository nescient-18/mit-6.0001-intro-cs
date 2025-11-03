# Reflection — Problem Set #1
**Course:** 6.0001 – Introduction to Computer Science  
**Date Completed:** 2025-10-26

---

## 1. Objective
Construct a basic input-math-output program, remaining aware of problematic cases.

---

## 2. Freeform Summary 
I had also finished this problem years ago and don't remember running into many problems with it. As expected, this time I wanted to be more robust. I made a more general `get_number()` function than the previous problem set by allowing for a custom condition to check. I also learned from my ignorance last time and ensured a clear flow of control within this function. You can argue passing strings as actual parameters is poor practice, and that I should have just allowed the function itself to take care of what the message should be. 

Frankly, I don't know what the best strategy there is. The purpose of `get_number()` is purely to *get the number* and ensure there are no errors or downstream domain issues. The caller shouldn't have to worry about which error message is printed, just the input message and condition. In retrospect, I probably should have approached it that way.

Most importantly, I practiced implementing a decrementing function within the `while` loop. Originally, I was decrementing a value different than the condition check. I now see how poor practice that was. I also used GPT to help me improve my bisection search loop. I was too fixated on examples from the book that I lost the forest for the trees. By allowing the decrementing function to be the distance between `high` and `low`, ensuring that once it was zero or less, the loop stopped.

GPT recommended to ensure the `high` was sufficient before starting the loop because that prevented an infinite loop, which makes total sense: if it's not possible, there's no point in doing unnecessary work down the line. Check upfront and proceed iff it's viable. Since the `high` was guaranteed sufficient by the time the loop initiates, we then simply perform a bisection search. But instead of bumping the low up to halfway between `mid` and `high`, incrementing it by only 1 allows us to find the *minimum* percentage required per `scale`.

I may have used too many default parameters and should have instead relied on global variables. That's perhaps a better strategy, but I felt this allowed it to be more generaized to the many users of this program.

---

## 2. Process & Reasoning


See above.

---

## 3. Key Insights
- Decrement the condition being checked in a `while` loop.
- Bend an algorithm (in this case, bisection search) if it allows you to reach your goals better/quicker

---

## 4. Challenges & Debugging
Implementing bisection search too rigidly and, quite literally, by the book.

