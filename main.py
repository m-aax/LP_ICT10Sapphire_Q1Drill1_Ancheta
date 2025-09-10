from pyscript import document

def compute_average(event):
    #get input values and convert to float
    score1 = float(document.getElementById("score1").value)
    score2 = float(document.getElementById("score2").value)

    #compute for the average
    average = (score1 + score2) / 2

    #determine if pass/fail
    if average >=75:
        result="Yes"
    else:
        result="No"

    #display result
    document.getElementById("average").innerText = str(round(average, 2)) #this rounds off da average in 2 decimal places
    document.getElementById("result").innerText = result