class Solution:
    def deckRevealedIncreasing(self, deck):
        length = len(deck)
        retval = [None] * length
        indices = list(range(0,length))
        # Since our numbers are in range 1 <= deck[i] <= 10^6, Radix sort can sort this in linear time.
        # I did not call it specifically, but linear sorting time algorithms should be kept in mind when
        # dealing with problems with acceptably small number ranges.
        sortedDeck = sorted(deck)

        # We will just go through the indices following the logic of reveal->put at bottom->repeat.
        # Each time we get to an index that is a reveal, we know we need to place the next largest number in that index.

        reveal = True
        revealidx = 0
        while indices:
            if reveal:
                idx = indices.pop(0)
                retval[idx] = sortedDeck[revealidx]
                revealidx = revealidx+1
                reveal = False
            else:
                indices.append(indices.pop(0))
                reveal = True
        return retval