import os
import csv

poll_csv = os.path.join("PyPoll","Resources", "election_data.csv")

totalVotes = int()
numberVotes = int()
winner = str()



c1 = "Khan"
c1votes = []
c1pct = float()

c2 = "Correy"
c2votes = []
c2pct = float()

c3 = "Li"
c3votes = []
c3pct = float()

c4 = "O'Tooley"
c4votes = []
c4pct = float()




with open(poll_csv, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    print(csvreader)


    csv_header = next(csvreader)


    

    for row in csvreader:
        
        totalVotes +=1
        
        if row[2] == "Khan":
            c1votes.append(row[2])
            c1pct = round(float(len(c1votes)/totalVotes)*100)
        elif row[2] == "Correy":
            c2votes.append(row[2])
            c2pct = round(float(len(c2votes)/totalVotes)*100)
        elif row[2] == "Li":
            c3votes.append(row[2])
            c3pct = round(float(len(c3votes)/totalVotes)*100)
        elif row[2] == "O'Tooley":
            c4votes.append(row[2])
            c4pct = round(float(len(c4votes)/totalVotes)*100)
    
    if c1pct > c2pct and c3pct and c4pct:
        winner = c1
    elif c2pct > c1pct and c3pct and c4pct:
        winner = c2
    elif c3pct > c1pct and c2pct and c4pct:
        winner = c3
    elif c4pct > c1pct and c2pct and c3pct:
        winner = c4



output_file = os.path.join("PollResults.txt")

with open(output_file, "w") as outfile:
    outfile.write(f"Election Results\n")
    outfile.write(f"-------------------------\n")
    outfile.write(f"Total Votes: {totalVotes}\n")
    outfile.write("-------------------------\n")
    outfile.write(f"{c1}: {c1pct}% ({len(c1votes)}) \n")
    outfile.write(f"{c2}: {c2pct}% ({len(c2votes)}) \n")
    outfile.write(f"{c3}: {c3pct}% ({len(c3votes)}) \n")
    outfile.write(f"{c4}: {c4pct}% ({len(c4votes)}) \n")
    outfile.write("-------------------------\n")
    outfile.write(f"Winner: {winner}")


   
    



print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalVotes}")
print("-------------------------")
print(f"{c1}: {c1pct}% ({len(c1votes)}) ")
print(f"{c2}: {c2pct}% ({len(c2votes)}) ")
print(f"{c3}: {c3pct}% ({len(c3votes)}) ")
print(f"{c4}: {c4pct}% ({len(c4votes)}) ")
print("-------------------------")
print(f"Winner: {winner}")

        
       