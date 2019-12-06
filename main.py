import os
import csv

Candidates = []

csvpath = os.path.join('.', 'Instructions', 'PyPoll', 'Resources', 'election_data.csv')
        
with open(csvpath, newline='') as electiondata:
    csvreader = csv.reader(electiondata, delimiter=',')

    # read header to pass row
    csv_header = next(electiondata)
    print(f"CSV Header: {csv_header}")

    def Analysis():
        # The total number of votes cast
        # A complete list of candidates who received votes
        Votes = 0
        for row in csvreader:
            if row[2] not in Candidates:
                Candidates.append(row[2])
                Votes += 1
            else:
                Votes += 1

        #find length of list of candidates
        Length = len(Candidates)
        Total_Votes = [0] * Length

        # The total number of votes each candidate won
        electiondata.seek(0)
        next(electiondata)
        for row in csvreader:
            for i in range(Length):
                if row[2] == Candidates[i]:
                    Total_Votes[i] += 1
        
        # The percentage of votes each candidate won
        Perc_Votes = [0] * Length
        for i in range(Length):
            Perc_Votes[i] = round(((Total_Votes[i] / Votes) * 100), 2)

        Cand_Votes = list(zip(Candidates, Perc_Votes, Total_Votes))

        # The winner of the election based on popular vote.
        Most_Votes = max(Total_Votes)
        Most_Index = Total_Votes.index(Most_Votes)
        Winner = Candidates[Most_Index]
        
        print("Election Analysis")
        print('----------------')
        for (x, y, z) in Cand_Votes:
            print(f"{x} : {y}% ({z})")
        print()
        print(f'Winner: {str(Winner)}') 

        with open("PyPollAnalysis.text", "w") as f:
            f.write("Election Analysis\n")
            f.write('-------------\n')
            for (x, y, z) in Cand_Votes:
                f.write(f"{x} : {y}% ({z})\n")
            f.write('\n')
            f.write(f'Winner: {str(Winner)}\n') 

    Analysis()
