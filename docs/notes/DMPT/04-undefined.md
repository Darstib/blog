## The Stable Matching Problem

The Stable Matching Problem is described below
![|475](attachments/04-undefined.png)

## The Propose-and-Reject Algorithm

(a.k.a. the Gale-Shapley algorithm)
We think of the algorithm as proceeding in “days” to have a clear unambiguous sense of discrete time.

> **Every Morning**: Each job proposes (i.e. makes an offer) to the most preferred candidate on its list who has not yet rejected this job. 
> **Every Afternoon**: Each candidate collects all the offers she received in the morning; to the job offer she likes best among these, she responds “maybe” (she now has it in hand or on a string), and to the other offers she says “no” (i.e., she rejects them). (This is just a way for us to virtually model that there are no “exploding offers” and a job can’t withdraw an offer once an offer is made.) 
> **Every Evening**: Each rejected job crosses off the candidate who rejected its offer from its list. 
> 
> The above loop is repeated each successive day until there are no offers rejected. At that point, each candidate has a job offer in hand (i.e. on a string); and on this day, each candidate accepts their offered job (i.e. the job offer she has in hand) and the algorithm terminates.

Let’s understand the algorithm by running it on our example above.
![|475](attachments/04-undefined-1.png)

## Properties of the Propose-and-Reject Algorithm

There are two properties we wish to show about the propose-and-reject algorithm: 
- First, that it doesn’t run forever, i.e., **it halts**; (it is easy to proof)
- and second, that it outputs a “**good**” (i.e., stable) matching.
We are going to talk about how good it is.
### Stability

too difficult!
### Analysis

