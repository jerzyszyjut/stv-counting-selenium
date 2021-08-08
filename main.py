from modules.votes import Votes
from modules.countingVotes import CountingVotes

path = input('Please input votes file path: ')
mandates = input('Please input mandates count: ')

votes = Votes('./votes/' + path + '.csv')
counting = CountingVotes(votes.votes, votes.candidates, mandates)

counting.startCounting()
