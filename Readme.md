# AI-Project-3: Adversarial Search
## Team members: Javid Guliyev; Riyad Abdurahimov
## Heuristics:
1. After reaching the maximum search depth without encountering a terminal state, all possible vertical, horizontal, and diagonal segments of length M are extracted from the N × N board. The occurrences of X and O symbols within each segment are counted. Based on these counts, a score is computed, which is then used to determine the optimal move. The score is computed as follows if AI is minimizer:
- If in the given segment there are only **n** opponent’s symbols without any AI symbols then score of the segment will calculated as **10^n**
- If in the given segment there are only n AI symbols without any opponent’s symbols then score of the segment will be calculated as **-10^n**
- If in the given segment there are at least one AI or opponent’s symbol then score of the segment will be **0**.
Later all those scores will be summed up and used during the decision about which move is more favorable.

2. Instead of scanning all possible moves, which is a computationally expensive process, the AI focuses only on the neighborhood around previously made moves. It maintains separate lists to store the move history of each player. A special variable controls the radius of this neighborhood; for example, a radius of one means the AI will consider only the positions one move away from the previous move when searching for available options.

3. If the same advantageous move is detected at different moments of time the one that was detected earlier (the move which has smaller depth value) would be rewarded more than the same move discovered later.
## Optimizers:
1. Alpha-beta pruning is used to cut branches and avoid unnecessary computations.

2. As code was written in Python **multiprocessing pool** was used to efficiently divide the search space between processes which significantly reduces the computation time.

 
