import random


class EVSESimController():
    """Controller Simulator. Either creates a controller for DC or AC case
    """
    def __init__(self):
        
        #dc Charging mode
        self.charging = None
    
        #EVSEStatus parameters
        self.notification_max_delay = 0
        self.evse_notification = None
            
            
        # DC parameters
        self.evse_maximum_current_limit = 50 #(A)
        self.isolation_status = "Valid"
        self.evse_maximum_power_limit = 5000
        self.evse_maximum_voltage_limit = 400
        self.evse_status_code = "EVSE_Ready"
        self.evse_minimum_current_limit = 16
        self.evse_minimum_voltage_limit =  400
        self.evse_peak_current_ripple = 0
        self.evse_present_voltage = 400
        self.evse_present_current =62
           

        # AC parameters
        self.rcd = False
        self.evse_nominal_voltage = 230
        self.evse_max_current = 50

    def set_to_dc_charging(self):
        self.charging = "DC"

    def set_to_ac_charging(self):
        self.charging = "AC"

    def is_DC_mode(self):
        return self.charging == "DC"

    def is_AC_mode(self):
        return self.charging == "AC"

    def get_evse_status(self):
        """This method will generate the EVSEStatus and EVSEProcessing elements
        Randomization will be used for testing purposes"""
        
        if self.charging == "DC":
            evse_status = {
                "NotificationMaxDelay": 0 ,
                "EVSENotification" : "None",
                "EVSEIsolationStatus" : self.randomize_EVSEIsolationStatus(),
                "EVSEStatusCode": "EVSE_Ready"
            }
        else:
            evse_status = {
                "NotificationMaxDelay": 0,
                "EVSENotification" : "None",
                "RCD" : self.rcd
            }

        return evse_status


    def randomize_EVSEIsolationStatus(self):
        """Randomizes EVSEIsolationStatus element
        """
        prob = 0.95
        isolation = "Valid" if random.random() < prob else "Invalid"
        return isolation
    
    def get_evse_processing(self, message):
        """Randomizes EVSEProcessing element for a specific Response Message
        Possible to customize the propability for each Response
        """
        if message=="ChargeParameterDiscoveryRes":
            prob = 0.0
        elif message =="CableCheckRes":
            prob = 0.0
        evseprocessing = "Ongoing" if random.random() < prob else "Finished"
        return evseprocessing

    def get_evse_current_limit_achieved(self):
        return bool(self.evse_present_current >= self.evse_maximum_current_limit)
    def get_evse_voltage_limit_achieved(self):
        return  bool(self.evse_present_voltage >= self.evse_maximum_voltage_limit)
    def get_evse_power_limit_achieved(self):
        return bool(self.evse_present_current >= self.evse_maximum_current_limit)



    




        

    

