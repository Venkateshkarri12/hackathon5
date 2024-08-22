class VotingSystem:
    def __init__(self, candidates):
        self.candidates = candidates
        self.tally = [0] * len(candidates) 
        self.voter_votes = {}  
    
    def cast_vote(self, voter_id, candidate):
        if voter_id in self.voter_votes:
            previous_vote = self.voter_votes[voter_id]
            self.tally[previous_vote] -= 1  
            print(f"Voter {voter_id} changed vote from {self.candidates[previous_vote]} to {candidate}")
        
        candidate_index = self.candidates.index(candidate)
        self.tally[candidate_index] += 1
        self.voter_votes[voter_id] = candidate_index  
    
    def get_results(self):
        return {self.candidates[i]: self.tally[i] for i in range(len(self.candidates))}
    
    def display_candidates(self):
        print("Candidates:")
        for i, candidate in enumerate(self.candidates):
            print(f"{i + 1}. {candidate}")

while True:
    try:
        num_candidates = int(input("Enter the number of candidates: "))
        if num_candidates > 0:
            break
        else:
            print("Number of candidates must be a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

candidates = []
for i in range(num_candidates):
    candidate_name = input(f"Enter the name of candidate {i + 1}: ").strip()
    candidates.append(candidate_name)

voting_system = VotingSystem(candidates)

while True:
    print("\n--- Electronic Voting System ---")
    voter_id = input("Enter your Voter ID (or type 'exit' to finish): ").strip()
    
    if voter_id.lower() == 'exit':
        break
    
    voting_system.display_candidates()
    
    while True:
        try:
            candidate_choice = int(input("Enter the number corresponding to your chosen candidate: "))
            if 1 <= candidate_choice <= len(candidates):
                selected_candidate = candidates[candidate_choice - 1]
                break
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    voting_system.cast_vote(voter_id, selected_candidate)
    print(f"Thank you, {voter_id}. You voted for {selected_candidate}.")

results = voting_system.get_results()
print("\n--- Final Voting Results ---")
for candidate, count in results.items():
    print(f"{candidate}: {count} votes")
