Synopsis //

This bot calculates your "chance" of a successful application by comparing your A levels, GCSEs and MAT scores against historical applicants scores. We use information from Freedom of Information requests from universities to gather the scores.

The purpose of the algorithm is to determine a rough estimate of a specific candidate's chance to enter Oxbridge universities by comparing their candidate profile to that of previous successful applications.

Algorithm //

The bot takes your grades and assigns a numerical value to each grade. The higher the grade, the higher the value. We then weigh your results - some scores are more important than others. A levels, for example, have the highest weight of 6, while GCSEs only has a weight of one. This ranks your A-level results far higher than your GCSE results, which is an accurate reflection of the Oxbridge selection process. 

Each "grade" increase is worth 8 points - this means an F is worth 8 points while an A* is worth 56 points. This applies to both A-levels and GCSE grades. However, since A levels are weighted much heigher realistically each A level grade increase is worth 6 points to every one 1 point of GCSE grade increase

Ufa = Ugc + (Uas * 6) + (MATScore *4) / 10

% = [(Afs - Ufa)/Ufa] * 100

Ufa - User's final score
Ugc - User's total GCSE value
Uas - User's total A-Level value
MATScore - User's MAT score
% - Percentage difference of the user compared to the average Oxbridge applicant historically


The bot does not take into account your extracurriculars and historical information before 2012. The bot has also purposely left out 2021-22 data due to large grade inflation.

As with all things, this is an estimate based off of historical data. It is not necessarily accurate. The data showed that many viable candidates with lower scores were given offers compared to less viable candidates with higher scores.
References:

1. Freedom of Information Request on GCSE Scores compared to application success - University of Oxford - https://www.whatdotheyknow.com/request/653923/response/1553410/attach/3/FOI%202020%20241%20Elliott%20data.pdf?cookie_passthrough=1
2. Freedom of Information Request on GCSE Scores compared to application success - University of Cambridge - https://www.whatdotheyknow.com/request/653923/response/1553410/attach/html/3/FOI%202020%20241%20Elliott%20data.pdf.html
2. Freedom of Information Request on MAT Scores compared to application success - University of Oxford - https://www.whatdotheyknow.com/request/678358/response/1621957/attach/html/3/Ravichandran%20Data%20Final%2014%20August.xlsx.html 
