---
number headings: first-level 1, max 6, contents ^toc, skip ^skipped, start-at 1, _.I.1
---
## I Introduce

In short, mathematical induction just likes domino, one pushes another.

**three simple steps:**
1. **Base Case**: Prove that P(0) is true. 
2. **Induction Hypothesis**: For arbitrary k ≥ 0, assume that P(k) is true.
3. **Inductive Step**: With the assumption of the Induction Hypothesis in hand, show that P(k + 1) is true

> **Theorem 1**
> For all $n\in N, n^{3}-n$ is divisible by 3.
> 
> **proof** proceed by induction
> ![](attachments/02-Mathematical%20Induction.png)
> (In fact, we can proof it by cases since $n^{3}-n=(n-1)n(n+1)$, and one of the factors on the right side of the equation must be a multiple of 3, then we get it.)

We now consider a more advanced proof by induction, which establishes a simplified version of the famous _four color theorem_. But it is too difficult for us to proof. Let's change it easier:

> **Theorem 2**
> (Two Color Theorem) our “map” is given by a rectangle which is divided into regions by drawing straight lines, such that each line divides the rectangle into two regions, then:using no more than two colors (say, red and blue) such that no two bordering regions have the same color(below is an example case)\
> ![|158](attachments/02-Mathematical%20Induction-1.png)
>
> **proof** proceed by induction
> we set <u>n</u> as the number of lines
> 1. <u>Base Case</u> (n = 0):  Clearly P(0) holds, since if we have n = 0 lines we can color the entire map using a single color.
> 2. <u>Induction Hypothesis</u>:  For some arbitrary n = k ≥ 0, assume P(k).
> 3. <u>Inductive Step</u>: Whenever we add a line, that is, P(k+1), we can always prove that P(k+1) is true by swapping parts of red and blue (as shown below)![](attachments/02-Mathematical%20Induction-2.png)

## II Strengthening the Induction Hypothesis

Sometimes, our Induction Hypothesis is too “weak”; it does not give us enough structure to say anything meaningful, for example:
> **Theorem 3**
> For all n ≥ 1, the sum of the first n odd numbers is a perfect square.

In fact, we can not proof it directly. The reason is that this claim <u>did not capture the true structure</u> of the underlying fact we were trying to prove — it was too <u>vague</u>. As a result, our Induction Hypothesis wasn’t strong enough to prove our desired result.

Let us try to show the following <u>stronger claim</u>. 
> **Theorem 3'** 
> For all n ≥ 1, the sum of the first n odd numbers is $n^{2}$ .
> (It is easy to proof by induction)

## III Strong Induction

Sometimes we can solve the question difficultly by using P(k) solely, that's why strong induction appears.

_strong induction:_ we assume the stronger statement that P(0), P(1), . . . , and P(k) are all true  ![|110](attachments/02-Mathematical%20Induction-3.png)

> Is there a difference between the power of strong and weak induction, i.e., <u>can strong induction prove statements which weak induction cannot?</u>
> **No!** Intuitively, this can be seen by returning to our dominoanalogy.

> **Theorem 4** 
> Every natural number n > 1 can be written as a product of one or more primes.
> 
> **proof** proceed by induction and cases
> Let P(n) be the proposition that n can be written as a product of primes. We will prove that P(n) is true for all n ≥ 2. 
> 1. Base Case (n = 2): We start at n = 2. Clearly P(2) holds, since 2 is a prime number. 
> 2. Induction Hypothesis: Assume P(n) is true for all 2 ≤ n ≤ k.
> 3. Inductive Step: Prove that n = k +1 can be written as a product of primes. We have two cases: either k +1 is a prime number, or it is not.
>> For the first case, if k +1 is a prime number, then we are done since k +1 is trivially the product of one prime (itself). 
>> For the second case, if k + 1 is not a prime number, then by definition k + 1 = xy for some x,y ∈ Z + satisfying 1 < x, y < k + 1. By the Induction Hypothesis, x and y can each be written as a product of primes (since x, y ≤ k). But this implies that k +1 can also be written as a product of primes.
> Then, we get it.

(Recursion, programming and induction are also mentioned here, but these will be covered in `FDS`, so we'll skip them)

## IV False proofs

Let's look at one of history's most famous false proofs which makes us laugh:

> **False theorem**
> All horses are the same color
> 
> **proof** proceed by induction
> 1. Base Case (n = 1): P(1) is certainly true, since if you have a set containing just one horse, all horses in the set have the same color.
> 2. Induction Hypothesis: Assume P(n) holds for some arbitrary n ≥ 1. 
> 3. Inductive Step: Given a set of n + 1 horses {h1,h2,...,hn+1}, we can exclude the last horse in the set and apply the induction hypothesis just to the first n horses {h1,...,hn}, deducing that they all have the same color. <u>Similarly, we can conclude that the last n horses {h2,...,hn+1} all have the same color. </u>But now the “middle” horses {h2,...,hn} (i.e., all but the first and the last) belong to both of these sets, so they have the same color as horse h1 and horse hn+1. It follows, therefore, that all n+1 horses have the same color. We conclude, by the principle of induction, that all horses have the same color.

## Inductive definition

The same idea can work to define a set of objects, as well as to prove statements about that set of objects, which means _Inductive definition_.

One of most famous cases is [Peano axioms](https://en.wikipedia.org/wiki/Peano_axioms), which will tell you how we define natural numbers and addition and multiplication.

Or you can read [this](https://www.yuque.com/xianyuxuan/coding/lfxqyr#2xHXJ) for a easy understanding.




