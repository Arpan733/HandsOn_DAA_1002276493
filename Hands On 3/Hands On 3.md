# Assignment Answers

function x = f(n)
   x = 1;
   for i = 1:n
        for j = 1:n
             x = x + 1;

## Question 1: Find the runtime of the algorithm mathematically.

![IMG_20250202_142351 1](https://github.com/user-attachments/assets/eca16881-05bc-4bf4-b823-868c208b4660)

---

## Question 2: Time this function for various n e.g. n = 1,2,3.... You should have small values of n all the way up to large values. Plot "time" vs "n" (time on y-axis and n on x-axis). Also, fit a curve to your data, hint it's a polynomial. 

The function is timed for values of \(n\), and the time for the execution is plotted against \(n\).
The data is fitted with a polynomial to capture the relationship between the input size and execution time.

![image](https://github.com/user-attachments/assets/07f40d9b-d498-40b3-ab8b-537eb3d6f648)

---

## Question 3: Upper and Lower Bound Polynomials, Big-O, Big-Omega, and Big-Theta

The fitted curve is a quadratic function of the form:

\[
y = ax^2 + bx + c
\]

- **Big-O**: \( O(n^2) \). This means the runtime is bound above every time by a constant multiple of \(n^2\).

- **Big-Omega**: \( \Omega(n^2) \). This means runtime is bound below every time by a constant multiple of \(n^2\).

- **Big-Theta**: \( \Theta(n^2) \). This means runtime is asymptotically equivalent to \(n^2\).

---

## Question 4: Approximate Location of `n_0`

The approximate value of `n_0`, where the measured time is height deviates from the actual time which is shown in the plot by `Location of N_0`.

![image](https://github.com/user-attachments/assets/30ff6195-1b3b-4554-8268-3821579ccb03)

In the plot, **`n_0`** is indicated by the green dashed line. Based on the visual inspection, we can conclude that `n_0` occurs around **[935]**.

---
