# Electronic Voting System

This Python program implements a console-based electronic voting system. It allows users to define the number of candidates, vote for them, and view the final results. The key features are as follows:

## Key Features

1. **User-Defined Candidates**  
   - The program prompts the user to specify the number of candidates.
   - The user then inputs the names of each candidate.

2. **Dynamic Voting**  
   - Voters cast their votes by entering their Voter ID and selecting a candidate by number.
   - Voters can change their vote by re-entering their Voter ID and selecting a different candidate.

3. **Efficient Vote Tallying**  
   - The system efficiently tracks votes using dynamic programming techniques.
   - It updates the tally incrementally, avoiding the need to recount all votes whenever a change is made.

4. **Final Results**  
   - After all votes are cast (when the user types "exit"), the system displays the final vote count for each candidate.

## Example Usage

```bash
Enter the number of candidates: 3
Enter the name of candidate 1: Alice
Enter the name of candidate 2: Bob
Enter the name of candidate 3: Charlie

--- Electronic Voting System ---
Enter your Voter ID (or type 'exit' to finish): Voter_1
Candidates:
1. Alice
2. Bob
3. Charlie
Enter the number corresponding to your chosen candidate: 1
Thank you, Voter_1. You voted for Alice.

--- Electronic Voting System ---
Enter your Voter ID (or type 'exit' to finish): exit

--- Final Voting Results ---
Alice: 1 votes
Bob: 0 votes
Charlie: 0 votes

OUTPUT:
## Screenshots
![](screenshot1.png)

