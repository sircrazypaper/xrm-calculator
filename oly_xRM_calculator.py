def xRMCalculator(weight, reps, rir):
    #calculate 1RM
    if(rir==0):
        if(reps==1):
            oneRM = weight
        elif(reps==2):
            oneRM = weight / 0.94
        elif(reps==3):
            oneRM = weight / 0.89
        elif(reps==4):
            oneRM = weight / 0.84
        elif(reps==5):
            oneRM = weight / 0.80

    if(rir==0.5):
        if(reps==1):
            oneRM = weight / 0.97
        elif(reps==2):
            oneRM = weight / 0.91
        elif(reps==3):
            oneRM = weight / 0.86
        elif(reps==4):
            oneRM = weight / 0.82
        elif(reps==5):
            oneRM = weight / 0.78

    if(rir==1):
        if(reps==1):
            oneRM = weight / 0.94
        elif(reps==2):
            oneRM = weight / 0.89
        elif(reps==3):
            oneRM = weight / 0.84
        elif(reps==4):
            oneRM = weight / 0.80
        elif(reps==5):
            oneRM = weight / 0.76

    if(rir==1.5):
        if(reps==1):
            oneRM = weight / 0.91
        elif(reps==2):
            oneRM = weight / 0.86
        elif(reps==3):
            oneRM = weight / 0.82
        elif(reps==4):
            oneRM = weight / 0.78
        elif(reps==5):
            oneRM = weight / 0.74

    if(rir==2):
        if(reps==1):
            oneRM = weight / 0.89
        elif(reps==2):
            oneRM = weight / 0.84
        elif(reps==3):
            oneRM = weight / 0.80
        elif(reps==4):
            oneRM = weight / 0.76
        elif(reps==5):
            oneRM = weight / 0.73

    if(rir==2.5):
        if(reps==1):
            oneRM = weight / 0.86
        elif(reps==2):
            oneRM = weight / 0.82
        elif(reps==3):
            oneRM = weight / 0.78
        elif(reps==4):
            oneRM = weight / 0.74
        elif(reps==5):
            oneRM = weight / 0.71

    if(rir==3):
        if(reps==1):
            oneRM = weight / 0.84
        elif(reps==2):
            oneRM = weight / 0.80
        elif(reps==3):
            oneRM = weight / 0.76
        elif(reps==4):
            oneRM = weight / 0.73
        elif(reps==5):
            oneRM = weight / 0.70

    if(rir==3.5):
        if(reps==1):
            oneRM = weight / 0.82
        elif(reps==2):
            oneRM = weight / 0.78
        elif(reps==3):
            oneRM = weight / 0.74
        elif(reps==4):
            oneRM = weight / 0.71
        elif(reps==5):
            oneRM = weight / 0.68

    if(rir==4):
        if(reps==1):
            oneRM = weight / 0.80
        elif(reps==2):
            oneRM = weight / 0.76
        elif(reps==3):
            oneRM = weight / 0.73
        elif(reps==4):
            oneRM = weight / 0.70
        elif(reps==5):
            oneRM = weight / 0.67

    #calculate xRM
    xRMList = [round(oneRM, 2), round(oneRM * 0.94, 2), round(oneRM * 0.89, 2), round(oneRM * 0.84, 2), round(oneRM * 0.80, 2)]
    pointFiveRIRList = [round(oneRM * 0.97, 2), round(oneRM * 0.91, 2), round(oneRM * 0.86, 2), round(oneRM * 0.82, 2), round(oneRM * 0.78, 2)]
    oneRIRList = [round(oneRM * 0.94, 2), round(oneRM * 0.89, 2), round(oneRM * 0.84, 2), round(oneRM * 0.80, 2), round(oneRM * 0.76, 2)]
    onePointFiveRIRList = [round(oneRM * 0.91, 2), round(oneRM * 0.86, 2), round(oneRM * 0.82, 2), round(oneRM * 0.78, 2), round(oneRM * 0.74, 2)]
    twoRIRList = [round(oneRM * 0.89, 2), round(oneRM * 0.84, 2), round(oneRM * 0.80, 2), round(oneRM * 0.76, 2), round(oneRM * 0.73, 2)]
    twoPointFiveRIRList = [round(oneRM * 0.86, 2), round(oneRM * 0.82, 2), round(oneRM * 0.78, 2), round(oneRM * 0.74, 2), round(oneRM * 0.71, 2)]
    threeRIRList = [round(oneRM * 0.84, 2), round(oneRM * 0.80, 2), round(oneRM * 0.76, 2), round(oneRM * 0.73, 2), round(oneRM * 0.70, 2)]
    threePointFiveRIRList = [round(oneRM * 0.82, 2), round(oneRM * 0.78, 2), round(oneRM * 0.74, 2), round(oneRM * 0.71, 2), round(oneRM * 0.68, 2)]
    fourRIRList = [round(oneRM * 0.80, 2), round(oneRM * 0.76, 2), round(oneRM * 0.73, 2), round(oneRM * 0.70, 2), round(oneRM * 0.67, 2)]

    return oneRM, [xRMList, pointFiveRIRList, oneRIRList, onePointFiveRIRList, twoRIRList, twoPointFiveRIRList, threeRIRList, threePointFiveRIRList, fourRIRList]
