from modules.votes import Votes
from modules.countingVotes import CountingVotes

mandates = 10

votes = Votes('./votes/glosy.csv')
counting = CountingVotes(votes.votes, votes.candidates, mandates)

counting.startCounting()
