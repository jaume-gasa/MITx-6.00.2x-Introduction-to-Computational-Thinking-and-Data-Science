# 6.00.2x Problem Set 4

import numpy
import random
import pylab
import copy
from ps3b import *


def updatePatientTimeSteps(patient, timeSteps):
    for ts in range(timeSteps):
        patient.update()


def uniqueSimulationDelayedTreatment(patient, drugPrescripted, numTrials,
                                     beforeTimeSteps, afterTimeSteps):
    data = []
    for i in range(numTrials):
        p = copy.deepcopy(patient)
        updatePatientTimeSteps(p, beforeTimeSteps)
        p.addPrescription(drugPrescripted)
        updatePatientTimeSteps(p, afterTimeSteps)
        data.append(p.getTotalPop())
    return data


#
# PROBLEM 1
#
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # Virus and some variables initialization
    virus = ResistantVirus(0.4, 0.05, {'guttagonol': False}, 0.005)
    viruses = [virus for i in range(100)]
    maxPop = 1000
    patient = TreatedPatient(viruses, maxPop)
    # timeSteps = [300, 150, 75, 0]
    timeSteps = [150]
    afterTimeSteps = 150
    drugPrescripted = 'guttagonol'
    data = []
    fig = pylab.figure()
    # Begin the simulation
    for ts in timeSteps:
        data.append(uniqueSimulationDelayedTreatment(patient, drugPrescripted,
                                                     numTrials, ts,
                                                     afterTimeSteps))
    # Plotting data
    pylab.hist(data[0], bins=numTrials)
    '''
    ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(222)
    ax3 = fig.add_subplot(223)
    ax4 = fig.add_subplot(224)
    ax1.hist(data[0], bins=numTrials)
    ax2.hist(data[1], bins=numTrials)
    ax3.hist(data[2], bins=numTrials)
    ax4.hist(data[3], bins=numTrials)
    '''
    pylab.show()


def createAndShowFourHistograms(data, numTrials):
    fig = pylab.figure()
    ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(222)
    ax3 = fig.add_subplot(223)
    ax4 = fig.add_subplot(224)
    ax1.hist(data[0], bins=numTrials)
    ax1.set_title('300 timesteps')
    ax2.hist(data[1], bins=numTrials)
    ax2.set_title('150 timesteps')
    ax3.hist(data[2], bins=numTrials)
    ax3.set_title('75 timesteps')
    ax4.hist(data[3], bins=numTrials)
    ax4.set_title('0 timesteps')
    pylab.show()


def getNewPatient():
    virus = ResistantVirus(0.1, 0.05, {'guttagonol': False, 'grimpex': False},
                           0.005)
    viruses = [virus for i in range(100)]
    patient = TreatedPatient(viruses, 1000)
    return patient


def uniqueSimulationTwoDrugsDelayedTreatment(numTrials, tsBeforeFirstDrug,
                                             tsBeforeSecondDrug, tsAfter,
                                             firstDrug, secondDrug):
    data = []
    for trial in range(numTrials):
        patient = getNewPatient()
        updatePatientTimeSteps(patient, tsBeforeFirstDrug)
        patient.addPrescription(firstDrug)
        updatePatientTimeSteps(patient, tsBeforeSecondDrug)
        patient.addPrescription(secondDrug)
        updatePatientTimeSteps(patient, tsAfter)
        data.append(patient.getTotalPop())
    return data


def numberOfPatientsCured(data):
    upperBoundToBeCured = 50
    timeSteps = [300, 150, 75, 0]
    cured = 0
    for ts in range(len(data)):
        for patient in data[ts]:
            if patient <= upperBoundToBeCured:
                cured += 1
        print 'Patient cured when delaying ', timeSteps[ts], ' timesteps ', cured
        cured = 0


def getVariances(data):
    variances = []
    for case in range(len(data)):
        mean = 0
        for patientVirPop in data[case]:
            mean += patientVirPop
        mean /= float(len(data[case]))
        variance = 0
        for patientVirPop in data[case]:
            variance += (patientVirPop - mean)**2
        variance /= float(len(data[case]))
        variances.append(variance)
    cases = [300, 150, 75, 0]
    for i in range(len(variances)):
        print 'variance for case ', cases[i], ': ', variances[i]


#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """

    firstDrug = 'guttagonol'
    secondDrug = 'grimpex'
    data = []
    # Time steps declaration
    tsBeforeFirstDrug = 150
    tsBeforeSecondDrug = [300, 150, 75, 0]
    tsAfter = 150
    # Begin simulation
    for tsSecond in tsBeforeSecondDrug:
        data.append(uniqueSimulationTwoDrugsDelayedTreatment(numTrials,
                                                             tsBeforeFirstDrug,
                                                             tsSecond, tsAfter,
                                                             firstDrug,
                                                             secondDrug))
    print data
    numberOfPatientsCured(data)
    getVariances(data)
    createAndShowFourHistograms(data, numTrials)


simulationTwoDrugsDelayedTreatment(150)
