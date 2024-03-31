## Introduction

The Stable Matching Problem is described below

![|475](attachments/04-undefined.png)

## The Propose-and-Reject Algorithm

(a.k.a. the Gale-Shapley algorithm)
We think of the algorithm as proceeding in “days” to have a clear unambiguous sense of discrete time.

> **Every Morning**: Each job proposes (i.e. makes an offer) to the most preferred candidate on its list who has not yet rejected this job. 
> 
> **Every Afternoon**: Each candidate collects all the offers she received in the morning; to the job offer she likes best among these, she responds “maybe” (she now has it in hand or on a string), and to the other offers she says “no” (i.e., she rejects them). (This is just a way for us to virtually model that there are no “exploding offers” and a job can’t withdraw an offer once an offer is made.) 
> 
> **Every Evening**: Each rejected job crosses off the candidate who rejected its offer from its list. 
> 
> The above loop is repeated each successive day until there are no offers rejected. At that point, each candidate has a job offer in hand (i.e. on a string); and on this day, each candidate accepts their offered job (i.e. the job offer she has in hand) and the algorithm terminates.

Let’s understand the algorithm by running it on our example above.
(bold type indicates the offer accepted by the candidate)

![|475](attachments/04-undefined-1.png)

## Properties of the Propose-and-Reject Algorithm

There are two properties we wish to show about the propose-and-reject algorithm: 

- First, that it doesn’t run forever, i.e., **it halts**; (it is easy to prove)
- and second, that it outputs a “**good**” (i.e., stable) matching.

We are going to talk about how good it is.
### Stability

> A matching is unstable  if there is ^^a job and a candidate who both prefer working with eachother over their current matchings^^ . We will call  such a pair a **rogue couple**. So a matching of n jobs and n candidates is stable if it has no rogue couples.
> 
> Why?
> 
> Because in such a situation, the rogue candidate could just renege on their official offer and the rogue job/employer could just fire the person that they officially hired to hire their preferred rogue candidate instead. Then one job is suddenly empty and one innocent person just got fired. This is not what we want to see happening. We want everyone to be happy enough that they all want to follow through on their final accepted offers.

Consider the following matching for the example above: 
> {(Approximation Inc., Christine), (Basis Co., Bridget), (Control Corp., Anita)}

Why is this matching unstable? 
(Hint: Approximation Inc. and Bridget are a rogue couple)

  Here is a stable matching for our example: 
> {(Basis Co., Anita), (Approximation Inc., Bridget), (Control Corp., Christine)}.

Why is (Approximation Inc., Anita) not a rogue couple here?

You just need to verify according to the concepts above.

In fact, not all matches can have a stable match result, the following is a counterexample:

![|500](attachments/04-undefined-2.png)

### Analysis

We do know about what is a stable match.

We now prove that the propose-and-reject algorithm always outputs a stable matching.

**Observation:** Each job begins the algorithm with its first choice being a possibility; as the algorithm proceeds, however, its best available option can only get worse over time. In contrast, ^^each candidate’s offers can only get better with time.^^  At some point, the jobs and the candidates must “meet” in the middle, and intuitively such a matching should be stable.

> **Lemma  1 (Improvement Lemma)**.
> 
>  If job J makes an offer to candidate C on the kth day, then on every subsequent day C has a job offer in hand (on a string) which she likes at least as much as J.

We can prove it by induction.

> **Theorem 1 _The Well-Ordering Principle_.**
> 
> If S ⊆ N and $S\ne \emptyset$, then S has a smallest element.

That is,  a non-empty set of integers must have a minimum value, which is obvious.

> **Lemma 2**

> The propose-and-reject algorithm always terminates with a matching.

We can prove it by contradiction.

Then comes what we are looking for:

> **Theorem 2**
> 
> The matching produced by the algorithm is always stable.
>
> **proof** ![](attachments/04-The%20Stable%20Matching%20Problem.png)

### Optimality

To offer the **best service** (and to displace the current approach), you would ideally strive for ^^some notion of optimality^^ in the solutions you obtain.

![](attachments/04-The%20Stable%20Matching%20Problem-1.png)

> **Definition  1 (_Optimal candidate for a job_)**
> 
>  For a given job J, the optimal candidate for J is the highest rank candidate on J’s preference list that J could be paired with in any stable matching.

> **Definition 2 (_Optimal job for a candidate_)**
> 
> For a given candidate C, the optimal job for C is the highestranked job on C’s preference list that C could be paired with in any stable matching.

> **Theorem 3**
> 
> The matching output by the Propose-and-Reject algorithm is job/employer optimal.

The proof process is omitted here, which you can see [here](https://www.eecs70.org/assets/pdf/notes/n4.pdf)