# CompatibilityPredictor
Python implementation of deciding if an applicant is compatible with a team of software developers

My solution has a .json file included in the current directory. In order to run my code please use the command
`python3 compatibility.py > output.json`

My solution attempted to determine how much each of the applicant's individual attributes improved the overall team score for that attribute. I allocated a number of points to each of the applicant's stats, based on the percentage change when adding an applicant's stat to the teams total stat. The number of points allocated to each of the stats could be made so that they can change depending on what is more valued at the time. Then when adding the total accumulated points, you get the total points earned for each applicant. The number of accumulated points is then divided by 100 to get the applicant's score. The percentage increases in team stats are always going to be within 0 and 1, and the number of obtainable points does not exceed 100.
