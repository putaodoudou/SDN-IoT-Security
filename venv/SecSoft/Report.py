class Report:

    #creates object that describes threat report for each station
    #station is in string form and threatResult is in Array of Threats (Threats.Threat) report
    def __init__(self,station,threatResult):
        self.station = station
        self.threatResult = threatResult
